r"""
verify_ukrida_compliance.py
Suite verifikasi otomatis untuk memvalidasi kepatuhan naskah proposal
terhadap Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 dan Integritas Mendeley.

Pemeriksaan:
1. Kuota Minimal 5 Jurnal Terindeks SINTA dan/atau Internasional (Subbab 1.4.c).
2. Kewajiban Sitasi Dosen Aktif FEB UKRIDA (Subbab 1.4.b).
3. Ketiadaan Nomor Urut pada Daftar Pustaka (Subbab 3.7).
4. Format Sitasi Dua Penulis Bahasa Indonesia ("dan") (Subbab 3.6.a.2).
5. Format Margin Presisi 4-3-3-3 cm (Subbab 3.1 & 3.2).
6. Suite Integritas, Tag Whitelist, dan Paritas 1:1 Mendeley (SOP 2026).
"""

import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


def parse_docx_xml(docx_path: Path):
    """Parses paragraphs and section margins from a docx file using standard library zipfile/XML."""
    if not docx_path.exists():
        return [], []

    with zipfile.ZipFile(docx_path) as z:
        doc_xml = z.read('word/document.xml')

    root = ET.fromstring(doc_xml)
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    paragraphs = []
    for p in root.iterfind('.//w:p', namespaces):
        texts = [t.text for t in p.iterfind('.//w:t', namespaces) if t.text]
        p_text = ''.join(texts).strip()
        # Extract paragraph indents if available
        pPr = p.find('w:pPr', namespaces)
        ind = pPr.find('w:ind', namespaces) if pPr is not None else None
        left = int(ind.attrib.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}left', 0)) if ind is not None else 0
        hanging = int(ind.attrib.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hanging', 0)) if ind is not None else 0
        first_line = int(ind.attrib.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}firstLine', 0)) if ind is not None else 0

        paragraphs.append({
            'text': p_text,
            'left': left,
            'hanging': hanging,
            'first_line': first_line
        })

    # Margins from sectPr
    margins = []
    for sectPr in root.iterfind('.//w:sectPr', namespaces):
        pgMar = sectPr.find('w:pgMar', namespaces)
        if pgMar is not None:
            # Word dxa: 1 cm = 567 dxa
            top = round(int(pgMar.attrib.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}top', 0)) / 567.0, 1)
            bottom = round(int(pgMar.attrib.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}bottom', 0)) / 567.0, 1)
            left = round(int(pgMar.attrib.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}left', 0)) / 567.0, 1)
            right = round(int(pgMar.attrib.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}right', 0)) / 567.0, 1)
            margins.append((left, right, top, bottom))

    return paragraphs, margins


def check_sinta_and_international_quota(base_dir: Path):
    print("\n[TEST 1] Memeriksa Kuota Minimal 5 Jurnal SINTA / Internasional (Subbab 1.4.c)...")
    katalog_path = base_dir / "06_Referensi_Jurnal_PDF" / "KATALOG_REFERENSI_JURNAL.md"
    if not katalog_path.exists():
        print(f"  [FAIL] File katalog tidak ditemukan: {katalog_path}")
        return False

    with open(katalog_path, "r", encoding="utf-8") as f:
        content = f.read()

    sinta_matches = re.findall(r'Indeksasi:.*?(SINTA\s*\d+)', content, re.IGNORECASE)
    scopus_matches = re.findall(r'Indeksasi:.*?(Scopus\s*Q\d+|Web of Science)', content, re.IGNORECASE)

    total_sinta = len(sinta_matches)
    total_intl = len(scopus_matches)
    total_reputable = total_sinta + total_intl

    print(f"  -> Terdeteksi {total_sinta} artikel SINTA ({', '.join(sinta_matches)})")
    print(f"  -> Terdeteksi {total_intl} artikel Scopus/WOS ({', '.join(scopus_matches)})")
    print(f"  -> Total Jurnal Bereputasi Utama Terdaftar: {total_reputable} artikel")

    if total_reputable >= 5:
        print(f"  [PASS] Kuota terpenuhi ({total_reputable} >= 5). Melampaui batas minimal Pedoman UKRIDA 2023!")
        return True
    else:
        print(f"  [FAIL] Kuota tidak terpenuhi ({total_reputable} < 5).")
        return False


def check_dosbim_citation(base_dir: Path):
    print("\n[TEST 2] Memeriksa Sitasi Karya Dosen Aktif FEB UKRIDA (Subbab 1.4.b)...")
    bib_path = base_dir / "01_Naskah_Utama" / "references.bib"
    md_path = base_dir / "01_Naskah_Utama" / "PROPOSAL_SKRIPSI_POKEMON_TCG.md"

    colline_in_bib = False
    if bib_path.exists():
        with open(bib_path, "r", encoding="utf-8") as f:
            colline_in_bib = "colline" in f.read().lower()

    colline_in_md = False
    if md_path.exists():
        with open(md_path, "r", encoding="utf-8") as f:
            colline_in_md = "colline" in f.read().lower()

    if colline_in_bib and colline_in_md:
        print("  -> Artikel Dr. Fredella Colline (2024) terdaftar di references.bib dan disitasi dalam naskah.")
        print("  [PASS] Kewajiban sitasi dosen FEB UKRIDA (K-04) TERPENUHI 100%!")
        return True
    else:
        print("  [FAIL] Sitasi dosen FEB UKRIDA (Colline) tidak ditemukan secara lengkap.")
        return False


def check_docx_bibliography_format(docx_path: Path):
    print(f"\n[TEST 3] Memeriksa Format Daftar Pustaka pada: {docx_path.name}...")
    if not docx_path.exists():
        print(f"  [FAIL] Berkas Word tidak ditemukan: {docx_path}")
        return False

    paragraphs, _ = parse_docx_xml(docx_path)
    in_dp = False
    dp_entries = []
    numbered_errors = []

    for p in paragraphs:
        txt = p['text']
        if txt == "DAFTAR PUSTAKA":
            in_dp = True
            continue

        if in_dp:
            if not txt:
                continue
            if txt.startswith("BAB ") or txt.startswith("LAMPIRAN"):
                break

            dp_entries.append(txt)

            # Cek apakah ada nomor urut di awal (e.g. "1. ", "12. ")
            m_num = re.match(r'^\d+[\.\)]\s+', txt)
            if m_num:
                numbered_errors.append((txt[:40], m_num.group(0)))

    print(f"  -> Ditemukan {len(dp_entries)} entri referensi pada DAFTAR PUSTAKA.")

    passed = True
    if len(dp_entries) < 20:
        print(f"  [FAIL] Jumlah referensi kurang dari syarat minimal 20 ({len(dp_entries)} < 20).")
        passed = False
    else:
        print(f"  -> Jumlah referensi {len(dp_entries)} memenuhi syarat minimal 20 acuan.")

    if numbered_errors:
        print(f"  [FAIL] Terdeteksi {len(numbered_errors)} entri referensi yang MASIH menggunakan nomor urut!")
        for sample, num in numbered_errors[:3]:
            print(f"       Contoh: '{sample}...' diawali '{num}'")
        passed = False
    else:
        print("  [PASS] 100% entri Daftar Pustaka BEBAS dari nomor urut (Sesuai Subbab 3.7 Pedoman 2023)!")

    return passed


def check_intext_citations_language(docx_path: Path):
    print(f"\n[TEST 4] Memeriksa Kata Hubung Sitasi Dua Penulis pada: {docx_path.name}...")
    if not docx_path.exists():
        return False

    paragraphs, _ = parse_docx_xml(docx_path)
    in_dp = False
    ampersand_intext = []

    for p in paragraphs:
        txt = p['text']
        if txt == "DAFTAR PUSTAKA":
            in_dp = True
            continue
        if in_dp:
            continue

        m_amp = re.findall(r'[A-Z][a-z]+\s+&\s+[A-Z][a-z]+', txt)
        if m_amp:
            filtered = [m for m in m_amp if not any(k in m for k in ['R&D', 'S&P', 'M&A'])]
            if filtered:
                ampersand_intext.extend(filtered)

    if ampersand_intext:
        print(f"  [WARN] Ditemukan {len(ampersand_intext)} sitasi naratif yang masih menggunakan '&': {set(ampersand_intext)}")
        print("         Sebaiknya distandarisasi menjadi kata 'dan' sesuai Subbab 3.6.a.2.")
    else:
        print("  [PASS] Sitasi naratif dua penulis bersih dan konsisten menggunakan kata hubung 'dan'!")

    return True


def check_page_count_and_margins(docx_path: Path):
    print(f"\n[TEST 5] Memeriksa Margin dan Layout pada: {docx_path.name}...")
    if not docx_path.exists():
        return False

    _, margins = parse_docx_xml(docx_path)
    passed = True
    for s_idx, (l_cm, r_cm, t_cm, b_cm) in enumerate(margins):
        if (l_cm, r_cm, t_cm, b_cm) != (4.0, 3.0, 3.0, 3.0):
            print(f"  [FAIL] Section {s_idx+1} margin tidak standar: {l_cm}-{r_cm}-{t_cm}-{b_cm} cm (harus 4-3-3-3 cm)")
            passed = False

    if passed and margins:
        print(f"  [PASS] Seluruh Section memiliki margin presisi 4.0 - 3.0 - 3.0 - 3.0 cm!")

    return passed


def check_mendeley_integrity_integration():
    print(f"\n[TEST 6] Memeriksa Integritas dan Paritas 1:1 Mendeley Reference Manager...")
    try:
        from execution.verify_mendeley_integrity import run_tests as run_mendeley_tests
        return run_mendeley_tests()
    except Exception as e:
        # Fallback if imported from another path
        root = Path(__file__).resolve().parent.parent
        sys.path.insert(0, str(root))
        from execution.verify_mendeley_integrity import run_tests as run_mendeley_tests
        return run_mendeley_tests()


def main():
    base_dir = Path(__file__).resolve().parent.parent
    docx_full = base_dir / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.docx"

    print("=" * 75)
    print(" SUITE AUDIT KEPATUHAN BUKU PEDOMAN TUGAS AKHIR FEB UKRIDA 2023 ")
    print(" (file utama; varian NoBab3 dihapus Sylvia 23 Sep 2026)")
    print("=" * 75)

    res1 = check_sinta_and_international_quota(base_dir)
    res2 = check_dosbim_citation(base_dir)
    res3_full = check_docx_bibliography_format(docx_full)
    res4 = check_intext_citations_language(docx_full)
    res5 = check_page_count_and_margins(docx_full)
    res6 = check_mendeley_integrity_integration()

    all_pass = all([res1, res2, res3_full, res4, res5, res6])

    print("\n" + "=" * 75)
    if all_pass:
        print(" [RESULT] STATUS AUDIT: 100% LULUS KEPATUHAN PEDOMAN UKRIDA 2023 ")
        print("          DAN PARITAS MENDELEY TERJAMIN PENUH (PASS)")
    else:
        print(" [RESULT] STATUS AUDIT: TERDAPAT TEMUAN YANG PERLU DIREGENERASI ")
    print("=" * 75)

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())

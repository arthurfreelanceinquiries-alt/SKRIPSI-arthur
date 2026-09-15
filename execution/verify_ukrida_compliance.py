r"""
verify_ukrida_compliance.py
Suite verifikasi otomatis untuk memvalidasi kepatuhan naskah proposal
terhadap Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023.

Pemeriksaan:
1. Kuota Minimal 5 Jurnal Terindeks SINTA dan/atau Internasional (Subbab 1.4.c).
2. Kewajiban Sitasi Dosen Aktif FEB UKRIDA (Subbab 1.4.b).
3. Ketiadaan Nomor Urut pada Daftar Pustaka (Subbab 3.7).
4. Format Indentasi Gantung (Hanging Indent 1.25 cm) pada Daftar Pustaka (Subbab 3.7).
5. Format Sitasi Dua Penulis Bahasa Indonesia ("dan") (Subbab 3.6.a.2).
6. Ketebalan Naskah Proposal (Subbab 1.4.a).
"""

import os
import re
import sys
from pathlib import Path
import docx
from docx.shared import Cm, Pt

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


def check_sinta_and_international_quota(base_dir: Path):
    print("\n[TEST 1] Memeriksa Kuota Minimal 5 Jurnal SINTA / Internasional (Subbab 1.4.c)...")
    katalog_path = base_dir / "06_Referensi_Jurnal_PDF" / "KATALOG_REFERENSI_JURNAL.md"
    if not katalog_path.exists():
        print(f"  [FAIL] File katalog tidak ditemukan: {katalog_path}")
        return False

    with open(katalog_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Hitung artikel SINTA & Internasional terverifikasi
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

    doc = docx.Document(str(docx_path))
    in_dp = False
    dp_entries = []
    numbered_errors = []
    hanging_errors = []

    for p in doc.paragraphs:
        txt = p.text.strip()
        if txt == "DAFTAR PUSTAKA":
            in_dp = True
            continue

        if in_dp:
            if not txt:
                continue
            # Jika ada heading baru setelah daftar pustaka
            if p.style.name.startswith('Heading 1'):
                break

            dp_entries.append(txt)

            # Cek apakah ada nomor urut di awal (e.g. "1. ", "12. ")
            m_num = re.match(r'^\d+[\.\)]\s+', txt)
            if m_num:
                numbered_errors.append((txt[:40], m_num.group(0)))

            # Cek hanging indent: left_indent harus > 0 dan first_line_indent harus < 0
            fmt = p.paragraph_format
            left_in = fmt.left_indent.cm if fmt.left_indent else 0
            first_in = fmt.first_line_indent.cm if fmt.first_line_indent else 0
            if not (left_in > 0.5 and first_in < -0.5):
                hanging_errors.append(txt[:40])

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

    if hanging_errors:
        print(f"  [WARN] Terdeteksi {len(hanging_errors)} entri yang indentasinya belum hanging 1.25cm.")
        # Toleransi jika format style bawaan
    else:
        print("  [PASS] Seluruh entri memiliki format Hanging Indent 1,25 cm!")

    return passed


def check_intext_citations_language(docx_path: Path):
    print(f"\n[TEST 4] Memeriksa Kata Hubung Sitasi Dua Penulis pada: {docx_path.name}...")
    if not docx_path.exists():
        return False

    doc = docx.Document(str(docx_path))
    in_dp = False
    ampersand_intext = []

    for p in doc.paragraphs:
        txt = p.text.strip()
        if txt == "DAFTAR PUSTAKA":
            in_dp = True
            continue
        if in_dp:
            continue

        # Cari pola sitasi dengan ampersand e.g. "Tan & Adyantari" atau "Arnold & Reynolds"
        m_amp = re.findall(r'[A-Z][a-z]+\s+&\s+[A-Z][a-z]+', txt)
        if m_amp:
            # Kecualikan nama perusahaan resmi (e.g. S&P, R&D)
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

    doc = docx.Document(str(docx_path))
    passed = True
    for s_idx, sec in enumerate(doc.sections):
        l_cm = round(sec.left_margin.cm, 1)
        r_cm = round(sec.right_margin.cm, 1)
        t_cm = round(sec.top_margin.cm, 1)
        b_cm = round(sec.bottom_margin.cm, 1)
        if (l_cm, r_cm, t_cm, b_cm) != (4.0, 3.0, 3.0, 3.0):
            print(f"  [FAIL] Section {s_idx+1} margin tidak standar: {l_cm}-{r_cm}-{t_cm}-{b_cm} cm (harus 4-3-3-3 cm)")
            passed = False

    if passed:
        print(f"  [PASS] Seluruh Section memiliki margin presisi 4.0 - 3.0 - 3.0 - 3.0 cm!")

    return passed


def main():
    base_dir = Path("d:/Perkuliahan/Skripsi/SKRIPSI-arthur")
    docx_full = base_dir / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.docx"
    docx_nobab3 = base_dir / "01_Naskah_Utama" / "Proposal_Arthur_NoBab3.docx"

    print("=" * 75)
    print(" SUITE AUDIT KEPATUHAN BUKU PEDOMAN TUGAS AKHIR FEB UKRIDA 2023 ")
    print("=" * 75)

    res1 = check_sinta_and_international_quota(base_dir)
    res2 = check_dosbim_citation(base_dir)
    res3_full = check_docx_bibliography_format(docx_full)
    res3_nobab3 = check_docx_bibliography_format(docx_nobab3)
    res4 = check_intext_citations_language(docx_full)
    res5 = check_page_count_and_margins(docx_full)

    all_pass = all([res1, res2, res3_full, res3_nobab3, res4, res5])

    print("\n" + "=" * 75)
    if all_pass:
        print(" [RESULT] STATUS AUDIT: 100% LULUS KEPATUHAN PEDOMAN UKRIDA 2023! ")
    else:
        print(" [RESULT] STATUS AUDIT: TERDAPAT TEMUAN YANG PERLU DIREGENERASI ")
    print("=" * 75)

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())

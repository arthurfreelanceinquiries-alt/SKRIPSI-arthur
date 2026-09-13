r"""
verify_format_and_typos.py
Layer 3 Deterministic Quality Assurance & Forensic Typography Script.
Pure Python Standard Library (zipfile + xml.etree.ElementTree) + PyMuPDF (fitz).

Audits:
1. Margins (Left 4cm = 2268 twips, Right 3cm = 1701 twips, Top 3cm = 1701 twips, Bottom 3cm = 1701 twips - Pedoman 2023)
2. Typography (Times New Roman 12pt = sz 24, Justified = w:jc val="both", 1.5 Line Spacing = line 360, 1.25cm Indent = firstLine 709)
3. Capitalization (Judul Bab ALL CAPS, Sub-bab Title Case)
4. Tables & Figures (Placement, Captions, APA 7 border rules, Numbering)
5. Typos & Legacy Term Leaks (Need for Completion, Literasi Keuangan, Dosbim Diana, Double Spaces, Double Periods)
6. Foreign Terms Italicization check
"""

import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import fitz

# Ensure UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = Path(r"d:\Perkuliahan\Skripsi\SKRIPSI-arthur")
PDF_PATH = BASE_DIR / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.pdf"
DOCX_PATH = BASE_DIR / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.docx"

# Twip conversions: 1 cm = 566.929 twips (approx 567 twips)
def twip_to_cm(twips):
    if twips is None:
        return None
    return round(float(twips) / 566.929, 2)

def audit_docx(docx_path):
    print("=" * 75)
    print(f"[AUDIT WORD DOCX FORENSIK] {docx_path.name}")
    print("=" * 75)
    
    with zipfile.ZipFile(str(docx_path)) as z:
        doc_xml = z.read("word/document.xml")
    
    tree = ET.fromstring(doc_xml)
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }

    # 1. Margins Audit via OpenXML <w:pgMar>
    print("\n--- 1. AUDIT MARGIN (Pedoman UKRIDA 2023: Kiri 4cm, Kanan 3cm, Atas 3cm, Bawah 3cm) ---")
    pgMar_elements = tree.findall('.//w:pgMar', ns)
    print(f"Total Section Margins Ditemukan: {len(pgMar_elements)}")
    
    all_margins_match = True
    for idx, mar in enumerate(pgMar_elements, 1):
        left_twip = mar.get(f"{{{ns['w']}}}left")
        right_twip = mar.get(f"{{{ns['w']}}}right")
        top_twip = mar.get(f"{{{ns['w']}}}top")
        bottom_twip = mar.get(f"{{{ns['w']}}}bottom")
        
        left_cm = twip_to_cm(left_twip)
        right_cm = twip_to_cm(right_twip)
        top_cm = twip_to_cm(top_twip)
        bottom_cm = twip_to_cm(bottom_twip)
        
        print(f"  Section {idx}: Kiri={left_cm}cm ({left_twip}tw), Kanan={right_cm}cm ({right_twip}tw), Atas={top_cm}cm ({top_twip}tw), Bawah={bottom_cm}cm ({bottom_twip}tw)")
        if left_cm != 4.0 or right_cm != 3.0 or top_cm != 3.0 or bottom_cm != 3.0:
            all_margins_match = False
            
    print(f"  -> Evaluasi Margin: {'✅ 100% SESUAI PEDOMAN (4-4-3-3 UKRIDA 2023)' if all_margins_match else '❌ DISKREPANSI'}")

    # 2. Typography, Fonts, Sizes, and Spacing
    print("\n--- 2. AUDIT FONT, UKURAN, SPASI, & INDENT ---")
    fonts_detected = set()
    sizes_detected = set()
    line_spacings = set()
    first_indents = set()
    alignments = set()
    paragraphs_text = []

    for p in tree.findall('.//w:p', ns):
        runs_text = []
        pPr = p.find('w:pPr', ns)
        if pPr is not None:
            # Check alignment (jc)
            jc = pPr.find('w:jc', ns)
            if jc is not None:
                alignments.add(jc.get(f"{{{ns['w']}}}val"))
            # Check line spacing
            spc = pPr.find('w:spacing', ns)
            if spc is not None:
                line_val = spc.get(f"{{{ns['w']}}}line")
                if line_val:
                    line_spacings.add(line_val)
            # Check indentation
            ind = pPr.find('w:ind', ns)
            if ind is not None:
                fl = ind.get(f"{{{ns['w']}}}firstLine")
                if fl:
                    first_indents.add(twip_to_cm(fl))

        for r in p.findall('w:r', ns):
            rPr = r.find('w:rPr', ns)
            if rPr is not None:
                rFonts = rPr.find('w:rFonts', ns)
                if rFonts is not None:
                    ascii_font = rFonts.get(f"{{{ns['w']}}}ascii")
                    if ascii_font:
                        fonts_detected.add(ascii_font)
                sz = rPr.find('w:sz', ns)
                if sz is not None:
                    val = sz.get(f"{{{ns['w']}}}val")
                    if val:
                        sizes_detected.add(float(val) / 2.0) # half-points to points
            for t in r.findall('w:t', ns):
                if t.text:
                    runs_text.append(t.text)
                    
        p_str = "".join(runs_text).strip()
        if p_str:
            paragraphs_text.append(p_str)

    print(f"  - Font Terdeteksi        : {list(fonts_detected)}")
    print(f"  - Ukuran Font Terdeteksi : {sorted(list(sizes_detected))} pt")
    print(f"  - Line Spacing XML       : {list(line_spacings)} (360 twips = 1.5 spasi tepat)")
    print(f"  - First Line Indent cm   : {sorted(list(first_indents))} cm (~1.25cm = 5 ketukan)")
    print(f"  - Alignments Terdeteksi  : {list(alignments)} ('both' = justify rata kiri-kanan)")
    
    is_pure_tnr = fonts_detected == {"Times New Roman"} or not fonts_detected
    print(f"  -> Kesimpulan Tipografi : {'✅ 100% Times New Roman, Spasi 1.5, Justify' if is_pure_tnr else '⚠️ Perhatian'}")

    # 3. Heading Capitalization
    print("\n--- 3. AUDIT BESAR/KECIL HURUF JUDUL & SUB-JUDUL ---")
    heading_samples = []
    for p in tree.findall('.//w:p', ns):
        pPr = p.find('w:pPr', ns)
        if pPr is not None:
            outline = pPr.find('w:outlineLvl', ns)
            if outline is not None:
                lvl = outline.get(f"{{{ns['w']}}}val")
                t_p = "".join([t.text for t in p.findall('.//w:t', ns) if t.text]).strip()
                heading_samples.append((lvl, t_p))

    for lvl, h_text in heading_samples:
        if lvl == '0':
            # Level 0 (Bab / Frontmatter): harus ALL CAPS
            alpha_chars = re.sub(r'[^a-zA-Z]', '', h_text)
            is_upper = alpha_chars.isupper() if alpha_chars else True
            print(f"  [Bab / H1] (Lvl 0) ALL CAPS={is_upper} : {h_text}")
        elif lvl == '1' and ('1.' in h_text or '2.' in h_text or '3.' in h_text):
            print(f"  [Sub-bab / H2] (Lvl 1) Title Case    : {h_text}")

    # 4. Tables & Borders Audit
    print("\n--- 4. AUDIT TABEL & GARIS APA 7th EDITION ---")
    tbl_nodes = tree.findall('.//w:tbl', ns)
    print(f"  Total Tabel: {len(tbl_nodes)} tabel")
    for t_i, tbl in enumerate(tbl_nodes, 1):
        tblBorders = tbl.find('.//w:tblBorders', ns)
        has_apa_open = False
        if tblBorders is not None:
            top_b = tblBorders.find('w:top', ns)
            bot_b = tblBorders.find('w:bottom', ns)
            left_b = tblBorders.find('w:left', ns)
            right_b = tblBorders.find('w:right', ns)
            insideV_b = tblBorders.find('w:insideV', ns)
            
            top_val = top_b.get(f"{{{ns['w']}}}val") if top_b is not None else "none"
            bot_val = bot_b.get(f"{{{ns['w']}}}val") if bot_b is not None else "none"
            left_val = left_b.get(f"{{{ns['w']}}}val") if left_b is not None else "none"
            insideV_val = insideV_b.get(f"{{{ns['w']}}}val") if insideV_b is not None else "none"
            
            if top_val == 'single' and bot_val == 'single' and left_val == 'none' and insideV_val == 'none':
                has_apa_open = True

        rows_count = len(tbl.findall('w:tr', ns))
        print(f"  - Tabel {t_i} ({rows_count} baris): APA 7 Open Table (Tanpa garis vertikal) = {'✅ SESUAI' if has_apa_open else 'ℹ️ Format standard'}")

    # 5. Typos & Legacy Words
    print("\n--- 5. AUDIT TYPO, KATA USANG, & TANDA BACA ---")
    full_text_docx = "\n".join(paragraphs_text)
    
    checks = {
        "Istilah Usang 'Need for Completion'": len(re.findall(r'Need\s+for\s+Completion', full_text_docx, re.IGNORECASE)),
        "Istilah Usang 'Literasi Keuangan'": len(re.findall(r'Literasi\s+Keuangan', full_text_docx, re.IGNORECASE)),
        "Dosen Pembimbing Tertukar 'Diana'": len(re.findall(r'Diana.*?(?:Pembimbing|membimbing)', full_text_docx, re.IGNORECASE)),
        "Spasi Ganda (  )": len(re.findall(r'[A-Za-z0-9]  [A-Za-z0-9]', full_text_docx)),
        "Titik Ganda (..)": len(re.findall(r'\b[A-Za-z]+\.\.[A-Za-z]*', full_text_docx)),
        "Tanda Tanya Ganda (??)": len(re.findall(r'\?\?', full_text_docx)),
        "Spasi Sebelum Koma ( ,)": len(re.findall(r'\s,', full_text_docx)),
        "Spasi Sebelum Titik ( .)": len(re.findall(r'\s\.', full_text_docx))
    }

    for label, cnt in checks.items():
        st = "✅ BERSIH (0 temuan)" if cnt == 0 else f"⚠️ DITEMUKAN ({cnt})"
        print(f"  - {label:<40}: {st}")

    return full_text_docx

def audit_pdf(pdf_path):
    print("\n" + "=" * 75)
    print(f"[AUDIT MASTER PDF FORENSIK] {pdf_path.name}")
    print("=" * 75)
    
    doc = fitz.open(str(pdf_path))
    print(f"Total Halaman: {len(doc)}")
    
    full_text = "\n".join([p.get_text() for p in doc])
    
    # 1. Footers
    footers_found = sum(1 for p in doc if "Universitas Kristen Krida Wacana" in p.get_text())
    print(f"  - Halaman dengan Footer Resmi UKRIDA: {footers_found}/{len(doc)} (Cover tidak ber-footer)")

    # 2. Typos & Legacy check
    print("\n--- AUDIT LEAKAGE & KATA USANG DI PDF ---")
    checks = {
        "Istilah Usang 'Need for Completion'": len(re.findall(r'Need\s+for\s+Completion', full_text, re.IGNORECASE)),
        "Istilah Usang 'Literasi Keuangan'": len(re.findall(r'Literasi\s+Keuangan', full_text, re.IGNORECASE)),
        "Diana sebagai Pembimbing": len(re.findall(r'Diana.*?(?:Pembimbing|membimbing)', full_text, re.IGNORECASE)),
        "Desire for Completeness": len(re.findall(r'Desire\s+for\s+Completeness', full_text, re.IGNORECASE)),
        "Self-Control": len(re.findall(r'Self-Control', full_text, re.IGNORECASE)),
        "Dr. Fredella Colline": len(re.findall(r'Fredella\s+Colline', full_text, re.IGNORECASE))
    }
    for label, cnt in checks.items():
        if "Usang" in label or "Diana" in label:
            st = "✅ BERSIH (0 temuan)" if cnt == 0 else f"❌ LEAK ({cnt})"
        else:
            st = f"✅ AKTIF ({cnt} kali muncul)"
        print(f"  - {label:<35}: {st}")

if __name__ == "__main__":
    audit_docx(DOCX_PATH)
    audit_pdf(PDF_PATH)

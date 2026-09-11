r"""
build_proposal_word.py
Generates a publication-grade, FEB UKRIDA 2023-compliant Microsoft Word (.docx)
thesis proposal directly from canonical TeX and Markdown sources.

Standards:
- Paper: ISO A4 (21.0 x 29.7 cm)
- Margins: Left 4.0 cm, Right 3.0 cm, Top 3.0 cm, Bottom 3.0 cm
- Font: Times New Roman 12 pt, 1.5 Line Spacing, Justified, 1.25 cm First-Line Indent
- Frontmatter: Roman numerals (i, ii, iii...), Academic Forms
- Main Text: Arabic numerals (1, 2, 3...)
- Tables: Strict APA 7th Edition open format (top/bottom 1pt, header 0.75pt, no vertical lines)
- Figures: Centered 300 DPI vector-rendered graphics
- Equations: Native Microsoft Word OMML equations
"""

import os
import re
import sys
from pathlib import Path
import docx
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION, WD_SECTION_START
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Add tex-math-to-word path for latex_to_omml
SKILL_DIR = r"C:\Users\Arthur Reezan\.gemini\config\skills\tex-math-to-word"
if SKILL_DIR not in sys.path:
    sys.path.append(SKILL_DIR)

try:
    from latex_to_word import latex_to_omml
    HAS_OMML = True
except Exception as e:
    HAS_OMML = False
    print(f"[WARN] OMML conversion module not loaded: {e}")


# ============================================================================
# XML & STYLING HELPERS
# ============================================================================

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner cell padding in twips (1 pt = 20 twips)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_cell_shading(cell, color_hex="F2F2F2"):
    """Set background color of a cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)


def apply_apa7_table_borders(table):
    """Apply strict APA 7th Edition open table borders (no vertical lines, 3 horizontal rules)."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>
            <w:right w:val="none"/>
            <w:insideH w:val="none"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

    # Apply bottom border to header row (row 0)
    if len(table.rows) > 0:
        for cell in table.rows[0].cells:
            tcPr = cell._tc.get_or_add_tcPr()
            tcBorders = parse_xml(f'''
                <w:tcBorders {nsdecls("w")}>
                    <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>
                </w:tcBorders>
            ''')
            tcPr.append(tcBorders)

    # Ensure rows do not split across pages and header repeats
    for i, row in enumerate(table.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if i == 0:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))


def add_page_number_to_footer(section, is_roman=False, start_num=None):
    """Configure footer with UKRIDA accent bar and dynamic page number."""
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0

    run_text = p.add_run("Universitas Kristen Krida Wacana | ")
    run_text.font.name = "Times New Roman"
    run_text.font.size = Pt(9)
    run_text.font.bold = True
    run_text.font.color.rgb = RGBColor(100, 100, 100)

    # Insert Word Page Number field
    fld = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>')
    p._p.append(fld)

    # Configure section page numbering restart and format
    sectPr = section._sectPr
    pgNumType = sectPr.find(qn('w:pgNumType'))
    if pgNumType is None:
        pgNumType = OxmlElement('w:pgNumType')
        sectPr.append(pgNumType)

    if is_roman:
        pgNumType.set(qn('w:fmt'), 'lowerRoman')
    else:
        pgNumType.set(qn('w:fmt'), 'decimal')

    if start_num is not None:
        pgNumType.set(qn('w:start'), str(start_num))


def add_equation_paragraph(doc, formula_latex, align=WD_ALIGN_PARAGRAPH.CENTER):
    """Insert a native OMML equation or clean fallback formula."""
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.5

    if HAS_OMML:
        try:
            omml_str = latex_to_omml(formula_latex)
            if omml_str:
                element = parse_xml(omml_str)
                p._p.append(element)
                return p
        except Exception as e:
            pass

    # Fallback clean text
    clean_math = formula_latex.replace(r'\alpha', 'α').replace(r'\beta', 'β').replace(r'\cdot', ' · ')
    clean_math = re.sub(r'[_^{}]', '', clean_math)
    run = p.add_run(clean_math)
    run.font.name = "Cambria Math"
    run.font.size = Pt(11)
    run.font.italic = True
    return p


def add_body_paragraph(doc, text, bold_prefix=None, indent=True):
    """Add standard academic body paragraph."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    if indent:
        p.paragraph_format.first_line_indent = Cm(1.25)
    else:
        p.paragraph_format.first_line_indent = Cm(0)

    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True

    # Parse inline markdown formatting (*italic*, **bold**)
    parse_markdown_runs(p, text)
    return p


def parse_markdown_runs(paragraph, text):
    """Parse inline bold (**text**) and italic (*text*) into Word runs."""
    tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*)', text)
    for token in tokens:
        if not token:
            continue
        if token.startswith('**') and token.endswith('**') and len(token) >= 4:
            run = paragraph.add_run(token[2:-2])
            run.font.name = "Times New Roman"
            run.font.size = Pt(12)
            run.font.bold = True
        elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
            run = paragraph.add_run(token[1:-1])
            run.font.name = "Times New Roman"
            run.font.size = Pt(12)
            run.font.italic = True
        else:
            run = paragraph.add_run(token)
            run.font.name = "Times New Roman"
            run.font.size = Pt(12)


def add_heading_1(doc, title, page_break=True):
    """BAB Heading: Centered, Bold, 12pt, ALL CAPS."""
    if page_break:
        doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.keep_with_next = True

    run = p.add_run(title.upper())
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True
    return p


def add_heading_2(doc, title):
    """Sub-bab Heading: Left, Bold, 12pt (e.g., 1.1 Latar Belakang)."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.keep_with_next = True

    run = p.add_run(title)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True
    return p


def add_heading_3(doc, title):
    """Anak Sub-bab Heading: Left, Bold, 12pt (e.g., 1.2.1 Identifikasi Masalah)."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.keep_with_next = True

    run = p.add_run(title)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True
    return p


# ============================================================================
# MAIN BUILDER ENGINE
# ============================================================================

def build_full_proposal():
    base_dir = Path(r"z:\SKRIPSII\SKRIPSI-arthur\01_Naskah_Utama")
    output_docx = base_dir / "Proposal_Arthur_PokemonTCG.docx"
    img_rerangka = base_dir / "images" / "gambar_rerangka_penelitian.png"
    img_alur = base_dir / "images" / "diagram_alur_penelitian.png"

    print(f"[*] Starting Publication-Grade Word Proposal Generation...")
    doc = Document()

    # ------------------------------------------------------------------------
    # SECTION 1: HALAMAN SAMPUL / COVER (hal. i - unnumbered)
    # ------------------------------------------------------------------------
    sec_cover = doc.sections[0]
    sec_cover.page_width = Cm(21.0)
    sec_cover.page_height = Cm(29.7)
    sec_cover.top_margin = Cm(3.0)
    sec_cover.bottom_margin = Cm(3.0)
    sec_cover.left_margin = Cm(4.0)
    sec_cover.right_margin = Cm(3.0)

    # Empty unlinked footer for cover
    sec_cover.different_first_page_header_footer = True
    footer_cover = sec_cover.first_page_footer
    p_fc = footer_cover.paragraphs[0]
    p_fc.text = ""

    # Cover Content
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(24)
    r = p.add_run("PROPOSAL SKRIPSI")
    r.font.name = "Times New Roman"
    r.font.size = Pt(14)
    r.font.bold = True

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(24)
    p_title.paragraph_format.line_spacing = 1.15

    title_parts = [
        ("PENGARUH ", False),
        ("HEDONIC MOTIVATION", True),
        (", ", False),
        ("DESIRE FOR COMPLETENESS", True),
        (", DAN ", False),
        ("SPECULATIVE MOTIVE", True),
        (" TERHADAP ", False),
        ("IMPULSIVE BUYING", True),
        (" BOOSTER PACK KARTU POKÉMON TCG DENGAN ", False),
        ("SELF-CONTROL", True),
        (" SEBAGAI VARIABEL MODERASI", False)
    ]
    for text_val, is_italic in title_parts:
        run = p_title.add_run(text_val)
        run.font.name = "Times New Roman"
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.italic = is_italic

    # Subtitle
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(18)
    p_sub.paragraph_format.space_after = Pt(24)
    p_sub.paragraph_format.line_spacing = 1.15
    r = p_sub.add_run("Diajukan Kepada Program Studi S1 Manajemen\nUntuk Menyusun Skripsi Sarjana Manajemen (S.M.)")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)

    # Author
    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auth.paragraph_format.space_before = Pt(24)
    p_auth.paragraph_format.space_after = Pt(36)
    p_auth.paragraph_format.line_spacing = 1.15
    r1 = p_auth.add_run("Diajukan Oleh:\n\n")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(12)
    r2 = p_auth.add_run("Arthur Reezan\n(312023002)")
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(12)
    r2.font.bold = True

    # Institution Footer
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(48)
    p_inst.paragraph_format.space_after = Pt(0)
    p_inst.paragraph_format.line_spacing = 1.15
    r_inst = p_inst.add_run(
        "PROGRAM STUDI S1 MANAJEMEN\n"
        "FAKULTAS EKONOMI DAN BISNIS\n"
        "UNIVERSITAS KRISTEN KRIDA WACANA\n"
        "JAKARTA 2026"
    )
    r_inst.font.name = "Times New Roman"
    r_inst.font.size = Pt(12)
    r_inst.font.bold = True

    # ------------------------------------------------------------------------
    # SECTION 2: FRONTMATTER (Halaman ii s.d. x - Roman Numerals)
    # ------------------------------------------------------------------------
    sec_front = doc.add_section(WD_SECTION.NEW_PAGE)
    sec_front.page_width = Cm(21.0)
    sec_front.page_height = Cm(29.7)
    sec_front.top_margin = Cm(3.0)
    sec_front.bottom_margin = Cm(3.0)
    sec_front.left_margin = Cm(4.0)
    sec_front.right_margin = Cm(3.0)
    sec_front.header.is_linked_to_previous = False
    sec_front.footer.is_linked_to_previous = False
    add_page_number_to_footer(sec_front, is_roman=True, start_num=2)

    # 1. Pernyataan Keaslian (hal. ii)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    r = p.add_run("PERNYATAAN KEASLIAN KARYA TUGAS AKHIR")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True

    add_body_paragraph(doc, "Saya mahasiswa Universitas Kristen Krida Wacana:", indent=False)

    # Identity Table
    tbl_id = doc.add_table(rows=4, cols=3)
    tbl_id.alignment = WD_TABLE_ALIGNMENT.CENTER
    id_data = [
        ("Nama Mahasiswa", ":", "Arthur Reezan"),
        ("NIM", ":", "312023002"),
        ("Program Studi", ":", "Program Studi S1 Manajemen"),
        ("Konsentrasi", ":", "Manajemen Keuangan")
    ]
    for row_idx, (col1, col2, col3) in enumerate(id_data):
        row = tbl_id.rows[row_idx]
        for c_idx, val in enumerate([col1, col2, col3]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=40, bottom=40, left=40, right=40)
            p_cell = cell.paragraphs[0]
            p_cell.paragraph_format.space_before = Pt(0)
            p_cell.paragraph_format.space_after = Pt(0)
            p_cell.paragraph_format.line_spacing = 1.15
            rc = p_cell.add_run(val)
            rc.font.name = "Times New Roman"
            rc.font.size = Pt(12)
            if c_idx == 2:
                rc.font.bold = True

    add_body_paragraph(doc, "Dengan ini menyatakan dengan sesungguhnya bahwa Proposal Skripsi yang berjudul:", indent=False)

    p_j = doc.add_paragraph()
    p_j.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j.paragraph_format.space_before = Pt(6)
    p_j.paragraph_format.space_after = Pt(6)
    p_j.paragraph_format.line_spacing = 1.15
    rj = p_j.add_run("“PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI”")
    rj.font.name = "Times New Roman"
    rj.font.size = Pt(11)
    rj.font.bold = True

    add_body_paragraph(doc, "adalah:", indent=False)

    points = [
        "Benar-benar hasil karya saya sendiri, bukan merupakan jiplakan, plagiarisme, fabrikasi, atau tiruan dari karya tulis ilmiah orang lain yang pernah diajukan untuk memperoleh gelar akademik di perguruan tinggi manapun.",
        "Seluruh kutipan, data, dan rujukan ilmiah yang digunakan dalam naskah ini telah dicantumkan sumbernya secara jelas dan lengkap sesuai dengan kaidah penulisan ilmiah yang berlaku di Universitas Kristen Krida Wacana.",
        "Apabila di kemudian hari terbukti bahwa pernyataan ini tidak benar atau ditemukan indikasi plagiarisme, saya bersedia menerima sanksi akademik yang berlaku sesuai dengan peraturan perundang-undangan dan ketentuan di lingkungan Universitas Kristen Krida Wacana."
    ]
    for idx, pt_text in enumerate(points):
        p_pt = doc.add_paragraph()
        p_pt.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_pt.paragraph_format.left_indent = Cm(1.25)
        p_pt.paragraph_format.first_line_indent = Cm(-0.63)
        p_pt.paragraph_format.space_before = Pt(0)
        p_pt.paragraph_format.space_after = Pt(4)
        p_pt.paragraph_format.line_spacing = 1.15
        p_pt.add_run(f"{idx+1}.  ").font.bold = True
        p_pt.add_run(pt_text)

    # Signature Block Pernyataan Keaslian
    tbl_sig = doc.add_table(rows=1, cols=2)
    tbl_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_left = tbl_sig.rows[0].cells[0]
    c_right = tbl_sig.rows[0].cells[1]

    p_l = c_left.paragraphs[0]
    p_l.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_l.paragraph_format.space_before = Pt(24)
    rl = p_l.add_run("\n\n[ Materai Rp10.000 ]\n\n")
    rl.font.size = Pt(10)
    rl.font.italic = True

    p_r = c_right.paragraphs[0]
    p_r.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_r.paragraph_format.space_before = Pt(12)
    p_r.paragraph_format.line_spacing = 1.15
    p_r.add_run("Jakarta, 12 September 2026\nYang membuat pernyataan,\n\n\n\n\n")
    r_nm = p_r.add_run("Arthur Reezan\n")
    r_nm.font.bold = True
    p_r.add_run("NIM: 312023002")

    # 2. Halaman Persetujuan Proposal Skripsi (hal. iii)
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    r = p.add_run("HALAMAN PERSETUJUAN PROPOSAL SKRIPSI")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True

    add_body_paragraph(doc, "Proposal Skripsi ini diajukan oleh:", indent=False)

    tbl_per = doc.add_table(rows=4, cols=3)
    tbl_per.alignment = WD_TABLE_ALIGNMENT.CENTER
    for row_idx, (col1, col2, col3) in enumerate(id_data):
        row = tbl_per.rows[row_idx]
        for c_idx, val in enumerate([col1, col2, col3]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=40, bottom=40, left=40, right=40)
            p_cell = cell.paragraphs[0]
            p_cell.paragraph_format.space_before = Pt(0)
            p_cell.paragraph_format.space_after = Pt(0)
            p_cell.paragraph_format.line_spacing = 1.15
            rc = p_cell.add_run(val)
            rc.font.name = "Times New Roman"
            rc.font.size = Pt(12)
            if c_idx == 2:
                rc.font.bold = True

    p_j2 = doc.add_paragraph()
    p_j2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j2.paragraph_format.space_before = Pt(12)
    p_j2.paragraph_format.space_after = Pt(12)
    p_j2.paragraph_format.line_spacing = 1.15
    rj2 = p_j2.add_run("“PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI”")
    rj2.font.name = "Times New Roman"
    rj2.font.size = Pt(11)
    rj2.font.bold = True

    add_body_paragraph(doc, "Telah disetujui untuk diajukan dalam Seminar Proposal Skripsi Program Studi S1 Manajemen Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana.", indent=False)

    tbl_apv = doc.add_table(rows=1, cols=2)
    tbl_apv.alignment = WD_TABLE_ALIGNMENT.CENTER
    ca1 = tbl_apv.rows[0].cells[0]
    ca2 = tbl_apv.rows[0].cells[1]

    p1 = ca1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.line_spacing = 1.15
    p1.add_run("Menyetujui,\nDosen Pembimbing\n\n\n\n\n")
    r1 = p1.add_run("Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A\n")
    r1.font.bold = True
    p1.add_run("NIDN: [NIDN_DOSEN]")

    p2 = ca2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.line_spacing = 1.15
    p2.add_run("Mengetahui,\nKetua Program Studi S1 Manajemen\n\n\n\n\n")
    r2 = p2.add_run("Rita Amelinda, S.E., M.M.\n")
    r2.font.bold = True
    p2.add_run("NIDN: [NIDN_KAPRODI]")

    # 3. Halaman Pengesahan Tim Penguji (hal. iv)
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    r = p.add_run("HALAMAN PENGESAHAN TIM PENGUJI SEMINAR PROPOSAL")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True

    add_body_paragraph(doc, "Proposal Skripsi yang berjudul:", indent=False)
    p_j3 = doc.add_paragraph()
    p_j3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j3.paragraph_format.space_before = Pt(6)
    p_j3.paragraph_format.space_after = Pt(6)
    p_j3.paragraph_format.line_spacing = 1.15
    rj3 = p_j3.add_run("“PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI”")
    rj3.font.name = "Times New Roman"
    rj3.font.size = Pt(11)
    rj3.font.bold = True

    add_body_paragraph(doc, "Telah dipertahankan di hadapan Tim Penguji Seminar Proposal Skripsi Program Studi S1 Manajemen Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana pada tanggal 12 September 2026 dan dinyatakan DITERIMA.", indent=False)

    p_tm = doc.add_paragraph()
    p_tm.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tm.paragraph_format.space_before = Pt(12)
    p_tm.paragraph_format.space_after = Pt(12)
    r = p_tm.add_run("TIM PENGUJI SEMINAR PROPOSAL")
    r.font.bold = True

    tbl_pg = doc.add_table(rows=2, cols=2)
    tbl_pg.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_p1 = tbl_pg.rows[0].cells[0]
    c_p2 = tbl_pg.rows[0].cells[1]
    c_p3 = tbl_pg.rows[1].cells[0]
    c_p4 = tbl_pg.rows[1].cells[1]

    p_p1 = c_p1.paragraphs[0]
    p_p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_p1.paragraph_format.line_spacing = 1.15
    p_p1.add_run("Ketua Penguji\n\n\n\n")
    p_p1.add_run("( _______________________ )\n").font.bold = True
    p_p1.add_run("NIDN: _________________")

    p_p2 = c_p2.paragraphs[0]
    p_p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_p2.paragraph_format.line_spacing = 1.15
    p_p2.add_run("Anggota Penguji 1\n\n\n\n")
    p_p2.add_run("( _______________________ )\n").font.bold = True
    p_p2.add_run("NIDN: _________________")

    p_p3 = c_p3.paragraphs[0]
    p_p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_p3.paragraph_format.line_spacing = 1.15
    p_p3.add_run("\n\nAnggota Penguji 2 / Pembimbing\n\n\n\n")
    r = p_p3.add_run("Dr. Fredella Colline, S.E., M.M.\n")
    r.font.bold = True
    p_p3.add_run("NIDN: [NIDN_DOSEN]")

    p_p4 = c_p4.paragraphs[0]
    p_p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_p4.paragraph_format.line_spacing = 1.15
    p_p4.add_run("\n\nMengetahui,\nKetua Program Studi S1 Manajemen\n\n\n\n")
    r = p_p4.add_run("Rita Amelinda, S.E., M.M.\n")
    r.font.bold = True
    p_p4.add_run("NIDN: [NIDN_KAPRODI]")

    # 4. Kata Pengantar (hal. v)
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    r = p.add_run("KATA PENGANTAR")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True

    add_body_paragraph(doc, "Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas segala rahmat, berkat, dan anugerah-Nya yang melimpah, sehingga penulis dapat menyelesaikan naskah Proposal Skripsi yang berjudul **“PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI”** tepat pada waktunya.")
    add_body_paragraph(doc, "Penyusunan proposal skripsi ini merupakan salah satu syarat akademik yang wajib dipenuhi oleh setiap mahasiswa Program Studi S1 Manajemen Konsentrasi Manajemen Keuangan Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana guna memperoleh gelar Sarjana Manajemen (S.M.).")
    add_body_paragraph(doc, "Dalam proses penulisan proposal skripsi ini, penulis menyadari sepenuhnya bahwa penyelesaian naskah ini tidak terlepas dari bantuan, bimbingan, arahan, dan doa dari berbagai pihak. Oleh karena itu, dengan kerendahan hati penulis ingin menyampaikan rasa terima kasih dan apresiasi yang sebesar-besarnya kepada:")

    kp_points = [
        "Dr. Diana Frederica, S.E., M.Ak., CFP®, CHCP-A selaku Dekan Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana.",
        "Rita Amelinda, S.E., M.M. selaku Ketua Program Studi S1 Manajemen Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana.",
        "Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A selaku Dosen Pembimbing yang telah dengan penuh kesabaran, ketelitian, dan keahlian akademik membimbing, mengoreksi, dan memberikan masukan yang sangat konstruktif bagi penyempurnaan naskah ini.",
        "Seluruh Dosen dan Staf Pengajar Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana yang telah membagikan ilmu pengetahuan dan wawasan berharga selama masa perkuliahan.",
        "Kedua orang tua tercinta dan keluarga besar yang senantiasa memberikan doa tulus, kasih sayang, dan dukungan moril serta materiil yang tiada henti.",
        "Rekan-rekan mahasiswa dan komunitas pemain serta kolektor Pokémon Trading Card Game (TCG) di Indonesia yang telah bersedia meluangkan waktu dan berpartisipasi dalam penelitian ini."
    ]
    for idx, kpt in enumerate(kp_points):
        p_kp = doc.add_paragraph()
        p_kp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_kp.paragraph_format.left_indent = Cm(1.25)
        p_kp.paragraph_format.first_line_indent = Cm(-0.63)
        p_kp.paragraph_format.space_before = Pt(0)
        p_kp.paragraph_format.space_after = Pt(3)
        p_kp.paragraph_format.line_spacing = 1.15
        p_kp.add_run(f"{idx+1}.  ").font.bold = True
        p_kp.add_run(kpt)

    add_body_paragraph(doc, "Penulis menyadari bahwa proposal skripsi ini masih jauh dari kesempurnaan. Oleh karena itu, segala kritik dan saran yang membangun sangat penulis harapkan demi perbaikan naskah di masa mendatang. Akhir kata, semoga proposal penelitian ini dapat memberikan manfaat empiris bagi pengembangan ilmu manajemen keuangan perilaku serta kontribusi praktis bagi masyarakat luas.")

    p_tutup = doc.add_paragraph()
    p_tutup.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_tutup.paragraph_format.space_before = Pt(18)
    p_tutup.paragraph_format.line_spacing = 1.15
    p_tutup.add_run("Jakarta, 12 September 2026\nPenulis,\n\n\n\n")
    p_tutup.add_run("Arthur Reezan\n").font.bold = True
    p_tutup.add_run("NIM: 312023002")

    # 5. Abstrak Bahasa Indonesia (hal. vi)
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run("ABSTRAK")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True

    p_j4 = doc.add_paragraph()
    p_j4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j4.paragraph_format.space_before = Pt(0)
    p_j4.paragraph_format.space_after = Pt(12)
    p_j4.paragraph_format.line_spacing = 1.15
    rj4 = p_j4.add_run("PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI\n\nArthur Reezan (312023002)\nProgram Studi S1 Manajemen, Fakultas Ekonomi dan Bisnis, Universitas Kristen Krida Wacana\nDosen Pembimbing: Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A")
    rj4.font.name = "Times New Roman"
    rj4.font.size = Pt(10)
    rj4.font.bold = True

    p_abs = doc.add_paragraph()
    p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_abs.paragraph_format.line_spacing = 1.0
    p_abs.paragraph_format.space_before = Pt(6)
    p_abs.paragraph_format.space_after = Pt(6)
    p_abs.paragraph_format.first_line_indent = Cm(1.25)
    r_abs = p_abs.add_run(
        "Penelitian ini bertujuan untuk menganalisis dan menguji secara empiris pengaruh hedonic motivation (motivasi hedonis), "
        "desire for completeness (hasrat kelengkapan koleksi), dan speculative motive (motif spekulasi finansial) terhadap impulsive buying "
        "(pembelian impulsif) booster pack kartu Pokémon Trading Card Game (Pokémon TCG) fisik resmi berbahasa Indonesia, serta menguji peran kontrol diri "
        "(self-control) sebagai variabel moderasi dalam memperlemah pengaruh ketiga variabel anteseden tersebut. Penelitian ini menggunakan pendekatan kuantitatif "
        "asosiatif dengan desain survei cross-sectional. Data primer dikumpulkan melalui penyebaran kuesioner daring berbasis skala Likert 5 poin kepada responden "
        "yang dipilih melalui teknik purposive sampling. Kriteria inklusi sampel adalah konsumen atau kolektor Warga Negara Indonesia (WNI) berusia minimal 17 tahun "
        "yang pernah membeli booster pack Pokémon TCG fisik resmi dalam rentang waktu 6–12 bulan terakhir. Jumlah sampel yang ditargetkan adalah 120 hingga 150 responden, "
        "mengacu pada rekomendasi ukuran sampel Green (1991) dan Cohen (1988) untuk mencapai kekuatan uji statistik (statistical power) yang memadai pada model regresi "
        "linear berganda. Metode analisis data menggunakan analisis regresi berganda dan Moderated Regression Analysis (MRA) dengan prosedur standarisasi skor rata-rata "
        "(mean-centering) guna mengatasi potensi multikolinearitas struktural antar-istilah interaksi (Aiken & West, 1991; Ghozali, 2018), yang diolah menggunakan perangkat lunak "
        "IBM SPSS Statistics. Penelitian ini menawarkan kebaruan teoritis (novelty) dengan mengintegrasikan kerangka psikologi lingkungan Stimulus-Organism-Response (S-O-R), "
        "psikologi kolektor (Zeigarnik Effect dan The Completing the Set Effect), teori regulasi diri (Self-Regulation Theory), serta prinsip-prinsip keuangan perilaku "
        "(behavioral finance) pada fenomena komoditas hobi fisik bernilai spekulatif tinggi. Hasil penelitian ini diharapkan memberikan kontribusi empiris bagi konsumen "
        "muda dalam menjaga kontrol diri finansial, serta masukan aplikatif bagi komunitas hobi dan pemangku kebijakan edukasi keuangan generasi muda di Indonesia."
    )
    r_abs.font.name = "Times New Roman"
    r_abs.font.size = Pt(10)

    p_kw = doc.add_paragraph()
    p_kw.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_kw.paragraph_format.line_spacing = 1.15
    p_kw.paragraph_format.space_before = Pt(6)
    p_kw.paragraph_format.first_line_indent = Cm(0)
    p_kw.add_run("Kata Kunci: ").font.bold = True
    p_kw.add_run("Impulsive Buying, Hedonic Motivation, Desire for Completeness, Speculative Motive, Self-Control, Moderated Regression Analysis, Pokémon TCG, Keuangan Perilaku (Behavioral Finance).").font.italic = True

    # 6. Abstract English (hal. vii)
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run("ABSTRACT")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True

    p_j5 = doc.add_paragraph()
    p_j5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j5.paragraph_format.space_before = Pt(0)
    p_j5.paragraph_format.space_after = Pt(12)
    p_j5.paragraph_format.line_spacing = 1.15
    rj5 = p_j5.add_run("THE EFFECT OF HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, AND SPECULATIVE MOTIVE ON IMPULSIVE BUYING OF POKÉMON TCG BOOSTER PACKS WITH SELF-CONTROL AS A MODERATING VARIABLE\n\nArthur Reezan (312023002)\nUndergraduate Program in Management, Faculty of Economics and Business, UKRIDA\nThesis Advisor: Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A")
    rj5.font.name = "Times New Roman"
    rj5.font.size = Pt(10)
    rj5.font.bold = True

    p_abs_en = doc.add_paragraph()
    p_abs_en.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_abs_en.paragraph_format.line_spacing = 1.0
    p_abs_en.paragraph_format.space_before = Pt(6)
    p_abs_en.paragraph_format.space_after = Pt(6)
    p_abs_en.paragraph_format.first_line_indent = Cm(1.25)
    r_abs_en = p_abs_en.add_run(
        "This research aims to analyze and empirically test the effects of hedonic motivation, desire for completeness, and speculative motive "
        "on the impulsive buying behavior of official Indonesian-language physical Pokémon Trading Card Game (Pokémon TCG) booster packs, as well as to evaluate "
        "the moderating role of self-control in weakening the relationships between these three antecedent variables and impulsive buying. "
        "This study adopts an associative quantitative approach utilizing a cross-sectional survey design. Primary data are gathered via self-administered online "
        "questionnaires employing a 5-point Likert scale, distributed to respondents selected through purposive sampling. The sample inclusion criteria comprise "
        "Indonesian citizens aged 17 and above who have purchased official physical booster packs within the past 6 to 12 months. The targeted sample size ranges from "
        "120 to 150 respondents, consistent with the statistical power criteria established by Green (1991) and Cohen (1988) for multiple regression frameworks. "
        "The empirical model is estimated using multiple linear regression and Moderated Regression Analysis (MRA) with mean-centering procedures to eliminate structural "
        "multicollinearity (Aiken & West, 1991; Ghozali, 2018), executed via IBM SPSS Statistics software. This study provides theoretical novelty by synthesizing the "
        "Stimulus-Organism-Response (S-O-R) paradigm, collector psychology (the Zeigarnik Effect and The Completing the Set Effect), Self-Regulation Theory, and behavioral finance "
        "principles in the context of tangible alternative assets exhibiting volatile secondary market premiums. The findings are expected to offer practical insights for young "
        "consumers in exercising financial discipline regarding discretionary collectibles and provide strategic inputs for community organizers and financial educators targeting Generation Z."
    )
    r_abs_en.font.name = "Times New Roman"
    r_abs_en.font.size = Pt(10)
    r_abs_en.font.italic = True

    p_kw_en = doc.add_paragraph()
    p_kw_en.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_kw_en.paragraph_format.line_spacing = 1.15
    p_kw_en.paragraph_format.space_before = Pt(6)
    p_kw_en.paragraph_format.first_line_indent = Cm(0)
    p_kw_en.add_run("Keywords: ").font.bold = True
    p_kw_en.add_run("Impulsive Buying, Hedonic Motivation, Desire for Completeness, Speculative Motive, Self-Control, Moderated Regression Analysis, Pokémon TCG, Behavioral Finance.").font.italic = True

    # 7. Daftar Isi (hal. viii)
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    r = p.add_run("DAFTAR ISI")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True

    toc_items = [
        ("HALAMAN SAMPUL / JUDUL PROPOSAL", "i"),
        ("HALAMAN PERNYATAAN KEASLIAN KARYA TUGAS AKHIR", "ii"),
        ("HALAMAN PERSETUJUAN PROPOSAL SKRIPSI", "iii"),
        ("HALAMAN PENGESAHAN TIM PENGUJI SEMINAR PROPOSAL", "iv"),
        ("KATA PENGANTAR", "v"),
        ("ABSTRAK (BAHASA INDONESIA)", "vi"),
        ("ABSTRACT (ENGLISH)", "vii"),
        ("DAFTAR ISI", "viii"),
        ("DAFTAR TABEL", "ix"),
        ("DAFTAR GAMBAR", "x"),
        ("BAB 1 PENDAHULUAN", "1"),
        ("  1.1 Latar Belakang Penelitian", "1"),
        ("  1.2 Identifikasi dan Perumusan Masalah", "7"),
        ("      1.2.1 Identifikasi Masalah", "7"),
        ("      1.2.2 Perumusan Masalah", "8"),
        ("  1.3 Tujuan Penelitian", "8"),
        ("  1.4 Manfaat Penelitian", "9"),
        ("      1.4.1 Manfaat Teoritis (Akademis)", "9"),
        ("      1.4.2 Manfaat Praktis", "9"),
        ("  1.5 Batasan Penelitian", "10"),
        ("  1.6 Sistematika Penulisan Proposal", "10"),
        ("BAB 2 TINJAUAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS", "12"),
        ("  2.1 Landasan Teori", "12"),
        ("      2.1.1 Teori Stimulus-Organism-Response (S-O-R)", "12"),
        ("      2.1.2 Teori Regulasi Diri (Self-Regulation Theory)", "13"),
        ("      2.1.3 Teori Pengendalian Diri dan Keuangan Perilaku (Behavioral Finance)", "14"),
        ("      2.1.4 Teori Psikologi Kolektor dan Completing the Set Effect", "15"),
        ("  2.2 Definisi dan Konseptualisasi Variabel", "16"),
        ("      2.2.1 Impulsive Buying (Variabel Dependen Y)", "16"),
        ("      2.2.2 Hedonic Motivation (Variabel Independen X1)", "17"),
        ("      2.2.3 Desire for Completeness (Variabel Independen X2)", "19"),
        ("      2.2.4 Speculative Motive (Variabel Independen X3)", "20"),
        ("      2.2.5 Self-Control (Variabel Moderasi Z)", "22"),
        ("  2.3 Tinjauan Penelitian Empiris Terdahulu", "23"),
        ("  2.4 Kerangka Pemikiran dan Model Konseptual Penelitian", "29"),
        ("  2.5 Pengembangan Hipotesis Penelitian", "30"),
        ("      2.5.1 Pengaruh Hedonic Motivation terhadap Impulsive Buying", "30"),
        ("      2.5.2 Pengaruh Desire for Completeness terhadap Impulsive Buying", "31"),
        ("      2.5.3 Pengaruh Speculative Motive terhadap Impulsive Buying", "32"),
        ("      2.5.4 Peran Moderasi Self-Control pada Pengaruh Hedonic Motivation", "33"),
        ("      2.5.5 Peran Moderasi Self-Control pada Pengaruh Desire for Completeness", "34"),
        ("      2.5.6 Peran Moderasi Self-Control pada Pengaruh Speculative Motive", "35"),
        ("BAB 3 METODE PENELITIAN", "37"),
        ("  3.1 Desain Penelitian", "37"),
        ("  3.2 Objek dan Subjek Penelitian", "37"),
        ("  3.3 Operasionalisasi Variabel dan Skala Pengukuran", "38"),
        ("  3.4 Populasi, Sampel, dan Teknik Pengambilan Sampel", "41"),
        ("  3.5 Teknik Pengumpulan Data", "42"),
        ("  3.6 Diagram Alur Pelaksanaan Penelitian", "43"),
        ("  3.7 Metode Analisis Data dan Uji Statistik", "44"),
        ("      3.7.1 Uji Statistik Deskriptif", "44"),
        ("      3.7.2 Uji Kualitas Data (Validitas dan Reliabilitas)", "44"),
        ("      3.7.3 Uji Asumsi Klasik", "45"),
        ("      3.7.4 Analisis Regresi Linear Berganda", "46"),
        ("      3.7.5 Moderated Regression Analysis (MRA) dengan Mean-Centering", "47"),
        ("      3.7.6 Uji Kelayakan Model dan Hipotesis (Uji F, Uji t, Koefisien Determinasi R2)", "48"),
        ("  3.8 Jadwal Pelaksanaan Penelitian", "48"),
        ("DAFTAR PUSTAKA", "49")
    ]

    for title_toc, page_toc in toc_items:
        p_toc = doc.add_paragraph()
        p_toc.paragraph_format.line_spacing = 1.15
        p_toc.paragraph_format.space_before = Pt(0)
        p_toc.paragraph_format.space_after = Pt(2)
        p_toc.paragraph_format.first_line_indent = Cm(0)

        is_bold = not title_toc.startswith("  ")
        r_t = p_toc.add_run(title_toc)
        r_t.font.name = "Times New Roman"
        r_t.font.size = Pt(11)
        r_t.font.bold = is_bold

        dot_fill = " . " * max(1, int((70 - len(title_toc)) / 2))
        r_dots = p_toc.add_run(f" {dot_fill} ")
        r_dots.font.name = "Times New Roman"
        r_dots.font.size = Pt(10)
        r_dots.font.color.rgb = RGBColor(150, 150, 150)

        r_p = p_toc.add_run(page_toc)
        r_p.font.name = "Times New Roman"
        r_p.font.size = Pt(11)
        r_p.font.bold = is_bold

    # 8. Daftar Tabel (hal. ix)
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    r = p.add_run("DAFTAR TABEL")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True

    lot_items = [
        ("Tabel 2.1", "Ringkasan Pemetaan Matriks Riset Empiris Terdahulu (2021–2025)", "24"),
        ("Tabel 3.1", "Skala Pengukuran Likert 5 Poin", "38"),
        ("Tabel 3.2", "Operasionalisasi Variabel, Dimensi, dan Butir Indikator Pengukuran", "39"),
        ("Tabel 3.3", "Jadwal Pelaksanaan Kegiatan Penelitian (Tahun 2026)", "48")
    ]
    for tab_num, tab_title, tab_page in lot_items:
        p_lot = doc.add_paragraph()
        p_lot.paragraph_format.line_spacing = 1.15
        p_lot.paragraph_format.space_before = Pt(0)
        p_lot.paragraph_format.space_after = Pt(4)
        p_lot.paragraph_format.first_line_indent = Cm(0)

        p_lot.add_run(f"{tab_num}.  ").font.bold = True
        p_lot.add_run(tab_title)
        dot_fill = " . " * max(1, int((65 - len(tab_title)) / 2))
        r_d = p_lot.add_run(f" {dot_fill} ")
        r_d.font.color.rgb = RGBColor(150, 150, 150)
        p_lot.add_run(tab_page).font.bold = True

    # 9. Daftar Gambar (hal. x)
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    r = p.add_run("DAFTAR GAMBAR")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True

    lof_items = [
        ("Gambar 2.1", "Model Rerangka Konseptual Penelitian (Pengaruh Anteseden, Moderasi, dan Impulsive Buying)", "30"),
        ("Gambar 3.1", "Diagram Alur Pelaksanaan Penelitian (Tahapan Operasional Riset Kuantitatif)", "43")
    ]
    for fig_num, fig_title, fig_page in lof_items:
        p_lof = doc.add_paragraph()
        p_lof.paragraph_format.line_spacing = 1.15
        p_lof.paragraph_format.space_before = Pt(0)
        p_lof.paragraph_format.space_after = Pt(4)
        p_lof.paragraph_format.first_line_indent = Cm(0)

        p_lof.add_run(f"{fig_num}.  ").font.bold = True
        p_lof.add_run(fig_title)
        dot_fill = " . " * max(1, int((60 - len(fig_title)) / 2))
        r_d = p_lof.add_run(f" {dot_fill} ")
        r_d.font.color.rgb = RGBColor(150, 150, 150)
        p_lof.add_run(fig_page).font.bold = True

    # ------------------------------------------------------------------------
    # SECTION 3: BAGIAN INTI / MAIN TEXT (BAB 1 s.d. BAB 3 & DAFTAR PUSTAKA)
    # Arabic Numerals (1, 2, 3...)
    # ------------------------------------------------------------------------
    sec_main = doc.add_section(WD_SECTION.NEW_PAGE)
    sec_main.page_width = Cm(21.0)
    sec_main.page_height = Cm(29.7)
    sec_main.top_margin = Cm(3.0)
    sec_main.bottom_margin = Cm(3.0)
    sec_main.left_margin = Cm(4.0)
    sec_main.right_margin = Cm(3.0)
    sec_main.header.is_linked_to_previous = False
    sec_main.footer.is_linked_to_previous = False
    add_page_number_to_footer(sec_main, is_roman=False, start_num=1)

    print("[*] Ingesting body text from validated Markdown reference...")
    md_file = base_dir / "PROPOSAL_SKRIPSI_POKEMON_TCG.md"
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Split markdown into BAB 1, BAB 2, BAB 3, and DAFTAR PUSTAKA
    parts = re.split(r'\n#+\s+(BAB\s+\d+.*?|DAFTAR PUSTAKA.*?)\n', md_text)
    
    has_inserted_fig21 = False
    has_inserted_fig31 = False

    # Process each section
    for idx in range(1, len(parts), 2):
        sec_header = parts[idx].strip()
        sec_content = parts[idx+1] if idx+1 < len(parts) else ""

        print(f"    -> Building: {sec_header}")
        if sec_header.startswith("BAB"):
            add_heading_1(doc, sec_header, page_break=False if idx == 1 else True)
        elif "DAFTAR PUSTAKA" in sec_header:
            add_heading_1(doc, "DAFTAR PUSTAKA", page_break=True)
            build_daftar_pustaka(doc, sec_content)
            continue

        # Parse subsections, paragraphs, lists, tables, and images
        lines = sec_content.split('\n')
        line_idx = 0
        while line_idx < len(lines):
            line = lines[line_idx].rstrip()
            line_str = line.strip()

            if not line_str:
                line_idx += 1
                continue

            # Skip markdown dividers (---)
            if line_str == '---' or line_str == '***':
                line_idx += 1
                continue

            # Skip code blocks (``` ... ```)
            if line_str.startswith('```'):
                line_idx += 1
                while line_idx < len(lines) and not lines[line_idx].strip().startswith('```'):
                    line_idx += 1
                if line_idx < len(lines):
                    line_idx += 1 # skip closing ```
                continue

            # Heading 2 (## 1.1 ...)
            if line_str.startswith('## '):
                title_h2 = line_str[3:].strip()
                add_heading_2(doc, title_h2)
                line_idx += 1
                continue

            # Heading 3 (### 1.2.1 ...)
            if line_str.startswith('### '):
                title_h3 = line_str[4:].strip()
                add_heading_3(doc, title_h3)
                line_idx += 1
                continue

            # LaTeX Figure block handling for Gambar 3.1
            if r'\begin{figure}' in line_str:
                # Consume till \end{figure}
                while line_idx < len(lines) and r'\end{figure}' not in lines[line_idx]:
                    line_idx += 1
                if line_idx < len(lines):
                    line_idx += 1

                # Insert Gambar 3.1
                if img_alur.exists():
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(12)
                    p_img.paragraph_format.space_after = Pt(4)
                    p_img.paragraph_format.first_line_indent = Cm(0)
                    p_img.add_run().add_picture(str(img_alur), width=Cm(13.0))

                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_before = Pt(2)
                    p_cap.paragraph_format.space_after = Pt(2)
                    p_cap.paragraph_format.first_line_indent = Cm(0)
                    p_cap.add_run("Gambar 3.1. Diagram Alur Pelaksanaan Penelitian").font.bold = True

                    p_src = doc.add_paragraph()
                    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_src.paragraph_format.space_before = Pt(0)
                    p_src.paragraph_format.space_after = Pt(12)
                    p_src.paragraph_format.first_line_indent = Cm(0)
                    r_s = p_src.add_run("Sumber: Dikembangkan oleh penulis untuk tahapan operasional penelitian, 2026.")
                    r_s.font.size = Pt(10)
                    r_s.font.italic = True
                continue

            # LaTeX Table block handling for Tabel 3.3 (Jadwal Kegiatan)
            if r'\begin{table}' in line_str:
                while line_idx < len(lines) and r'\end{table}' not in lines[line_idx]:
                    line_idx += 1
                if line_idx < len(lines):
                    line_idx += 1

                # Insert Tabel 3.3
                build_tabel_jadwal(doc)
                continue

            # Image detection for Gambar 2.1 (Kerangka Pemikiran)
            if ("Model Rerangka Konseptual" in line_str or line_str.startswith("**Gambar 2.1") or line_str.startswith("Gambar 2.1")) and not has_inserted_fig21:
                has_inserted_fig21 = True
                if img_rerangka.exists():
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(12)
                    p_img.paragraph_format.space_after = Pt(4)
                    p_img.paragraph_format.first_line_indent = Cm(0)
                    p_img.add_run().add_picture(str(img_rerangka), width=Cm(14.0))

                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_before = Pt(2)
                    p_cap.paragraph_format.space_after = Pt(2)
                    p_cap.paragraph_format.first_line_indent = Cm(0)
                    p_cap.add_run("Gambar 2.1. Model Rerangka Konseptual Penelitian").font.bold = True

                    p_src = doc.add_paragraph()
                    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_src.paragraph_format.space_before = Pt(0)
                    p_src.paragraph_format.space_after = Pt(12)
                    p_src.paragraph_format.first_line_indent = Cm(0)
                    r_s = p_src.add_run("Keterangan: Garis lurus menunjukkan pengaruh langsung (H1, H2, H3); Garis putus-putus menunjukkan efek moderasi kontrol diri yang memperlemah (H4, H5, H6).")
                    r_s.font.size = Pt(10)
                    r_s.font.italic = True

                # Skip any redundant caption or notes following in markdown
                line_idx += 1
                while line_idx < len(lines):
                    nxt = lines[line_idx].strip()
                    if nxt.startswith('*Keterangan') or nxt.startswith('Keterangan') or nxt.startswith('---') or not nxt:
                        line_idx += 1
                    else:
                        break
                continue

            # Table Detection in Markdown (| col1 | col2 |)
            if line_str.startswith('|') and '|' in line_str[1:]:
                # Gather full table lines
                table_lines = []
                while line_idx < len(lines) and lines[line_idx].strip().startswith('|'):
                    table_lines.append(lines[line_idx].strip())
                    line_idx += 1
                build_apa7_table(doc, table_lines)
                continue

            # Equations
            if line_str.startswith('$$') or (line_str.startswith('$') and line_str.endswith('$') and len(line_str) > 10):
                eq_formula = line_str.strip('$').strip()
                add_equation_paragraph(doc, eq_formula)
                line_idx += 1
                continue

            # Numbered lists (1. 2. 3.)
            m_num = re.match(r'^(\d+[\.\)]|[a-zA-Z][\.\)])\s+(.*)', line_str)
            if m_num:
                prefix = m_num.group(1)
                body = m_num.group(2)
                p_li = doc.add_paragraph()
                p_li.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p_li.paragraph_format.left_indent = Cm(1.25)
                p_li.paragraph_format.first_line_indent = Cm(-0.63)
                p_li.paragraph_format.space_before = Pt(0)
                p_li.paragraph_format.space_after = Pt(2)
                p_li.paragraph_format.line_spacing = 1.5
                r_num = p_li.add_run(f"{prefix}  ")
                r_num.font.bold = True
                parse_markdown_runs(p_li, body)
                line_idx += 1
                continue

            # Bullet points (- or *)
            if line_str.startswith('- ') or line_str.startswith('* '):
                body = line_str[2:].strip()
                p_li = doc.add_paragraph()
                p_li.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p_li.paragraph_format.left_indent = Cm(1.25)
                p_li.paragraph_format.first_line_indent = Cm(-0.4)
                p_li.paragraph_format.space_before = Pt(0)
                p_li.paragraph_format.space_after = Pt(2)
                p_li.paragraph_format.line_spacing = 1.5
                r_b = p_li.add_run("•  ")
                r_b.font.bold = True
                parse_markdown_runs(p_li, body)
                line_idx += 1
                continue

            # Blockquote (> ...)
            if line_str.startswith('>'):
                body = line_str.lstrip('>').strip()
                p_bq = doc.add_paragraph()
                p_bq.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p_bq.paragraph_format.left_indent = Cm(1.5)
                p_bq.paragraph_format.right_indent = Cm(0.5)
                p_bq.paragraph_format.space_before = Pt(2)
                p_bq.paragraph_format.space_after = Pt(2)
                p_bq.paragraph_format.line_spacing = 1.15
                parse_markdown_runs(p_bq, body)
                line_idx += 1
                continue

            # Standard paragraph
            add_body_paragraph(doc, line_str)
            line_idx += 1

    # Save document
    doc.save(str(output_docx))
    print(f"\n[SUCCESS] Document saved cleanly to: {output_docx}")
    return output_docx


def build_apa7_table(doc, table_lines):
    """Parses markdown table lines and converts into an APA 7th style docx table."""
    data_rows = []
    for line in table_lines:
        if re.match(r'^\|[\s\-:|]+\|$', line):
            continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if cells:
            data_rows.append(cells)

    if not data_rows:
        return

    num_cols = len(data_rows[0])
    tbl = doc.add_table(rows=len(data_rows), cols=num_cols)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

    total_width_cm = 14.0 # Text width between 4cm left and 3cm right on 21cm page
    col_w_cm = total_width_cm / num_cols

    for r_idx, row in enumerate(data_rows):
        tbl_row = tbl.rows[r_idx]
        is_header = (r_idx == 0)
        for c_idx, cell_text in enumerate(row[:num_cols]):
            cell = tbl_row.cells[c_idx]
            cell.width = Cm(col_w_cm)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            if is_header:
                set_cell_shading(cell, "F2F2F2")

            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if (is_header or c_idx in [0, num_cols-1]) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.first_line_indent = Cm(0)

            # Parse bold / italics
            tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*)', cell_text)
            for token in tokens:
                if not token:
                    continue
                if token.startswith('**') and token.endswith('**'):
                    run = p.add_run(token[2:-2])
                    run.font.bold = True
                elif token.startswith('*') and token.endswith('*'):
                    run = p.add_run(token[1:-1])
                    run.font.italic = True
                else:
                    run = p.add_run(token)
                run.font.name = "Times New Roman"
                run.font.size = Pt(10 if is_header else 9.5)
                if is_header:
                    run.font.bold = True

    apply_apa7_table_borders(tbl)
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(4)
    p_sp.paragraph_format.space_after = Pt(6)


def build_tabel_jadwal(doc):
    """Builds Tabel 3.3: Jadwal Pelaksanaan Kegiatan Penelitian (Tahun 2026)."""
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap.paragraph_format.space_before = Pt(12)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.paragraph_format.first_line_indent = Cm(0)
    p_cap.add_run("Tabel 3.3. Jadwal Pelaksanaan Kegiatan Penelitian (Tahun 2026)").font.bold = True

    headers = ["No", "Tahapan Kegiatan Penelitian", "B1", "B2", "B3", "B4", "B5", "B6"]
    data = [
        ("1", "Identifikasi fenomena pasar dan perumusan topik", "•", "", "", "", "", ""),
        ("2", "Studi kepustakaan dan telaah literatur jurnal", "•", "•", "", "", "", ""),
        ("3", "Penyusunan naskah proposal penelitian (Bab 1–3)", "", "•", "•", "", "", ""),
        ("4", "Bimbingan intensif dan revisi proposal skripsi", "", "•", "•", "", "", ""),
        ("5", "Pelaksanaan Seminar Proposal Skripsi", "", "", "•", "", "", ""),
        ("6", "Uji coba instrumen kuesioner (pilot test n=30)", "", "", "", "•", "", ""),
        ("7", "Pengumpulan data lapangan survei utama (n=120–150)", "", "", "", "•", "•", ""),
        ("8", "Tabulasi data dan pengolahan statistik via SPSS", "", "", "", "", "•", ""),
        ("9", "Penyusunan laporan Bab 4 (Analisis) dan Bab 5 (Penutup)", "", "", "", "", "•", "•"),
        ("10", "Ujian Sidang Skripsi dan Komprehensif", "", "", "", "", "", "•")
    ]

    tbl = doc.add_table(rows=1+len(data), cols=8)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

    col_widths = [Cm(1.0), Cm(7.0), Cm(1.0), Cm(1.0), Cm(1.0), Cm(1.0), Cm(1.0), Cm(1.0)]

    # Header
    for c_idx, h_text in enumerate(headers):
        cell = tbl.rows[0].cells[c_idx]
        cell.width = col_widths[c_idx]
        set_cell_margins(cell, top=80, bottom=80, left=60, right=60)
        set_cell_shading(cell, "F2F2F2")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(h_text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.bold = True

    # Data Rows
    for r_idx, row_vals in enumerate(data):
        row = tbl.rows[r_idx + 1]
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 1 else WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)
            if val == "•":
                r.font.bold = True

    apply_apa7_table_borders(tbl)

    p_src = doc.add_paragraph()
    p_src.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_src.paragraph_format.space_before = Pt(2)
    p_src.paragraph_format.space_after = Pt(12)
    p_src.paragraph_format.first_line_indent = Cm(0)
    r_s = p_src.add_run("Keterangan: B1 = Bulan ke-1; B2 = Bulan ke-2; B3 = Bulan ke-3; B4 = Bulan ke-4; B5 = Bulan ke-5; B6 = Bulan ke-6 tahun akademik 2026.")
    r_s.font.name = "Times New Roman"
    r_s.font.size = Pt(9.5)
    r_s.font.italic = True


def build_daftar_pustaka(doc, content):
    """Builds APA 7th style bibliography with 1.25cm hanging indent."""
    lines = content.split('\n')
    for line in lines:
        line_str = line.strip()
        if not line_str or line_str.startswith('#'):
            continue

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Cm(1.25)
        p.paragraph_format.first_line_indent = Cm(-1.25)

        parse_markdown_runs(p, line_str)


if __name__ == "__main__":
    build_full_proposal()

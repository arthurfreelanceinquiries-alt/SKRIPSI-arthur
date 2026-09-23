"""
build_study_guide_pdf.py
Converts PANDUAN_BELAJAR_PROPOSAL.md to a clean, readable PDF.

Layer 3 Execution Script (3-Layer Architecture)
Directive: directives/update_study_guide_and_pdf.md

Engine: ReportLab (pure Python, full Unicode support via Helvetica)
Usage:
    python execution/build_study_guide_pdf.py
Output:
    02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.pdf
"""

import sys
import re
from pathlib import Path

# Ensure UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Resolve paths
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
INPUT_MD = BASE_DIR / "02_Persiapan_Sidang" / "PANDUAN_BELAJAR_PROPOSAL.md"
OUTPUT_PDF = BASE_DIR / "02_Persiapan_Sidang" / "PANDUAN_BELAJAR_PROPOSAL.pdf"

# A4 dimensions in points (ReportLab uses pts by default: 1pt = 1/72 inch)
PAGE_W = 595.28
PAGE_H = 841.89
MARGIN_L = 60
MARGIN_R = 50
MARGIN_T = 56
MARGIN_B = 56
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R


# CATATAN FONT: PDF panduan memakai Helvetica (WinAnsi) — subscript unicode
# ₁₂₃ (U+2080+), ᵢ (U+1D62), dan ☐/☑ TIDAK punya glyph (tofu ■). Maka digit
# subscript ditulis polos (X1), dan checkbox memakai ( )/(x). Superscript
# ¹²³ (Latin-1) AMAN. Hasil probe render 23 Sep 2026.
LATEX_UNICODE = [
    (r'\\text\{([^}]*)\}', r'\1'),
    (r'\\bar\{X\}_i', 'mean(Xi)'),
    (r'\\bar\{M\}', 'mean(M)'),
    (r'\\bar\{([A-Za-z])\}', r'mean(\1)'),
    (r'\\alpha', '\u03b1'), (r'\\beta', '\u03b2'),
    (r'\\Delta', '\u0394'), (r'\\cdot', '\u00b7'),
    (r'\\ge', '\u2265'), (r'\\le', '\u2264'),
    (r'\\times', '\u00d7'), (r'\\rightarrow', '\u2192'),
    (r'\\quad', ' '), (r'\\[ ,;]', ' '),
]
_SUP = {'1': '\u00b9', '2': '\u00b2', '3': '\u00b3'}


def _latex_to_unicode(s: str) -> str:
    """Convert common LaTeX math fragments to readable unicode (rule M1/M2)."""
    for pat, rep in LATEX_UNICODE:
        s = re.sub(pat, rep, s)
    s = re.sub(r'_\{?([1-7])\}?', r'\1', s)  # X_1 -> X1 (subscript tofu)
    s = re.sub(r'_\{?i\}?', 'i', s)  # X_i -> Xi (setelah \bar ditangani)
    s = re.sub(r'\^([123])', lambda m: _SUP[m.group(1)], s)
    s = re.sub(r'\^(?=\*)', '', s)  # M^* -> M*
    s = re.sub(r'r_\{?hitung\}?', 'r-hitung', s)
    s = re.sub(r'r_\{?tabel\}?', 'r-tabel', s)
    s = re.sub(r'[{}]', '', s)
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    return s


def strip_inline_md(text: str) -> str:
    """Remove inline markdown markers from text for plain-text rendering.

    Math is extracted to placeholders FIRST so markdown *-stripping never
    eats asterisks inside formulas (e.g. X_i^* ... M^*).
    """
    held = []

    def _hold(m):
        held.append(_latex_to_unicode(m.group(1)))
        return '\x00%d\x00' % len(held)

    text = re.sub(r'\$\$(.+?)\$\$', _hold, text, flags=re.S)
    text = re.sub(r'\$([^$\n]+?)\$', _hold, text)
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'\1', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'`(.*?)`', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    for i, conv in enumerate(held, 1):
        text = text.replace('\x00%d\x00' % i, conv)
    # Printable checklist (rule M6): ( ) Helvetica-safe (☐/☑ tofu di WinAnsi).
    text = re.sub(r'^\s*(?:- )?\[ \]', '( ) ', text)
    text = re.sub(r'^\s*(?:- )?\[x\]', '(x) ', text, flags=re.I)
    text = re.sub(r'[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]',
                  '', text)
    # Replace special chars that may cause issues
    text = text.replace('\u2014', '-').replace('\u2013', '-').replace('\u2019', "'").replace('\u2018', "'")
    text = text.replace('\u201c', '"').replace('\u201d', '"').replace('\u00ae', '(R)').replace('\u00e9', 'e')
    text = text.replace('\u00e8', 'e').replace('\u00e0', 'a').replace('\u2026', '...')
    return text.strip()


def build_pdf(input_path: Path, output_path: Path):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.units import cm, mm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
        Table, TableStyle, PageBreak, Preformatted
    )
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
    from reportlab.lib.colors import HexColor, white, black

    # --- Color palette ---
    C_DARK_BLUE  = HexColor('#1a237e')
    C_MED_BLUE   = HexColor('#283593')
    C_LIGHT_BLUE = HexColor('#3f51b5')
    C_ACCENT     = HexColor('#90caf9')
    C_BG_BQ      = HexColor('#e3f2fd')
    C_TABLE_HDR  = HexColor('#1a237e')
    C_TABLE_ALT  = HexColor('#e8eaf6')
    C_TABLE_BRD  = HexColor('#c5cae9')
    C_CODE_BG    = HexColor('#263238')
    C_CODE_FG    = HexColor('#eceff1')
    C_TEXT       = HexColor('#1a1a1a')
    C_GRAY       = HexColor('#546e7a')
    C_HR         = HexColor('#c5cae9')

    base_styles = getSampleStyleSheet()

    # --- Define custom styles ---
    styles = {
        'h1': ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=15, textColor=C_DARK_BLUE,
                             spaceAfter=10, spaceBefore=16, alignment=TA_LEFT),
        'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=12, textColor=C_MED_BLUE,
                             spaceAfter=6, spaceBefore=12, alignment=TA_LEFT,
                             backColor=C_BG_BQ, leftIndent=6, rightIndent=6,
                             borderPad=4, borderRadius=2),
        'h3': ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=11, textColor=C_LIGHT_BLUE,
                             spaceAfter=4, spaceBefore=8, alignment=TA_LEFT),
        'h4': ParagraphStyle('h4', fontName='Helvetica-Bold', fontSize=10.5, textColor=C_GRAY,
                             spaceAfter=3, spaceBefore=6, alignment=TA_LEFT),
        'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10, textColor=C_TEXT,
                               leading=14, spaceAfter=4, spaceBefore=2,
                               alignment=TA_JUSTIFY),
        'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=10, textColor=C_TEXT,
                                 leading=14, spaceAfter=2, spaceBefore=0,
                                 leftIndent=12, bulletIndent=0, alignment=TA_LEFT),
        'blockquote': ParagraphStyle('bq', fontName='Helvetica-Oblique', fontSize=10,
                                     textColor=C_MED_BLUE, leading=13, spaceAfter=4, spaceBefore=4,
                                     leftIndent=8, rightIndent=8, backColor=C_BG_BQ,
                                     borderColor=C_ACCENT, borderWidth=0, alignment=TA_LEFT),
        'code': ParagraphStyle('code', fontName='Courier', fontSize=8.5, textColor=C_CODE_FG,
                               backColor=C_CODE_BG, leading=11, spaceAfter=6, spaceBefore=6,
                               leftIndent=8, rightIndent=8),
        'cover_title': ParagraphStyle('ct', fontName='Helvetica-Bold', fontSize=20,
                                      textColor=C_DARK_BLUE, spaceAfter=8, alignment=TA_CENTER),
        'cover_sub': ParagraphStyle('cs', fontName='Helvetica-Bold', fontSize=14,
                                    textColor=C_MED_BLUE, spaceAfter=12, alignment=TA_CENTER),
        'cover_body': ParagraphStyle('cb', fontName='Helvetica', fontSize=10,
                                     textColor=C_TEXT, spaceAfter=4, alignment=TA_CENTER),
        'footer': ParagraphStyle('ft', fontName='Helvetica-Oblique', fontSize=8.5,
                                 textColor=C_LIGHT_BLUE, alignment=TA_CENTER),
    }

    story = []

    # ---- COVER PAGE ----
    story.append(Spacer(1, 40))
    story.append(Paragraph("PANDUAN BELAJAR &amp; PENGUASAAN MATERI", styles['cover_title']))
    story.append(Paragraph("PROPOSAL SKRIPSI", styles['cover_sub']))
    story.append(HRFlowable(width='100%', thickness=2, color=C_DARK_BLUE, spaceAfter=14))
    story.append(Paragraph(
        '"PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE '
        'TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKEMON TCG '
        'DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI"',
        styles['cover_body']
    ))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Program Studi S1 Manajemen — Konsentrasi Manajemen Keuangan", styles['cover_body']))
    story.append(Paragraph("Universitas Kristen Krida Wacana (UKRIDA)", styles['cover_body']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Arthur Reezan | NIM: 312023002</b>", styles['cover_body']))
    story.append(Paragraph("Pembimbing: Dr. Fredella Colline, S.E., M.M., CFP(R), PFM, CHCP-A", styles['cover_body']))
    story.append(Paragraph("Versi 3.0 | September 2026", styles['cover_body']))
    story.append(HRFlowable(width='100%', thickness=1, color=C_MED_BLUE, spaceBefore=14))
    story.append(PageBreak())

    # ---- PARSE MARKDOWN ----
    print(f"[*] Reading source: {input_path}")
    lines = input_path.read_text(encoding='utf-8').splitlines()

    in_code = False
    code_lines = []
    in_bq = False
    bq_lines = []
    in_table = False
    table_lines_buf = []

    # Box-drawing (Courier/Helvetica tak punya glyph -> tofu). Petakan ke ASCII.
    _BOX = str.maketrans({'┌': '+', '┐': '+', '└': '+', '┘': '+', '├': '+',
                          '┤': '+', '┬': '+', '┴': '+', '┼': '+', '─': '-',
                          '│': '|', '►': '>', '▲': '^', '▼': 'v'})

    def flush_code():
        nonlocal code_lines, in_code
        if code_lines:
            txt = '\n'.join(strip_inline_md(l).translate(_BOX)
                            for l in code_lines)
            story.append(Preformatted(txt, styles['code']))
            story.append(Spacer(1, 4))
        code_lines = []
        in_code = False

    def flush_bq():
        nonlocal bq_lines, in_bq
        if bq_lines:
            txt = ' '.join(bq_lines)
            story.append(Paragraph(strip_inline_md(txt), styles['blockquote']))
            story.append(Spacer(1, 4))
        bq_lines = []
        in_bq = False

    def flush_table():
        nonlocal table_lines_buf, in_table
        if len(table_lines_buf) < 2:
            table_lines_buf = []
            in_table = False
            return
        headers = [strip_inline_md(c).strip() for c in table_lines_buf[0].strip('|').split('|')]
        data_rows = [
            [strip_inline_md(c).strip() for c in r.strip('|').split('|')]
            for r in table_lines_buf[2:]
        ]
        if not headers:
            table_lines_buf = []
            in_table = False
            return

        n_cols = len(headers)
        col_w = CONTENT_W / n_cols

        tbl_data = [headers] + data_rows
        t = Table(tbl_data, colWidths=[col_w] * n_cols, repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), C_TABLE_HDR),
            ('TEXTCOLOR',  (0, 0), (-1, 0), white),
            ('FONTNAME',   (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE',   (0, 0), (-1, 0), 9),
            ('ALIGN',      (0, 0), (-1, 0), 'CENTER'),
            ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME',   (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE',   (0, 1), (-1, -1), 8.5),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, C_TABLE_ALT]),
            ('GRID',       (0, 0), (-1, -1), 0.5, C_TABLE_BRD),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ]))
        story.append(Spacer(1, 6))
        story.append(t)
        story.append(Spacer(1, 8))
        table_lines_buf = []
        in_table = False

    for raw_line in lines:
        line = raw_line.rstrip()

        # Code blocks
        if line.strip().startswith('```'):
            if in_code:
                flush_code()
            else:
                if in_bq: flush_bq()
                if in_table: flush_table()
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        # Tables
        if line.strip().startswith('|'):
            if in_bq: flush_bq()
            table_lines_buf.append(line)
            in_table = True
            continue
        else:
            if in_table:
                flush_table()

        # Blockquotes
        if line.startswith('>'):
            inner = line[1:].strip()
            inner = re.sub(r'^\[!\w+\]\s*', '', inner)
            if inner:
                bq_lines.append(inner)
            in_bq = True
            continue
        else:
            if in_bq:
                flush_bq()

        # Horizontal rules
        if re.match(r'^[-*=]{3,}$', line.strip()):
            story.append(HRFlowable(width='100%', thickness=0.5, color=C_HR,
                                    spaceBefore=8, spaceAfter=8))
            continue

        # Headings
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            level = len(m.group(1))
            text = strip_inline_md(m.group(2))
            if level == 1:
                story.append(PageBreak())
                story.append(Paragraph(text, styles['h1']))
                story.append(HRFlowable(width='100%', thickness=1.5, color=C_DARK_BLUE, spaceAfter=6))
            elif level == 2:
                story.append(Paragraph(text, styles['h2']))
            elif level == 3:
                story.append(Paragraph(text, styles['h3']))
            else:
                story.append(Paragraph(text, styles['h4']))
            continue

        # Lists
        m_bullet = re.match(r'^(\s*)([-*\u2022])\s+(.*)', line)
        if m_bullet:
            indent = len(m_bullet.group(1)) // 2
            item_text = strip_inline_md(m_bullet.group(3))
            s = ParagraphStyle(f'bul{indent}', parent=styles['bullet'],
                               leftIndent=12 + indent * 14, bulletIndent=0 + indent * 14)
            story.append(Paragraph(f'• {item_text}', s))
            continue

        m_num = re.match(r'^(\s*)(\d+[\.\)])\s+(.*)', line)
        if m_num:
            indent = len(m_num.group(1)) // 2
            num_label = m_num.group(2)
            item_text = strip_inline_md(m_num.group(3))
            s = ParagraphStyle(f'num{indent}', parent=styles['bullet'],
                               leftIndent=16 + indent * 14)
            story.append(Paragraph(f'{num_label} {item_text}', s))
            continue

        # Empty line
        if not line.strip():
            story.append(Spacer(1, 4))
            continue

        # Regular paragraph
        text = strip_inline_md(line)
        if text:
            story.append(Paragraph(text, styles['body']))

    # Flush remainders
    if in_code and code_lines:
        flush_code()
    if in_bq and bq_lines:
        flush_bq()
    if in_table and table_lines_buf:
        flush_table()

    # --- Build PDF ---
    def on_first_page(canvas, doc):
        canvas.saveState()
        canvas.restoreState()

    def on_later_pages(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica-Oblique', 8.5)
        canvas.setFillColor(C_LIGHT_BLUE)
        canvas.drawCentredString(
            PAGE_W / 2, 28,
            f"Panduan Belajar Proposal Skripsi | Arthur Reezan (312023002) | Hal. {doc.page}"
        )
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=MARGIN_L,
        rightMargin=MARGIN_R,
        topMargin=MARGIN_T,
        bottomMargin=MARGIN_B,
        title="Panduan Belajar Proposal Skripsi - Arthur Reezan",
        author="Arthur Reezan",
        subject="Proposal Skripsi Pokemon TCG",
    )

    print(f"[*] Building PDF with ReportLab...")
    doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)

    size_kb = output_path.stat().st_size / 1024
    print(f"\n[OK] PDF generated successfully!")
    print(f"     Output : {output_path}")
    print(f"     Size   : {size_kb:.1f} KB")


if __name__ == "__main__":
    if not INPUT_MD.exists():
        print(f"[ERROR] Input file not found: {INPUT_MD}")
        sys.exit(1)
    build_pdf(INPUT_MD, OUTPUT_PDF)

"""
build_proposal_nobab3_pdf.py
Generates a thesis-quality PDF of the proposal WITHOUT Bab 3.

Layer 3 Execution Script (3-Layer Architecture)
Directive: directives/build_docx_without_chapter3.md

Engine: ReportLab (pure Python, full Unicode support)
Usage:
    python execution/build_proposal_nobab3_pdf.py
Output:
    01_Naskah_Utama/Proposal_Arthur_NoBab3.pdf
"""

import sys
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR   = SCRIPT_DIR.parent
INPUT_MD   = BASE_DIR / "01_Naskah_Utama" / "PROPOSAL_SKRIPSI_POKEMON_TCG.md"
OUTPUT_PDF = BASE_DIR / "01_Naskah_Utama" / "Proposal_Arthur_NoBab3.pdf"


# ── Unicode normaliser ────────────────────────────────────────────────────────
REPLACEMENTS = {
    '\u2014': '-', '\u2013': '-', '\u2019': "'", '\u2018': "'",
    '\u201c': '"', '\u201d': '"', '\u00ae': '(R)', '\u00e9': 'e',
    '\u00e8': 'e', '\u00e0': 'a', '\u2026': '...', '\u00e1': 'a',
    '\u00ed': 'i', '\u00f3': 'o', '\u00fa': 'u', '\u00f1': 'n',
    '\u00e9': 'e', '\u00e9': 'e', '\u2022': '*', '\u00b7': '.',
    '\u03b1': 'alpha', '\u03b2': 'beta', '\u03b5': 'e',
    '\u2248': '~', '\u2265': '>=', '\u2264': '<=', '\u00d7': 'x',
    '\u00f7': '/', '\u0394': 'D', '\u03a3': 'S', '\u03bc': 'u',
    '\u00b2': '^2', '\u00b3': '^3',
}

def normalise(text: str) -> str:
    for src, dst in REPLACEMENTS.items():
        text = text.replace(src, dst)
    # Strip any HTML tags (e.g. <br>, <para>, etc.)
    text = re.sub(r'<[^>]+>', ' ', text)
    # Escape angle brackets that remain (not valid XML)
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Remove remaining non-latin-1 chars safely
    return text.encode('latin-1', errors='replace').decode('latin-1')

def strip_md(text: str) -> str:
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'\1', text)
    text = re.sub(r'\*\*(.*?)\*\*',     r'\1', text)
    text = re.sub(r'\*(.*?)\*',         r'\1', text)
    text = re.sub(r'`(.*?)`',           r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove LaTeX math ($$...$$  and $...$)
    text = re.sub(r'\$\$[^$]+\$\$', '[persamaan]', text)
    text = re.sub(r'\$[^$]+\$',     '[rumus]',     text)
    text = re.sub(r'^\[!\w+\]\s*',  '',            text.strip())
    return normalise(text).strip()


# ── Pre-process: split MD into sections, drop BAB 3 ──────────────────────────
def load_sections(input_path: Path):
    """
    Returns list of (heading_level, heading_text, body_lines).
    BAB 3 and all its sub-sections are omitted.
    Also returns frontmatter lines (before first #).
    """
    raw = input_path.read_text(encoding='utf-8').splitlines()

    sections   = []          # list of (level, title, [body lines])
    frontmatter = []
    current     = None
    in_bab3     = False

    for line in raw:
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            # Save previous section
            if current is not None:
                sections.append(current)

            level = len(m.group(1))
            title = m.group(2).strip()

            # Detect Bab 3 entry (level-1 heading containing "BAB 3" or "BAB III")
            if level == 1 and re.search(r'\bBAB\s+3\b|\bBAB\s+III\b', title, re.I):
                in_bab3 = True
                current = None
                continue

            # Any top-level heading after Bab 3 ends the skip zone
            if level == 1 and in_bab3:
                in_bab3 = False

            if in_bab3:
                current = None
                continue

            current = (level, title, [])
        else:
            if current is None:
                if not sections:       # still in frontmatter
                    frontmatter.append(line)
            elif not in_bab3:
                current[2].append(line)

    if current is not None:
        sections.append(current)

    return frontmatter, sections


# ── PDF Builder ───────────────────────────────────────────────────────────────
def build_pdf(input_path: Path, output_path: Path):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units    import cm
    from reportlab.lib.colors   import HexColor, white, black
    from reportlab.platypus     import (
        SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
        Table, TableStyle, PageBreak, Preformatted, KeepTogether
    )
    from reportlab.lib.styles   import ParagraphStyle
    from reportlab.lib.enums    import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT

    # Palette
    C_DARK   = HexColor('#1a237e')
    C_MED    = HexColor('#283593')
    C_LT     = HexColor('#3f51b5')
    C_BG_BQ  = HexColor('#e3f2fd')
    C_ACC    = HexColor('#90caf9')
    C_THD    = HexColor('#1a237e')
    C_TALT   = HexColor('#e8eaf6')
    C_TBRD   = HexColor('#c5cae9')
    C_CODE_B = HexColor('#263238')
    C_CODE_F = HexColor('#eceff1')
    C_TEXT   = HexColor('#111111')
    C_GRAY   = HexColor('#546e7a')
    C_HR     = HexColor('#c5cae9')

    PW, PH     = A4
    ML, MR     = 64, 54          # left / right margins in pts (4cm / 3cm)
    MT, MB     = 60, 56
    CW         = PW - ML - MR    # content width

    def S(name, **kw):
        defaults = dict(
            fontName='Helvetica', fontSize=11, textColor=C_TEXT,
            leading=16, spaceAfter=6, spaceBefore=0, alignment=TA_JUSTIFY,
        )
        defaults.update(kw)
        return ParagraphStyle(name, **defaults)

    st = {
        'cover_h1' : S('ch1', fontName='Helvetica-Bold', fontSize=14, textColor=C_DARK, alignment=TA_CENTER, leading=18, spaceAfter=10),
        'cover_sub': S('cs',  fontName='Helvetica',      fontSize=11, textColor=C_TEXT, alignment=TA_CENTER, leading=14, spaceAfter=5),
        'cover_nm' : S('cnm', fontName='Helvetica-Bold', fontSize=12, textColor=C_MED,  alignment=TA_CENTER, leading=16, spaceAfter=4),
        'h1'       : S('h1',  fontName='Helvetica-Bold', fontSize=13, textColor=C_DARK, alignment=TA_CENTER, leading=18, spaceAfter=8,  spaceBefore=0),
        'h2'       : S('h2',  fontName='Helvetica-Bold', fontSize=11.5, textColor=C_MED, alignment=TA_LEFT,  leading=16, spaceAfter=6,  spaceBefore=10),
        'h3'       : S('h3',  fontName='Helvetica-Bold', fontSize=11,   textColor=C_LT,  alignment=TA_LEFT,  leading=15, spaceAfter=4,  spaceBefore=8),
        'h4'       : S('h4',  fontName='Helvetica-Bold', fontSize=10.5, textColor=C_GRAY,alignment=TA_LEFT,  leading=14, spaceAfter=3,  spaceBefore=6),
        'body'     : S('bd',  leading=16, spaceAfter=5, firstLineIndent=24),
        'body_ni'  : S('bni', leading=16, spaceAfter=5),
        'bq'       : S('bq',  fontName='Helvetica-Oblique', fontSize=10, textColor=C_MED, backColor=C_BG_BQ,
                        leftIndent=8, rightIndent=8, leading=14, spaceAfter=5, spaceBefore=5, alignment=TA_LEFT),
        'bul'      : S('bul', leading=14, spaceAfter=2, leftIndent=14, alignment=TA_LEFT),
        'num'      : S('num', leading=14, spaceAfter=2, leftIndent=16, alignment=TA_LEFT),
        'code'     : S('co',  fontName='Courier', fontSize=8, textColor=C_CODE_F,
                        backColor=C_CODE_B, leading=11, spaceAfter=6, spaceBefore=6,
                        leftIndent=8, rightIndent=8),
        'footer'   : S('ft',  fontName='Helvetica-Oblique', fontSize=8.5, textColor=C_LT, alignment=TA_CENTER),
        'toc_bab'  : S('toc1',fontName='Helvetica-Bold', fontSize=11, textColor=C_DARK, alignment=TA_LEFT, spaceAfter=3),
        'toc_sub'  : S('toc2',fontName='Helvetica',      fontSize=10, textColor=C_TEXT, alignment=TA_LEFT, spaceAfter=2, leftIndent=12),
        'toc_sub2' : S('toc3',fontName='Helvetica',      fontSize=9.5, textColor=C_GRAY, alignment=TA_LEFT, spaceAfter=1, leftIndent=24),
        'fronthead': S('fh',  fontName='Helvetica-Bold', fontSize=12, textColor=C_DARK, alignment=TA_CENTER, leading=16, spaceAfter=10, spaceBefore=0),
    }

    story = []

    # ── COVER PAGE ──────────────────────────────────────────────────────────
    story.append(Spacer(1, 50))
    story.append(Paragraph("PROPOSAL SKRIPSI", st['cover_h1']))
    story.append(HRFlowable(width='100%', thickness=2, color=C_DARK, spaceAfter=14))
    story.append(Paragraph(
        "PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN "
        "SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK "
        "KARTU POKEMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI",
        st['cover_h1']
    ))
    story.append(Spacer(1, 20))
    story.append(Paragraph("[Versi Tanpa Bab 3 — Menunggu Penugasan Dosen Pembimbing]",
        S('note', fontName='Helvetica-Oblique', fontSize=10, textColor=C_LT, alignment=TA_CENTER)))
    story.append(Spacer(1, 30))
    story.append(Paragraph("Diajukan Oleh:", st['cover_sub']))
    story.append(Paragraph("Arthur Reezan", st['cover_nm']))
    story.append(Paragraph("NIM: 312023002", st['cover_sub']))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Dosen Pembimbing:", st['cover_sub']))
    story.append(Paragraph("Dr. Fredella Colline, S.E., M.M., CFP(R), PFM, CHCP-A", st['cover_sub']))
    story.append(Spacer(1, 20))
    story.append(HRFlowable(width='100%', thickness=1, color=C_MED, spaceAfter=12))
    story.append(Paragraph("PROGRAM STUDI S1 MANAJEMEN", st['cover_sub']))
    story.append(Paragraph("FAKULTAS EKONOMI DAN BISNIS", st['cover_sub']))
    story.append(Paragraph("UNIVERSITAS KRISTEN KRIDA WACANA", st['cover_sub']))
    story.append(Paragraph("JAKARTA 2026", st['cover_sub']))
    story.append(PageBreak())

    # ── TABLE OF CONTENTS (static, no Bab 3) ─────────────────────────────
    story.append(Paragraph("DAFTAR ISI", st['fronthead']))
    story.append(HRFlowable(width='100%', thickness=1, color=C_DARK, spaceAfter=10))
    toc_entries = [
        (0, "Halaman Sampul / Judul Proposal"),
        (0, "Halaman Pernyataan Keaslian"),
        (0, "Halaman Persetujuan Proposal Skripsi"),
        (0, "Halaman Pengesahan Tim Penguji Seminar Proposal"),
        (0, "Kata Pengantar"),
        (0, "Abstrak (Bahasa Indonesia)"),
        (0, "Abstract (English)"),
        (0, "Daftar Isi"),
        (0, "Daftar Tabel"),
        (0, "Daftar Gambar"),
        (0, "BAB 1  PENDAHULUAN"),
        (1, "1.1  Latar Belakang Penelitian"),
        (1, "1.2  Identifikasi dan Perumusan Masalah"),
        (1, "1.3  Tujuan Penelitian"),
        (1, "1.4  Manfaat Penelitian"),
        (1, "1.5  Batasan Penelitian"),
        (1, "1.6  Sistematika Penulisan Proposal"),
        (0, "BAB 2  TINJAUAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS"),
        (1, "2.1  Landasan Teori"),
        (1, "2.2  Definisi dan Konseptualisasi Variabel"),
        (1, "2.3  Tinjauan Penelitian Empiris Terdahulu"),
        (1, "2.4  Kerangka Pemikiran dan Model Konseptual"),
        (1, "2.5  Pengembangan Hipotesis Penelitian"),
        (0, "DAFTAR PUSTAKA"),
    ]
    for depth, title in toc_entries:
        sty = st['toc_bab'] if depth == 0 else (st['toc_sub'] if depth == 1 else st['toc_sub2'])
        story.append(Paragraph(normalise(title), sty))
    story.append(PageBreak())

    # ── BODY: parse sections (no Bab 3) ────────────────────────────────────
    print("[*] Loading and filtering Markdown source (skipping Bab 3)...")
    _, sections = load_sections(input_path)
    print(f"    -> {len(sections)} sections loaded (Bab 3 excluded)")

    def render_body_lines(lines):
        """Render a list of raw Markdown body lines into flowables."""
        in_code  = False
        code_buf = []
        in_bq    = False
        bq_buf   = []
        tbl_buf  = []
        in_tbl   = False

        def flush_code():
            nonlocal code_buf, in_code
            if code_buf:
                txt = '\n'.join(normalise(l) for l in code_buf)
                story.append(Preformatted(txt, st['code']))
                story.append(Spacer(1, 4))
            code_buf = []; in_code = False

        def flush_bq():
            nonlocal bq_buf, in_bq
            if bq_buf:
                story.append(Paragraph(strip_md(' '.join(bq_buf)), st['bq']))
                story.append(Spacer(1, 3))
            bq_buf = []; in_bq = False

        def flush_tbl(rows):
            if len(rows) < 2:
                return
            hdrs = [strip_md(c) for c in rows[0].strip('|').split('|')]
            data = [[strip_md(c) for c in r.strip('|').split('|')] for r in rows[2:]]
            nc   = len(hdrs)
            cw   = CW / nc
            tdata = [hdrs] + data
            t = Table(tdata, colWidths=[cw]*nc, repeatRows=1)
            t.setStyle(TableStyle([
                ('BACKGROUND',    (0,0),(-1,0),  C_THD),
                ('TEXTCOLOR',     (0,0),(-1,0),  white),
                ('FONTNAME',      (0,0),(-1,0),  'Helvetica-Bold'),
                ('FONTSIZE',      (0,0),(-1,0),  9),
                ('ALIGN',         (0,0),(-1,0),  'CENTER'),
                ('FONTNAME',      (0,1),(-1,-1), 'Helvetica'),
                ('FONTSIZE',      (0,1),(-1,-1), 8.5),
                ('ROWBACKGROUNDS',(0,1),(-1,-1),  [white, C_TALT]),
                ('GRID',          (0,0),(-1,-1),  0.5, C_TBRD),
                ('VALIGN',        (0,0),(-1,-1),  'TOP'),
                ('TOPPADDING',    (0,0),(-1,-1),  4),
                ('BOTTOMPADDING', (0,0),(-1,-1),  4),
                ('LEFTPADDING',   (0,0),(-1,-1),  5),
                ('RIGHTPADDING',  (0,0),(-1,-1),  5),
            ]))
            story.append(Spacer(1, 6))
            story.append(t)
            story.append(Spacer(1, 8))

        for raw in lines:
            line = raw.rstrip()

            # Code blocks
            if line.strip().startswith('```'):
                if in_code:
                    flush_code()
                else:
                    if in_bq: flush_bq()
                    if in_tbl: flush_tbl(tbl_buf); tbl_buf = []; in_tbl = False
                    in_code = True
                continue
            if in_code:
                code_buf.append(line)
                continue

            # Tables
            if line.strip().startswith('|'):
                if in_bq: flush_bq()
                tbl_buf.append(line)
                in_tbl = True
                continue
            else:
                if in_tbl:
                    flush_tbl(tbl_buf); tbl_buf = []; in_tbl = False

            # Blockquotes
            if line.startswith('>'):
                inner = re.sub(r'^\[!\w+\]\s*', '', line[1:].strip())
                if inner:
                    bq_buf.append(inner)
                in_bq = True
                continue
            else:
                if in_bq: flush_bq()

            # HR
            if re.match(r'^[-*=]{3,}$', line.strip()):
                story.append(HRFlowable(width='100%', thickness=0.5, color=C_HR,
                                        spaceBefore=6, spaceAfter=6))
                continue

            # Sub-headings inside body
            mh = re.match(r'^(#{2,6})\s+(.*)', line)
            if mh:
                lvl = len(mh.group(1))
                txt = strip_md(mh.group(2))
                sty = st['h2'] if lvl == 2 else (st['h3'] if lvl == 3 else st['h4'])
                story.append(Paragraph(txt, sty))
                continue

            # Bullet list
            mb = re.match(r'^(\s*)([-*\u2022])\s+(.*)', line)
            if mb:
                ind = len(mb.group(1)) // 2
                txt = strip_md(mb.group(3))
                sty = ParagraphStyle(f'b{ind}', parent=st['bul'], leftIndent=14 + ind*14)
                story.append(Paragraph(f'• {txt}', sty))
                continue

            # Numbered list
            mn = re.match(r'^(\s*)(\d+[\.\)])\s+(.*)', line)
            if mn:
                ind = len(mn.group(1)) // 2
                lbl = mn.group(2)
                txt = strip_md(mn.group(3))
                sty = ParagraphStyle(f'n{ind}', parent=st['num'], leftIndent=16 + ind*14)
                story.append(Paragraph(f'{lbl} {txt}', sty))
                continue

            # LaTeX math lines → skip / placeholder
            if line.strip().startswith('$$') or (line.strip().startswith('$') and line.strip().endswith('$')):
                txt = strip_md(line.strip())
                story.append(Paragraph(txt, S('eq', fontName='Courier', fontSize=10,
                                              alignment=TA_CENTER, textColor=C_MED,
                                              spaceAfter=4, spaceBefore=4)))
                continue

            # LaTeX environments → skip
            if re.match(r'^\\(begin|end)\{', line.strip()):
                continue

            # Empty line
            if not line.strip():
                story.append(Spacer(1, 3))
                continue

            # Regular paragraph
            txt = strip_md(line)
            if txt:
                story.append(Paragraph(txt, st['body']))

        # Flush remainders
        if in_code and code_buf: flush_code()
        if in_bq and bq_buf: flush_bq()
        if in_tbl and tbl_buf: flush_tbl(tbl_buf)

    bab_count = 0
    for level, title, body_lines in sections:
        title_clean = strip_md(title)
        if level == 1:
            if title_clean.upper().startswith('DAFTAR ISI') or 'DAFTAR ISI' in title_clean.upper():
                continue  # skip inline TOC from MD
            if title_clean.upper().startswith('PROPOSAL SKRIPSI') and bab_count == 0:
                continue  # skip meta-title
            bab_count += 1
            story.append(PageBreak())
            story.append(Paragraph(title_clean.upper(), st['h1']))
            story.append(HRFlowable(width='100%', thickness=1, color=C_DARK, spaceAfter=10))
        elif level == 2:
            story.append(Paragraph(title_clean, st['h2']))
        elif level == 3:
            story.append(Paragraph(title_clean, st['h3']))
        else:
            story.append(Paragraph(title_clean, st['h4']))

        render_body_lines(body_lines)

    # ── Footer handler ───────────────────────────────────────────────────────
    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica-Oblique', 8.5)
        canvas.setFillColorRGB(0.247, 0.318, 0.710)  # C_LT
        canvas.drawCentredString(
            PW / 2, 30,
            normalise(f"Proposal Skripsi (Tanpa Bab 3) | Arthur Reezan (312023002) | UKRIDA 2026 | Hal. {doc.page}")
        )
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=ML, rightMargin=MR,
        topMargin=MT,  bottomMargin=MB,
        title="Proposal Skripsi Tanpa Bab 3 - Arthur Reezan",
        author="Arthur Reezan",
        subject="Proposal Skripsi Pokemon TCG - No Chapter 3",
    )

    print("[*] Rendering PDF...")
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    size_kb = output_path.stat().st_size / 1024
    print(f"\n[OK] PDF generated!")
    print(f"     Output : {output_path}")
    print(f"     Size   : {size_kb:.1f} KB")
    print(f"     Bab 3  : SKIPPED (as directed)")


if __name__ == "__main__":
    if not INPUT_MD.exists():
        print(f"[ERROR] Input not found: {INPUT_MD}")
        sys.exit(1)
    build_pdf(INPUT_MD, OUTPUT_PDF)

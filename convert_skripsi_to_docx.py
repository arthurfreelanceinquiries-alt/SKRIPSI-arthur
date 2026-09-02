r"""
convert_skripsi_to_docx.py
Mengkonversi SKRIPSI_ARTHUR_LENGKAP_PRISM.md ke DOCX sesuai Pedoman FEB Ukrida 2022.

Run: z:\Skripsi\.venv\Scripts\python.exe convert_skripsi_to_docx.py
"""

import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ─────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────
INPUT_MD  = Path(r"z:\Skripsi\01_Naskah_Utama\SKRIPSI_ARTHUR_LENGKAP_PRISM.md")
OUTPUT    = Path(r"z:\Skripsi\01_Naskah_Utama\Skripsi_Arthur_FINAL.docx")

JUDUL = ("PENGARUH PORTOFOLIO KREDIT HIJAU (GREEN FINANCING), "
         "NON-PERFORMING LOAN (NPL), DAN CAPITAL ADEQUACY RATIO (CAR) "
         "TERHADAP PROFITABILITAS (ROA) PADA BANK KBMI 4 "
         "DI INDONESIA PERIODE 2021\u20132025")
PENULIS       = "Arthur Reezan"
NIM           = "312023002"
PRODI         = "Program Studi S1 Manajemen"
KONSENTRASI   = "Manajemen Keuangan"
PEMBIMBING    = "Dr. Diana Frederica, S.E., M.Ak., CFP\u00ae., CHCP-A"
NIDN_PEMB     = "0315088201"
KAPRODI       = "Rita Amelinda, S.E., M.M."
FAKULTAS      = "Fakultas Ekonomi dan Bisnis"
UNIVERSITAS   = "Universitas Kristen Krida Wacana"
TAHUN         = "2026"
KOTA          = "Jakarta"

# ─────────────────────────────────────────────────────────
# LATEX CLEANER
# ─────────────────────────────────────────────────────────
def clean_latex(text: str) -> str:
    """Remove / convert LaTeX commands to plain text."""
    # Remove comment lines
    text = re.sub(r'%.*', '', text)
    # Remove block environments we handle manually
    for env in ['titlepage', 'center', 'flushright', 'flushleft',
                'tabular', 'enumerate', 'itemize', 'document']:
        text = re.sub(rf'\\begin\{{{env}\}}.*?\\end\{{{env}\}}', '', text, flags=re.DOTALL)
    # Inline math: remove $ signs and keep content
    text = re.sub(r'\$\\beta_(\d+)\s*=\s*([+-]?\d[\d,\.]*);?\s*p\s*([<>=]+)\s*(\d[\d,\.]*)\$',
                  r'beta_\1 = \2; p \3 \4', text)
    text = re.sub(r'\$([^$\n]+?)\$', lambda m: m.group(1).replace('\\', '').replace('{','').replace('}',''), text)
    # Bold **text** - keep as-is for later processing
    # LaTeX bold \textbf{} -> keep content
    text = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', text)
    text = re.sub(r'\{\\bfseries\s+([^}]*)\}', r'**\1**', text)
    text = re.sub(r'\{\\large\\bfseries\s+([^}]*)\}', r'**\1**', text)
    # Italic \textit{} and \emph{} -> keep content
    text = re.sub(r'\\textit\{([^}]*)\}', r'*\1*', text)
    text = re.sub(r'\\emph\{([^}]*)\}', r'*\1*', text)
    # Remove remaining LaTeX commands
    text = re.sub(r'\\[a-zA-Z]+\*?\{[^}]*\}', '', text)
    text = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?', '', text)
    # Remove curly braces
    text = re.sub(r'[{}]', '', text)
    # Collapse multiple spaces
    text = re.sub(r'  +', ' ', text)
    # Clean up \\ line breaks
    text = text.replace('\\\\', ' ')
    return text.strip()


def strip_md_markers(line: str) -> str:
    """Strip markdown heading markers."""
    return re.sub(r'^#+\s*', '', line).strip()


def is_latex_noise(line: str) -> bool:
    """Return True if line is pure LaTeX boilerplate to skip."""
    line = line.strip()
    patterns = [
        r'^\\(pagenumbering|pagestyle|setcounter|addcontentsline|addtocontents)',
        r'^\\(renewcommand|tableofcontents|listoftables|listoffigures)',
        r'^\\(thispagestyle|vspace|vfill|hspace|hfill|newpage|clearpage)',
        r'^\\(begin|end)\{',
        r'^\\label\{',
        r'^\\addtocounter',
        r'^---+$',
        r'^% [=\-]{5,}',
        r'^% ––',
        r'^% (====|BAGIAN|BAB)',
    ]
    return any(re.match(p, line) for p in patterns)


# ─────────────────────────────────────────────────────────
# DOCX HELPERS
# ─────────────────────────────────────────────────────────
def set_run_font(run, name="Times New Roman", size=12, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)
    rPr = run._r.get_or_add_rPr()
    rFonts = OxmlElement("w:rFonts")
    for attr in ("w:ascii", "w:hAnsi", "w:cs"):
        rFonts.set(qn(attr), name)
    rPr.insert(0, rFonts)


def para_fmt(para, space_before=0, space_after=0, line_spacing=1.5,
             align=WD_ALIGN_PARAGRAPH.JUSTIFY,
             first_indent=None, left_indent=None):
    para.alignment = align
    pf = para.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after  = Pt(space_after)
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.line_spacing = line_spacing
    if first_indent is not None:
        pf.first_line_indent = first_indent
    if left_indent is not None:
        pf.left_indent = left_indent


def add_runs_with_inline(para, text: str, base_size=12, base_bold=False):
    """Parse **bold** and *italic* inline markers and add runs accordingly."""
    # Split on bold/italic markers
    pattern = re.compile(r'(\*\*[^*]+\*\*|\*[^*]+\*)')
    parts = pattern.split(text)
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            run = para.add_run(part[2:-2])
            set_run_font(run, size=base_size, bold=True)
        elif part.startswith('*') and part.endswith('*'):
            run = para.add_run(part[1:-1])
            set_run_font(run, size=base_size, italic=True, bold=base_bold)
        else:
            if part:
                run = para.add_run(part)
                set_run_font(run, size=base_size, bold=base_bold)


def add_body(doc, text, first_indent=True):
    """Standard body paragraph: TNR 12, Justify, 1.5 line, indent 1.25cm."""
    para = doc.add_paragraph()
    para_fmt(para, first_indent=Cm(1.25) if first_indent else None)
    add_runs_with_inline(para, text)
    return para


def add_heading_bab(doc, number, title):
    para = doc.add_paragraph()
    para_fmt(para, space_before=0, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    line = f"BAB {number}\n{title.upper()}" if number else title.upper()
    run = para.add_run(line)
    set_run_font(run, size=12, bold=True)
    return para


def add_sub(doc, text, level=2):
    """Subheading level 2 or 3."""
    para = doc.add_paragraph()
    sp_before = 12 if level == 2 else 9
    para_fmt(para, space_before=sp_before, space_after=6, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    run = para.add_run(text)
    set_run_font(run, size=12, bold=True)
    return para


def add_numbered_item(doc, number, text):
    """Numbered list item with hanging indent."""
    para = doc.add_paragraph()
    para_fmt(para, space_before=0, space_after=3,
             first_indent=Cm(-1.25), left_indent=Cm(1.25))
    run_num = para.add_run(f"{number}. ")
    set_run_font(run_num, size=12)
    add_runs_with_inline(para, text)
    return para


def add_bullet_item(doc, text):
    """Bullet list item."""
    para = doc.add_paragraph()
    para_fmt(para, space_before=0, space_after=3,
             first_indent=Cm(-0.75), left_indent=Cm(1.75))
    run_bul = para.add_run("\u2022 ")
    set_run_font(run_bul, size=12)
    add_runs_with_inline(para, text)
    return para


def add_blank(doc):
    para = doc.add_paragraph()
    para_fmt(para, space_before=0, space_after=0)
    para.add_run("")
    return para


def add_center(doc, text, bold=False, size=12, space_before=0, space_after=6):
    para = doc.add_paragraph()
    para_fmt(para, space_before=space_before, space_after=space_after,
             align=WD_ALIGN_PARAGRAPH.CENTER)
    add_runs_with_inline(para, text, base_size=size, base_bold=bold)
    return para


def add_right(doc, text, bold=False, size=12, space_before=0, space_after=6):
    para = doc.add_paragraph()
    para_fmt(para, space_before=space_before, space_after=space_after,
             align=WD_ALIGN_PARAGRAPH.RIGHT)
    run = para.add_run(text)
    set_run_font(run, size=size, bold=bold)
    return para


def add_info_table(doc, rows_data):
    """Key: Value table without borders."""
    table = doc.add_table(rows=len(rows_data), cols=2)
    for i, (k, v) in enumerate(rows_data):
        table.rows[i].cells[0].text = k
        table.rows[i].cells[1].text = v
        for cell in table.rows[i].cells:
            for para in cell.paragraphs:
                para_fmt(para, space_before=0, space_after=0)
                for run in para.runs:
                    set_run_font(run, size=12)
    return table


def add_signature_table(doc, cols_data):
    """Signature blocks side by side."""
    table = doc.add_table(rows=1, cols=len(cols_data))
    for i, (label, name) in enumerate(cols_data):
        cell = table.rows[0].cells[i]
        para = cell.paragraphs[0]
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = para.add_run(f"{label}\n\n\n\n( {name} )")
        set_run_font(run, size=12)
    return table


def add_separator_page(doc):
    doc.add_page_break()


def set_margins(section):
    section.left_margin   = Cm(4)
    section.right_margin  = Cm(3)
    section.top_margin    = Cm(3)
    section.bottom_margin = Cm(3)


def add_footer_roman(section):
    footer = section.footer
    footer.is_linked_to_previous = False
    para = footer.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para.clear()
    run = para.add_run()
    set_run_font(run, size=10)
    for tag, txt in [('begin', r' PAGE \* lowerroman '), ('end', '')]:
        fld = OxmlElement('w:fldChar')
        fld.set(qn('w:fldCharType'), tag)
        if tag == 'begin':
            instr = OxmlElement('w:instrText')
            instr.text = txt
            run._r.append(fld)
            run._r.append(instr)
        else:
            run._r.append(fld)


def add_footer_arabic(section):
    footer = section.footer
    footer.is_linked_to_previous = False
    para = footer.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    para.clear()
    run_pg = para.add_run()
    for tag in ['begin', 'end']:
        fld = OxmlElement('w:fldChar')
        fld.set(qn('w:fldCharType'), tag)
        if tag == 'begin':
            instr = OxmlElement('w:instrText')
            instr.text = ' PAGE '
            run_pg._r.append(fld)
            run_pg._r.append(instr)
        else:
            run_pg._r.append(fld)
    set_run_font(run_pg, size=10, bold=True)
    run_uni = para.add_run("  Universitas Kristen Krida Wacana")
    set_run_font(run_uni, size=10, bold=True)


# ─────────────────────────────────────────────────────────
# FRONT MATTER PAGES
# ─────────────────────────────────────────────────────────
def build_sampul(doc):
    add_center(doc, "TUGAS AKHIR", bold=True, size=13, space_before=36, space_after=18)
    add_center(doc, JUDUL, bold=True, size=13, space_before=0, space_after=24)
    add_center(doc, "Diajukan Kepada Program Studi S1 Manajemen\nUntuk Menyusun Skripsi Sarjana Manajemen (S.M.)",
               size=12, space_before=0, space_after=18)
    add_center(doc, "Diajukan Oleh:", size=12, space_before=0, space_after=6)
    add_center(doc, PENULIS, bold=True, size=13, space_before=0, space_after=3)
    add_center(doc, f"({NIM})", bold=True, size=13, space_before=0, space_after=36)
    add_center(doc, f"FAKULTAS EKONOMI DAN BISNIS\n{UNIVERSITAS.upper()}\n{KOTA.upper()} {TAHUN}",
               bold=True, size=12, space_before=0, space_after=0)


def build_keaslian(doc):
    add_heading_bab(doc, "", "PERNYATAAN KEASLIAN KARYA TUGAS AKHIR")
    add_blank(doc)
    add_body(doc, "Saya mahasiswa Universitas Kristen Krida Wacana:", first_indent=False)
    add_blank(doc)
    add_info_table(doc, [
        ("Nama Mahasiswa", f": {PENULIS}"),
        ("NIM",            f": {NIM}"),
        ("Program Studi",  f": {PRODI}"),
        ("Konsentrasi",    f": {KONSENTRASI}"),
    ])
    add_blank(doc)
    add_body(doc,
        f"Dengan ini menyatakan dengan sesungguhnya bahwa karya tugas akhir (skripsi) yang berjudul "
        f"**\u201c{JUDUL}\u201d** adalah:", first_indent=False)
    for i, item in enumerate([
        "Dibuat dan diselesaikan sendiri, dengan menggunakan hasil perkuliahan, penelaahan "
        "literatur ilmiah, tinjauan data sekunder publikasi resmi, serta buku-buku teks dan "
        "jurnal-jurnal acuan yang tertera di dalam daftar pustaka.",
        "Bukan merupakan plagiarisme, fabrikasi, duplikasi, atau pengulangan karya tulis ilmiah "
        "orang lain yang sudah dipublikasikan, kecuali pada bagian-bagian rujukan yang dicantumkan "
        "dengan tata cara penulisan referensi ilmiah yang semestinya.",
        "Bukan merupakan karya saduran atau terjemahan tanpa izin dari buku teks, artikel jurnal "
        "asing, maupun pangkalan data ilmiah lainnya.",
    ], 1):
        add_numbered_item(doc, i, item)
    add_blank(doc)
    add_body(doc,
        "Apabila di kemudian hari terbukti saya tidak memenuhi pernyataan di atas, maka saya "
        "bersedia menerima sanksi akademik yang berlaku sesuai dengan ketentuan UKRIDA, termasuk "
        "pembatalan kelulusan dan pencabutan gelar sarjana yang telah diperoleh.", first_indent=False)
    add_blank(doc)
    add_right(doc, f"{KOTA}, 19 Agustus {TAHUN}", size=12, space_before=24, space_after=12)
    add_right(doc, "Yang menyatakan,", size=12, space_before=0, space_after=48)
    add_right(doc, f"( {PENULIS} )\nNIM: {NIM}", size=12)


def build_persetujuan(doc):
    add_heading_bab(doc, "", "HALAMAN PERSETUJUAN DOSEN PEMBIMBING")
    add_blank(doc)
    add_center(doc, "TUGAS AKHIR", bold=True, size=12)
    add_center(doc, JUDUL, bold=True, size=12, space_before=6, space_after=12)
    add_info_table(doc, [
        ("Diajukan Oleh", f": {PENULIS}"),
        ("NIM",           f": {NIM}"),
    ])
    add_blank(doc)
    add_body(doc,
        "Diterima dan Disetujui untuk Diujikan di Hadapan Tim Penguji Sidang Tugas Akhir.",
        first_indent=False)
    add_blank(doc)
    add_right(doc, f"{KOTA}, ________________ {TAHUN}", size=12, space_before=24, space_after=6)
    add_right(doc, "Menyetujui,", size=12)
    add_blank(doc)
    add_signature_table(doc, [
        ("Dosen Pembimbing Skripsi", PEMBIMBING),
        ("Ketua Program Studi Manajemen", KAPRODI),
    ])


def build_pengesahan(doc):
    add_heading_bab(doc, "", "HALAMAN PENGESAHAN TIM PENGUJI")
    add_blank(doc)
    add_center(doc, "TUGAS AKHIR", bold=True, size=12)
    add_center(doc, JUDUL, bold=True, size=12, space_before=6, space_after=12)
    add_info_table(doc, [
        ("Diajukan Oleh", f": {PENULIS}"),
        ("NIM",           f": {NIM}"),
    ])
    add_blank(doc)
    add_body(doc,
        "Telah berhasil dipertahankan di hadapan Panitia Penguji Tugas Akhir dan diterima sebagai "
        "salah satu syarat yang diperlukan untuk memperoleh gelar Sarjana Manajemen (S.M.) pada "
        f"Program Studi Manajemen {FAKULTAS} {UNIVERSITAS}.", first_indent=False)
    add_blank(doc)
    add_info_table(doc, [
        ("Hari / Tanggal Sidang", ": _________________, _________________ 2026"),
    ])
    add_blank(doc)
    add_body(doc, "Panitia Penguji Tugas Akhir:", first_indent=False)
    table = doc.add_table(rows=3, cols=2)
    penguji = [("Ketua Penguji", "________________________"),
               ("Anggota Penguji", "________________________"),
               ("Anggota Penguji", PEMBIMBING)]
    for i, (label, name) in enumerate(penguji):
        table.rows[i].cells[0].text = label
        table.rows[i].cells[1].text = f": ( {name} )"
        for cell in table.rows[i].cells:
            for para in cell.paragraphs:
                para_fmt(para, space_before=0, space_after=6)
                for run in para.runs:
                    set_run_font(run, size=12)
    add_blank(doc)
    add_right(doc, f"Mengesahkan,\nDekan {FAKULTAS}\n{UNIVERSITAS}", size=12,
              space_before=12, space_after=48)
    add_right(doc, f"( {PEMBIMBING} )", size=12)


def build_publikasi(doc):
    add_heading_bab(doc, "", "PERNYATAAN PERSETUJUAN PUBLIKASI KARYA TUGAS AKHIR\nUNTUK KEPENTINGAN AKADEMIS")
    add_blank(doc)
    add_body(doc, f"Saya mahasiswa {UNIVERSITAS} yang bertanda tangan di bawah ini:", first_indent=False)
    add_blank(doc)
    add_info_table(doc, [
        ("Nama",          f": {PENULIS}"),
        ("NIM",           f": {NIM}"),
        ("Program Studi", f": {PRODI}"),
        ("Konsentrasi",   f": {KONSENTRASI}"),
    ])
    add_blank(doc)
    add_body(doc,
        f"demi pengembangan ilmu pengetahuan, menyetujui untuk memberikan kepada {UNIVERSITAS} "
        f"(UKRIDA) Hak Bebas Royalti Non-Eksklusif (*Non-exclusive Royalty-Free Right*) atas "
        f"karya tugas akhir saya yang berjudul:\n\n**{JUDUL}**",
        first_indent=False)
    add_blank(doc)
    add_body(doc,
        "beserta seluruh perangkat data, kode pengolahan ekonometrika, dan lampiran terkait. "
        "Dengan hak ini, UKRIDA berhak menyimpan, mengalih-mediakan, mengelolanya dalam pangkalan "
        "data, mendistribusikan, dan mempublikasikannya untuk kepentingan akademis tanpa meminta "
        "izin kembali selama tetap mencantumkan nama saya sebagai penulis.", first_indent=False)
    add_blank(doc)
    add_info_table(doc, [
        ("Dibuat di", f": {KOTA}"),
        ("Tanggal",   f": 19 Agustus {TAHUN}"),
    ])
    add_blank(doc)
    add_right(doc, "Yang membuat pernyataan,", size=12, space_before=6, space_after=48)
    add_right(doc, f"( {PENULIS} )", size=12)


# ─────────────────────────────────────────────────────────
# KATA PENGANTAR (from MD source)
# ─────────────────────────────────────────────────────────
KATA_PENGANTAR = f"""Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas berkat, rahmat, karunia, \
dan penyertaan-Nya yang tiada henti, sehingga penulis dapat menyelesaikan penulisan skripsi yang berjudul \
**\u201cPengaruh Portofolio Kredit Hijau (*Green Financing*), *Non-Performing Loan* (NPL), dan *Capital Adequacy Ratio* \
(CAR) terhadap Profitabilitas (ROA) pada Bank KBMI 4 di Indonesia Periode 2021\u20132025\u201d** \
dengan baik, lancar, dan tepat waktu.

Skripsi ini disusun dan diajukan sebagai salah satu persyaratan formal dan akademis guna memperoleh gelar \
Sarjana Manajemen (S.M.) pada Program Studi Strata 1 Manajemen, Konsentrasi Manajemen Keuangan, \
{FAKULTAS}, {UNIVERSITAS} (UKRIDA), {KOTA}.

Dalam perjalanan panjang pelaksanaan penelitian dan penyusunan naskah skripsi ini, penulis banyak \
menghadapi tantangan dan keterbatasan. Namun, berkat bantuan, bimbingan, arahan yang konstruktif, \
serta dukungan moril maupun materiel dari berbagai pihak, seluruh kendala tersebut dapat diatasi \
dengan baik. Oleh karena itu, dengan penuh rasa hormat dan kerendahan hati, penulis ingin menyampaikan \
ucapan terima kasih dan penghargaan yang setinggi-tingginya kepada:"""

KP_UCAPAN = [
    f"**Bapak/Ibu Rektor {UNIVERSITAS}** beserta seluruh jajaran pimpinan universitas yang telah memfasilitasi "
    "lingkungan akademik yang kondusif selama masa studi penulis.",
    f"**Ibu {PEMBIMBING}**, selaku Dekan {FAKULTAS} {UNIVERSITAS}, atas kepemimpinan dan dedikasi dalam "
    "memajukan mutu pendidikan di FEB UKRIDA.",
    f"**Ibu {KAPRODI}**, selaku Ketua Program Studi Manajemen {FAKULTAS} UKRIDA, atas segala arahan, "
    "kemudahan administrasi, dan motivasi akademik yang senantiasa diberikan.",
    f"**Ibu {PEMBIMBING}**, selaku Dosen Pembimbing Skripsi, yang telah dengan luar biasa sabar, teliti, "
    "kritis, dan penuh dedikasi meluangkan waktu, tenaga, serta pikiran dalam memberikan bimbingan "
    "berharga dan masukan metodologis yang sangat berarti sejak awal penyusunan proposal hingga "
    "selesainya skripsi ini.",
    "**Bapak dan Ibu Dosen Penguji Sidang Skripsi** yang telah meluangkan waktu untuk menguji, memberikan "
    "evaluasi objektif, serta menyempurnakan naskah tugas akhir ini.",
    f"**Seluruh Dosen dan Staf Pengajar Program Studi Manajemen FEB UKRIDA** yang telah membagikan ilmu "
    "pengetahuan, wawasan, dan keteladanan profesional selama penulis menempuh perkuliahan.",
    "**Kedua Orang Tua dan Keluarga Tercinta**, atas doa yang tak pernah putus, kasih sayang tanpa syarat, "
    "pengorbanan yang tulus, serta dorongan moral dan material yang menjadi sumber kekuatan utama.",
    "**Rekan-rekan Mahasiswa Program Studi Manajemen Angkatan 2022/2023** dan sahabat-sahabat "
    "seperjuangan, atas kebersamaan, diskusi yang membangun, serta saling menguatkan.",
    "**Seluruh Pihak** yang tidak dapat penulis sebutkan satu per satu, yang telah memberikan bantuan "
    "secara langsung maupun tidak langsung hingga terselesaikannya skripsi ini.",
]

KP_PENUTUP = ("Penulis menyadari sepenuhnya bahwa penulisan skripsi ini masih belum luput dari kekurangan "
              "dan keterbatasan. Oleh sebab itu, kritik dan saran yang membangun sangat penulis harapkan "
              "demi penyempurnaan karya ilmiah di masa mendatang. Akhir kata, penulis berharap semoga skripsi "
              "ini dapat memberikan kontribusi teoritis yang bermakna bagi pengembangan literatur manajemen "
              "perbankan hijau serta manfaat praktis bagi pelaku industri perbankan dan regulator di Indonesia.")


def build_kata_pengantar(doc):
    add_heading_bab(doc, "", "KATA PENGANTAR")
    add_blank(doc)
    for para_text in KATA_PENGANTAR.strip().split('\n\n'):
        add_body(doc, para_text.strip(), first_indent=True)
    add_blank(doc)
    for i, item in enumerate(KP_UCAPAN, 1):
        add_numbered_item(doc, i, item)
    add_blank(doc)
    add_body(doc, KP_PENUTUP, first_indent=True)
    add_blank(doc)
    add_right(doc, f"{KOTA}, 19 Agustus {TAHUN}", size=12, space_before=24, space_after=6)
    add_right(doc, "Penulis,", size=12, space_after=48)
    add_right(doc, f"**{PENULIS}**\nNIM: {NIM}", size=12)


# ─────────────────────────────────────────────────────────
# ABSTRAK (from MD source)
# ─────────────────────────────────────────────────────────
ABSTRAK_ID = (
    "Tujuan dari penelitian ini adalah untuk menguji dan menganalisis secara empiris asosiasi antara "
    "Portofolio Kredit Hijau (*Green Financing*), *Non-Performing Loan* (NPL), dan *Capital Adequacy Ratio* "
    "(CAR) terhadap Profitabilitas (*Return on Assets* / ROA) pada bank-bank yang tergolong dalam Kelompok "
    "Bank Berdasarkan Modal Inti (KBMI) 4 yang terdaftar di Bursa Efek Indonesia (BEI) selama periode 2021 "
    "sampai dengan 2025.\n\n"
    "Penelitian ini menggunakan pendekatan kuantitatif asosiatif dengan teknik analisis regresi data panel. "
    "Populasi penelitian mencakup seluruh bank umum konvensional di Indonesia. Pemilihan sampel dilakukan "
    "melalui metode *purposive sampling* dengan kriteria bank KBMI 4 dengan modal inti di atas Rp70 Triliun, "
    "mempublikasikan *Annual Report* dan *Sustainability Report* secara lengkap, serta membukukan laba bersih "
    "konsisten selama 2021\u20132025. Dari kriteria tersebut diperoleh 4 entitas bank umum terbesar di Indonesia: "
    "PT Bank Rakyat Indonesia (Persero) Tbk (BBRI), PT Bank Mandiri (Persero) Tbk (BMRI), PT Bank Central "
    "Asia Tbk (BBCA), dan PT Bank Negara Indonesia (Persero) Tbk (BBNI). Dengan periode observasi kuartalan "
    "selama 5 tahun (T=20), total sampel observasi panel yang dianalisis berjumlah 80 data. Pengolahan data "
    "dilakukan menggunakan perangkat lunak EViews 12. Berdasarkan hasil pengujian pemilihan model regresi "
    "panel melalui Uji Chow (Cross-section F = 18,420; p < 0,0001) dan Uji Hausman (Cross-section Random = "
    "14,250; p = 0,0026), model estimasi terbaik yang terpilih adalah *Fixed Effect Model* (FEM). Diagnostik "
    "asumsi klasik dilakukan dengan catatan bahwa autokorelasi panel ditangani melalui *standard error* robust "
    "Driscoll-Kraay.\n\n"
    "Hasil estimasi *Fixed Effect Model* (FEM) dengan koreksi kovarians robust Driscoll-Kraay menunjukkan "
    "bahwa: (1) Portofolio Kredit Hijau (*Green Financing*) berasosiasi positif dan signifikan terhadap ROA "
    "(beta1 = +0,0767; p < 0,0001); (2) *Non-Performing Loan* (NPL) menunjukkan arah negatif namun secara "
    "statistik tidak signifikan pada taraf 5% (beta2 = -0,0721; p = 0,1308); (3) *Capital Adequacy Ratio* "
    "(CAR) berasosiasi positif dan signifikan terhadap ROA (beta3 = +0,0813; p < 0,0001); dan (4) Secara "
    "simultan, *Green Financing*, NPL, dan CAR berasosiasi signifikan terhadap ROA (F = 1756,2; p < 0,0001) "
    "dengan nilai *Adjusted R-Squared* sebesar 0,9855 (98,55%). Temuan ini mengindikasikan bahwa ekspansi "
    "pembiayaan berwawasan lingkungan dan bantalan permodalan yang kokoh berasosiasi positif dengan "
    "profitabilitas bank KBMI 4, sementara risiko kredit pada bank bermodal besar termitigasi oleh cadangan "
    "permodalan dan CKPN yang tebal."
)

KATA_KUNCI_ID = "*Green Financing*, *Non-Performing Loan*, *Capital Adequacy Ratio*, *Return on Assets*, Bank KBMI 4, Ekonometrika Data Panel, Keuangan Berkelanjutan."

ABSTRAK_EN = (
    "*The objective of this research is to empirically examine, verify, and analyze the effect of Green "
    "Financing Portfolio, Non-Performing Loan (NPL), and Capital Adequacy Ratio (CAR) on Profitability "
    "(Return on Assets / ROA) in commercial banks classified under Core Capital Commercial Bank Group "
    "(KBMI) 4 listed on the Indonesia Stock Exchange (IDX) during the period of 2021 to 2025.*\n\n"
    "*This study adopts an explanatory causal quantitative approach utilizing panel data regression "
    "analysis. Sample selection was conducted through purposive sampling: banks categorized under KBMI 4 "
    "with core capital exceeding IDR 70 Trillion, consistently publishing comprehensive Annual Reports and "
    "Sustainability Reports, and generating positive net income throughout 2021\u20132025. Four of Indonesia's "
    "largest commercial banking entities met the criteria: BBRI, BMRI, BBCA, and BBNI. With a quarterly "
    "observation timeframe across 5 years (T=20), a total of 80 balanced panel observations were analyzed "
    "using EViews 12. Model specification through the Chow Test (F = 18.420, p < 0.0001) and Hausman Test "
    "(Random = 14.250, p = 0.0026) formally established that the Fixed Effect Model (FEM) is the optimal "
    "estimator.*\n\n"
    "*The FEM estimation with Driscoll-Kraay robust standard errors reveals: (1) Green Financing exerts a "
    "positive and statistically significant association with ROA (beta1 = +0.0767; p < 0.0001); (2) NPL "
    "exhibits a negative coefficient but is not statistically significant at the 5% level (beta2 = -0.0721; "
    "p = 0.1308); (3) CAR exerts a positive and statistically significant association with ROA (beta3 = "
    "+0.0813; p < 0.0001); and (4) Simultaneously, Green Financing, NPL, and CAR have a statistically "
    "significant joint association with ROA (F = 1756.2; p < 0.0001) with an Adjusted R-Squared of 0.9855 "
    "(98.55%). These findings demonstrate that sustainable green lending and robust capital buffers are the "
    "principal drivers associated with superior profitability among KBMI 4 banks.*"
)

KEYWORDS_EN = "Green Financing, Non-Performing Loan, Capital Adequacy Ratio, Return on Assets, KBMI 4 Banks, Panel Data Econometrics, Sustainable Finance."


def build_abstrak(doc, lang="id"):
    if lang == "id":
        add_heading_bab(doc, "", "ABSTRAK")
        add_blank(doc)
        # Header line
        hdr = (f"{PENULIS} (NIM: {NIM}). {JUDUL}. {PRODI}, {FAKULTAS}, "
               f"{UNIVERSITAS}, {TAHUN}. Pembimbing: {PEMBIMBING}.")
        add_body(doc, hdr, first_indent=True)
        add_blank(doc)
        for blk in ABSTRAK_ID.split('\n\n'):
            add_body(doc, blk.strip(), first_indent=True)
        add_blank(doc)
        para = doc.add_paragraph()
        para_fmt(para, space_before=0, space_after=0)
        r1 = para.add_run("Kata Kunci: ")
        set_run_font(r1, size=12, bold=True)
        r2 = para.add_run(KATA_KUNCI_ID)
        set_run_font(r2, size=12, italic=True)
        add_blank(doc)
        add_signature_table(doc, [
            ("Mahasiswa", PENULIS),
            ("Dosen Pembimbing", PEMBIMBING),
        ])
    else:
        add_heading_bab(doc, "", "ABSTRACT")
        add_blank(doc)
        hdr = (f"{PENULIS} (Student ID: {NIM}). {JUDUL}. {PRODI}, {FAKULTAS}, "
               f"{UNIVERSITAS}, {TAHUN}. Supervisor: {PEMBIMBING}.")
        add_body(doc, hdr, first_indent=True)
        add_blank(doc)
        for blk in ABSTRAK_EN.split('\n\n'):
            add_body(doc, blk.strip(), first_indent=True)
        add_blank(doc)
        para = doc.add_paragraph()
        para_fmt(para, space_before=0, space_after=0)
        r1 = para.add_run("Keywords: ")
        set_run_font(r1, size=12, bold=True, italic=True)
        r2 = para.add_run(KEYWORDS_EN)
        set_run_font(r2, size=12, italic=True)
        add_blank(doc)
        add_signature_table(doc, [
            ("Student", PENULIS),
            ("Supervisor", PEMBIMBING),
        ])


# ─────────────────────────────────────────────────────────
# DAFTAR ISI (static)
# ─────────────────────────────────────────────────────────
TOC_ENTRIES = [
    ("PERNYATAAN KEASLIAN KARYA TUGAS AKHIR", "ii", True),
    ("HALAMAN PERSETUJUAN DOSEN PEMBIMBING", "iii", True),
    ("HALAMAN PENGESAHAN TIM PENGUJI", "iv", True),
    ("PERSETUJUAN PROPOSAL TUGAS AKHIR", "v", True),
    ("PERNYATAAN PERSETUJUAN PUBLIKASI KARYA TUGAS AKHIR", "vi", True),
    ("KATA PENGANTAR", "vii", True),
    ("ABSTRAK", "viii", True),
    ("ABSTRACT", "ix", True),
    ("DAFTAR ISI", "x", True),
    ("DAFTAR TABEL", "xiii", True),
    ("DAFTAR GAMBAR", "xiv", True),
    ("", "", False),
    ("BAB 1  PENDAHULUAN", "1", True),
    ("    1.1 Latar Belakang Penelitian", "1", False),
    ("    1.2 Identifikasi Masalah", "14", False),
    ("    1.3 Pembatasan Masalah", "15", False),
    ("    1.4 Perumusan Masalah", "16", False),
    ("    1.5 Tujuan Penelitian", "16", False),
    ("    1.6 Manfaat Penelitian", "17", False),
    ("    1.7 Sistematika Penulisan Skripsi", "18", False),
    ("", "", False),
    ("BAB 2  TINJAUAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS", "19", True),
    ("    2.1 Landasan Teori", "19", False),
    ("    2.2 Konseptualisasi Variabel Penelitian", "32", False),
    ("    2.3 Penelitian Sebelumnya", "43", False),
    ("    2.4 Kerangka Pemikiran Konseptual", "50", False),
    ("    2.5 Pengembangan Hipotesis", "52", False),
    ("", "", False),
    ("BAB 3  METODE PENELITIAN", "56", True),
    ("    3.1 Desain dan Paradigma Penelitian", "56", False),
    ("    3.2 Populasi dan Sampel", "57", False),
    ("    3.3 Jenis dan Sumber Data", "60", False),
    ("    3.4 Definisi Operasional dan Pengukuran Variabel", "60", False),
    ("    3.5 Model Ekonometrika Data Panel", "63", False),
    ("    3.6 Teknik Analisis Data", "65", False),
    ("", "", False),
    ("BAB 4  ANALISIS DAN PEMBAHASAN", "78", True),
    ("    4.1 Gambaran Umum Objek Penelitian", "78", False),
    ("    4.2 Analisis Tren Variabel Triwulanan 2021\u20132025", "86", False),
    ("    4.3 Statistik Deskriptif", "90", False),
    ("    4.4 Uji Stasioneritas Panel (Unit Root)", "93", False),
    ("    4.5 Pemilihan Model Regresi Panel", "94", False),
    ("    4.6 Uji Asumsi Klasik", "96", False),
    ("    4.7 Hasil Estimasi Fixed Effect Model (FEM)", "101", False),
    ("    4.8 Pembuktian Hipotesis", "108", False),
    ("    4.9 Pembahasan Mendalam", "113", False),
    ("", "", False),
    ("BAB 5  PENUTUP", "128", True),
    ("    5.1 Kesimpulan", "128", False),
    ("    5.2 Saran", "131", False),
    ("    5.3 Keterbatasan Penelitian", "133", False),
    ("", "", False),
    ("DAFTAR PUSTAKA", "135", True),
    ("LAMPIRAN", "147", True),
    ("DAFTAR RIWAYAT HIDUP", "158", True),
]


def build_daftar_isi(doc):
    add_heading_bab(doc, "", "DAFTAR ISI")
    add_blank(doc)
    for entry, page, bold in TOC_ENTRIES:
        if not entry:
            add_blank(doc)
            continue
        para = doc.add_paragraph()
        para_fmt(para, space_before=0, space_after=0)
        run_e = para.add_run(entry)
        set_run_font(run_e, size=12, bold=bold)
        para.add_run("\t")
        run_p = para.add_run(page)
        set_run_font(run_p, size=12, bold=bold)
        pPr = para._p.get_or_add_pPr()
        tabs = OxmlElement('w:tabs')
        tab = OxmlElement('w:tab')
        tab.set(qn('w:val'), 'right')
        tab.set(qn('w:leader'), 'dot')
        tab.set(qn('w:pos'), '8640')
        tabs.append(tab)
        pPr.append(tabs)


# ─────────────────────────────────────────────────────────
# DAFTAR TABEL & GAMBAR (from source)
# ─────────────────────────────────────────────────────────
DAFTAR_TABEL = [
    ("Tabel 1.1.", "Ringkasan Kebijakan Insentif Makroprudensial Hijau BI dan OJK (2021\u20132025)", "10"),
    ("Tabel 2.1.", "Matriks Sintesis Penelitian Terdahulu", "43"),
    ("Tabel 3.1.", "Kriteria dan Proses Seleksi Sampel", "58"),
    ("Tabel 3.2.", "Daftar Sampel Penelitian Bank KBMI 4", "59"),
    ("Tabel 3.3.", "Definisi Operasional dan Pengukuran Variabel Penelitian", "62"),
    ("Tabel 3.4.", "Pedoman Interpretasi Koefisien Determinasi (R-Squared)", "67"),
    ("Tabel 3.5.", "Pedoman Interpretasi Uji Durbin-Watson", "73"),
    ("Tabel 4.1.", "Profil Singkat Bank KBMI 4 (Data per Akhir 2025)", "79"),
    ("Tabel 4.2.", "Data Green Financing (% dari Total Kredit) per Kuartal, 2021\u20132025", "86"),
    ("Tabel 4.3.", "Data NPL (%) per Kuartal, 2021\u20132025", "87"),
    ("Tabel 4.4.", "Data CAR (%) per Kuartal, 2021\u20132025", "88"),
    ("Tabel 4.5.", "Data ROA (%) per Kuartal, 2021\u20132025", "89"),
    ("Tabel 4.6.", "Statistik Deskriptif Variabel Penelitian (N=80)", "91"),
    ("Tabel 4.7.", "Hasil Uji Stasioneritas Panel \u2013 Levin-Lin-Chu (LLC) Test", "93"),
    ("Tabel 4.8.", "Hasil Uji Chow (Cross-section F Test)", "94"),
    ("Tabel 4.9.", "Hasil Uji Hausman (Correlated Random Effects Hausman Test)", "95"),
    ("Tabel 4.10.", "Hasil Uji Jarque-Bera Normalitas Residual", "96"),
    ("Tabel 4.11.", "Hasil Uji VIF Multikolinearitas Antar Variabel Independen", "97"),
    ("Tabel 4.12.", "Hasil Uji White Heteroskedastisitas", "98"),
    ("Tabel 4.13.", "Hasil Uji Durbin-Watson Autokorelasi", "99"),
    ("Tabel 4.14.", "Rekapitulasi Hasil Uji Asumsi Klasik BLUE", "100"),
    ("Tabel 4.15.", "Hasil Estimasi Fixed Effect Model (FEM) \u2013 Driscoll-Kraay Robust SE", "102"),
    ("Tabel 4.16.", "Efek Spesifik Individual (Fixed Effects) Masing-Masing Bank KBMI 4", "105"),
    ("Tabel 4.17.", "Ringkasan Hasil Pembuktian Hipotesis Penelitian", "112"),
    ("Tabel 4.18.", "Perbandingan Temuan Penelitian dengan Studi Terdahulu", "113"),
    ("Tabel 5.1.", "Ringkasan Kesimpulan Hasil Pengujian Hipotesis", "130"),
]

DAFTAR_GAMBAR = [
    ("Gambar 2.1.", "Kerangka Pemikiran Konseptual Penelitian", "51"),
    ("Gambar 4.1.", "Tren Portofolio Green Financing Bank KBMI 4 (2021\u20132025)", "86"),
    ("Gambar 4.2.", "Tren NPL Bank KBMI 4 (2021\u20132025)", "88"),
    ("Gambar 4.3.", "Tren CAR Bank KBMI 4 (2021\u20132025)", "89"),
    ("Gambar 4.4.", "Tren ROA Bank KBMI 4 (2021\u20132025)", "90"),
    ("Gambar 4.5.", "Grafik Residual vs. Fitted Values (Uji Heteroskedastisitas Visual)", "98"),
    ("Gambar 4.6.", "Histogram Distribusi Residual FEM (Uji Normalitas Jarque-Bera)", "97"),
]


def build_daftar_tabel(doc):
    add_heading_bab(doc, "", "DAFTAR TABEL")
    add_blank(doc)
    for num, judul, hal in DAFTAR_TABEL:
        para = doc.add_paragraph()
        para_fmt(para, space_before=0, space_after=0,
                 first_indent=Cm(-1.9), left_indent=Cm(1.9))
        r1 = para.add_run(f"{num} ")
        set_run_font(r1, size=12)
        r2 = para.add_run(judul)
        set_run_font(r2, size=12)
        para.add_run("\t")
        r3 = para.add_run(hal)
        set_run_font(r3, size=12)
        pPr = para._p.get_or_add_pPr()
        tabs = OxmlElement('w:tabs')
        tab = OxmlElement('w:tab')
        tab.set(qn('w:val'), 'right')
        tab.set(qn('w:leader'), 'dot')
        tab.set(qn('w:pos'), '8640')
        tabs.append(tab)
        pPr.append(tabs)


def build_daftar_gambar(doc):
    add_heading_bab(doc, "", "DAFTAR GAMBAR")
    add_blank(doc)
    for num, judul, hal in DAFTAR_GAMBAR:
        para = doc.add_paragraph()
        para_fmt(para, space_before=0, space_after=0,
                 first_indent=Cm(-2.1), left_indent=Cm(2.1))
        r1 = para.add_run(f"{num} ")
        set_run_font(r1, size=12)
        r2 = para.add_run(judul)
        set_run_font(r2, size=12)
        para.add_run("\t")
        r3 = para.add_run(hal)
        set_run_font(r3, size=12)
        pPr = para._p.get_or_add_pPr()
        tabs = OxmlElement('w:tabs')
        tab = OxmlElement('w:tab')
        tab.set(qn('w:val'), 'right')
        tab.set(qn('w:leader'), 'dot')
        tab.set(qn('w:pos'), '8640')
        tabs.append(tab)
        pPr.append(tabs)


# ─────────────────────────────────────────────────────────
# CONTENT PARSER (BAB 1-5 + DAFTAR PUSTAKA)
# ─────────────────────────────────────────────────────────
def parse_and_write_content(doc, md_text: str):
    """
    Parse the MD content (BAB 1-5, Daftar Pustaka, Lampiran)
    and write it into the DOCX with proper formatting.
    """
    lines = md_text.splitlines()
    i = 0
    in_enumerate = False
    enum_counter = 0
    in_itemize = False
    current_bab = None

    def flush_list():
        nonlocal in_enumerate, enum_counter, in_itemize
        in_enumerate = False
        enum_counter = 0
        in_itemize = False

    while i < len(lines):
        raw = lines[i]
        line = raw.strip()

        # Skip pure LaTeX boilerplate
        if is_latex_noise(line) or not line:
            i += 1
            continue

        # ── BAB headings from MD ──
        if re.match(r'^#\s+BAB\s+\d', line) or re.match(r'^# BAB \d', line):
            flush_list()
            # Extract BAB number and title
            m = re.match(r'^#+\s+BAB\s+(\d+).*', line)
            if m:
                bab_num = m.group(1)
                # Look ahead for title on next non-empty line
                j = i + 1
                title_parts = []
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines):
                    next_l = lines[j].strip()
                    if not next_l.startswith('#') and not next_l.startswith('\\') and not is_latex_noise(next_l):
                        title_parts.append(clean_latex(next_l))
                bab_titles = {
                    "1": "PENDAHULUAN",
                    "2": "TINJAUAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS",
                    "3": "METODE PENELITIAN",
                    "4": "ANALISIS DAN PEMBAHASAN",
                    "5": "PENUTUP",
                }
                title = bab_titles.get(bab_num, " ".join(title_parts) or "")
                current_bab = bab_num
                doc.add_page_break()
                add_heading_bab(doc, bab_num, title)
                add_blank(doc)
            i += 1
            continue

        # ── DAFTAR PUSTAKA ──
        if re.search(r'DAFTAR PUSTAKA', line, re.IGNORECASE) and line.startswith('#'):
            flush_list()
            doc.add_page_break()
            add_heading_bab(doc, "", "DAFTAR PUSTAKA")
            add_blank(doc)
            i += 1
            continue

        # ── LAMPIRAN ──
        if re.search(r'^#+\s*LAMPIRAN', line, re.IGNORECASE):
            flush_list()
            doc.add_page_break()
            add_heading_bab(doc, "", "LAMPIRAN")
            add_blank(doc)
            i += 1
            continue

        # ── DAFTAR RIWAYAT HIDUP ──
        if re.search(r'DAFTAR RIWAYAT HIDUP', line, re.IGNORECASE) and line.startswith('#'):
            flush_list()
            doc.add_page_break()
            add_heading_bab(doc, "", "DAFTAR RIWAYAT HIDUP PENULIS SKRIPSI")
            add_blank(doc)
            i += 1
            continue

        # ── H2 subheadings (## ) ──
        if line.startswith('## ') and not line.startswith('### '):
            flush_list()
            title = clean_latex(strip_md_markers(line))
            # Detect if it has a section number pattern
            if re.match(r'^\d+\.\d+', title) or re.match(r'^\d+\.', title):
                add_sub(doc, title, level=2)
            else:
                add_sub(doc, title, level=2)
            i += 1
            continue

        # ── H3 subheadings (### ) ──
        if line.startswith('### '):
            flush_list()
            title = clean_latex(strip_md_markers(line))
            add_sub(doc, title, level=3)
            i += 1
            continue

        # ── H4 subheadings (#### ) ──
        if line.startswith('#### '):
            flush_list()
            title = clean_latex(strip_md_markers(line))
            para = doc.add_paragraph()
            para_fmt(para, space_before=6, space_after=3)
            run = para.add_run(title)
            set_run_font(run, size=12, bold=True, italic=True)
            i += 1
            continue

        # ── LaTeX \begin{enumerate} ──
        if re.match(r'\\begin\{enumerate', line):
            flush_list()
            in_enumerate = True
            enum_counter = 0
            i += 1
            continue

        # ── LaTeX \end{enumerate} ──
        if re.match(r'\\end\{enumerate', line):
            in_enumerate = False
            enum_counter = 0
            i += 1
            continue

        # ── LaTeX \begin{itemize} ──
        if re.match(r'\\begin\{itemize', line):
            flush_list()
            in_itemize = True
            i += 1
            continue

        # ── LaTeX \end{itemize} ──
        if re.match(r'\\end\{itemize', line):
            in_itemize = False
            i += 1
            continue

        # ── LaTeX \item ──
        if re.match(r'\s*\\item', line):
            item_text = re.sub(r'^\s*\\item\s*(\[[^\]]*\])?\s*', '', line)
            # Collect multiline item
            j = i + 1
            while j < len(lines):
                next_raw = lines[j].strip()
                if (not next_raw or next_raw.startswith('\\item') or
                        next_raw.startswith('\\begin') or next_raw.startswith('\\end') or
                        next_raw.startswith('#') or next_raw.startswith('%')):
                    break
                item_text += ' ' + next_raw
                j += 1
            item_text = clean_latex(item_text).strip()
            if item_text:
                if in_enumerate:
                    enum_counter += 1
                    add_numbered_item(doc, enum_counter, item_text)
                else:
                    add_bullet_item(doc, item_text)
            i = j
            continue

        # ── Markdown numbered list ──
        m_num = re.match(r'^(\d+)\.\s+(.+)', line)
        if m_num:
            num = m_num.group(1)
            text = clean_latex(m_num.group(2)).strip()
            # Collect multiline
            j = i + 1
            while j < len(lines):
                next_raw = lines[j].strip()
                if (not next_raw or re.match(r'^\d+\.', next_raw) or
                        next_raw.startswith('#') or next_raw.startswith('\\')):
                    break
                text += ' ' + clean_latex(next_raw)
                j += 1
            text = text.strip()
            if text:
                add_numbered_item(doc, num, text)
            i = j
            continue

        # ── Markdown bullet list ──
        if re.match(r'^[-*•▪]\s+', line):
            text = re.sub(r'^[-*•▪]\s+', '', line)
            text = clean_latex(text).strip()
            j = i + 1
            while j < len(lines):
                next_raw = lines[j].strip()
                if (not next_raw or re.match(r'^[-*•▪]\s+', next_raw) or
                        next_raw.startswith('#') or next_raw.startswith('\\')):
                    break
                text += ' ' + clean_latex(next_raw)
                j += 1
            if text:
                add_bullet_item(doc, text)
            i = j
            continue

        # ── Regular paragraph text ──
        # Skip pure LaTeX lines
        if line.startswith('\\') and not re.match(r'\\textbf|\\textit|\\emph', line):
            i += 1
            continue

        # Collect full paragraph (multi-line text until blank or heading)
        para_lines = [line]
        j = i + 1
        while j < len(lines):
            next_raw = lines[j].strip()
            if (not next_raw or
                    next_raw.startswith('#') or
                    re.match(r'^\s*\\(item|begin|end|vspace|vfill|hfill|newpage|clearpage|pagenumbering|pagestyle|setcounter|addcontents|renewcommand|thispagestyle)', next_raw) or
                    next_raw.startswith('%') or
                    re.match(r'^---+$', next_raw) or
                    re.match(r'^\d+\.\s+', next_raw) or
                    re.match(r'^[-*•▪]\s+', next_raw)):
                break
            if not is_latex_noise(next_raw):
                para_lines.append(next_raw)
            j += 1

        full_text = ' '.join(para_lines)
        full_text = clean_latex(full_text)
        full_text = full_text.strip()

        if full_text and len(full_text) > 3:
            add_body(doc, full_text, first_indent=True)

        i = j
        continue


# ─────────────────────────────────────────────────────────
# MAIN BUILD
# ─────────────────────────────────────────────────────────
def build():
    print("Membaca file sumber...")
    md_text = INPUT_MD.read_text(encoding='utf-8')
    total_lines = md_text.count('\n')
    print(f"  {INPUT_MD.name} — {total_lines} baris, {len(md_text)//1024} KB")

    print("Membuat dokumen DOCX...")
    doc = Document()

    # Default style
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)

    # ── SECTION 1: Bagian Awal (nomor romawi) ──
    sec1 = doc.sections[0]
    set_margins(sec1)
    add_footer_roman(sec1)

    print("  [1/15] Halaman Sampul...")
    build_sampul(doc)
    doc.add_page_break()

    print("  [2/15] Pernyataan Keaslian...")
    build_keaslian(doc)
    doc.add_page_break()

    print("  [3/15] Persetujuan Pembimbing...")
    build_persetujuan(doc)
    doc.add_page_break()

    print("  [4/15] Pengesahan Tim Penguji...")
    build_pengesahan(doc)
    doc.add_page_break()

    print("  [5/15] Persetujuan Proposal...")
    # Simplified page
    add_heading_bab(doc, "", "PERSETUJUAN PROPOSAL TUGAS AKHIR")
    add_blank(doc)
    add_info_table(doc, [
        ("Nama",          f": {PENULIS}"),
        ("N.I.M.",        f": {NIM}"),
        ("Program Studi", f": {PRODI}"),
        ("Konsentrasi",   f": {KONSENTRASI}"),
    ])
    add_blank(doc)
    add_body(doc, f"**Judul yang Diajukan:**\n{JUDUL}", first_indent=False)
    add_blank(doc)
    add_signature_table(doc, [
        ("Dosen Pembimbing", PEMBIMBING),
        ("Dosen Pendamping", "________________________"),
    ])
    add_blank(doc)
    add_body(doc, f"Mengetahui,\nKetua Program Studi Manajemen\n\n( {KAPRODI} )", first_indent=False)
    doc.add_page_break()

    print("  [6/15] Persetujuan Publikasi...")
    build_publikasi(doc)
    doc.add_page_break()

    print("  [7/15] Kata Pengantar...")
    build_kata_pengantar(doc)
    doc.add_page_break()

    print("  [8/15] Abstrak (Indonesia)...")
    build_abstrak(doc, "id")
    doc.add_page_break()

    print("  [9/15] Abstract (English)...")
    build_abstrak(doc, "en")
    doc.add_page_break()

    print("  [10/15] Daftar Isi...")
    build_daftar_isi(doc)
    doc.add_page_break()

    print("  [11/15] Daftar Tabel...")
    build_daftar_tabel(doc)
    doc.add_page_break()

    print("  [12/15] Daftar Gambar...")
    build_daftar_gambar(doc)

    # ── SECTION 2: Bagian Isi (nomor arab) ──
    sec2 = doc.add_section(WD_SECTION.NEW_PAGE)
    set_margins(sec2)
    add_footer_arabic(sec2)

    print("  [13/15] BAB 1-5, Daftar Pustaka, Lampiran (parsing MD)...")
    # Find the content start (after ABSTRACT section in MD)
    # Find the BAB 1 heading position
    bab1_match = re.search(r'^# BAB 1', md_text, re.MULTILINE)
    if bab1_match:
        content_md = md_text[bab1_match.start():]
    else:
        content_md = md_text

    parse_and_write_content(doc, content_md)

    # ── DAFTAR RIWAYAT HIDUP ──
    print("  [14/15] Daftar Riwayat Hidup...")
    doc.add_page_break()
    add_heading_bab(doc, "", "DAFTAR RIWAYAT HIDUP PENULIS SKRIPSI")
    add_blank(doc)
    table = doc.add_table(rows=1, cols=2)
    lc = table.rows[0].cells[0]
    rc = table.rows[0].cells[1]
    lp = lc.paragraphs[0]
    lp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    lr = lp.add_run("[ Foto 4 x 6 ]")
    set_run_font(lr, size=11, italic=True, color=(128, 128, 128))
    info_riwayat = [
        f"Nama Lengkap   : {PENULIS}",
        f"NIM             : {NIM}",
        "Tempat/Tgl Lahir: ........................................",
        "Alamat          : ........................................",
        "Email           : ........................................",
        f"Program Studi   : {PRODI}",
        "",
        "Riwayat Pendidikan:",
        f"2022 \u2013 {TAHUN} : {PRODI}, FEB {UNIVERSITAS}",
        "20XX \u2013 20XX  : [Nama SMA]",
        "20XX \u2013 20XX  : [Nama SMP]",
    ]
    for idx, info_line in enumerate(info_riwayat):
        rcp = rc.paragraphs[0] if idx == 0 else rc.add_paragraph()
        para_fmt(rcp, space_before=0, space_after=0)
        set_run_font(rcp.add_run(info_line), size=12,
                     bold=info_line.startswith("Riwayat"))

    print("  [15/15] Menyimpan file...")
    doc.save(OUTPUT)
    print(f"\n  SELESAI! File tersimpan di:")
    print(f"   {OUTPUT}")
    size_kb = OUTPUT.stat().st_size // 1024
    print(f"   Ukuran: {size_kb} KB")


if __name__ == "__main__":
    build()

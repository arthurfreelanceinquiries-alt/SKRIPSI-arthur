"""
generate_template_word.py
Membuat template Word (.docx) skripsi FEB UKRIDA 2022
Sesuai Buku Pedoman Penyusunan Skripsi FEB Ukrida SK 221/SK/UKKW/FEB/D/IV/2022

Run: z:\Skripsi\.venv\Scripts\python.exe generate_template_word.py
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION, WD_ORIENTATION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def set_run_font(run, name="Times New Roman", size=12, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)
    rPr = run._r.get_or_add_rPr()
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:cs"), name)
    rPr.insert(0, rFonts)


def set_para_spacing(para, space_before=0, space_after=0,
                     line_spacing=1.5, line_spacing_rule=WD_LINE_SPACING.MULTIPLE):
    pf = para.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing_rule = line_spacing_rule
    pf.line_spacing = line_spacing


def add_paragraph(doc, text="", style=None, bold=False, italic=False,
                  alignment=WD_ALIGN_PARAGRAPH.JUSTIFY, size=12,
                  space_before=0, space_after=0, line_spacing=1.5,
                  first_line_indent=None, left_indent=None, color=None):
    if style:
        para = doc.add_paragraph(style=style)
    else:
        para = doc.add_paragraph()

    para.alignment = alignment
    set_para_spacing(para, space_before, space_after, line_spacing)

    pf = para.paragraph_format
    if first_line_indent is not None:
        pf.first_line_indent = first_line_indent
    if left_indent is not None:
        pf.left_indent = left_indent

    if text:
        run = para.add_run(text)
        set_run_font(run, size=size, bold=bold, italic=italic, color=color)

    return para


def add_heading_bab(doc, bab_number, bab_title):
    """BAB heading: ALL CAPS, Bold, Center, TNR 12"""
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_spacing(para, space_before=0, space_after=12)

    if bab_number:
        run1 = para.add_run(f"BAB {bab_number}\n")
        set_run_font(run1, size=12, bold=True)

    run2 = para.add_run(bab_title.upper())
    set_run_font(run2, size=12, bold=True)

    return para


def add_subheading(doc, number, title, level=2):
    """Sub-heading: Title Case Bold, Justify"""
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    set_para_spacing(para, space_before=12, space_after=6)
    run = para.add_run(f"{number} {title}")
    set_run_font(run, size=12, bold=True)
    return para


def add_body_text(doc, text):
    """Body text: TNR 12, Justify, 1.5 spasi, indent 1.25cm"""
    para = add_paragraph(
        doc, text,
        alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
        size=12,
        space_before=0, space_after=0,
        line_spacing=1.5,
        first_line_indent=Cm(1.25),
    )
    return para


def add_page_break(doc):
    doc.add_page_break()


def add_placeholder_note(doc, text):
    """Gray italic placeholder note"""
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_spacing(para, space_before=6, space_after=6)
    run = para.add_run(f"[ {text} ]")
    set_run_font(run, size=11, italic=True, color=(128, 128, 128))
    return para


def set_page_margins(section):
    section.left_margin = Cm(4)
    section.right_margin = Cm(3)
    section.top_margin = Cm(3)
    section.bottom_margin = Cm(3)


def add_footer_romawi(section, doc):
    footer = section.footer
    footer.is_linked_to_previous = False
    para = footer.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para.clear()
    run = para.add_run()
    set_run_font(run, size=10)
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.text = r' PAGE \* lowerroman '
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'end')
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)


def add_footer_latin(section):
    footer = section.footer
    footer.is_linked_to_previous = False
    para = footer.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    para.clear()

    run_num = para.add_run()
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.text = ' PAGE '
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'end')
    run_num._r.append(fldChar1)
    run_num._r.append(instrText)
    run_num._r.append(fldChar2)
    set_run_font(run_num, size=10, bold=True)

    run_uni = para.add_run("  Universitas Kristen Krida Wacana")
    set_run_font(run_uni, size=10, bold=True)


def add_section_break(doc, break_type=WD_SECTION.NEW_PAGE):
    new_section = doc.add_section(break_type)
    return new_section


def add_table_caption(doc, caption_text):
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_spacing(para, space_before=12, space_after=3)
    run = para.add_run(caption_text)
    set_run_font(run, size=12)
    return para


def add_figure_caption(doc, caption_text):
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_spacing(para, space_before=3, space_after=12)
    run = para.add_run(caption_text)
    set_run_font(run, size=12)
    return para


# ─────────────────────────────────────────────
# HALAMAN-HALAMAN AWAL
# ─────────────────────────────────────────────

def build_halaman_sampul(doc):
    add_paragraph(
        doc,
        "JUDUL SKRIPSI DITULIS DI SINI\nDENGAN HURUF KAPITAL DAN BOLD",
        bold=True, size=14,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=48, space_after=24, line_spacing=1.5
    )
    add_placeholder_note(doc, "Logo UKRIDA 5cm x 5cm — tinta emas")
    add_paragraph(doc, "SKRIPSI", bold=True, size=12,
                  alignment=WD_ALIGN_PARAGRAPH.CENTER,
                  space_before=24, space_after=12)
    add_paragraph(doc,
                  "Diajukan untuk memenuhi salah satu syarat\n"
                  "menjadi Sarjana Manajemen / Sarjana Akuntansi",
                  size=12, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                  space_before=6, space_after=18, line_spacing=1.5)
    add_paragraph(doc, "Oleh:", size=12, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                  space_before=6, space_after=6)
    add_paragraph(doc, "NAMA MAHASISWA", bold=True, size=12,
                  alignment=WD_ALIGN_PARAGRAPH.CENTER, space_before=3, space_after=3)
    add_paragraph(doc, "NIM: XXXXXXXXX", size=12,
                  alignment=WD_ALIGN_PARAGRAPH.CENTER, space_before=3, space_after=36)
    add_paragraph(doc,
                  "PROGRAM STUDI MANAJEMEN / AKUNTANSI\n"
                  "FAKULTAS EKONOMI DAN BISNIS\n"
                  "UNIVERSITAS KRISTEN KRIDA WACANA\n"
                  "JAKARTA\n"
                  "20XX",
                  bold=True, size=12, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                  space_before=6, space_after=0, line_spacing=1.5)


def build_halaman_judul(doc):
    add_heading_bab(doc, "", "HALAMAN JUDUL")
    add_paragraph(doc, "(Isi sama dengan halaman sampul — kertas HVS putih 80 gram A4)",
                  size=11, italic=True, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                  space_before=12, space_after=6, color=(128, 128, 128))


def build_halaman_keaslian(doc):
    add_heading_bab(doc, "", "PERNYATAAN KEASLIAN KARYA TUGAS AKHIR")
    add_paragraph(doc, "", space_before=12)
    add_body_text(doc, "Saya yang bertanda tangan di bawah ini:")
    add_paragraph(doc, "", space_before=6)

    table = doc.add_table(rows=4, cols=2)
    info = [
        ("Nama", ": ..................................."),
        ("NIM", ": ..................................."),
        ("Program Studi", ": ..................................."),
        ("Judul Skripsi", ": ..................................."),
    ]
    for i, (label, val) in enumerate(info):
        table.rows[i].cells[0].text = label
        table.rows[i].cells[1].text = val
        for cell in table.rows[i].cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    set_run_font(run, size=12)

    add_paragraph(doc, "", space_before=6)
    add_body_text(doc,
        "Menyatakan bahwa skripsi ini adalah hasil karya saya sendiri dan bukan "
        "merupakan jiplakan dari hasil karya orang lain. Apabila dikemudian hari "
        "terbukti pernyataan ini tidak benar, saya bersedia menerima sanksi yang berlaku.")
    add_paragraph(doc, "", space_before=36)
    add_paragraph(doc, "Jakarta, .......................... 20XX",
                  size=12, alignment=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=48)
    add_paragraph(doc, "( ................................................ )",
                  size=12, alignment=WD_ALIGN_PARAGRAPH.RIGHT)


def build_halaman_persetujuan(doc):
    add_heading_bab(doc, "", "HALAMAN PERSETUJUAN DOSEN PEMBIMBING")
    add_paragraph(doc, "", space_before=12)
    add_body_text(doc, "Skripsi berjudul:")
    add_paragraph(doc, '"JUDUL SKRIPSI DITULIS DI SINI"',
                  bold=True, size=12, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                  space_before=12, space_after=12, line_spacing=1.5)
    add_body_text(doc,
        "yang disusun oleh Nama Mahasiswa (NIM: XXXXXXXXX), Mahasiswa Program Studi "
        "Manajemen / Akuntansi Fakultas Ekonomi dan Bisnis Universitas Kristen Krida "
        "Wacana, telah disetujui untuk diseminarkan / diujikan.")
    add_paragraph(doc, "", space_before=36)

    table = doc.add_table(rows=1, cols=2)
    for cell, label in [(table.rows[0].cells[0], "Dosen Pembimbing,"),
                        (table.rows[0].cells[1], "Dosen Pendamping,")]:
        para = cell.paragraphs[0]
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = para.add_run(label + "\n\n\n\n\n( .................................. )")
        set_run_font(run, size=12)


def build_halaman_pengesahan(doc):
    add_heading_bab(doc, "", "HALAMAN PENGESAHAN TIM PENGUJI")
    add_paragraph(doc, "", space_before=12)
    add_body_text(doc,
        "Skripsi ini telah dipertahankan di hadapan Tim Penguji Skripsi Fakultas "
        "Ekonomi dan Bisnis Universitas Kristen Krida Wacana pada:")
    add_paragraph(doc, "", space_before=6)

    table = doc.add_table(rows=3, cols=2)
    info = [("Hari / Tanggal", ": ..................................."),
            ("Waktu", ": ..................................."),
            ("Tempat", ": ...................................")]
    for i, (label, val) in enumerate(info):
        table.rows[i].cells[0].text = label
        table.rows[i].cells[1].text = val
        for cell in table.rows[i].cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    set_run_font(run, size=12)

    add_paragraph(doc, "", space_before=24)
    add_body_text(doc, "Tim Penguji:")
    tbl = doc.add_table(rows=3, cols=2)
    penguji = [("Ketua Penguji", ""), ("Penguji 1", ""), ("Penguji 2", "")]
    for i, (label, _) in enumerate(penguji):
        tbl.rows[i].cells[0].text = label
        tbl.rows[i].cells[1].text = ": ( ...................................... )"
        for cell in tbl.rows[i].cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    set_run_font(run, size=12)


def build_halaman_publikasi(doc):
    add_heading_bab(doc, "", "PERNYATAAN PERSETUJUAN PUBLIKASI KARYA TUGAS AKHIR")
    add_paragraph(doc, "", space_before=12)
    add_body_text(doc, "Saya yang bertanda tangan di bawah ini menyatakan bahwa skripsi dengan judul:")
    add_paragraph(doc, '"JUDUL SKRIPSI DITULIS DI SINI"',
                  bold=True, size=12, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                  space_before=12, space_after=12, line_spacing=1.5)
    add_body_text(doc,
        "adalah benar-benar hasil karya saya sendiri. Dengan ini saya menyatakan "
        "persetujuan untuk mempublikasikan skripsi tersebut melalui perpustakaan "
        "Universitas Kristen Krida Wacana dengan tetap menghormati hak cipta saya sebagai penulis.")
    add_paragraph(doc, "", space_before=36)
    add_paragraph(doc, "Jakarta, .......................... 20XX",
                  size=12, alignment=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=48)
    add_paragraph(doc, "( ................................................ )",
                  size=12, alignment=WD_ALIGN_PARAGRAPH.RIGHT)


def build_kata_pengantar(doc):
    add_heading_bab(doc, "", "KATA PENGANTAR")
    add_paragraph(doc, "", space_before=6)
    add_body_text(doc,
        "Puji dan syukur penulis panjatkan kepada Tuhan Yang Maha Esa atas berkat "
        "dan rahmat-Nya sehingga penulis dapat menyelesaikan skripsi yang berjudul "
        '"[JUDUL SKRIPSI]" ini dengan baik.')
    add_body_text(doc,
        "Skripsi ini disusun sebagai salah satu syarat untuk memperoleh gelar "
        "Sarjana [Manajemen / Akuntansi] pada Program Studi [Manajemen / Akuntansi] "
        "Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana.")
    add_body_text(doc,
        "Dalam proses penulisan skripsi ini, penulis mendapat banyak bantuan, "
        "bimbingan, dan dukungan dari berbagai pihak. Oleh karena itu, penulis ingin "
        "menyampaikan ucapan terima kasih yang sebesar-besarnya kepada:")

    ucapan = [
        "Bapak/Ibu .......................... selaku Dosen Pembimbing yang telah memberikan "
        "bimbingan, arahan, dan masukan selama penyusunan skripsi ini.",
        "Bapak/Ibu .......................... selaku Ketua Program Studi [Manajemen / Akuntansi] "
        "Fakultas Ekonomi dan Bisnis UKRIDA.",
        "Seluruh Dosen Fakultas Ekonomi dan Bisnis UKRIDA yang telah memberikan ilmu dan "
        "pengetahuan kepada penulis selama masa perkuliahan.",
        "Orang tua dan keluarga yang telah memberikan doa, dukungan, dan semangat.",
        "Semua pihak yang tidak dapat disebutkan satu per satu yang telah membantu "
        "dalam penyelesaian skripsi ini.",
    ]
    for i, item in enumerate(ucapan, 1):
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=3, line_spacing=1.5)
        pf = para.paragraph_format
        pf.left_indent = Cm(1.25)
        pf.first_line_indent = Cm(-1.25)
        run = para.add_run(f"{i}. {item}")
        set_run_font(run, size=12)

    add_body_text(doc,
        "Penulis menyadari bahwa skripsi ini masih jauh dari sempurna. Oleh karena itu, "
        "penulis mengharapkan kritik dan saran yang membangun dari semua pihak demi "
        "perbaikan di masa mendatang.")
    add_paragraph(doc, "", space_before=24)
    add_paragraph(doc, "Jakarta, .......................... 20XX",
                  size=12, alignment=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=24)
    add_paragraph(doc, "Penulis,", size=12, alignment=WD_ALIGN_PARAGRAPH.RIGHT)
    add_paragraph(doc, "", size=12, alignment=WD_ALIGN_PARAGRAPH.RIGHT, space_before=36)
    add_paragraph(doc, "( Nama Lengkap Penulis )",
                  size=12, alignment=WD_ALIGN_PARAGRAPH.RIGHT)


def build_abstrak(doc, language="indonesia"):
    if language == "indonesia":
        add_heading_bab(doc, "", "ABSTRAK")
        add_paragraph(doc, "", space_before=6)
        add_body_text(doc,
            "[Nama Penulis] (NIM: XXXXXXXXX). [Judul Skripsi]. Program Studi "
            "[Manajemen / Akuntansi], Fakultas Ekonomi dan Bisnis, Universitas "
            "Kristen Krida Wacana, 20XX. Pembimbing: [Nama Dosen Pembimbing].")
        add_paragraph(doc, "", space_before=6)
        add_body_text(doc,
            "Tuliskan isi abstrak di sini. Abstrak berisi gambaran singkat mengenai "
            "latar belakang, tujuan, metode, hasil, dan kesimpulan penelitian. "
            "Abstrak ditulis dalam satu paragraf, tidak lebih dari 250 kata, tanpa referensi.")
        add_paragraph(doc, "", space_before=12)
        add_paragraph(doc,
                      "Kata Kunci: kata kunci 1, kata kunci 2, kata kunci 3, kata kunci 4, kata kunci 5",
                      size=12, italic=True, alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
                      space_before=0, space_after=0, line_spacing=1.5)
    else:
        add_heading_bab(doc, "", "ABSTRACT")
        add_paragraph(doc, "", space_before=6)
        add_body_text(doc,
            "[Author Name] (Student ID: XXXXXXXXX). [Thesis Title]. Study Program of "
            "[Management / Accounting], Faculty of Economics and Business, Universitas "
            "Kristen Krida Wacana, 20XX. Supervisor: [Supervisor Name].")
        add_paragraph(doc, "", space_before=6)
        add_body_text(doc,
            "Write the abstract content here. The abstract provides a brief overview "
            "of the background, objectives, methods, results, and conclusions of the "
            "research. The abstract is written in one paragraph, no more than 250 words, "
            "without references.")
        add_paragraph(doc, "", space_before=12)
        para = add_paragraph(doc, "", size=12, italic=True,
                      alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
                      space_before=0, space_after=0, line_spacing=1.5)
        run = para.add_run("Keywords: ")
        set_run_font(run, size=12, bold=True, italic=True)
        run2 = para.add_run("keyword 1, keyword 2, keyword 3, keyword 4, keyword 5")
        set_run_font(run2, size=12, italic=True)


def build_daftar_isi(doc):
    add_heading_bab(doc, "", "DAFTAR ISI")
    add_paragraph(doc, "", space_before=6)

    entries = [
        ("Halaman Judul", "i"), ("Pernyataan Keaslian Karya Tugas Akhir", "ii"),
        ("Halaman Persetujuan Dosen Pembimbing", "iii"),
        ("Halaman Pengesahan Tim Penguji", "iv"),
        ("Pernyataan Persetujuan Publikasi", "v"), ("Kata Pengantar", "vi"),
        ("Abstrak", "vii"), ("Abstract", "viii"),
        ("Daftar Isi", "ix"), ("Daftar Tabel", "x"), ("Daftar Gambar", "xi"),
        ("", ""),
        ("BAB 1  PENDAHULUAN", "1"),
        ("    1.1. Latar Belakang Penelitian", "1"),
        ("    1.2. Perumusan Masalah", "x"),
        ("    1.3. Tujuan Penelitian", "x"),
        ("    1.4. Manfaat Penelitian", "x"),
        ("", ""),
        ("BAB 2  TINJAUAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS", "x"),
        ("    2.1. Teori-teori", "x"),
        ("    2.2. Penelitian Sebelumnya", "x"),
        ("    2.3. Pengembangan Hipotesis", "x"),
        ("    2.4. Rerangka Penelitian", "x"),
        ("", ""),
        ("BAB 3  METODE PENELITIAN", "x"),
        ("    3.1. Jenis dan Sumber Data", "x"),
        ("    3.2. Populasi dan Sampel", "x"),
        ("    3.3. Model Penelitian", "x"),
        ("    3.4. Operasionalisasi Variabel", "x"),
        ("    3.5. Metode Analisis Data", "x"),
        ("", ""),
        ("BAB 4  ANALISIS DAN PEMBAHASAN", "x"),
        ("    4.1. Deskripsi Sampel Penelitian", "x"),
        ("    4.2. Statistik Deskriptif", "x"),
        ("    4.3. Hasil Uji Asumsi Klasik", "x"),
        ("    4.4. Hasil Pengujian Hipotesis", "x"),
        ("    4.5. Pembahasan", "x"),
        ("", ""),
        ("BAB 5  PENUTUP", "x"),
        ("    5.1. Kesimpulan", "x"),
        ("    5.2. Saran", "x"),
        ("", ""),
        ("DAFTAR PUSTAKA", "x"),
        ("LAMPIRAN", "x"),
        ("DAFTAR RIWAYAT HIDUP", "x"),
    ]

    for entry, page in entries:
        if not entry:
            add_paragraph(doc, "", space_before=3)
            continue
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=0, line_spacing=1.5)
        is_bab = entry.startswith("BAB")
        is_final = entry in ("DAFTAR PUSTAKA", "LAMPIRAN", "DAFTAR RIWAYAT HIDUP")
        run_text = para.add_run(entry)
        set_run_font(run_text, size=12, bold=(is_bab or is_final))
        para.add_run("\t")
        run_page = para.add_run(page)
        set_run_font(run_page, size=12, bold=(is_bab or is_final))
        pPr = para._p.get_or_add_pPr()
        tabs = OxmlElement('w:tabs')
        tab = OxmlElement('w:tab')
        tab.set(qn('w:val'), 'right')
        tab.set(qn('w:leader'), 'dot')
        tab.set(qn('w:pos'), '8640')
        tabs.append(tab)
        pPr.append(tabs)

    add_paragraph(doc, "", space_before=12)
    add_paragraph(doc,
                  "* Nomor halaman diperbarui saat Field daftar isi di-update (Klik kanan -> Update Field)",
                  size=10, italic=True, alignment=WD_ALIGN_PARAGRAPH.CENTER, color=(128, 128, 128))


# ─────────────────────────────────────────────
# BAB-BAB ISI
# ─────────────────────────────────────────────

def build_bab1(doc):
    add_heading_bab(doc, "1", "PENDAHULUAN")
    add_paragraph(doc, "", space_before=6)

    add_subheading(doc, "1.1.", "Latar Belakang Penelitian")
    add_body_text(doc,
        "Uraikan latar belakang penelitian di sini. Jelaskan mengapa topik ini menarik "
        "untuk diteliti, kesenjangan penelitian (research gap) yang ada, baik secara "
        "teoritis maupun praktis. Paparkan teori secara ringkas, hasil penelitian "
        "terdahulu, dan kontribusi penelitian ini.")

    add_subheading(doc, "1.2.", "Perumusan Masalah")
    add_body_text(doc, "Berdasarkan latar belakang di atas, perumusan masalah dalam penelitian ini adalah:")
    for i, p in enumerate([
        "Apakah variabel X1 berpengaruh terhadap variabel Y?",
        "Apakah variabel X2 berpengaruh terhadap variabel Y?",
        "Apakah variabel X3 berpengaruh terhadap variabel Y?",
    ], 1):
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=0, line_spacing=1.5)
        para.paragraph_format.left_indent = Cm(1.25)
        para.paragraph_format.first_line_indent = Cm(-1.25)
        set_run_font(para.add_run(f"{i}. {p}"), size=12)

    add_subheading(doc, "1.3.", "Tujuan Penelitian")
    add_body_text(doc, "Sesuai perumusan masalah di atas, tujuan penelitian ini adalah:")
    for i, t in enumerate([
        "Untuk menguji dan menganalisis pengaruh variabel X1 terhadap variabel Y.",
        "Untuk menguji dan menganalisis pengaruh variabel X2 terhadap variabel Y.",
        "Untuk menguji dan menganalisis pengaruh variabel X3 terhadap variabel Y.",
    ], 1):
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=0, line_spacing=1.5)
        para.paragraph_format.left_indent = Cm(1.25)
        para.paragraph_format.first_line_indent = Cm(-1.25)
        set_run_font(para.add_run(f"{i}. {t}"), size=12)

    add_subheading(doc, "1.4.", "Manfaat Penelitian")
    add_body_text(doc, "Hasil penelitian ini diharapkan dapat memberikan manfaat bagi berbagai pihak:")
    for i, (judul_m, isi_m) in enumerate([
        ("Aspek Teoritis", "Penelitian ini diharapkan dapat memberikan kontribusi terhadap pengembangan ilmu pengetahuan, khususnya di bidang [sebutkan bidang]."),
        ("Aspek Praktis", "Hasil penelitian ini diharapkan dapat menjadi bahan pertimbangan bagi [sebutkan pihak] dalam pengambilan keputusan."),
    ], 1):
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=0, line_spacing=1.5)
        para.paragraph_format.left_indent = Cm(1.25)
        para.paragraph_format.first_line_indent = Cm(-1.25)
        run1 = para.add_run(f"{i}. {judul_m}: ")
        set_run_font(run1, size=12, bold=True)
        set_run_font(para.add_run(isi_m), size=12)


def build_bab2(doc):
    add_heading_bab(doc, "2", "TINJAUAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS")
    add_paragraph(doc, "", space_before=6)

    add_subheading(doc, "2.1.", "Teori-teori")
    add_subheading(doc, "2.1.1.", "[Nama Teori 1]", level=3)
    add_body_text(doc, "Jelaskan teori yang mendasari penelitian ini. Paparkan konsep, definisi, dan proposisi yang dikemukakan oleh para ahli yang relevan dengan topik penelitian. Minimal 20 referensi.")
    add_subheading(doc, "2.1.2.", "[Nama Teori 2]", level=3)
    add_body_text(doc, "Jelaskan teori kedua yang relevan dengan topik penelitian.")

    add_subheading(doc, "2.2.", "Penelitian Sebelumnya")
    add_body_text(doc, "Uraikan penelitian-penelitian sebelumnya yang relevan dengan topik dan permasalahan yang diteliti. Identifikasi keterbatasan penelitian sebelumnya dan bagaimana penelitian ini berupaya memperbaikinya.")

    add_subheading(doc, "2.3.", "Pengembangan Hipotesis")
    add_subheading(doc, "2.3.1.", "Pengaruh Variabel X1 terhadap Variabel Y", level=3)
    add_body_text(doc, "Uraikan penelitian terdahulu yang relevan dan jelaskan logika hubungan antara variabel X1 dan variabel Y berdasarkan teori yang ada.")
    para_h1 = doc.add_paragraph()
    para_h1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    set_para_spacing(para_h1, space_before=6, space_after=6, line_spacing=1.5)
    para_h1.paragraph_format.left_indent = Cm(1.25)
    set_run_font(para_h1.add_run("H1 : Variabel X1 berpengaruh positif terhadap variabel Y"), size=12, bold=True)

    add_subheading(doc, "2.3.2.", "Pengaruh Variabel X2 terhadap Variabel Y", level=3)
    add_body_text(doc, "Uraikan penelitian terdahulu yang relevan dan jelaskan logika hubungan antara variabel X2 dan variabel Y.")
    para_h2 = doc.add_paragraph()
    para_h2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    set_para_spacing(para_h2, space_before=6, space_after=6, line_spacing=1.5)
    para_h2.paragraph_format.left_indent = Cm(1.25)
    set_run_font(para_h2.add_run("H2 : Variabel X2 berpengaruh positif terhadap variabel Y"), size=12, bold=True)

    add_subheading(doc, "2.4.", "Rerangka Penelitian")
    add_body_text(doc, "Rerangka penelitian menunjukkan hubungan antar variabel yang diteliti beserta hipotesisnya dalam bentuk bagan.")
    add_placeholder_note(doc, "Gambar bagan rerangka penelitian dimasukkan di sini")
    add_figure_caption(doc, "Gambar 2.1. Rerangka Penelitian")


def build_bab3(doc):
    add_heading_bab(doc, "3", "METODE PENELITIAN")
    add_paragraph(doc, "", space_before=6)

    add_subheading(doc, "3.1.", "Jenis dan Sumber Data")
    add_body_text(doc, "Penelitian ini menggunakan data [kuantitatif/kualitatif] yang bersifat [primer/sekunder]. Data diperoleh dari [sebutkan sumber data]. Data penelitian meliputi data tahun 20XX sampai dengan 20XX.")

    add_subheading(doc, "3.2.", "Populasi dan Sampel")
    add_body_text(doc, "Populasi dalam penelitian ini adalah [deskripsikan populasi]. Pemilihan sampel dilakukan dengan metode [purposive sampling] dengan kriteria sebagai berikut:")
    for i, k in enumerate(["[Kriteria 1]", "[Kriteria 2]", "[Kriteria 3]"], 1):
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=0, line_spacing=1.5)
        para.paragraph_format.left_indent = Cm(1.25)
        para.paragraph_format.first_line_indent = Cm(-1.25)
        set_run_font(para.add_run(f"{i}. {k}"), size=12)

    add_paragraph(doc, "", space_before=6)
    add_table_caption(doc, "Tabel 3.1. Proses Seleksi Sampel")
    tbl = doc.add_table(rows=5, cols=3)
    tbl.style = 'Table Grid'
    for i, h in enumerate(["Keterangan", "Jumlah Perusahaan", "Jumlah Observasi"]):
        cell = tbl.rows[0].cells[i]
        cell.text = h
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                set_run_font(run, size=11, bold=True)
    for r_idx, row_data in enumerate([
        ["Total populasi", "...", "..."],
        ["Dikurangi: [Kriteria 1]", "(...)", "(...)"],
        ["Dikurangi: [Kriteria 2]", "(...)", "(...)"],
        ["Total sampel final", "...", "..."],
    ], 1):
        for c_idx, val in enumerate(row_data):
            tbl.rows[r_idx].cells[c_idx].text = val
            for para in tbl.rows[r_idx].cells[c_idx].paragraphs:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in para.runs:
                    set_run_font(run, size=11)

    add_subheading(doc, "3.3.", "Model Penelitian")
    add_body_text(doc, "Model penelitian yang digunakan dalam penelitian ini adalah sebagai berikut:")
    para_eq = doc.add_paragraph()
    para_eq.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    set_para_spacing(para_eq, space_before=6, space_after=6, line_spacing=1.5)
    para_eq.paragraph_format.left_indent = Cm(1.25)
    set_run_font(para_eq.add_run("Y = alpha + beta1*X1 + beta2*X2 + beta3*X3 + epsilon  ...............  (3.1)"), size=12)
    add_body_text(doc, "Keterangan:\nY = Variabel dependen\nalpha = Konstanta\nbeta1, beta2, beta3 = Koefisien regresi\nX1 = Variabel independen 1\nX2 = Variabel independen 2\nX3 = Variabel independen 3\nepsilon = Error term")

    add_subheading(doc, "3.4.", "Operasionalisasi Variabel")
    add_body_text(doc, "Berikut ini adalah tabel operasionalisasi variabel yang digunakan dalam penelitian ini:")
    add_paragraph(doc, "", space_before=6)
    add_table_caption(doc, "Tabel 3.2. Operasionalisasi Variabel")
    tbl2 = doc.add_table(rows=5, cols=4)
    tbl2.style = 'Table Grid'
    for i, h in enumerate(["Variabel", "Dimensi", "Indikator", "Sumber"]):
        cell = tbl2.rows[0].cells[i]
        cell.text = h
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                set_run_font(run, size=11, bold=True)
    for r_idx, row_data in enumerate([
        ["Y (Variabel Dependen)", "...", "...", "..."],
        ["X1 (Variabel Independen 1)", "...", "...", "..."],
        ["X2 (Variabel Independen 2)", "...", "...", "..."],
        ["X3 (Variabel Independen 3)", "...", "...", "..."],
    ], 1):
        for c_idx, val in enumerate(row_data):
            tbl2.rows[r_idx].cells[c_idx].text = val
            for para in tbl2.rows[r_idx].cells[c_idx].paragraphs:
                for run in para.runs:
                    set_run_font(run, size=11)

    add_subheading(doc, "3.5.", "Metode Analisis Data")
    add_body_text(doc, "Penelitian ini menggunakan analisis regresi [berganda / data panel] dengan bantuan perangkat lunak [SPSS / EViews / R / Stata]. Langkah-langkah analisis data:")
    for i, l in enumerate([
        "Uji Asumsi Klasik: (a) Uji Normalitas, (b) Uji Multikolinearitas, (c) Uji Heteroskedastisitas, (d) Uji Autokorelasi.",
        "Uji Koefisien Determinasi (R-squared)",
        "Uji Signifikansi Simultan (Uji F)",
        "Uji Signifikansi Parameter Individual (Uji t)",
    ], 1):
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=0, line_spacing=1.5)
        para.paragraph_format.left_indent = Cm(1.25)
        para.paragraph_format.first_line_indent = Cm(-1.25)
        set_run_font(para.add_run(f"{i}. {l}"), size=12)


def build_bab4(doc):
    add_heading_bab(doc, "4", "ANALISIS DAN PEMBAHASAN")
    add_paragraph(doc, "", space_before=6)

    add_subheading(doc, "4.1.", "Deskripsi Sampel Penelitian")
    add_body_text(doc, "Penelitian ini menggunakan sampel [X] perusahaan yang terdaftar di [sebutkan bursa/lembaga] selama periode [tahun]. Total observasi yang digunakan dalam penelitian ini adalah [X] observasi.")

    add_subheading(doc, "4.2.", "Statistik Deskriptif")
    add_body_text(doc, "Berikut ini adalah hasil analisis statistik deskriptif dari variabel-variabel yang digunakan dalam penelitian ini:")
    add_paragraph(doc, "", space_before=6)
    add_table_caption(doc, "Tabel 4.1. Statistik Deskriptif")
    tbl = doc.add_table(rows=6, cols=6)
    tbl.style = 'Table Grid'
    for i, h in enumerate(["Variabel", "N", "Mean", "Min", "Maks", "Std. Dev."]):
        cell = tbl.rows[0].cells[i]
        cell.text = h
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                set_run_font(run, size=11, bold=True)
    for r_idx, var in enumerate(["Y", "X1", "X2", "X3", "Kontrol"], 1):
        tbl.rows[r_idx].cells[0].text = var
        for c_idx in range(1, 6):
            tbl.rows[r_idx].cells[c_idx].text = "..."
        for c_idx in range(6):
            for para in tbl.rows[r_idx].cells[c_idx].paragraphs:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in para.runs:
                    set_run_font(run, size=11)

    add_subheading(doc, "4.3.", "Hasil Uji Asumsi Klasik")
    for sub, judul in [("4.3.1.", "Uji Normalitas"), ("4.3.2.", "Uji Multikolinearitas"),
                       ("4.3.3.", "Uji Heteroskedastisitas"), ("4.3.4.", "Uji Autokorelasi")]:
        add_subheading(doc, sub, judul, level=3)
        add_body_text(doc, f"Jelaskan metode dan hasil uji {judul.lower()} di sini.")

    add_subheading(doc, "4.4.", "Hasil Pengujian Hipotesis")
    add_body_text(doc, "Berikut ini adalah hasil pengujian regresi [berganda / data panel]:")
    add_paragraph(doc, "", space_before=6)
    add_table_caption(doc, "Tabel 4.2. Hasil Pengujian Hipotesis")
    tbl2 = doc.add_table(rows=6, cols=4)
    tbl2.style = 'Table Grid'
    for i, h in enumerate(["Variabel", "Koefisien", "t-Statistik", "p-Value"]):
        cell = tbl2.rows[0].cells[i]
        cell.text = h
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                set_run_font(run, size=11, bold=True)
    for r_idx, row_data in enumerate([
        ["Konstanta (alpha)", "...", "...", "..."],
        ["X1", "...", "...", "..."],
        ["X2", "...", "...", "..."],
        ["X3", "...", "...", "..."],
        ["R2 = ...   F-stat = ...   Prob(F) = ...", "", "", ""],
    ], 1):
        for c_idx, val in enumerate(row_data):
            tbl2.rows[r_idx].cells[c_idx].text = val
            for para in tbl2.rows[r_idx].cells[c_idx].paragraphs:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in para.runs:
                    set_run_font(run, size=11)

    add_subheading(doc, "4.5.", "Pembahasan")
    for sub, xi in [("4.5.1.", "X1"), ("4.5.2.", "X2"), ("4.5.3.", "X3")]:
        add_subheading(doc, sub, f"Pengaruh {xi} terhadap Y", level=3)
        add_body_text(doc,
            f"Hasil pengujian hipotesis menunjukkan bahwa {xi} [berpengaruh positif / "
            "berpengaruh negatif / tidak berpengaruh] terhadap Y dengan nilai koefisien "
            "... dan p-value .... Dengan demikian, H[n] [diterima / ditolak]. "
            "Hasil ini [konsisten / tidak konsisten] dengan penelitian [nama peneliti, tahun].")


def build_bab5(doc):
    add_heading_bab(doc, "5", "PENUTUP")
    add_paragraph(doc, "", space_before=6)

    add_subheading(doc, "5.1.", "Kesimpulan")
    add_body_text(doc, "Berdasarkan hasil analisis dan pembahasan yang telah dilakukan, maka dapat ditarik kesimpulan sebagai berikut:")
    for i, k in enumerate([
        "Variabel X1 [berpengaruh positif / berpengaruh negatif / tidak berpengaruh] terhadap variabel Y. Hal ini dibuktikan dengan nilai koefisien ... dan p-value ... < 0,05, sehingga H1 [diterima / ditolak].",
        "Variabel X2 [berpengaruh positif / berpengaruh negatif / tidak berpengaruh] terhadap variabel Y. Hal ini dibuktikan dengan nilai koefisien ... dan p-value ..., sehingga H2 [diterima / ditolak].",
        "Variabel X3 [berpengaruh positif / berpengaruh negatif / tidak berpengaruh] terhadap variabel Y. Hal ini dibuktikan dengan nilai koefisien ... dan p-value ..., sehingga H3 [diterima / ditolak].",
    ], 1):
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=3, line_spacing=1.5)
        para.paragraph_format.left_indent = Cm(1.25)
        para.paragraph_format.first_line_indent = Cm(-1.25)
        set_run_font(para.add_run(f"{i}. {k}"), size=12)

    add_subheading(doc, "5.2.", "Saran")
    add_body_text(doc, "Berdasarkan kesimpulan di atas, saran yang dapat diberikan adalah sebagai berikut:")
    for i, s in enumerate([
        "Bagi peneliti selanjutnya, disarankan untuk [saran untuk penelitian mendatang, misalnya: menambah variabel lain, memperluas periode pengamatan, dll.].",
        "Bagi [pihak praktis, misalnya: perusahaan / investor / regulator], hasil penelitian ini menunjukkan bahwa [implikasi praktis dari temuan penelitian].",
    ], 1):
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=3, line_spacing=1.5)
        para.paragraph_format.left_indent = Cm(1.25)
        para.paragraph_format.first_line_indent = Cm(-1.25)
        set_run_font(para.add_run(f"{i}. {s}"), size=12)


def build_daftar_pustaka(doc):
    add_heading_bab(doc, "", "DAFTAR PUSTAKA")
    add_paragraph(doc, "", space_before=6)
    add_body_text(doc, "Daftar pustaka disusun secara alfabetis berdasarkan nama penulis. Format penulisan mengikuti gaya APA (American Psychological Association). Contoh penulisan:")
    for ref in [
        "Penulis, A. A., & Penulis, B. B. (Tahun). Judul artikel. Nama Jurnal, Volume(Nomor), Halaman. https://doi.org/xxxx",
        "Penulis, A. A. (Tahun). Judul buku (Edisi ke-x). Nama Penerbit.",
        "Penulis, A. A., Penulis, B. B., & Penulis, C. C. (Tahun). Judul artikel. Nama Jurnal, Volume(Nomor), Halaman.",
    ]:
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        set_para_spacing(para, space_before=0, space_after=6, line_spacing=1.5)
        para.paragraph_format.left_indent = Cm(1.27)
        para.paragraph_format.first_line_indent = Cm(-1.27)
        set_run_font(para.add_run(ref), size=12)
    add_paragraph(doc, "", space_before=12)
    add_paragraph(doc, "[ Tambahkan daftar pustaka lengkap di sini -- minimal 20 referensi ]",
                  size=11, italic=True, alignment=WD_ALIGN_PARAGRAPH.CENTER, color=(128, 128, 128))


def build_lampiran(doc):
    add_heading_bab(doc, "", "LAMPIRAN")
    add_paragraph(doc, "", space_before=6)
    add_subheading(doc, "Lampiran 1.", "Tabulasi Data")
    add_placeholder_note(doc, "Tabulasi data lengkap dimasukkan di sini")
    add_paragraph(doc, "", space_before=12)
    add_subheading(doc, "Lampiran 2.", "Hasil Output [SPSS / EViews / R]")
    add_placeholder_note(doc, "Output analisis statistik dimasukkan di sini")


def build_riwayat_hidup(doc):
    add_heading_bab(doc, "", "DAFTAR RIWAYAT HIDUP PENULIS SKRIPSI")
    add_paragraph(doc, "", space_before=6)
    table = doc.add_table(rows=1, cols=2)
    left = table.rows[0].cells[0]
    right = table.rows[0].cells[1]
    left_para = left.paragraphs[0]
    left_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = left_para.add_run("[ Foto 4x6 ]")
    set_run_font(run, size=11, italic=True, color=(128, 128, 128))
    info = [
        "Nama Lengkap    : ........................................",
        "NIM             : ........................................",
        "Tempat/Tgl Lahir: ........................................",
        "Alamat          : ........................................",
        "Email           : ........................................",
        "Program Studi   : ........................................",
        "",
        "Riwayat Pendidikan:",
        "20XX - 20XX : [Nama Universitas / Sekolah]",
        "20XX - 20XX : [Nama Sekolah]",
        "20XX - 20XX : [Nama Sekolah]",
    ]
    for i, line in enumerate(info):
        para = right.paragraphs[0] if i == 0 else right.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        set_para_spacing(para, space_before=0, space_after=0, line_spacing=1.5)
        set_run_font(para.add_run(line), size=12, bold=line.startswith("Riwayat"))


# ─────────────────────────────────────────────
# MAIN BUILD
# ─────────────────────────────────────────────

def build_document():
    doc = Document()

    # Default style
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)

    # Section 1: Bagian Awal (romawi)
    section1 = doc.sections[0]
    set_page_margins(section1)
    add_footer_romawi(section1, doc)

    build_halaman_sampul(doc)
    add_page_break(doc)
    build_halaman_judul(doc)
    add_page_break(doc)
    build_halaman_keaslian(doc)
    add_page_break(doc)
    build_halaman_persetujuan(doc)
    add_page_break(doc)
    build_halaman_pengesahan(doc)
    add_page_break(doc)
    build_halaman_publikasi(doc)
    add_page_break(doc)
    build_kata_pengantar(doc)
    add_page_break(doc)
    build_abstrak(doc, "indonesia")
    add_page_break(doc)
    build_abstrak(doc, "english")
    add_page_break(doc)
    build_daftar_isi(doc)
    add_page_break(doc)

    # Daftar Tabel
    add_heading_bab(doc, "", "DAFTAR TABEL")
    add_paragraph(doc, "", space_before=6)
    add_body_text(doc, "Tabel 3.1. Proses Seleksi Sampel  ...................................................  x")
    add_body_text(doc, "Tabel 3.2. Operasionalisasi Variabel  ...............................................  x")
    add_body_text(doc, "Tabel 4.1. Statistik Deskriptif  ....................................................  x")
    add_body_text(doc, "Tabel 4.2. Hasil Pengujian Hipotesis  ...............................................  x")
    add_page_break(doc)

    # Daftar Gambar
    add_heading_bab(doc, "", "DAFTAR GAMBAR")
    add_paragraph(doc, "", space_before=6)
    add_body_text(doc, "Gambar 2.1. Rerangka Penelitian  ...................................................  x")
    add_page_break(doc)

    # Section 2: Bagian Isi (latin)
    section2 = add_section_break(doc, WD_SECTION.NEW_PAGE)
    set_page_margins(section2)
    add_footer_latin(section2)

    build_bab1(doc)
    add_page_break(doc)
    build_bab2(doc)
    add_page_break(doc)
    build_bab3(doc)
    add_page_break(doc)
    build_bab4(doc)
    add_page_break(doc)
    build_bab5(doc)
    add_page_break(doc)
    build_daftar_pustaka(doc)
    add_page_break(doc)
    build_lampiran(doc)
    add_page_break(doc)
    build_riwayat_hidup(doc)

    output_path = r"z:\Skripsi\02_Persiapan_Sidang\TEMPLATE_SKRIPSI_FEB_UKRIDA_2022.docx"
    doc.save(output_path)
    print(f"\n  Template berhasil dibuat!")
    print(f"   {output_path}")
    print(f"\nFormat yang diterapkan:")
    print(f"   - Kertas A4, margin: kiri 4cm, kanan/atas/bawah 3cm")
    print(f"   - Font: Times New Roman 12pt, Justify, spasi 1.5")
    print(f"   - Indent paragraf: 1.25 cm (5 ketukan)")
    print(f"   - Footer: romawi kecil (bagian awal) | latin + UKRIDA (bagian isi)")
    print(f"   - Judul BAB: ALL CAPS + Bold, center")
    print(f"   - Sub-judul: Title Case + Bold")
    print(f"   - Semua halaman: sampul, judul, keaslian, persetujuan, pengesahan,")
    print(f"     publikasi, kata pengantar, abstrak (ID+EN), daftar isi,")
    print(f"     daftar tabel, daftar gambar, BAB 1-5, daftar pustaka,")
    print(f"     lampiran, riwayat hidup")


if __name__ == "__main__":
    build_document()

r"""
extract_frontmatter_pages.py
Mengekstrak 6 halaman frontmatter dari naskah utama menjadi file DOCX individual
di folder 01_Lembar_Persetujuan_Proposal/.

Output:
  01_Pernyataan_Keaslian.docx
  02_Halaman_Persetujuan.docx
  03_Halaman_Pengesahan_Penguji.docx
  04_Kata_Pengantar.docx
  05_Abstrak_Indonesia.docx
  06_Abstract_English.docx
"""

import sys
import os
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# ---------------------------------------------------------------------------
# Import helpers dari build_proposal_word.py (re-use, hindari duplikasi)
# ---------------------------------------------------------------------------
script_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(script_dir))

from build_proposal_word import (
    make_run_pure_black,
    add_body_paragraph,
    add_frontmatter_heading,
    set_col_widths_fixed,
    remove_table_borders,
    set_cell_margins,
    build_formal_approval_sheets,
    _setup_doc_base_styles,
)


# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------
BASE_DIR = script_dir.parent / "01_Naskah_Utama"
OUT_DIR = BASE_DIR / "01_Lembar_Persetujuan_Proposal"
OUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# Helper: buat dokumen baru dengan layout FEB UKRIDA 2023
# ---------------------------------------------------------------------------
def _new_doc():
    doc = Document()
    _setup_doc_base_styles(doc)
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(3.0)
    sec.bottom_margin = Cm(3.0)
    sec.left_margin = Cm(4.0)
    sec.right_margin = Cm(3.0)
    return doc


# Data identitas mahasiswa (re-used across pages)
ID_DATA = [
    ("Nama Mahasiswa", ":", "Arthur Reezan"),
    ("NIM",            ":", "312023002"),
    ("Program Studi",  ":", "Program Studi S1 Manajemen"),
    ("Konsentrasi",    ":", "Manajemen Keuangan"),
]
COL_ID_WIDTHS = [Cm(3.8), Cm(0.4), Cm(9.8)]

JUDUL = (
    "\u201cPENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, "
    "DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK "
    "KARTU POK\u00c9MON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI\u201d"
)


# ---------------------------------------------------------------------------
# 1. Pernyataan Keaslian Karya Tugas Akhir
# ---------------------------------------------------------------------------
def build_01_pernyataan():
    doc = _new_doc()
    add_frontmatter_heading(doc, "PERNYATAAN KEASLIAN KARYA TUGAS AKHIR", page_break=False)
    add_body_paragraph(doc, "Saya mahasiswa Universitas Kristen Krida Wacana:", indent=False)

    tbl_id = doc.add_table(rows=4, cols=3)
    tbl_id.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths_fixed(tbl_id, COL_ID_WIDTHS)
    remove_table_borders(tbl_id)
    for row_idx, (c1, c2, c3) in enumerate(ID_DATA):
        row = tbl_id.rows[row_idx]
        for c_idx, val in enumerate([c1, c2, c3]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=20, bottom=20, left=0 if c_idx == 0 else 40, right=40)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.first_line_indent = Cm(0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 1 else WD_ALIGN_PARAGRAPH.LEFT
            make_run_pure_black(p.add_run(val), "Times New Roman", Pt(12), bold=(c_idx == 2))

    add_body_paragraph(doc, "Dengan ini menyatakan dengan sesungguhnya bahwa Proposal Skripsi yang berjudul:", indent=False)

    p_j = doc.add_paragraph()
    p_j.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j.paragraph_format.space_before = Pt(6)
    p_j.paragraph_format.space_after = Pt(6)
    p_j.paragraph_format.line_spacing = 1.15
    p_j.paragraph_format.first_line_indent = Cm(0)
    make_run_pure_black(p_j.add_run(JUDUL), "Times New Roman", Pt(11), bold=True)

    add_body_paragraph(doc, "adalah:", indent=False)

    points = [
        "Benar-benar hasil karya saya sendiri, bukan merupakan jiplakan, plagiarisme, fabrikasi, atau tiruan dari karya tulis ilmiah orang lain yang pernah diajukan untuk memperoleh gelar akademik di perguruan tinggi manapun.",
        "Seluruh kutipan, data, dan rujukan ilmiah yang digunakan dalam naskah ini telah dicantumkan sumbernya secara jelas dan lengkap sesuai dengan kaidah penulisan ilmiah yang berlaku di Universitas Kristen Krida Wacana.",
        "Apabila di kemudian hari terbukti bahwa pernyataan ini tidak benar atau ditemukan indikasi plagiarisme, saya bersedia menerima sanksi akademik yang berlaku sesuai dengan peraturan perundang-undangan dan ketentuan di lingkungan Universitas Kristen Krida Wacana.",
    ]
    for idx, pt_text in enumerate(points):
        p_pt = doc.add_paragraph()
        p_pt.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_pt.paragraph_format.left_indent = Cm(1.25)
        p_pt.paragraph_format.first_line_indent = Cm(-0.63)
        p_pt.paragraph_format.space_before = Pt(0)
        p_pt.paragraph_format.space_after = Pt(4)
        p_pt.paragraph_format.line_spacing = 1.15
        make_run_pure_black(p_pt.add_run(f"{idx+1}.  "), "Times New Roman", Pt(12), bold=True)
        make_run_pure_black(p_pt.add_run(pt_text), "Times New Roman", Pt(12))

    tbl_sig = doc.add_table(rows=1, cols=2)
    tbl_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths_fixed(tbl_sig, [Cm(7.0), Cm(7.0)])
    remove_table_borders(tbl_sig)

    p_l = tbl_sig.rows[0].cells[0].paragraphs[0]
    p_l.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_l.paragraph_format.space_before = Pt(24)
    p_l.paragraph_format.first_line_indent = Cm(0)
    make_run_pure_black(p_l.add_run("\n\n[ Materai Rp10.000 ]\n\n"), "Times New Roman", Pt(10), italic=True)

    p_r = tbl_sig.rows[0].cells[1].paragraphs[0]
    p_r.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_r.paragraph_format.space_before = Pt(12)
    p_r.paragraph_format.line_spacing = 1.15
    p_r.paragraph_format.first_line_indent = Cm(0)
    make_run_pure_black(p_r.add_run("Jakarta, 12 September 2026\nYang membuat pernyataan,\n\n\n\n\n"), "Times New Roman", Pt(12))
    make_run_pure_black(p_r.add_run("Arthur Reezan\n"), "Times New Roman", Pt(12), bold=True)
    make_run_pure_black(p_r.add_run("NIM: 312023002"), "Times New Roman", Pt(12))

    out = OUT_DIR / "01_Pernyataan_Keaslian.docx"
    doc.save(str(out))
    print(f"[OK] {out.name}")
    return out


# ---------------------------------------------------------------------------
# 2. Halaman Persetujuan Proposal Skripsi
# ---------------------------------------------------------------------------
def build_02_persetujuan():
    doc = _new_doc()
    add_frontmatter_heading(doc, "HALAMAN PERSETUJUAN PROPOSAL SKRIPSI", page_break=False)
    add_body_paragraph(doc, "Proposal Skripsi ini diajukan oleh:", indent=False)

    tbl_per = doc.add_table(rows=4, cols=3)
    tbl_per.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths_fixed(tbl_per, COL_ID_WIDTHS)
    remove_table_borders(tbl_per)
    for row_idx, (c1, c2, c3) in enumerate(ID_DATA):
        row = tbl_per.rows[row_idx]
        for c_idx, val in enumerate([c1, c2, c3]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=20, bottom=20, left=0 if c_idx == 0 else 40, right=40)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.first_line_indent = Cm(0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 1 else WD_ALIGN_PARAGRAPH.LEFT
            make_run_pure_black(p.add_run(val), "Times New Roman", Pt(12), bold=(c_idx == 2))

    p_j2 = doc.add_paragraph()
    p_j2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j2.paragraph_format.space_before = Pt(12)
    p_j2.paragraph_format.space_after = Pt(12)
    p_j2.paragraph_format.line_spacing = 1.15
    p_j2.paragraph_format.first_line_indent = Cm(0)
    make_run_pure_black(p_j2.add_run(JUDUL), "Times New Roman", Pt(11), bold=True)

    add_body_paragraph(doc, "Telah disetujui untuk diajukan dalam Seminar Proposal Skripsi Program Studi S1 Manajemen Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana.", indent=False)

    tbl_apv = doc.add_table(rows=3, cols=2)
    tbl_apv.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths_fixed(tbl_apv, [Cm(7.0), Cm(7.0)])
    remove_table_borders(tbl_apv)

    for cell, title in [
        (tbl_apv.rows[0].cells[0], "Menyetujui,\nDosen Pembimbing"),
        (tbl_apv.rows[0].cells[1], "Mengetahui,\nKetua Program Studi S1 Manajemen"),
    ]:
        set_cell_margins(cell, top=0, bottom=0, left=20, right=20)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.first_line_indent = Cm(0)
        make_run_pure_black(p.add_run(title), "Times New Roman", Pt(12))

    for cell in [tbl_apv.rows[1].cells[0], tbl_apv.rows[1].cells[1]]:
        set_cell_margins(cell, top=0, bottom=0, left=20, right=20)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(55)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0

    for cell, name, nidn in [
        (tbl_apv.rows[2].cells[0], "Dr. Fredella Colline, S.E., M.M., CFP\u00ae, PFM, CHCP-A\n", "NIDN: [NIDN_DOSEN]"),
        (tbl_apv.rows[2].cells[1], "Rita Amelinda, S.E., M.M.\n", "NIDN: [NIDN_KAPRODI]"),
    ]:
        set_cell_margins(cell, top=0, bottom=0, left=20, right=20)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.first_line_indent = Cm(0)
        make_run_pure_black(p.add_run(name), "Times New Roman", Pt(12), bold=True)
        make_run_pure_black(p.add_run(nidn), "Times New Roman", Pt(12))

    out = OUT_DIR / "02_Halaman_Persetujuan.docx"
    doc.save(str(out))
    print(f"[OK] {out.name}")
    return out


# ---------------------------------------------------------------------------
# 3. Halaman Pengesahan Tim Penguji Seminar Proposal
# ---------------------------------------------------------------------------
def build_03_pengesahan():
    doc = _new_doc()
    add_frontmatter_heading(doc, "HALAMAN PENGESAHAN TIM PENGUJI SEMINAR PROPOSAL", page_break=False)
    add_body_paragraph(doc, "Proposal Skripsi yang berjudul:", indent=False)

    p_j3 = doc.add_paragraph()
    p_j3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j3.paragraph_format.space_before = Pt(6)
    p_j3.paragraph_format.space_after = Pt(6)
    p_j3.paragraph_format.line_spacing = 1.15
    p_j3.paragraph_format.first_line_indent = Cm(0)
    make_run_pure_black(p_j3.add_run(JUDUL), "Times New Roman", Pt(11), bold=True)

    add_body_paragraph(doc, "Telah dipertahankan di hadapan Tim Penguji Seminar Proposal Skripsi Program Studi S1 Manajemen Fakultas Ekonomi dan Bisnis Universitas Kristen Krida Wacana pada tanggal yang ditetapkan dan dinyatakan telah memenuhi syarat kelayakan.", indent=False)

    tbl_penguji = doc.add_table(rows=2, cols=2)
    tbl_penguji.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths_fixed(tbl_penguji, [Cm(7.0), Cm(7.0)])
    remove_table_borders(tbl_penguji)

    entries = [
        (tbl_penguji.rows[0].cells[0], "Ketua Tim Penguji\n\n\n\n\n_________________________\n", "NIDN: _________________"),
        (tbl_penguji.rows[0].cells[1], "Anggota Penguji 1\n\n\n\n\n_________________________\n", "NIDN: _________________"),
        (tbl_penguji.rows[1].cells[0], "Anggota Penguji 2 / Pembimbing\n\n\n\n\nDr. Fredella Colline, S.E., M.M.\n", "NIDN: [NIDN_DOSEN]"),
        (tbl_penguji.rows[1].cells[1], "Mengetahui,\nKetua Program Studi S1 Manajemen\n\n\n\n\nRita Amelinda, S.E., M.M.\n", "NIDN: [NIDN_KAPRODI]"),
    ]
    for cell, title_text, nidn_text in entries:
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(6) if "Ketua Tim" in title_text or "Anggota Penguji 1" in title_text else Pt(12)
        make_run_pure_black(p.add_run(title_text), "Times New Roman", Pt(12), bold=True)
        make_run_pure_black(p.add_run(nidn_text), "Times New Roman", Pt(12))

    out = OUT_DIR / "03_Halaman_Pengesahan_Penguji.docx"
    doc.save(str(out))
    print(f"[OK] {out.name}")
    return out


# ---------------------------------------------------------------------------
# 4. Kata Pengantar
# ---------------------------------------------------------------------------
def build_04_kata_pengantar():
    doc = _new_doc()
    add_frontmatter_heading(doc, "KATA PENGANTAR", page_break=False)

    add_body_paragraph(doc, "Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas kasih, anugerah, dan penyertaan-Nya yang senantiasa melimpah, sehingga penulis dapat menyelesaikan penyusunan proposal skripsi yang berjudul **\u201cPENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POK\u00c9MON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI\u201d** dengan baik, lancar, dan tepat waktu.")
    add_body_paragraph(doc, "Proposal skripsi ini disusun sebagai salah satu tahapan akademik yang diwajibkan dalam rangka menempuh ujian seminar proposal guna menyelesaikan studi pada Program Studi S1 Manajemen, Konsentrasi Manajemen Keuangan, Fakultas Ekonomi dan Bisnis, Universitas Kristen Krida Wacana (UKRIDA), Jakarta.")
    add_body_paragraph(doc, "Dalam proses penyusunan naskah proposal ini, penulis mendapatkan banyak bimbingan, arahan metodologis, dukungan moril, serta fasilitas dari berbagai pihak. Oleh karena itu, dengan penuh rasa hormat dan kerendahan hati, penulis menyampaikan terima kasih dan apresiasi yang setinggi-tingginya kepada:")

    kp_points = [
        "Dr. Fredella Colline, S.E., M.M., CFP\u00ae, PFM, CHCP-A, selaku Dosen Pembimbing Skripsi, yang telah dengan luar biasa sabar, teliti, kritis, dan penuh dedikasi meluangkan waktu serta mencurahkan tenaga dan pikiran dalam membimbing, mengarahkan, dan menyempurnakan naskah proposal ini sejak tahap awal perumusan gagasan hingga penyusunan naskah komprehensif.",
        "Rita Amelinda, S.E., M.M., selaku Ketua Program Studi S1 Manajemen FEB UKRIDA, atas segala arahan, kemudahan proses administratif, dan bimbingan akademik yang diberikan.",
        "Bapak dan Ibu Dosen Penguji Seminar Proposal, yang telah bersedia meluangkan waktu untuk menguji, memberikan koreksi kritis, serta masukan yang konstruktif guna menyempurnakan naskah penelitian ini.",
        "Seluruh Dosen dan Staf Pengajar FEB UKRIDA, yang telah membagikan ilmu pengetahuan, wawasan analisis keuangan, serta etika profesional selama masa perkuliahan penulis.",
        "Kedua Orang Tua dan Keluarga Tercinta, atas doa yang tiada putus, limpahan kasih sayang, ketulusan pengorbanan, serta dorongan moral dan material yang menjadi sumber kekuatan utama bagi penulis.",
        "Rekan-rekan Mahasiswa Manajemen FEB UKRIDA Angkatan 2023 dan sahabat seperjuangan, atas diskusi yang membangun, motivasi, dan kerja sama selama proses perkuliahan.",
        "Komunitas Kolektor dan Pemain Pok\u00e9mon TCG di Indonesia, yang telah memberikan gambaran nyata mengenai fenomena pasar kartu koleksi di lapangan.",
    ]
    for idx, kpt in enumerate(kp_points):
        p_kp = doc.add_paragraph()
        p_kp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_kp.paragraph_format.left_indent = Cm(1.25)
        p_kp.paragraph_format.first_line_indent = Cm(-0.63)
        p_kp.paragraph_format.space_before = Pt(0)
        p_kp.paragraph_format.space_after = Pt(3)
        p_kp.paragraph_format.line_spacing = 1.15
        make_run_pure_black(p_kp.add_run(f"{idx+1}.  "), "Times New Roman", Pt(12), bold=True)
        make_run_pure_black(p_kp.add_run(kpt), "Times New Roman", Pt(12))

    add_body_paragraph(doc, "Penulis menyadari bahwa proposal ini masih jauh dari kesempurnaan. Kritik dan saran yang membangun sangat diharapkan demi penyempurnaan karya ilmiah ini ke depan. Semoga proposal skripsi ini dapat memberikan manfaat akademis dan praktis bagi perkembangan kajian ilmu manajemen keuangan perilaku di Indonesia.")

    p_tutup = doc.add_paragraph()
    p_tutup.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_tutup.paragraph_format.space_before = Pt(18)
    p_tutup.paragraph_format.line_spacing = 1.15
    make_run_pure_black(p_tutup.add_run("Jakarta,                  2026\nPenulis,\n\n\n\n\n"), "Times New Roman", Pt(12))
    make_run_pure_black(p_tutup.add_run("Arthur Reezan\n"), "Times New Roman", Pt(12), bold=True)
    make_run_pure_black(p_tutup.add_run("NIM: 312023002"), "Times New Roman", Pt(12))

    out = OUT_DIR / "04_Kata_Pengantar.docx"
    doc.save(str(out))
    print(f"[OK] {out.name}")
    return out


# ---------------------------------------------------------------------------
# 5. Abstrak (Bahasa Indonesia)
# ---------------------------------------------------------------------------
def build_05_abstrak():
    doc = _new_doc()
    add_frontmatter_heading(doc, "ABSTRAK", page_break=False)

    p_j4 = doc.add_paragraph()
    p_j4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j4.paragraph_format.space_before = Pt(0)
    p_j4.paragraph_format.space_after = Pt(12)
    p_j4.paragraph_format.line_spacing = 1.15
    rj4 = p_j4.add_run(
        "PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE "
        "TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POK\u00c9MON TCG DENGAN SELF-CONTROL "
        "SEBAGAI VARIABEL MODERASI\n\n"
        "Arthur Reezan (312023002)\n"
        "Program Studi S1 Manajemen, Fakultas Ekonomi dan Bisnis, Universitas Kristen Krida Wacana\n"
        "Dosen Pembimbing: Dr. Fredella Colline, S.E., M.M., CFP\u00ae, PFM, CHCP-A"
    )
    make_run_pure_black(rj4, "Times New Roman", Pt(12), bold=True)

    p_abs = doc.add_paragraph()
    p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_abs.paragraph_format.line_spacing = 1.0
    p_abs.paragraph_format.space_before = Pt(6)
    p_abs.paragraph_format.space_after = Pt(6)
    p_abs.paragraph_format.first_line_indent = Cm(1.25)
    r_abs = p_abs.add_run(
        "Penelitian ini bertujuan untuk menganalisis dan menguji secara empiris pengaruh hedonic motivation (motivasi hedonis), "
        "desire for completeness (hasrat kelengkapan koleksi), dan speculative motive (motif spekulasi finansial) terhadap impulsive buying "
        "(pembelian impulsif) booster pack kartu Pok\u00e9mon Trading Card Game (Pok\u00e9mon TCG) fisik resmi berbahasa Indonesia, serta menguji peran kontrol diri "
        "(self-control) sebagai variabel moderasi dalam memperlemah pengaruh ketiga variabel anteseden tersebut. Penelitian ini menggunakan pendekatan kuantitatif "
        "asosiatif dengan desain survei cross-sectional. Data primer dikumpulkan melalui penyebaran kuesioner daring berbasis skala Likert 5 poin kepada responden "
        "yang dipilih melalui teknik purposive sampling. Kriteria inklusi sampel adalah konsumen atau kolektor Warga Negara Indonesia (WNI) berusia minimal 17 tahun "
        "yang pernah membeli booster pack Pok\u00e9mon TCG fisik resmi dalam rentang waktu 6\u201312 bulan terakhir. Jumlah sampel yang ditargetkan adalah 120 hingga 150 responden, "
        "mengacu pada rekomendasi ukuran sampel Green (1991) dan Cohen (1988) untuk mencapai kekuatan uji statistik (statistical power) yang memadai pada model regresi "
        "linear berganda. Metode analisis data menggunakan analisis regresi berganda dan Moderated Regression Analysis (MRA) dengan prosedur pemusatan rata-rata "
        "(mean-centering) guna mereduksi potensi multikolinearitas non-esensial antara variabel prediktor dengan produk interaksinya (Aiken dan West, 1991; Ghozali, 2018), yang diolah menggunakan perangkat lunak "
        "IBM SPSS Statistics. Penelitian ini menawarkan kebaruan teoritis (novelty) dengan mengintegrasikan kerangka psikologi lingkungan Stimulus-Organism-Response (S-O-R), "
        "psikologi kolektor (Zeigarnik Effect dan The Completing the Set Effect), teori regulasi diri (Self-Regulation Theory), serta prinsip-prinsip keuangan perilaku "
        "(behavioral finance) pada fenomena komoditas hobi fisik bernilai spekulatif tinggi. Hasil penelitian ini diharapkan memberikan kontribusi empiris bagi konsumen "
        "muda dalam menjaga kontrol diri finansial, serta masukan aplikatif bagi komunitas hobi dan pemangku kebijakan edukasi keuangan generasi muda di Indonesia."
    )
    make_run_pure_black(r_abs, "Times New Roman", Pt(12))

    p_kw = doc.add_paragraph()
    p_kw.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_kw.paragraph_format.line_spacing = 1.15
    p_kw.paragraph_format.space_before = Pt(6)
    p_kw.paragraph_format.first_line_indent = Cm(0)
    make_run_pure_black(p_kw.add_run("Kata Kunci: "), "Times New Roman", Pt(12), bold=True)
    r_kw = p_kw.add_run("Impulsive Buying, Hedonic Motivation, Desire for Completeness, Speculative Motive, Self-Control, Moderated Regression Analysis, Pok\u00e9mon TCG, Keuangan Perilaku (Behavioral Finance).")
    make_run_pure_black(r_kw, "Times New Roman", Pt(12), italic=True)

    out = OUT_DIR / "05_Abstrak_Indonesia.docx"
    doc.save(str(out))
    print(f"[OK] {out.name}")
    return out


# ---------------------------------------------------------------------------
# 6. Abstract (English)
# ---------------------------------------------------------------------------
def build_06_abstract():
    doc = _new_doc()
    add_frontmatter_heading(doc, "ABSTRACT", page_break=False)

    p_j5 = doc.add_paragraph()
    p_j5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_j5.paragraph_format.space_before = Pt(0)
    p_j5.paragraph_format.space_after = Pt(12)
    p_j5.paragraph_format.line_spacing = 1.15
    rj5 = p_j5.add_run(
        "THE EFFECT OF HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, AND SPECULATIVE MOTIVE "
        "ON IMPULSIVE BUYING OF POK\u00c9MON TCG BOOSTER PACKS WITH SELF-CONTROL AS A MODERATING VARIABLE\n\n"
        "Arthur Reezan (312023002)\n"
        "Undergraduate Program in Management, Faculty of Economics and Business, UKRIDA\n"
        "Thesis Advisor: Dr. Fredella Colline, S.E., M.M., CFP\u00ae, PFM, CHCP-A"
    )
    make_run_pure_black(rj5, "Times New Roman", Pt(12), bold=True)

    p_abs_en = doc.add_paragraph()
    p_abs_en.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_abs_en.paragraph_format.line_spacing = 1.0
    p_abs_en.paragraph_format.space_before = Pt(6)
    p_abs_en.paragraph_format.space_after = Pt(6)
    p_abs_en.paragraph_format.first_line_indent = Cm(1.25)
    r_abs_en = p_abs_en.add_run(
        "This research aims to analyze and empirically test the effects of hedonic motivation, desire for completeness, and speculative motive "
        "on the impulsive buying behavior of official Indonesian-language physical Pok\u00e9mon Trading Card Game (Pok\u00e9mon TCG) booster packs, as well as to evaluate "
        "the moderating role of self-control in weakening the relationships between these three antecedent variables and impulsive buying. "
        "This study adopts an associative quantitative approach utilizing a cross-sectional survey design. Primary data are gathered via self-administered online "
        "questionnaires employing a 5-point Likert scale, distributed to respondents selected through purposive sampling. The sample inclusion criteria comprise "
        "Indonesian citizens aged 17 and above who have purchased official physical booster packs within the past 6 to 12 months. The targeted sample size ranges from "
        "120 to 150 respondents, consistent with the statistical power criteria established by Green (1991) and Cohen (1988) for multiple regression frameworks. "
        "The empirical model is estimated using multiple linear regression and Moderated Regression Analysis (MRA) with mean-centering procedures to reduce non-essential "
        "multicollinearity between predictor variables and their interaction products (Aiken dan West, 1991; Ghozali, 2018), executed via IBM SPSS Statistics software. This study provides theoretical novelty by synthesizing the "
        "Stimulus-Organism-Response (S-O-R) paradigm, collector psychology (the Zeigarnik Effect and The Completing the Set Effect), Self-Regulation Theory, and behavioral finance "
        "principles in the context of tangible alternative assets exhibiting volatile secondary market premiums. The findings are expected to offer practical insights for young "
        "consumers in exercising financial discipline regarding discretionary collectibles and provide strategic inputs for community organizers and financial educators targeting Generation Z."
    )
    make_run_pure_black(r_abs_en, "Times New Roman", Pt(12), italic=True)

    p_kw_en = doc.add_paragraph()
    p_kw_en.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_kw_en.paragraph_format.line_spacing = 1.15
    p_kw_en.paragraph_format.space_before = Pt(6)
    p_kw_en.paragraph_format.first_line_indent = Cm(0)
    make_run_pure_black(p_kw_en.add_run("Keywords: "), "Times New Roman", Pt(12), bold=True)
    r_kw_en = p_kw_en.add_run("Impulsive Buying, Hedonic Motivation, Desire for Completeness, Speculative Motive, Self-Control, Moderated Regression Analysis, Pok\u00e9mon TCG, Behavioral Finance.")
    make_run_pure_black(r_kw_en, "Times New Roman", Pt(12), italic=True)

    out = OUT_DIR / "06_Abstract_English.docx"
    doc.save(str(out))
    print(f"[OK] {out.name}")
    return out


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("[*] Mengekstrak 6 halaman frontmatter ke file DOCX individual...")
    print(f"    Output dir: {OUT_DIR}\n")

    build_01_pernyataan()
    build_02_persetujuan()
    build_03_pengesahan()
    build_04_kata_pengantar()
    build_05_abstrak()
    build_06_abstract()

    print(f"\n[DONE] 6 file frontmatter berhasil dibuat di:\n  {OUT_DIR}")

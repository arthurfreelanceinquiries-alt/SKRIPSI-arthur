# Directive: Generate Publication-Grade Thesis Proposal in Microsoft Word (.docx)

## Goal
Transform the raw, uncalibrated thesis proposal document into a pristine, publication-grade academic document in Microsoft Word (`.docx`) that matches the visual elegance, typographical rigor, and structural standards of the 48-page XeLaTeX PDF (`Proposal_Arthur_PokemonTCG.pdf`) according to Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 (Model B).

## Inputs
1. **Canonical TeX Source:** `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex`
2. **Canonical Markdown Reference:** `01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md`
3. **Bibliography:** `01_Naskah_Utama/references.bib` and `Proposal_Arthur_PokemonTCG.bbl`
4. **Figure Assets:**
   - `01_Naskah_Utama/images/gambar_rerangka_penelitian.png` (300 DPI crop of Model Rerangka Konseptual)
   - `01_Naskah_Utama/images/diagram_alur_penelitian.png` (300 DPI crop of Diagram Alur Pelaksanaan Penelitian)

## Tools & Execution Script
- **Environment:** `C:\Users\Arthur Reezan\.gemini\config\skills\tex-math-to-word\.venv\Scripts\python.exe`
- **Execution Script:** `execution/build_proposal_word.py`
- **Verification Script:** `execution/verify_word_layout.py`
- **Live Automation:** PowerShell / Windows COM (`Word.Application.16`)

## Standards & Formatting Rules (Pedoman FEB UKRIDA 2023)
1. **Paper & Margins:**
   - Paper Size: ISO A4
   - Margins: Left: 4.0 cm, Right: 3.0 cm, Top: 3.0 cm, Bottom: 3.0 cm
2. **Typography:**
   - Primary Font: Times New Roman across all headings and body text
   - Body text: 12 pt, 1.5 line spacing, Justified alignment, First-line indent 1.25 cm
   - Spacing: 0 pt before, 0 pt after (except headings and table/figure captions)
3. **Headings:**
   - BAB: Heading 1, Centered, Bold, 12 pt, ALL CAPS. Page break before each chapter.
   - Sub-bab: Heading 2, Left-aligned, Bold, 12 pt (e.g., `1.1 Latar Belakang Penelitian`).
   - Anak sub-bab: Heading 3, Left-aligned, Bold, 12 pt (e.g., `1.2.1 Identifikasi Masalah`).
4. **Frontmatter Layout:**
   - Halaman Sampul (hal. i): Judul, identitas mahasiswa, prodi, fakultas, universitas, tahun (tanpa nomor halaman tercetak).
   - Halaman Pernyataan Keaslian (hal. ii): Pernyataan integritas akademik, boks tanda tangan & placeholder materai.
   - Halaman Persetujuan Proposal Skripsi (hal. iii): Tanda tangan Dosen Pembimbing (Dr. Fredella Colline) dan Ketua Program Studi (Rita Amelinda).
   - Halaman Pengesahan Tim Penguji Seminar Proposal (hal. iv): 4 kolom tanda tangan tim penguji.
   - Kata Pengantar (hal. v): Ucapan syukur dan terima kasih.
   - Abstrak Bahasa Indonesia (hal. vi): 1 spasi, font 11 pt, kata kunci bold.
   - Abstract English (hal. vii): 1 spasi, italic, keywords bold.
   - Daftar Isi, Daftar Tabel, Daftar Gambar (hal. viii–x): Nomor halaman bertitik (dot leaders).
5. **Pagination & Sectioning:**
   - Section 1: Halaman Sampul (Unnumbered).
   - Section 2: Halaman Awal (hal. ii s.d. x) dengan penomoran Romawi kecil (`ii, iii, iv...`) di kanan bawah: `Universitas Kristen Krida Wacana | ii`.
   - Section 3: Bagian Utama (BAB 1–3 dan Daftar Pustaka) dengan penomoran Arab (`1, 2, 3...`) di kanan bawah: `Universitas Kristen Krida Wacana | 1`.
6. **Tables (APA 7th Edition Format):**
   - Garis atas tebal (1 pt), garis pemisah header (0.75 pt), garis bawah penutup (1 pt).
   - Tanpa garis vertikal sama sekali.
   - Judul tabel di atas tabel (11 pt bold).
   - Keterangan/Sumber di bawah tabel (10 pt italic).
7. **Figures:**
   - Gambar terpusat (*center-aligned*).
   - Judul gambar di bawah gambar (11 pt bold).
   - Sumber gambar di bawah judul (10 pt italic).
8. **Equations:**
   - Persamaan matematika regresi berganda dan MRA disisipkan sebagai native Word OMML equation.
9. **Daftar Pustaka:**
   - Format APA 7th style, urut abjad nama belakang penulis, hanging indent 1.25 cm, spasi 1.15.

## Outputs
- `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx` (Publication-grade DOCX deliverable)

## Edge Cases & Error Handling
- If Word is currently open with the file (`~$oposal_Arthur_PokemonTCG.docx`), close the document or terminate lingering Word processes before overwriting.
- Verify that every table cell width is explicitly set to prevent text overflow outside page margins.
- Verify that Word COM loads the generated file without "Corrupt Document" recovery prompts.

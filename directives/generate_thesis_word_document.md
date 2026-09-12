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
3. **Headings & Outline Navigation (Document Tabs & Navigation Pane):**
   - Must use Word built-in styles (`Heading 1`, `Heading 2`, `Heading 3`) overridden to Times New Roman 12 pt, Bold, Black (`#000000`), 1.5 line spacing (strict FEB UKRIDA 2023 format, no default Word blue colors or large font sizes).
   - Paragraph properties must include explicit OpenXML `<w:outlineLvl>` tags (`w:val="0"` for Level 1, `w:val="1"` for Level 2, `w:val="2"` for Level 3) so headings populate both Microsoft Word Navigation Pane and Google Docs Document Tabs automatically.
   - **Level 1 (Heading 1, outlineLvl 0):**
     - Frontmatter titles: `PERNYATAAN KEASLIAN`, `HALAMAN PERSETUJUAN`, `HALAMAN PENGESAHAN`, `KATA PENGANTAR`, `ABSTRAK`, `ABSTRACT`, `DAFTAR ISI`, `DAFTAR TABEL`, `DAFTAR GAMBAR`.
     - Main Body & Backmatter: `BAB 1 PENDAHULUAN`, `BAB 2 TINJAUAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS`, `BAB 3 METODE PENELITIAN`, `DAFTAR PUSTAKA`.
     - Alignment: Centered, Bold, 12 pt, ALL CAPS. Page break before each chapter.
   - **Level 2 (Heading 2, outlineLvl 1):**
     - Sub-bab (e.g., `1.1 Latar Belakang Penelitian`, `2.1 Landasan Teori`, `3.1 Desain Penelitian`).
     - Alignment: Left-aligned, Bold, 12 pt, Title Case. Space before: 12 pt, space after: 6 pt.
   - **Level 3 (Heading 3, outlineLvl 2):**
     - Anak sub-bab (e.g., `1.2.1 Identifikasi Masalah`, `2.1.1 Teori S-O-R`, `3.5.1 Analisis Statistik Deskriptif`).
     - Alignment: Left-aligned, Bold, 12 pt, Title Case. Space before: 6 pt, space after: 3 pt.
4. **Frontmatter Layout:**
   - Halaman Sampul (hal. i): Judul, identitas mahasiswa, prodi, fakultas, universitas, tahun (tanpa nomor halaman tercetak).
   - Halaman Pernyataan Keaslian (hal. ii): Pernyataan integritas akademik, boks tanda tangan & placeholder materai.
   - Halaman Persetujuan Proposal Skripsi (hal. iii): Tanda tangan Dosen Pembimbing (Dr. Fredella Colline) dan Ketua Program Studi (Rita Amelinda).
   - Halaman Pengesahan Tim Penguji Seminar Proposal (hal. iv): 4 kolom tanda tangan tim penguji.
   - Kata Pengantar (hal. v): Ucapan syukur dan terima kasih.
   - Abstrak Bahasa Indonesia (hal. vi): 1 spasi, font 11 pt, kata kunci bold.
   - Abstract English (hal. vii): 1 spasi, italic, keywords bold.
   - Daftar Isi, Daftar Tabel, Daftar Gambar (hal. viii–x): Nomor halaman bertitik (dot leaders).
5. **Pagination & Sectioning (Accent Bar 4 & Google Docs Web Compatibility):**
   - Section 1: Halaman Sampul (Unnumbered, separate first-page footer).
   - Section 2: Halaman Awal (hal. ii s.d. x) dengan penomoran Romawi kecil (`ii, iii, iv...`) di kanan bawah: `Universitas Kristen Krida Wacana | ii`.
   - Section 3: Bagian Utama (BAB 1–3 dan Daftar Pustaka) dengan penomoran Arab (`1, 2, 3...`) di kanan bawah: `Universitas Kristen Krida Wacana | 1`.
   - **Google Docs Web & Word Typography Rule:** Per Buku Pedoman FEB UKRIDA (§3.3.b), footer menggunakan format standar *Accent Bar 4* dengan teks `Universitas Kristen Krida Wacana | ` berukuran **Times New Roman 10 pt Bold Black (`#000000`)**.
   - **OpenXML Technical Requirement:** The dynamic page number field `<w:fldSimple w:instr="PAGE">` must contain an explicit child `<w:r>` with `<w:rPr>` containing `<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>`, `<w:b/>`, `<w:sz w:val="20"/>` (10 pt), and `<w:color w:val="000000"/>`. Without this explicit `<w:rPr>`, Google Docs Web falls back to default body text (11–12 pt Regular), causing a jarring typographical mismatch with the prefix text.
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

## BAB 1 Content Rules (Dikunci Sejak September 2026)

**Hukum Keselarasan 1-to-1 (baku, berdasarkan Google Scholar survey 2022–2026):**
```
Jumlah Rumusan Masalah = Jumlah Tujuan Penelitian = Jumlah Hipotesis
```

Karena model menggunakan **MRA dengan 6 hipotesis** ($H_1$–$H_6$: 3 pengaruh langsung + 3 pengaruh moderasi), maka:
- **§1.2 Perumusan Masalah: 6 butir** (pertanyaan penelitian)
  - Butir 1–3: Apakah $X_1$, $X_2$, $X_3$ berpengaruh terhadap $Y$?
  - Butir 4–6: Apakah *Self-Control* memoderasi pengaruh $X_1$, $X_2$, $X_3$ terhadap $Y$?
- **§1.3 Tujuan Penelitian: 6 butir** (kalimat deklaratif sinkron dengan §1.2)
  - Butir 1–3: Untuk menganalisis pengaruh langsung.
  - Butir 4–6: Untuk menganalisis peran moderasi *Self-Control*.

**Pelanggaran yang harus dihindari:**
- ❌ Hanya 3 rumusan masalah padahal hipotesis 6 → inkonsistensi internal, akan ditolak penguji.
- ❌ Tujuan penelitian tidak sinkron 1-to-1 dengan rumusan masalah.
- ✅ Body text BAB 1 diambil dari canonical markdown: `01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md`.


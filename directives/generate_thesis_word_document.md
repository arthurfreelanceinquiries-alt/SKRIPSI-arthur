# Directive: Generate Publication-Grade Thesis Proposal in Microsoft Word (.docx)

## Goal
Transform the raw, uncalibrated thesis proposal document into a pristine, publication-grade academic document in Microsoft Word (`.docx`) that matches the visual elegance, typographical rigor, and structural standards of the XeLaTeX PDF (`Proposal_Arthur_PokemonTCG.pdf`) according to Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 (Model B).

## Inputs
1. **Canonical TeX Source:** `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex`
2. **Canonical Markdown Reference:** `01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md`
3. **Bibliography:** `01_Naskah_Utama/references.bib` and `Proposal_Arthur_PokemonTCG.bbl`
4. **Figure Assets:**
   - `01_Naskah_Utama/images/gambar_rerangka_penelitian.png` (300 DPI crop of Model Rerangka Konseptual)
   - `01_Naskah_Utama/images/diagram_alur_penelitian.png` (300 DPI crop of Diagram Alur Pelaksanaan Penelitian)

## Tools & Execution Script (3-Layer Architecture)
- **Layer 1 (Directive):** `directives/generate_thesis_word_document.md` & `04_Riset_&_Metodologi/PRD_HYBRID_PANDOC_SCRIPT_GENERATOR.md`
- **Layer 2 (Orchestration):** Agentic coordinator for pipeline sequencing, self-annealing, and parity validation.
- **Layer 3 (Execution):**
  - **Master Governor:** `execution/build_proposal_word.py` (Layout, styles, sectioning, APA 7th tables, TOC dot leaders, pure black).
  - **Math OMML Sub-Engine:** `pandoc.exe` (Surgical LaTeX math conversion into native Microsoft Word `<m:oMathPara>` equations).
  - **Audit Verifiers:** `execution/verify_docx_typography.py` & `execution/verify_pdf_docx_parity.py`.

## Standards & Formatting Rules (Pedoman FEB UKRIDA 2023)
1. **Paper & Margins:**
   - Paper Size: ISO A4 (21.0 x 29.7 cm)
   - Margins: Left: 4.0 cm, Right: 3.0 cm, Top: 3.0 cm, Bottom: 3.0 cm (Area teks efektif = 14.0 cm)

2. **Typography:**
   - Primary Font: Times New Roman across all headings, body text, tables, and frontmatter
   - Body text: 12 pt, 1.5 line spacing, Justified alignment, First-line indent 1.25 cm
   - Spacing: 0 pt before, 0 pt after (except headings and table/figure captions)

3. **Zero AI Artifacts & Clean Academic Typography (Mandatory):**
   - **No Raw Asterisks:** Dilarang keras menyisakan tanda asteris markdown (`*`, `**`, `***`) pada teks running. Format tebal (*bold*) dan miring (*italic*) harus diparsing secara hierarkis (*nested parsing*) menjadi *run formatting* Word murni.
   - **No Raw Dollar Math Signs:** Notasi matematika inline tidak boleh bocor sebagai kode mentah ber-dollar sign.
     - `$X_1$`, `$X_2$`, `$X_3$` dikonversi menjadi *X*₁, *X*₂, *X*₃ (italic dengan subscript Unicode).
     - `$Y$`, `$M$`, `$Z$` dikonversi menjadi *Y*, *M*, *Z*.
     - `$R^2$`, `$\Delta R^2$` dikonversi menjadi *R*², Δ*R*².
     - `$p < 0,05$`, `$\alpha = 0,05$` dikonversi menjadi *p* < 0,05, α = 0,05.
     - `$n = 30$`, `$n = 120-150$` dikonversi menjadi *n* = 30, *n* = 120–150.
   - **No Raw LaTeX Citation Leakage:** Perintah seperti `\citealp{...}`, `\citep{...}`, `\citet{...}`, `\ref{...}` wajib diterjemahkan menjadi teks sitasi nama dan tahun APA 7th (*Babin et al., 1994*).

4. **Frontmatter & Abstract Rules:**
   - **Abstrak (Bahasa Indonesia):** Judul 12 pt bold, identitas 12 pt bold, teks isi **12 pt regular** (1.0 spasi tunggal, alinea menjorok 1.25 cm), kata kunci 12 pt italic.
   - **Abstract (English):** Judul 12 pt bold, identitas 12 pt bold, teks isi **12 pt italic** (1.0 spasi tunggal, alinea menjorok 1.25 cm), keywords 12 pt italic.

5. **Daftar Isi, Daftar Tabel, & Daftar Gambar (Dot Leaders, Tab Stops, & Pemisahan Halaman Mandiri):**
   - **Pemisahan Halaman Mandiri Mutlak:** Sesuai Pedoman FEB UKRIDA 2023 (Subbab 2.1 hlm 9–10), `Daftar Isi` (j), `Daftar Tabel` (k), dan `Daftar Gambar` (l) adalah 3 entitas struktural independen yang masing-masing WAJIB berdiri sendiri pada halaman baru terpisah dengan angka romawi kecil.
   - **Proteksi Teknis OOXML & COM Interop:** Paragraf heading `DAFTAR TABEL` dan `DAFTAR GAMBAR` wajib disetel dengan `p.paragraph_format.page_break_before = True` (`<w:pageBreakBefore/>`). Pada injeksi native Table of Contents via Word COM Interop, wajib disisipkan buffer paragraf pemisah setelah DAFTAR ISI agar field TOC tidak melebur/merge dengan heading DAFTAR TABEL.
   - **Tab Stop & Dot Leaders:** Menggunakan tab stop rata kanan (*Right Alignment*) dengan titik-titik (*Dot Leader*) pada `14.0 cm = 7938 dxa` dan `right_indent = 0`.
   - **Formula Posisi Tab Stop Relatif terhadap Indentasi Paragraf:**
     Untuk mencegah tab stop melewati margin kanan (yang menyebabkan Word/WPS membatalkan titik-titik), posisi tab stop dihitung dengan rumus:
     $$\text{Tab Stop Position} = 13.8\text{ cm} - \text{Left Indent}$$
     - Tingkat 1 (Bab / Frontmatter, Left Indent 0 cm): Tab Stop di `13.8 cm` (atau `14.0 cm` di style native Word)
     - Tingkat 2 (Sub-bab, Left Indent 0.6 cm): Tab Stop di `13.2 cm`
     - Tingkat 3 (Anak Sub-bab, Left Indent 1.2 cm): Tab Stop di `12.6 cm`
   - Dengan formula ini, seluruh nomor halaman di Daftar Isi akan rata kanan presisi pada garis margin dan titik-titik penghubung (*dot leaders*) dipastikan muncul 100% sempurna di Microsoft Word maupun Google Docs/WPS Office.

6. **Pagination & Sectioning:**
   - Section 1: Halaman Sampul (Unnumbered, separate first-page footer).
   - Section 2: Halaman Awal (hal. ii s.d. x) dengan penomoran Romawi kecil (`ii, iii, iv...`) di kanan bawah: `Universitas Kristen Krida Wacana | ii`.
   - Section 3: Bagian Utama dengan penomoran Arab (`1, 2, 3...`) di kanan bawah: `Universitas Kristen Krida Wacana | 1`.

7. **Tables (APA 7th Edition Format):**
   - Garis atas tebal (1 pt), garis pemisah header (0.75 pt), garis bawah penutup (1 pt).
   - Tanpa garis vertikal sama sekali.

8. **Figures:**
   - Gambar terpusat (*center-aligned*). Judul gambar di bawah gambar (11 pt bold). Sumber gambar di bawah judul (10 pt italic).

9. **Equations:**
   - Persamaan matematika regresi berganda dan MRA disisipkan sebagai native Word OMML equation.

10. **Daftar Pustaka:**
    - Format APA 7th style, urut abjad nama belakang penulis, hanging indent 1.25 cm, spasi 1.15.

## Outputs
- `01_Naskah_Utama/Proposal_Arthur_NoBab3.docx` (Varian tanpa Bab 3)
- `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx` (Varian lengkap)

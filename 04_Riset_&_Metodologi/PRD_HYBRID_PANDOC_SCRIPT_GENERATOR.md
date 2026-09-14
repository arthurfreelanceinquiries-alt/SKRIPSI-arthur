# 📋 PRODUCT REQUIREMENTS DOCUMENT (PRD)
## Arsitektur Hybrid (Pandoc + Script Python-docx) untuk Generasi Naskah Skripsi DOCX Berstandar Emas (Golden Standard)

> [!SUMMARY] Tujuan & Solusi Dokumen Ini
> - **Untuk Apa:** Menetapkan arsitektur terintegrasi *Hybrid (Pandoc + Script)* dalam pembuatan naskah proposal skripsi Microsoft Word (`Proposal_Arthur_PokemonTCG.docx` dan `Proposal_Arthur_NoBab3.docx`) dengan membagi tugas secara optimal antara Pandoc sebagai parser/sub-engine rumus matematika dan `build_proposal_word.py` sebagai perakit tata letak dan pengawal tata kelola (*Layout & Governance Master*).
> - **Masalah yang Diselesaikan:** 
>   1. Persamaan matematika regresi MRA di Bab 3 sebelumnya dipaksa turun derajat (*downgraded*) menjadi teks biasa bertanda baca datar (`clean_math = re.sub(r'[_^{}]', '', clean_math)`), sehingga notasi subskrip ($X_1, \beta_1$) dan superskrip ($R^2$) menjadi teks biasa tanpa format rumus matematika resmi Word.
>   2. Pandoc secara mandiri tidak mampu mematuhi pedoman kampus FEB UKRIDA 2023 (margin 4-3-3-3 cm, pemisahan nomor romawi di bawah dan arab di atas, titik-titik daftar isi di 14.0 cm, tabel APA 7th edition tanpa garis vertikal, dan pemisahan otomatis varian NoBab3 vs Full).
> - **Keputusan Arsitektur:** Menerapkan **3-Layer Architecture**:
>   - **Layer 1 (Directive):** `directives/generate_thesis_word_document.md` & PRD ini sebagai SOP tata kelola.
>   - **Layer 2 (Orchestration):** Agen AI mengendalikan urutan eksekusi, verifikasi paritas, penanganan galat (*self-annealing*), dan pencatatan Obsidian Second Brain.
>   - **Layer 3 (Execution):** Skrip deterministik Python `execution/build_proposal_word.py` yang memanggil `pandoc.exe` via subprocess untuk menghasilkan elemen OpenXML `<m:oMathPara>` / `<m:oMath>` asli Microsoft Word (Cambria Math).

---

## 1. Spesifikasi Teknis & Pembagian Peran Hybrid

```
                  ┌─────────────────────────────────────────────────────────┐
                  │              Sumber Kanonikal Skripsi                   │
                  │   (Markdown / TeX: Bab 1, Bab 2, Bab 3, Pustaka)       │
                  └──────────────────────────┬──────────────────────────────┘
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼                                           ▼
       ┌───────────────────────────────┐           ┌───────────────────────────────┐
       │     SUB-ENGINE: PANDOC 3.11   │           │    GOVERNOR: PYTHON-DOCX      │
       │ (Surgical Conversion Engine)  │           │ (Layout & Compliance Engine)  │
       ├───────────────────────────────┤           ├───────────────────────────────┤
       │ 1. Parse LaTeX math notation  │           │ 1. Margins 4-3-3-3 cm         │
       │ 2. Generate native OpenXML    │           │ 2. Pure Black color #000000   │
       │    <m:oMathPara> (OMML)       │           │ 3. Header/Footer Sectioning   │
       │ 3. High-fidelity Greek/symbol │           │ 4. Dot leaders TOC at 14.0 cm │
       │    equations (Cambria Math)   │           │ 5. APA 7th Edition Tables     │
       └───────────────┬───────────────┘           │ 6. Mode NoBab3 vs Full Split  │
                       │                           └───────────────┬───────────────┘
                       └─────────────────────┬─────────────────────┘
                                             ▼
                       ┌───────────────────────────────────────────┐
                       │       HASIL AKHIR MAKSIMAL (.DOCX)        │
                       │ - Proposal_Arthur_PokemonTCG.docx         │
                       │ - Proposal_Arthur_NoBab3.docx             │
                       └───────────────────────────────────────────┘
```

### A. Peran Pandoc 3.11 (Math Sub-Engine)
1. Menangani blok formula matematika yang diawali `$$...$$` atau lingkungan `\begin{equation}`.
2. Mengonversi formula ke format dokumen OpenXML Word via perintah CLI:
   `pandoc -f latex -t docx`
3. Menghasilkan pohon elemen XML matematika resmi:
   `{http://schemas.openxmlformats.org/officeDocument/2006/math}oMathPara`
4. Menjaga ketepatan lambang Yunani ($\alpha, \beta, \Delta$), subskrip ($\beta_1, X_1$), superskrip ($R^2$), dan operator interaksi ($\cdot$).

### B. Peran `build_proposal_word.py` (Master Governor & Assembler)
1. **Template & Section Geometry**: Mengunci ukuran A4, margin Kiri 4 cm, Kanan 3 cm, Atas 3 cm, Bawah 3 cm, dengan area cetak efektif 14.0 cm.
2. **Kepatuhan Tipografi**: Font Times New Roman 12 pt, spasi 1.5, warna hitam absolut `#000000` (tanpa warna aksen tema Word).
3. **Daftar Isi, Gambar, & Tabel**: Tab stop rata kanan di 14.0 cm (7938 dxa) dengan `w:leader="dot"` yang kompatibel di Word Desktop, Word Online, dan Google Docs.
4. **Pemisahan Varian**:
   - `--no-chapter3`: Menghasilkan naskah review (hanya Bab 1 & 2, tanpa Bab 3, tanpa lembar persetujuan formal, halaman awal mulai dari `ii`).
   - Default: Menghasilkan naskah lengkap (Bab 1 s.d. 3, lembar persetujuan formal, instrumen penelitian).
5. **Injeksi OMML**: Mengambil elemen `<m:oMathPara>` dari Pandoc dan menyematkannya langsung ke dalam paragraf Word.

---

## 2. Model Persamaan yang Dikonversi Secara Hybrid

Berikut 6 persamaan kanonikal yang dijamin 100% tampil sebagai *Native Word Equation* di naskah lengkap:

1. **Formula Ukuran Sampel Simultan Green (1991):**
   $$N \ge 50 + 8k$$
2. **Kalkulasi Sampel Simultan ($k=7$):**
   $$N \ge 50 + 8(7) = 50 + 56 = 106\text{ responden}$$
3. **Formula Ukuran Sampel Individual Green (1991):**
   $$N \ge 104 + k$$
4. **Kalkulasi Sampel Individual ($k=7$):**
   $$N \ge 104 + 7 = 111\text{ responden}$$
5. **Model 1: Regresi Linear Berganda (Efek Utama):**
   $$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + e$$
6. **Model 2: Moderated Regression Analysis (MRA Interaksi Penuh):**
   $$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_4 M + \beta_5 (X_1 \cdot M) + \beta_6 (X_2 \cdot M) + \beta_7 (X_3 \cdot M) + e$$

---

## 3. Acceptance Criteria (Kriteria Keberhasilan)

| No | Pengujian | Spesifikasi Lulus |
| :---: | :--- | :--- |
| 1 | **Keberadaan Objek OMML** | Setiap formula matematika di Bab 3 terdaftar sebagai elemen `<m:oMathPara>` atau `<m:oMath>`, bukan teks biasa. |
| 2 | **Kompatibilitas Word COM** | Dokumen dapat dibuka dan diekspor ke PDF via Microsoft Word headless tanpa memunculkan dialog peringatan kerusakan XML. |
| 3 | **Warna Hitam Murni** | 100% teks di seluruh bab berwana `#000000`. |
| 4 | **Dot Leaders Daftar Isi** | Seluruh baris TOC/LOT/LOF memiliki titik-titik rapi hingga batas 14.0 cm tanpa ada teks yang terpotong aneh. |
| 5 | **Mode NoBab3 Steril** | `Proposal_Arthur_NoBab3.docx` tidak memuat Bab 3 dan tidak memuat lembar persetujuan formal. |
| 6 | **Audit Otomatis Lulus** | `verify_docx_typography.py` dan `verify_pdf_docx_parity.py` menghasilkan status **PASS 100%**. |

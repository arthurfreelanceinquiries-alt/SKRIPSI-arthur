# Product Requirements Document (PRD)
## Standardisasi Heading, Sub-Bab, dan Navigasi Outline Dokumen Word Proposal Skripsi

- **Dokumen Target:** `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx`
- **Tujuan:** Mengonfigurasi seluruh Bab, Sub-Bab, Sub-Sub-Bab, dan Judul Halaman Awal agar terdaftar penuh dalam **Document Tabs / Document Outline (Panel Navigasi Google Docs & MS Word)** dengan format baku FEB UKRIDA 2023.
- **Versi:** 1.0 (12 September 2026)
- **Status:** Approved / In Progress

---

## 1. Latar Belakang & Masalah (Problem Statement)
Saat berkas `Proposal_Arthur_PokemonTCG.docx` dibuka di Google Docs atau Microsoft Word, panel navigasi kiri (*Document tabs / Document outline*) menampilkan pesan:
> *"Headings you add to the document will appear here."* (Kosong / Tidak ada outline).

### Akar Masalah (Root Cause):
Pada generator `execution/build_proposal_word.py`, seluruh judul bab, sub-bab, dan judul bagian depan dibuat menggunakan paragraf teks biasa (`doc.add_paragraph()`) dengan gaya bawaan `Normal`. Walaupun teks diformat tebal (*bold*) dan berukuran 12 pt, elemen tersebut **tidak memiliki atribut gaya Heading Word (`Heading 1`, `Heading 2`, `Heading 3`)** dan **tidak memiliki tag XML `w:outlineLvl`**. Akibatnya, sistem navigasi Google Docs dan Word tidak dapat mendeteksi hierarki naskah.

---

## 2. Tujuan & Sasaran Produk (Goals & Objectives)
1. **Navigasi Otomatis & Terstruktur:** Seluruh Bab (Level 1), Sub-Bab (Level 2), Sub-Sub-Bab (Level 3), serta bagian penting depan/belakang muncul secara hierarkis dan dapat diklik pada *Document tabs* / *Document outline*.
2. **Kepatuhan Format FEB UKRIDA 2023:**
   - **Gaya Teks:** Tetap Times New Roman 12 pt, Tebal (*Bold*), Spasi 1.5, Warna Hitam Otomatis (tanpa warna biru default Word).
   - **Heading 1 (Bab & Bagian Depan):** Huruf Kapital (*ALL CAPS*), Rata Tengah (*Center*), Page Break sebelum bab baru.
   - **Heading 2 (Sub-Bab):** Rata Kiri (*Left-aligned*), Kapitalisasi Judul (*Title Case*), spasi sebelum 12 pt, sesudah 6 pt.
   - **Heading 3 (Anak Sub-Bab):** Rata Kiri (*Left-aligned*), Kapitalisasi Kalimat (*Sentence Case* / *Title Case*), spasi sebelum 6 pt, sesudah 3 pt.
3. **Kompatibilitas Ganda:** Bekerja sempurna 100% di **Microsoft Word Desktop** (Navigation Pane `Ctrl+F` -> Headings) dan **Google Docs** (Document tabs sidebar).

---

## 3. Spesifikasi Pemetaan Hirarki Heading (*Outline Hierarchy Mapping*)

### A. Level 1 — `Heading 1` (`w:outlineLvl = 0`)
* **Bagian Awal (Frontmatter):**
  - `PERNYATAAN KEASLIAN KARYA TUGAS AKHIR`
  - `HALAMAN PERSETUJUAN PROPOSAL SKRIPSI`
  - `HALAMAN PENGESAHAN TIM PENGUJI SEMINAR PROPOSAL`
  - `KATA PENGANTAR`
  - `ABSTRAK`
  - `ABSTRACT`
  - `DAFTAR ISI`
  - `DAFTAR TABEL`
  - `DAFTAR GAMBAR`
* **Bagian Utama:**
  - `BAB I PENDAHULUAN`
  - `BAB II TINJAUAN PUSTAKA`
  - `BAB III METODE PENELITIAN`
  - `DAFTAR PUSTAKA`
  - `LAMPIRAN`

### B. Level 2 — `Heading 2` (`w:outlineLvl = 1`)
* **BAB I:**
  - `1.1 Latar Belakang Penelitian`
  - `1.2 Identifikasi Masalah`
  - `1.3 Pembatasan Masalah`
  - `1.4 Rumusan Masalah`
  - `1.5 Tujuan Penelitian`
  - `1.6 Manfaat Penelitian`
  - `1.7 Sistematika Penulisan`
* **BAB II:**
  - `2.1 Landasan Teori`
  - `2.2 Variabel Dependen: Impulsive Buying (Y)`
  - `2.3 Variabel Independen 1: Hedonic Motivation (X1)`
  - `2.4 Variabel Independen 2: Desire for Completeness (X2)`
  - `2.5 Variabel Independen 3: Speculative Motive (X3)`
  - `2.6 Variabel Moderasi: Self-Control (M)`
  - `2.7 Penelitian Terdahulu`
  - `2.8 Pengembangan Hipotesis`
  - `2.9 Rerangka Konseptual Penelitian`
* **BAB III:**
  - `3.1 Desain Penelitian`
  - `3.2 Objek, Populasi, dan Sampel Penelitian`
  - `3.3 Operasionalisasi Variabel`
  - `3.4 Metode Pengumpulan Data`
  - `3.5 Metode Analisis Data`

### C. Level 3 — `Heading 3` (`w:outlineLvl = 2`)
* **BAB I:**
  - `1.6.1 Manfaat Teoretis`
  - `1.6.2 Manfaat Praktis`
* **BAB II:**
  - `2.1.1 Grand Theory: Behavioral Finance (Keuangan Perilaku)`
  - `2.1.2 Supporting Theory 1: Model S-O-R (Stimulus-Organism-Response)`
  - `2.1.3 Supporting Theory 2: The "Completing the Set" Effect & Zeigarnik Effect`
  - `2.1.4 Supporting Theory 3: Teori Regulasi Diri (Self-Regulation Theory)`
  - `2.8.1 Pengaruh Hedonic Motivation terhadap Impulsive Buying (H1)`
  - `2.8.2 Pengaruh Desire for Completeness terhadap Impulsive Buying (H2)`
  - `2.8.3 Pengaruh Speculative Motive terhadap Impulsive Buying (H3)`
  - `2.8.4 Peran Moderasi Self-Control pada Pengaruh Hedonic Motivation terhadap Impulsive Buying (H4)`
  - `2.8.5 Peran Moderasi Self-Control pada Pengaruh Desire for Completeness terhadap Impulsive Buying (H5)`
  - `2.8.6 Peran Moderasi Self-Control pada Pengaruh Speculative Motive terhadap Impulsive Buying (H6)`
* **BAB III:**
  - `3.2.1 Objek Penelitian`
  - `3.2.2 Populasi Penelitian`
  - `3.2.3 Sampel dan Teknik Sampling`
  - `3.5.1 Analisis Statistik Deskriptif`
  - `3.5.2 Uji Kualitas Data (Uji Validitas dan Reliabilitas)`
  - `3.5.3 Uji Asumsi Klasik`
  - `3.5.4 Analisis Regresi Linier Berganda dan Moderated Regression Analysis (MRA)`
  - `3.5.5 Uji Kelayakan Model (Uji F dan Koefisien Determinasi R²)`
  - `3.5.6 Uji Hipotesis (Uji t)`

---

## 4. Kriteria Keberhasilan (Acceptance Criteria)
1. Dokumen `Proposal_Arthur_PokemonTCG.docx` berhasil dibangun tanpa eror.
2. Ketika dibuka di Word / Google Docs, seluruh daftar di atas muncul di tab navigasi (*Document tabs / Navigation Pane*).
3. Mengklik salah satu butir di panel navigasi langsung mengarahkan kursor (*jump*) ke bagian naskah yang bersangkutan.
4. Format visual naskah tetap memenuhi Buku Pedoman FEB UKRIDA 2023 (Times New Roman 12 pt, Bold, Hitam, Spasi 1.5, tanpa warna biru Word).

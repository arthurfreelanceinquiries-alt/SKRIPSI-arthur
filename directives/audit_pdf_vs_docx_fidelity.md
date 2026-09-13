# Directive: SOP Audit Komparasi Integritas Dokumen (PDF vs DOCX)

## 1. Tujuan
Menetapkan prosedur standar operasi (SOP) untuk memverifikasi kesetaraan substansi (*content fidelity*) 1:1 antara naskah proposal tugas akhir versi PDF (hasil kompilasi LaTeX) dan versi Microsoft Word (.docx).

Dokumen ini memastikan tidak ada diskrepansi data, argumen, sitasi, rumusan masalah, tabel empiris, atau metodologi sebelum dokumen diserahkan kepada Dosen Pembimbing (Dr. Fredella Colline) atau diujikan pada Seminar Proposal FEB UKRIDA.

## 2. Input Data
- `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf` (PDF master kompilasi LaTeX)
- `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx` (DOCX hasil generasi Word OpenXML)
- `05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md` (Pondasi acuan format)

## 3. Alat Eksekusi (Layer 3)
- Skrip: `execution/compare_pdf_docx_fidelity.py`
- Engine: Python `pymupdf` (fitz) dan OpenXML parsing (`zipfile`, `xml.etree.ElementTree`).

## 4. Dimensi dan Kriteria Audit
Pemeriksaan harus mencakup 5 pilar substansi:

1. **Pilar A: Bagian Awal (*Frontmatter*)**
   - Halaman Sampul (Judul, Nama, NIM, Dosen Pembimbing: Dr. Fredella Colline, Tahun: 2026).
   - Pernyataan Keaslian Karya Tugas Akhir.
   - Halaman Persetujuan & Pengesahan Proposal.
   - Kata Pengantar (Konsistensi butir ucapan terima kasih: Dekan, Kaprodi, Pembimbing, Penguji, Orang Tua).
   - Abstrak Bahasa Indonesia & Bahasa Inggris (Struktur IMRAD, kata kunci).
   - Daftar Isi, Daftar Tabel, Daftar Gambar.

2. **Pilar B: Bab 1 Pendahuluan**
   - Latar Belakang Masalah (Paragraf fenomena Pokemon TCG, booster pack, pasar sekunder, *gap* empiris).
   - Perumusan Masalah: Wajib memuat **6 butir pertanyaan penelitian**.
   - Tujuan Penelitian: Wajib memuat **6 butir tujuan penelitian**.
   - Manfaat Penelitian: Manfaat Teoritis & Manfaat Praktis.

3. **Pilar C: Bab 2 Kajian Pustaka & Pengembangan Hipotesis**
   - Grand Theory: Keuangan Perilaku (*Behavioral Finance*).
   - Supporting Theories: Teori S-O-R, *The "Completing the Set" Effect*, Teori Regulasi Diri (*Self-Regulation Theory*).
   - Kajian Variabel: $Y$ (*Impulsive Buying*), $X_1$ (*Hedonic Motivation*), $X_2$ (*Desire for Completeness*), $X_3$ (*Speculative Motive*), $M$ (*Self-Control*).
   - Tabel 2.1: Wajib memuat **10 Jurnal Empiris Utama (2021–2025)** yang terverifikasi.
   - Kerangka Pemikiran & Hipotesis: Wajib memuat **6 hipotesis ($H_1$–$H_6$)**.

4. **Pilar D: Bab 3 Metode Penelitian**
   - Batasan Penelitian (Ruang lingkup operasional).
   - Desain & Sumber Data (Data primer via kuesioner daring).
   - Populasi & Sampel: Target **150 responden**, kriteria inklusi sampling.
   - Model Penelitian: Persamaan matematis Moderated Regression Analysis (MRA) dengan *mean-centering*.
   - Tabel Operasionalisasi Variabel (Tabel 3.1 & 3.2).
   - Gambar 3.1 (Diagram Alur Penelitian) & Tabel 3.3 (Jadwal Penelitian).

5. **Pilar E: Daftar Pustaka & Sitasi**
   - Kelengkapan referensi antara file LaTeX `.bib` dengan daftar pustaka Word.
   - Konsistensi gaya sitasi APA Edisi ke-7.

## 5. Ambang Batas Toleransi (*Tolerance Thresholds*)
- **Perbedaan Redaksional**: Toleransi 0% pada nama variabel, hipotesis, dan angka metodologis.
- **Perbedaan Format Visual**: Tata letak baris/halaman berbeda karena perbedaan engine rendering (LaTeX vs Word) dapat diterima, selama nomor urut dan isi paragraf lengkap.
- **Output Audit**: File laporan komparasi wajib ditulis ke `04_Riset_&_Metodologi/LAPORAN_KOMPARASI_PDF_VS_DOCX.md`.

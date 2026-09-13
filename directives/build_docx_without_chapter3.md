# Directive: Build DOCX Proposal Tanpa Bab 3

## Tujuan
SOP resmi untuk menghasilkan versi DOCX proposal skripsi yang **identik dengan file utama** (`Proposal_Arthur_PokemonTCG.docx`) KECUALI seluruh konten Bab 3 dihilangkan, karena dosen pembimbing belum menugaskan pengerjaan Bab 3.

## File Output
- **Nama:** `01_Naskah_Utama/Proposal_Arthur_NoBab3.docx`
- **Bukan pengganti** file utama — file utama tetap utuh dan tidak dimodifikasi

## Elemen Bab 3 Yang Dihilangkan
Hapus SELURUH konten berikut dari output:
- Sub-bab 3.1: Batasan Penelitian dan Ruang Lingkup
- Sub-bab 3.2: Populasi dan Kriteria Inklusi Sampel
- Sub-bab 3.3: Ukuran Sampel dan Teknik Pengambilan Sampel
- Sub-bab 3.4: Sumber Data dan Instrumen Penelitian
- Sub-bab 3.5: Model Penelitian dan Teknik Analisis (MRA)
- Sub-bab 3.6: Tabel Operasionalisasi Variabel (Tabel 3.1 & 3.2)
- Sub-bab 3.7: Jadwal Penelitian (Tabel 3.3) & Gambar 3.1 (Diagram Alur)
- Heading "BAB III METODE PENELITIAN" (halaman judul bab)

## Elemen Yang Tetap Ada
- Seluruh Frontmatter (Sampul, Kata Pengantar, Abstrak, Daftar Isi, Daftar Tabel, Daftar Gambar)
- Bab 1: Pendahuluan (lengkap)
- Bab 2: Tinjauan Pustaka (lengkap)
- Daftar Pustaka (lengkap)

## Penyesuaian Otomatis
- **Daftar Isi:** Entry Bab 3 dan semua sub-babnya DIHAPUS dari Daftar Isi
- **Penomoran Halaman:** Tetap berurutan, tidak ada lompatan (Bab 2 langsung ke Daftar Pustaka)
- **Daftar Tabel & Gambar:** Entry Tabel 3.1, 3.2, 3.3 dan Gambar 3.1 dihapus

## Kriteria Keberhasilan
- File DOCX berhasil dibuat tanpa error
- Membuka file DOCX: tidak ada konten Bab 3 sama sekali
- Daftar Isi akurat dan tidak ada entry Bab 3
- Penomoran halaman konsisten dan berurutan

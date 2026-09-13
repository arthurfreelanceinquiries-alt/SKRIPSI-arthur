# Directive: Build PDF Proposal Tanpa Bab 3 (XeLaTeX Native)

## 1. Tujuan
Standar Operasional Prosedur (SOP) resmi untuk menghasilkan dokumen PDF proposal skripsi versi varian tanpa Bab 3 (`Proposal_Arthur_NoBab3.pdf`) yang **100% identik dan persis sama hingga detail terkecil** dengan file utama (`Proposal_Arthur_PokemonTCG.pdf`), mengikuti seluruh kaidah Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023, dengan **satu-satunya perbedaan: seluruh materi Bab 3 ditiadakan**, serta **tanpa menyentuh atau memodifikasi file original**.

---

## 2. Jaminan Non-Destructive Invariance (File Utama Tetap Utuh)
- File sumber utama berikut **DILARANG KERAS DIUBAH ATAU DISENTUH**:
  - `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex`
  - `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf`
  - `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx`
- Semua proses kompilasi dilakukan pada file build varian independen:
  - `01_Naskah_Utama/Proposal_Arthur_NoBab3.tex`
  - Output PDF target: `01_Naskah_Utama/Proposal_Arthur_NoBab3.pdf`

---

## 3. Standar Tipografi & Format FEB UKRIDA 2023
- **Engine Kompilasi:** XeLaTeX (`xelatex.exe`) dengan paket `fontspec`.
- **Kertas & Margin:** ISO A4 (21.0 x 29.7 cm), Margin Kiri 4.0 cm, Atas 3.0 cm, Kanan 3.0 cm, Bawah 3.0 cm (Pedoman §3.2.a).
- **Font & Spasi:** Times New Roman 12 pt, 1.5 spasi (`onehalfspacing`), indent alinea 1.25 cm / 5 ketukan (Pedoman §3.2.b & §3.2.e).
- **Header & Footer:** Footer kanan bawah `Universitas Kristen Krida Wacana | [Hal]` dengan penomoran romawi kecil pada frontmatter dan penomoran arab pada teks utama (Pedoman §3.3.b).
- **Tabel & Gambar:** Format booktabs terbuka standar jurnal tanpa garis vertikal, caption tabel di atas, caption gambar di bawah (Pedoman §3.2.g).
- **Daftar Pustaka:** Format APA 7th edition via `natbib` (`apalike`) dan database `references.bib`.

---

## 4. Spesifikasi Pemotongan Bab 3
- **Konten yang Dihilangkan:**
  - Heading bab: `\section*{BAB 3\\[0.3cm]METODE PENELITIAN}`
  - Entri TOC Bab 3: `\addcontentsline{toc}{section}{\texorpdfstring{BAB 3\quad METODE PENELITIAN}{BAB 3 METODE PENELITIAN}}`
  - Seluruh sub-bab (3.1 sampai 3.5 beserta seluruh paragraf dan rumus MRA).
  - Tabel 3.1 (Skala Pengukuran Likert 5 Poin).
  - Tabel 3.2 (Operasionalisasi Variabel Penelitian).
  - Tabel 3.3 (Jadwal Penelitian).
- **Konten yang Dipertahankan 100%:**
  - Halaman Judul Luar / Sampul (hal. i).
  - Halaman Judul Dalam (hal. ii).
  - Lembar Persetujuan Pembimbing (hal. iii).
  - Lembar Pengesahan Tim Penguji (hal. iv).
  - Kata Pengantar (hal. v).
  - Abstrak Bahasa Indonesia (hal. vi).
  - Abstract Bahasa Inggris (hal. vii).
  - Daftar Isi (TOC) — diperbarui otomatis oleh XeLaTeX, hanya memuat BAB 1, BAB 2, DAFTAR PUSTAKA.
  - Daftar Tabel (LOT) — hanya memuat Tabel 2.1.
  - Daftar Gambar (LOF) — memuat Gambar 2.1 (Rerangka Konseptual via TikZ).
  - Bab 1 Pendahuluan (1.1 - 1.4).
  - Bab 2 Kajian Pustaka & Pengembangan Hipotesis (2.1 - 2.5).
  - Daftar Pustaka (seluruh referensi yang disitasi di Bab 1 & Bab 2).

---

## 5. Prosedur Eksekusi (Layer 3)
Pipeline kompilasi dijalankan melalui script `execution/build_proposal_nobab3_pdf.py`:
1. Baca `Proposal_Arthur_PokemonTCG.tex` secara aman.
2. Ekstraksi segmen `pre-Bab 3` (sebelum baris penanda Bab 3) dan segmen `post-Bab 3` (mulai dari penanda `DAFTAR PUSTAKA`).
3. Tulis file `01_Naskah_Utama/Proposal_Arthur_NoBab3.tex`.
4. Jalankan kompilasi multi-pass di direktori `01_Naskah_Utama/`:
   ```powershell
   xelatex -interaction=nonstopmode Proposal_Arthur_NoBab3.tex
   bibtex Proposal_Arthur_NoBab3
   xelatex -interaction=nonstopmode Proposal_Arthur_NoBab3.tex
   xelatex -interaction=nonstopmode Proposal_Arthur_NoBab3.tex
   ```
5. Jalankan audit verifikasi via `execution/verify_nobab3_pdf.py`.

---

## 6. Kriteria Keberhasilan & Validasi
- [ ] File `Proposal_Arthur_NoBab3.pdf` berhasil dihasilkan tanpa error fatal.
- [ ] Ukuran file wajar (antara 200 KB - 400 KB, sebanding dengan file original ~291 KB).
- [ ] Halaman 1-16 (Bab 1 dan Bab 2) identik secara visual dan teks dengan file original.
- [ ] Tidak ada kata kunci Bab 3 (Metode Penelitian, Uji Kualitas Data, Operasionalisasi Variabel) pada body dokumen.
- [ ] Daftar Isi tidak mengandung entri Bab 3.
- [ ] Daftar Tabel hanya memuat Tabel 2.1.
- [ ] File original `Proposal_Arthur_PokemonTCG.tex`, `.pdf`, dan `.docx` tidak mengalami perubahan timestamp modifikasi.

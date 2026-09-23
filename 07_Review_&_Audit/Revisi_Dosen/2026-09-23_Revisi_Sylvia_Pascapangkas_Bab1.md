> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Mencatat seluruh revisi pascapangkas Bab 1 dari Sylvia agar tertelusur dan dapat dipertanggungjawabkan saat bimbingan.
> - **Masalah yang Diselesaikan:** Temuan tersebar di chat (hal iii, 2, 3, 9, 46 + Bab 3 + diagram) dirangkum menjadi daftar kerja tunggal dengan akar masalah dan rencana perbaikan per butir.
> - **Keputusan/Output:** Perbaikan dieksekusi pada TeX master, pipeline sinkronisasi, dan naskah utama; file NoBab3 dihapus (mengerucut ke file utama).

# Revisi Sylvia — Pascapangkas Bab 1 (23 September 2026)

- **Sumber:** Masukan Sylvia atas `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]]` (varian utama)
- **Status:** Dieksekusi penuh pada sesi ini

## 1. Transkrip Temuan (verbatim, diringkas per halaman)

| # | Lokasi | Temuan Sylvia |
|:---:|:---|:---|
| 1 | Hal iii | Nama tabel (1.1, 1.2, 1.3); semua judul Bab memakai *shift+enter* (contoh: `BAB I` + baris baru + `Pendahuluan`) |
| 2 | Hal 2 | Rujukan "pada gambar 1.1" (teks hanya menulis "pada Gambar" tanpa nomor) |
| 3 | Hal 3 | Typo `\` (render `125\` di akhir baris akibat sisa perintah LaTeX `\%`) |
| 4 | Hal 9 | Font di tabel tidak selaras; Manfaat Penelitian ("generasi z" dkk.) |
| 5 | Umum Bab 1 | Setiap penyebutan "pada gambar" wajib bernomor (1.1/1.2/...) |
| 6 | Umum | Banyak spasi tidak berguna di awal kalimat |
| 7 | Tabel 1.1 | "Uji n.s. langsung apa?" (singkatan `n.s.` membingungkan) |
| 8 | Hal 46 (3.5.2+) | Penyusunan skor komposit dan seterusnya bukan subbab 3.5.2, melainkan poin-poin tahapan analisis data (1, 2, 3, ...) |
| 9 | Umum | Banyak typo tanda `\` (sisa sintaks LaTeX bocor ke DOCX) |
| 10 | 3.5 | Pearson hanya berkisar 0–1, tidak sampai 5 (klarifikasi rentang korelasi vs skala Likert) |
| 11 | 3.5 | *Cronbach's Alpha* bilateral di atas 0,70 (koreksi dari 0,60) |
| 12 | Gambar 3.1 | Diagram alur belum memuat uji Kolmogorov-Smirnov dkk.; tiap tahap wajib mencantumkan input dan output |

## 2. Akar Masalah (hasil audit Second Brain)

| Temuan | Akar masalah |
|:---|:---|
| Judul Bab satu baris | `add_heading_1` di `[[execution/build_proposal_word.py]]` tidak menyisipkan jeda baris lunak (`<w:br/>`) |
| "pada Gambar." tanpa nomor | `~\ref{}` dibuang konverter (`sync` baris 610) tanpa pengganti angka |
| `125\` | Sisa `\` di ujung paragraf lolos dari `clean_academic_text` (pola `\%` + newline) |
| Font tabel | Tabel generik 9,5pt vs Tabel 1.1 9,0pt (bedakan diselaraskan) |
| `n.s.` | Singkatan statistik tanpa penjelasan di sel Tabel 1.1 |
| 3.5.2–3.5.6 | Tahapan analisis diformat sebagai subanak-subbab bernomor |
| Typo `\` massal | Notasi matematika sebaris (`\bar`, `\in`, `\{`, `\url`, `$M^*$`) dan `\ref` lolos ke DOCX |
| Pearson/Alpha | Redaksi ambigu + ambang 0,60 |
| Diagram 3.1 | Kotak tahap 7 generik ("Uji Asumsi Klasik") tanpa rincian uji dan tanpa pasangan input-output |

## 3. Tindakan (terlaksana sesi ini)

1. Judul `BAB 1/2/3` di DOCX menjadi dua baris via jeda baris lunak; TeX sudah dua baris.
2. Seluruh `Gambar~\ref` / `Tabel~\ref` / `Persamaan~\ref` narasi di-hardcode angkanya di TeX master (14 titik).
3. Pembersih pipeline diperkuat (`\%`, sisa `\` ujung, `\url`, `\ref` cadangan, spasi ganda) + notasi legenda model 3.3 ditulis ulang dengan kata-kata.
4. Font tubuh seluruh tabel DOCX diseragamkan 9,0pt.
5. `n.s.` → `tidak signifikan` di Tabel 1.1 (TeX, MD, DOCX).
6. Subbab 3.5.2–3.5.6 menjadi Tahap 1–5 di bawah 3.5.
7. Klarifikasi rentang Pearson (-1 hingga +1) dan ambang Alpha 0,70 (naskah + diagram).
8. Diagram alur dirinci (KS, Tolerance/VIF, Glejser) + pasangan input-output tiap tahap; PNG DOCX diregenerasi dari PDF.
9. File NoBab3 dihapus; `[[execution/verify_pdf_docx_parity.py]]` dan gerbang X2 disesuaikan ke file utama.

> [!NOTE] Terbuka
> - Butir hal iii soal "nama tabel 1.1, 1.2, 1.3" masih perlu konfirmasi (entri Daftar Tabel saat ini sudah tunggal dan baku).

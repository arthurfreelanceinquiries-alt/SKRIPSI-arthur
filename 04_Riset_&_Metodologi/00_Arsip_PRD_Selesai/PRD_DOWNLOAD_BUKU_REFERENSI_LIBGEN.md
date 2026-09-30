# PRD: Akuisisi & Pengunduhan Berkas Digital PDF Buku Referensi dari Library Genesis (LibGen)

> **Status:** APPROVED & IN PLANNING  
> **Versi:** 1.0.0  
> **Tanggal:** 16 September 2026  
> **Penanggung Jawab:** Tim Peneliti & Antigravity IDE  
> **Lokasi Repositori Target:** `06_Referensi_Jurnal_PDF/03_Buku_Referensi_PDF/`  
> **Dasar Regulasi:** `.agents/rules/mandatory_verifiable_theories_and_books.md` & `directives/verify_book_sources_libgen.md`

---

## 1. Latar Belakang & Urgensi

Berdasarkan aturan baku (*mandatory rule*) yang telah ditetapkan pada Sesi 14, setiap teori buku dan artikel ilmiah yang disitasi dalam naskah Skripsi Arthur Reezan wajib memiliki bukti fisik/digital autentik yang dapat dilacak dan diunduh. Pengecekan pada basis data **Library Genesis (`https://libgen.li/`)** telah membuktikan bahwa 100% buku teks internasional seminal (9 judul) tersedia di LibGen dengan banyak edisi aktif.

Untuk memastikan kesiapan 100% saat seminar proposal dan sidang skripsi di hadapan dewan penguji Fakultas Ekonomi dan Bisnis (FEB) UKRIDA, seluruh berkas digital (PDF) buku-buku tersebut harus diunduh secara fisik dan diorganisasikan ke dalam repositori lokal naskah.

---

## 2. Inventarisasi Buku yang Diunduh

Target unduhan mencakup 9 buku teks internasional seminal dari LibGen serta penyediaan berkas representatif bab bagi 2 buku metodologi nasional:

| No | Citation Key | Penulis & Tahun | Judul Buku | Format Target | Estimasi Ukuran | Peran dalam Skripsi |
|:---:|:---|:---|:---|:---:|:---:|:---|
| 1 | `shiller2000irrational` | Shiller (2000) | *Irrational Exuberance* | PDF | ~5–15 MB | Grand Theory: Behavioral Finance & Motif Spekulasi ($X_3$) |
| 2 | `keynes1936general` | Keynes (1936) | *The General Theory of Employment, Interest and Money* | PDF | ~2–8 MB | Landasan Motif Spekulasi Finansial ($X_3$) |
| 3 | `mehrabian1974approach` | Mehrabian & Russell (1974) | *An Approach to Environmental Psychology* | PDF | ~10–25 MB | Supporting Theory: Kerangka S-O-R ($X_1 \rightarrow Y$) |
| 4 | `belk1995collecting` | Belk (1995) | *Collecting in a Consumer Society* | PDF | ~5–12 MB | Supporting Theory: Psikologi Koleksi ($X_2$) |
| 5 | `cohen1988statistical` | Cohen (1988) | *Statistical Power Analysis for the Behavioral Sciences* | PDF | ~15–30 MB | Metodologi: Penentuan Ukuran Sampel $N=120-150$ |
| 6 | `aiken1991multiple` | Aiken & West (1991) | *Multiple Regression: Testing and Interpreting Interactions* | PDF | ~5–15 MB | Metodologi: Ekonometrika MRA & Mean-Centering |
| 7 | `hayes2018introduction` | Hayes (2018) | *Introduction to Mediation, Moderation, and Conditional Process Analysis* | PDF | ~10–20 MB | Metodologi: Uji Moderasi MRA Lanjutan & Simple Slopes |
| 8 | `sekaran2016research` | Sekaran & Bougie (2016) | *Research Methods for Business: A Skill-Building Approach* | PDF | ~10–25 MB | Metodologi: Riset Bisnis & Skala Pengukuran |
| 9 | `hair2019multivariate` | Hair et al. (2019) | *Multivariate Data Analysis* | PDF | ~20–45 MB | Metodologi: Uji Kualitas Data & Komparasi MRA vs SEM |
| 10 | `ghozali2018aplikasi` | Ghozali (2018) | *Aplikasi Analisis Multivariate SPSS 25* | PDF (Scan Bab) | ~2–5 MB | Metodologi: Panduan Baku Uji SPSS Lokal Indonesia |
| 11 | `sugiyono2019metode` | Sugiyono (2019) | *Metode Penelitian Kuantitatif, Kualitatif, dan R&D* | PDF (Scan Bab) | ~2–5 MB | Metodologi: Purposive Sampling & Skala Likert Lokal |

---

## 3. Spesifikasi Fungsional & Kebutuhan Teknis

1. **Struktur Folder Baru:**
   - Folder dibuat di: `06_Referensi_Jurnal_PDF/03_Buku_Referensi_PDF/`
   - Sinkronisasi dengan penamaan folder sebelumnya (`01_Empiris_Utama_2021-2025/`, `02_Jurnal_Teori_&_Metodologi/`).
   - Setiap berkas PDF diberi nama terstandardisasi: `[Tahun]_[PenulisUtama]_[KataKunciJudul].pdf` (contoh: `2000_Shiller_Irrational_Exuberance.pdf`).

2. **Protokol Pengunduhan Multi-Cermin (*Multi-Mirror Fallback*):**
   - LibGen memiliki beberapa cermin dan server unduhan (`libgen.li/ads.php`, `libgen.rocks`, `annas-archive.org`, `library.lol`).
   - Skrip pengunduh harus menerapkan urutan cermin otomatis dengan penanganan kegagalan (*failover*) jika salah satu cermin mengalami *rate limit* atau 503.
   - Header HTTP wajib menyertakan User-Agent peramban desktop modern dan `Referer` yang sesuai.

3. **Verifikasi Integritas Biner (Binary Verification):**
   - Setiap berkas yang diunduh wajib lolos verifikasi tanda tangan biner: 4 byte pertama harus bernilai `%PDF` (`b'%PDF'`).
   - Batas ukuran minimal (*minimum threshold*): Berkas PDF harus berukuran $\ge 300\text{ KB}$ untuk memastikan berkas bukan laman galat HTML (*error landing page*).
   - Menghitung nilai hash SHA-256 dan ukuran berkas (*file size*) untuk dicatat ke dalam katalog.

4. **Katalog & Dokumentasi Terintegrasi:**
   - Membuat `06_Referensi_Jurnal_PDF/03_Buku_Referensi_PDF/README.md` yang memuat tabel katalog berkas, ukuran, hash, dan sitasi.
   - Memperbarui `06_Referensi_Jurnal_PDF/KATALOG_REFERENSI_JURNAL.md` (menambahkan Bagian 3: Buku Referensi).
   - Memperbarui `07_Review_&_Audit/Paper_Audits/audit_libgen_books_report.json` dengan status *DOWNLOADED* dan jalur berkas lokal.

---

## 4. Kriteria Keberhasilan (Acceptance Criteria)

- [ ] Folder baru `06_Referensi_Jurnal_PDF/03_Buku_Referensi_PDF/` terbentuk dengan rapi.
- [ ] Seluruh buku referensi internasional yang tersedia di LibGen berhasil diunduh dalam format PDF asli.
- [ ] 100% berkas PDF terverifikasi memiliki magic byte `%PDF` dan ukuran valid.
- [ ] Katalog referensi naskah (`KATALOG_REFERENSI_JURNAL.md`) dan README folder memetakan seluruh berkas dengan tautan aktif.
- [ ] Automated test suite (`verify_ukrida_compliance.py`, `verify_mendeley_integrity.py`, `verify_docx_typography.py`, `verify_pdf_docx_parity.py`) tetap lulus 100%.
- [ ] Seluruh perubahan di-commit dan di-push ke GitHub repository.

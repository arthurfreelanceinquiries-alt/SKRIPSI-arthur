# Product Requirements Document (PRD) — Sinkronisasi Penuh DOCX & Audit Paritas File
### *Naskah Proposal Tugas Akhir S1 Manajemen FEB UKRIDA — Pokémon TCG Impulsive Buying*

> [!SUMMARY] Tujuan & Solusi Dokumen Ini
> - **Untuk Apa:** Menjadi spesifikasi teknis dan acuan komprehensif untuk menyinkronkan dokumen Word (`Proposal_Arthur_NoBab3.docx` dan `Proposal_Arthur_PokemonTCG.docx`) agar 100% identik (*high-fidelity parity*) dengan naskah PDF master (`Proposal_Arthur_NoBab3.pdf` dan `Proposal_Arthur_PokemonTCG.pdf`).
> - **Masalah yang Diselesaikan:** Menghilangkan diskrepansi struktur cover, lembar formal yang bocor di naskah review, offset penomoran halaman romawi, urutan ucapan terima kasih kata pengantar, dan outline Daftar Isi lama di Word generator.
> - **Keputusan/Output:** Panduan eksekusi rekayasa skrip [[execution/build_proposal_word.py]], perbaikan jalur [[execution/sync_markdown_from_tex.py]], serta audit sinkronisasi lintas seluruh dokumen repositori.

---

## 1. Latar Belakang & Akar Masalah (Root Cause Analysis)

### 1.1 Temuan Desinkronisasi DOCX vs PDF
Dari hasil audit komparatif mendalam antara file master [[01_Naskah_Utama/Proposal_Arthur_NoBab3.pdf]] (33 halaman terkompilasi XeLaTeX) dan [[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]], ditemukan sejumlah ketidakselarasan krusial:
1. **Kebocoran 3 Lembar Formal:**
   - Pada PDF `NoBab3`, lembar *Pernyataan Keaslian*, *Persetujuan Proposal*, dan *Pengesahan Tim Penguji* telah dipotong bersih untuk keperluan review/bimbingan dosen tanpa lembar formal.
   - Pada DOCX `NoBab3`, ketiga lembar ini masih dibuat, menyebabkan naskah tidak mengalir langsung ke Kata Pengantar.
2. **Offset Penomoran Halaman Romawi (*Frontmatter*):**
   - PDF: Sampul (hal. i unnumbered) $\rightarrow$ Kata Pengantar (hal. ii–iii) $\rightarrow$ Abstrak (hal. iv) $\rightarrow$ Abstract (hal. v) $\rightarrow$ Daftar Isi (hal. vi–vii) $\rightarrow$ Daftar Tabel (hal. viii) $\rightarrow$ Daftar Gambar (hal. ix).
   - DOCX: Karena adanya 3 lembar pengesahan, Kata Pengantar bergeser ke hal. v dan Daftar Gambar ke hal. x.
3. **Outline Daftar Isi Usang (*Outdated Outline Mapping*):**
   - Pada generator DOCX [[execution/build_proposal_word.py]], list `toc_items_full` masih memuat subbab lama era sebelum revisi dosen:
     - `1.2 Identifikasi dan Perumusan Masalah`
     - `1.2.1 Identifikasi Masalah`
     - `1.2.2 Perumusan Masalah`
     - `1.5 Batasan Penelitian`
     - `1.6 Sistematika Penulisan Proposal`
     - Halaman `DAFTAR PUSTAKA: 49` (padahal naskah NoBab3 hanya ~25–30 halaman).
   - Di PDF, Bab 1 hanya memuat 4 subbab baku: `1.1 Latar Belakang`, `1.2 Perumusan Masalah` (3 butir per D15), `1.3 Tujuan Penelitian` (3 butir), dan `1.4 Manfaat Penelitian` (1.4.1 & 1.4.2). Subbab Batasan Penelitian telah dipindahkan ke Bab 3 (Subbab 3.1.1) sesuai D16.
4. **Urutan Apresiasi Kata Pengantar:**
   - PDF: Butir 1 memprioritaskan [[07_Review_&_Audit/Revisi_Dosen/|Dr. Fredella Colline]] selaku Dosen Pembimbing Skripsi, disusul Kaprodi, Tim Penguji, Dosen FEB, Orang Tua, Rekan Mahasiswa 2023, dan Komunitas Pokémon TCG (total 7 butir).
   - DOCX: Masih memuat daftar lama di mana Dekan berada di butir 1 dan Dosen Pembimbing di butir 3 (total 6 butir).
5. **Logo Cover:**
   - PDF: Menggunakan logo pentagram vektor resolusi tinggi (`ukrida_pentagram.pdf`).
   - DOCX: Masih mengimpor gambar raster bitmap lama (`Logo_UKRIDA_300x300.png`).

---

## 2. Peta Audit Sinkronisasi Seluruh File Repositori

| File / Komponen | Status Sinkronisasi | Masalah / Temuan | Tindakan Perbaikan |
|---|:---:|---|---|
| [[01_Naskah_Utama/Proposal_Arthur_NoBab3.pdf]] | 🟢 **SOURCE OF TRUTH** | 33 halaman, terkompilasi bersih tanpa Bab 3 dan tanpa lembar pengesahan formal. | Dijadikan tolok ukur utama (*golden reference*). |
| [[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]] | 🔴 **DESYNC** | Bocor 3 lembar formal, penomoran romawi offset, TOC memuat outline lama & hal. 49, logo bitmap lama. | Rekompilasi penuh via skrip generator yang telah dimutakhirkan. |
| [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf]] | 🟢 **SYNC** | 46–48 halaman, proposal lengkap (Bab 1–3, Draf Pustaka, 10 Jurnal Empiris). | Dipertahankan sebagai master PDF proposal lengkap. |
| [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]] | 🟡 **PARTIAL DESYNC** | Outline TOC di Word masih memuat subbab 1.2.1, 1.2.2, 1.5, 1.6 lama; Kata Pengantar belum memprioritaskan dosbim di urutan 1. | Sinkronkan TOC dan Kata Pengantar agar identik dengan TeX. |
| [[execution/sync_markdown_from_tex.py]] | 🔴 **BROKEN PATH** | Menggunakan `script_dir` yang mengasumsikan file ada di `execution/`, menyebabkan crash `FileNotFoundError`. | Perbaiki relative path ke `01_Naskah_Utama/`. |
| [[execution/build_proposal_word.py]] | 🔴 **LOGIC DESYNC** | Format hardcoded pada TOC, tidak memotong lembar formal di mode `--no-chapter3`, logo raster lama. | Refaktor modular untuk mendukung 2 mode (`full` dan `no-chapter3`) secara presisi. |
| [[01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md]] | 🟢 **SYNC** | Struktur Bab 1–3, 10 jurnal di Tabel 2.1, rumus MRA, dan instrumen sudah mutakhir. | Sinkronkan ulang via skrip setelah perbaikan jalur. |
| [[03_Draft_Per_Bab/]] (Bab 1, 2, 3, DP) | 🟢 **SYNC** | Heading dan isi terpisah per bab sudah selaras dengan keputusan D01–D19. | Pertahankan. |
| [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]] | 🟢 **SYNC** | Memuat keputusan terkunci D01–D19 dan 10 jurnal terverifikasi. | Rujukan parameter validasi. |
| [[04_Riset_&_Metodologi/LAPORAN_KOMPARASI_PDF_VS_DOCX.md]] | 🟡 **OUTDATED** | Masih mendokumentasikan kondisi perbandingan awal sebelum pemisahan varian NoBab3. | Perbarui laporan pasca-sinkronisasi. |

---

## 3. Spesifikasi Teknis Pemutakhiran DOCX Generator

### 3.1 Mode `skip_chapter3=True` (`Proposal_Arthur_NoBab3.docx`)
1. **Cover Page:**
   - Gunakan aset `01_Naskah_Utama/images/ukrida_pentagram.png` (resolusi tinggi hasil konversi vektor SVG/PDF).
   - Format judul, penulis, konsentrasi, dan institusi konsisten ISO A4.
2. **Eliminasi Lembar Formal:**
   - Lewati pembuatan *Pernyataan Keaslian*, *Persetujuan Proposal*, dan *Pengesahan Tim Penguji*.
3. **Penomoran Halaman Romawi (*Frontmatter*):**
   - Kata Pengantar dimulai tepat pada halaman **ii** (Footer: `Universitas Kristen Krida Wacana | ii`).
   - Abstrak Bahasa Indonesia pada halaman **iv**.
   - Abstract Bahasa Inggris pada halaman **v**.
   - Daftar Isi pada halaman **vi** & **vii**.
   - Daftar Tabel pada halaman **viii**.
   - Daftar Gambar pada halaman **ix**.
4. **Struktur Kata Pengantar Baru (7 Butir):**
   - Butir 1: Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A (Dosen Pembimbing Skripsi).
   - Butir 2: Rita Amelinda, S.E., M.M. (Ketua Program Studi S1 Manajemen).
   - Butir 3: Bapak/Ibu Dosen Penguji Seminar Proposal.
   - Butir 4: Seluruh Dosen dan Staf Pengajar FEB UKRIDA.
   - Butir 5: Kedua Orang Tua dan Keluarga Tercinta.
   - Butir 6: Rekan-rekan Mahasiswa Manajemen FEB UKRIDA Angkatan 2023.
   - Butir 7: Komunitas Kolektor dan Pemain Pokémon TCG di Indonesia.
5. **Daftar Isi (TOC) Presisi:**
   - Bab 1:
     - `1.1 Latar Belakang Penelitian` (hal. 1)
     - `1.2 Perumusan Masalah` (hal. 8)
     - `1.3 Tujuan Penelitian` (hal. 9)
     - `1.4 Manfaat Penelitian` (hal. 9)
       - `1.4.1 Manfaat Teoritis` (hal. 9)
       - `1.4.2 Manfaat Praktis` (hal. 10)
   - Bab 2:
     - `2.1 Landasan Teori` (hal. 11)
       - `2.1.1 Grand Theory: Keuangan Perilaku (Behavioral Finance)` (hal. 11)
       - `2.1.2 Supporting Theory: Teori Stimulus-Organism-Response (S-O-R)` (hal. 11)
       - `2.1.3 Supporting Theory: Psikologi Kolektor dan The "Completing the Set" Effect` (hal. 12)
       - `2.1.4 Supporting Theory: Teori Regulasi Diri (Self-Regulation Theory)` (hal. 12)
     - `2.2 Kajian Variabel Penelitian` (hal. 12)
       - `2.2.1 Variabel Dependen (Y): Impulsive Buying (Pembelian Impulsif)` (hal. 12)
       - `2.2.2 Variabel Independen (X1): Hedonic Motivation (Motivasi Hedonis)` (hal. 13)
       - `2.2.3 Variabel Independen (X2): Desire for Completeness (Hasrat Kelengkapan Koleksi)` (hal. 13)
       - `2.2.4 Variabel Independen (X3): Speculative Motive (Motif Spekulasi Finansial)` (hal. 13)
       - `2.2.5 Variabel Moderasi (M): Self-Control (Kontrol Diri)` (hal. 14)
     - `2.3 Penelitian Sebelumnya` (hal. 14)
     - `2.4 Pengembangan Hipotesis` (hal. 17)
       - `2.4.1 Pengaruh Hedonic Motivation terhadap Impulsive Buying` (hal. 17)
       - `2.4.2 Pengaruh Desire for Completeness terhadap Impulsive Buying` (hal. 17)
       - `2.4.3 Pengaruh Speculative Motive terhadap Impulsive Buying` (hal. 18)
       - `2.4.4 Pengaruh Moderasi Self-Control terhadap Hubungan Hedonic Motivation dan Impulsive Buying` (hal. 18)
       - `2.4.5 Pengaruh Moderasi Self-Control terhadap Hubungan Desire for Completeness dan Impulsive Buying` (hal. 19)
       - `2.4.6 Pengaruh Moderasi Self-Control terhadap Hubungan Speculative Motive dan Impulsive Buying` (hal. 19)
     - `2.5 Rerangka Penelitian` (hal. 20)
   - Daftar Pustaka (hal. 21)
6. **Daftar Tabel (LOT):**
   - Hanya memuat: `Tabel 2.1 Ringkasan Penelitian Sebelumnya` (hal. 14).
7. **Daftar Gambar (LOF):**
   - Memuat:
     - `Gambar 1.1 Peringkat 10 Waralaba Media Berpendapatan Tertinggi di Dunia Sepanjang Masa` (hal. 2)
     - `Gambar 1.2 Pertumbuhan Kumulatif Produksi Kartu Pokémon TCG Global Tahun 2019–2024` (hal. 3)
     - `Gambar 1.3 Estimasi Pangsa Pasar Industri Trading Card Game (TCG) Global Tahun 2024` (hal. 4)
     - `Gambar 2.1 Model Rerangka Konseptual Penelitian` (hal. 20)

### 3.2 Mode `skip_chapter3=False` (`Proposal_Arthur_PokemonTCG.docx`)
- Mempertahankan 3 lembar pengesahan formal.
- Menggunakan outline baru yang selaras di mana `Batasan Penelitian` berada di Bab 3 (Subbab 3.1.1).
- Menggunakan urutan Kata Pengantar 7 butir yang sama.
- Memperbarui halaman TOC, LOT, dan LOF secara akurat.

---

## 4. Kriteria Keberhasilan (*Acceptance Criteria*)

1. **Paritas Visual & Struktural:**
   - Struktur seksi `Proposal_Arthur_NoBab3.docx` 100% cocok dengan `Proposal_Arthur_NoBab3.pdf` (Cover $\rightarrow$ Kata Pengantar $\rightarrow$ Abstrak $\rightarrow$ Abstract $\rightarrow$ TOC $\rightarrow$ LOT $\rightarrow$ LOF $\rightarrow$ Bab 1 $\rightarrow$ Bab 2 $\rightarrow$ Daftar Pustaka).
2. **Nol Outdated Heading:**
   - Tidak ada lagi entri `1.2.1 Identifikasi Masalah`, `1.2.2 Perumusan Masalah`, `1.5 Batasan Penelitian`, atau `1.6 Sistematika Penulisan` di Daftar Isi Bab 1.
3. **Nomor Halaman Realistis & Akurat:**
   - Daftar Pustaka di DOCX `NoBab3` tidak lagi tertulis halaman 49, melainkan halaman sebenarnya (~21).
4. **Executable Script Integrity:**
   - Menjalankan `python execution/sync_markdown_from_tex.py` berhasil tanpa `FileNotFoundError`.
   - Menjalankan `python execution/build_proposal_word.py --no-chapter3` menghasilkan `Proposal_Arthur_NoBab3.docx` yang sinkron.
   - Menjalankan `python execution/build_proposal_word.py` menghasilkan `Proposal_Arthur_PokemonTCG.docx` yang sinkron.
5. **Verifikasi Otomatis:**
   - Skrip verifikasi memvalidasi bahwa seluruh heading dan metrik paritas bernilai TRUE.

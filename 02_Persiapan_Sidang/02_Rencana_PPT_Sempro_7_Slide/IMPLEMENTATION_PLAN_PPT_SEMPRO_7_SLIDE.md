# 🛠️ IMPLEMENTATION PLAN: Redesain Total Presentasi Sempro 7 Slide (Canva Human-Designed)

### *Rencana Eksekusi Teknis Pembaruan `index.html` — S1 Manajemen Keuangan FEB UKRIDA*

> [!SUMMARY] Tujuan & Solusi Dokumen Ini
> - **Untuk Apa:** Panduan rencana teknis (*Technical Implementation Plan*) langkah demi langkah untuk merombak berkas [`index.html`](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/02_Persiapan_Sidang/02_Rencana_PPT_Sempro_7_Slide/index.html) menjadi presentasi standar Canva editorial yang bersih, tidak bertumpuk, dan gambarnya jernih.
> - **Masalah yang Diselesaikan:** Mengatasi masalah gambar buram/terpotong, teks meluap di luar kanvas 16:9, kartu variabel yang terlalu sempit, serta logo bertumpuk kotak putih.
> - **Keluaran/Output:** Arsitektur CSS responsif 16:9 tanpa overflow, struktur markup HTML baru per slide, penggunaan aset logo transparan, dan protokol uji verifikasi.

---

## 📅 1. Tahapan Eksekusi Teknis (Phased Execution Workflow)

```
[Fase 1: Normalisasi Aset & Gambar] ──> [Fase 2: Arsitektur CSS Anti-Overflow]
                                                      │
[Fase 4: Verifikasi & Uji Responsif] <── [Fase 3: Rekonstruksi Slide 1 s.d. 7]
```

---

### 🔹 FASE 1: Normalisasi Aset Gambar & Resolusi Visual
* **Masalah:** Logo UKRIDA berlatar kotak putih pekat, gambar grafik resolusi 4000px diperkecil ekstrem ke 135px sehingga tidak terbaca dan pecah.
* **Tindakan Teknis:**
  1. **Substitusi Logo:** Ganti referensi `ukrida_pentagram.png` (non-transparan) dengan `Logo_UKRIDA_300x300.png` yang memiliki kanal transparansi alpha murni (`RGBA`) agar menyatu mulus di latar terang maupun gelap.
  2. **Proporsi Gambar 1.2 (Slide 2):** Alokasikan ruang vertikal minimal 220px dengan rasio aspek alami (~16:9 landscape) dan latar bingkai foto Canva putih bersih dengan border halus `#E2E8F0`.
  3. **Penyelamatan Gambar 1.3 (Slide 3):** Gambar disparitas harga PSA 10 (4000×2320 px) diperbesar ke container minimal lebar 280px dengan `object-fit: contain` dan padding proporsional sehingga nama kartu (*Pikachu, Charizard, Umbreon*) dan bar disparitasnya terbaca oleh penguji.

---

### 🔹 FASE 2: Arsitektur CSS & Sistem Desain Canva (Anti-Overflow)
* **Masalah:** Slide 16:9 mengalami overflow vertikal jika konten melebihi `56.25vw`.
* **Tindakan Teknis:**
  1. **Dynamic Viewport Clamping:**
     - Gunakan perhitungan fleksibel: `height: 100%; display: flex; flex-direction: column; justify-content: space-between;`.
     - Hindari tinggi statis yang kaku (`calc(100% - 94px)` digantikan oleh `flex: 1; min-height: 0;`).
  2. **Font Scaling Proporsional:**
     - Judul Utama: `1.4rem` – `1.55rem` (Outfit, bold 800).
     - Subjudul: `0.78rem` – `0.82rem` (Plus Jakarta Sans, regular).
     - Body Text: `0.72rem` – `0.76rem` dengan `line-height: 1.38`.
     - Angka Metrik: `1.3rem` – `1.6rem` (Outfit, bold 800).
  3. **Dual Theme Architecture:**
     - Default: **Canva Editorial Light** (Latar putih gading `#FAF9F6`, kartu putih `#FFFFFF`, teks navy gelap `#0F172A`).
     - Variant: **Canva Navy Executive** (`data-theme="dark"`, latar `#0F172A`, kartu `#1E293B`, teks putih `#F8FAFC`).

---

### 🔹 FASE 3: Rekonstruksi Markup HTML Slide-by-Slide

#### 1. Slide 1 (Cover Identitas)
- **Komposisi:** Split layout asimetris.
- **Kiri:** Logo transparan UKRIDA, Kicker "SEMINAR PROPOSAL TUGAS AKHIR (MODEL B)", Judul lengkap berhuruf tebal dengan highlight warna lembut, deskripsi ruang lingkup riset.
- **Kanan:** Kartu profil Canva berisi Peneliti (Arthur Reezan, NIM 312023002), Pembimbing (Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A), dan Forum Sidang FEB UKRIDA 2026.

#### 2. Slide 2 (Konteks Industri & Fenomena)
- **Komposisi:** Split 50% Kiri (Hero Visuals) + 50% Kanan (Context Points).
- **Kiri:** 2 Canva Metric Cards (`> US$ 100 Miliar` & `64,8 Miliar Kartu`) + Gambar 1.2 Produksi Kumulatif TCG yang jernih dan tajam.
- **Kanan:** 3 Kartu Berurutan (`01. Ritel Modern Indonesia`, `02. Mekanisme Blind Pack Gacha`, `03. Peluang Kartu Langka & Spekulasi`).

#### 3. Slide 3 (Masalah Penelitian & Research Gap)
- **Komposisi:** Split 45% Kiri (Kausalitas & Gambar 1.3) + 55% Kanan (Matriks Gap & Novelty).
- **Kiri:** Stepper 5 langkah kausalitas belanja impulsif + Gambar 1.3 Disparitas PSA 10 berukuran proporsional dengan catatan ilustrasi fenomena.
- **Kanan:** 3 Kartu Kesenjangan Empiris (Gap Hedonis, Gap Kelengkapan, Gap Spekulasi) + Banner Hijau Novelty Arthur.

#### 4. Slide 4 (Tinjauan Pustaka & 5 Variabel Baku)
- **Komposisi:** Banner Teori Horisontal (Atas) + 5 Kolom Variabel Ramping & Rapi (Bawah).
- **Atas:** Grand Theory *Behavioral Finance* & 3 Supporting Theories (S-O-R, Pseudo-Set, Regulasi Diri).
- **Bawah:** 5 Kartu Variabel ($Y, X_1, X_2, X_3, M$) dengan definisi 1 baris, 3 indikator esensial, dan nama skala ukur baku internasional (IBTS, Babin, Barasz, Keynes, BSCS).

#### 5. Slide 5 (Riset Terdahulu & Model MRA)
- **Komposisi:** Tabel Komparasi Empiris (Atas) + Split Model & Hipotesis (Bawah).
- **Atas:** Tabel 4 riset terdahulu dengan baris pastel selang-seling.
- **Bawah:** Diagram jalur SVG bergaya Canva Flowchart yang tebal dan anggun + 6 Hipotesis bernomor tegas + Persamaan Model MRA 2-Tahap.

#### 6. Slide 6 (Metodologi Penelitian)
- **Komposisi:** 4 Kuadran Eksekutif Bersih (Grid 2×2).
- **Isi:** 1. Desain Riset, 2. Populasi & Sampel Green $N \ge 111$ (Target 120–150 + Pilot 30), 3. Kualitas Data & Asumsi Klasik (tanpa autokorelasi), 4. Analisis Data MRA OLS dengan **penegasan mutlak Mean-Centering**.

#### 7. Slide 7 (Penutup & Tanya Jawab)
- **Komposisi:** 2 Kartu Kontribusi (Atas) + Podium Penutup & Status Q&A (Bawah).
- **Isi:** Kontribusi Teoretis, Kontribusi Praktis, serta apresiasi formal kepada pembimbing dan dewan penguji.

---

### 🔹 FASE 4: Verifikasi & Kontrol Kualitas (Acceptance Testing)

Sebelum pekerjaan dinyatakan selesai, verifikasi 5 poin wajib dilakukan:
1. **Uji Resolusi & Overflow:** Buka `index.html` pada layar 16:9, pastikan 0 scrollbar vertikal pada setiap slide (Slide 1–7).
2. **Uji Keterbacaan Gambar:** Pastikan teks pada Gambar 1.2 dan Gambar 1.3 dapat terbaca tanpa buram.
3. **Uji Transparansi Logo:** Pastikan logo UKRIDA tidak memiliki kotak putih di sekitarnya pada tema terang maupun gelap.
4. **Uji Naskah Bicara (Speaker Notes):** Tekan tombol `N`, pastikan naskah bicara per slide tampil lengkap dan persis sama dengan [`ALUR_PRESENTASI_7_SLIDE_DETAIL.md`](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/02_Persiapan_Sidang/02_Rencana_PPT_Sempro_7_Slide/ALUR_PRESENTASI_7_SLIDE_DETAIL.md).
5. **Uji Navigasi:** Pastikan tombol panah keyboard (Kiri, Kanan, Spasi) dan toggle tema (`🌓`) berfungsi mulus.

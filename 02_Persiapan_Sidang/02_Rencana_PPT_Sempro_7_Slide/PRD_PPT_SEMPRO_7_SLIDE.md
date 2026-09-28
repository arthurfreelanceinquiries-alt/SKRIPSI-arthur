# 📋 PRODUCT REQUIREMENTS DOCUMENT (PRD) — AUDIT & REDESAIN TOTAL SLIDE SEMPRO 7 SLIDE

### *Transformasi Presentasi Seminar Proposal Arthur Reezan (FEB UKRIDA) Menjadi Standar Canva Editorial Human-Designed*

> [!SUMMARY] Ringkasan Eksekutif PRD Ini
> - **Untuk Apa:** Dokumen persyaratan produk (PRD) mutlak untuk memandu redesain total presentasi Seminar Proposal 7 slide (`index.html`) yang sebelumnya dinilai berantakan dan gambarnya jelek/buram.
> - **Masalah yang Dipecahkan:** Mengeliminasi elemen bertumpuk (*layout overflow*), kartu sempit yang sesak teks, gambar grafik resolusi tinggi yang terkompresi menjadi prangko kecil tak terbaca, serta logo berlatar kotak putih pekat.
> - **Keluaran/Output:** Spesifikasi visual Canva editorial human-crafted (bukan bot AI), tata letak proporsional 16:9 anti-tumpuk, integrasi bukti empiris beresolusi tinggi yang tajam, dan pemetaan naskah bicara 100% selaras alur sidang.

---

## 🔍 1. Hasil Audit Menyeluruh (Slide-by-Slide Audit Findings)

Berdasarkan audit teknis dan visual terhadap `index.html` yang aktif:

| No | Slide | Temuan Masalah Visual & Gambar | Evaluasi Keselarasan Alur | Kebutuhan Solusi Desain Canva |
|:---:|:---|:---|:---|:---|
| **1** | **Slide 1: Cover** | Logo UKRIDA menggunakan `ukrida_pentagram.png` (RGB, non-transparan) yang memunculkan kotak putih persegi di sekeliling logo. Layout terbagi 2 kolom kaku dengan border tajam. | **100% Selaras** (Identitas Arthur, Dr. Fredella Colline, FEB UKRIDA, konsentrasi Keuangan). | Ganti logo ke `Logo_UKRIDA_300x300.png` (transparan RGBA) atau SVG. Terapkan gaya cover majalah editorial Canva dengan aksen pita warna institusional dan tipografi berbobot. |
| **2** | **Slide 2: Fenomena Pasar** | Dua grafik raksasa (Gambar 1.1 Statista & Gambar 1.2 Produksi) dipaksakan berjejer mini di bawah dua kartu angka, terkompresi hingga tinggi <140px. Akibatnya teks grafik Statista menjadi buram seperti cacing. | **100% Selaras** (Valuasi >$100M, produksi 28,8M ➔ 64,8M, ritel modern Indonesia, blind pack). | Reorganisasi tata letak: Jadikan Gambar 1.2 sebagai **Hero Visual** besar dan jernih di sisi kiri (tinggi ~220px). Tampilkan metrik Statista sebagai kartu angka pahlawan besar (Canva stat card) tanpa memaksakan gambar Statista yang sempit. |
| **3** | **Slide 3: Masalah & Gap** | Gambar 1.3 (Disparitas Harga PSA 10 berukuran asli 4000×2320 px) diperkecil secara paksa ke ukuran CSS `135px × 90px`. Grafik batang horizontal menjadi tidak terbaca sama sekali dan tampak rusak/jelek. Di kanan, 3 kartu gap berdesakan dengan novelty banner. | **100% Selaras** (Alur kausalitas gacha ➔ impulsif, ilustrasi pasar sekunder PSA 10, 3 gap literatur, novelty). | Berikan ruang horizontal yang layak untuk Gambar 1.3 (minimal lebar 260–280px) dengan rasio aspek terjaga. Format alur kausalitas dengan stepper Canva yang bersih, dan sederhanakan kartu gap menjadi 3 baris elegan bergaris aksen. |
| **4** | **Slide 4: Teori & Variabel** | Membagi 5 kolom variabel secara sejajar dalam satu baris membuat lebar tiap kartu hanya ~180px. Teks 4 butir indikator per variabel bertumpuk 8 baris dan meluap ke bawah memotong batas slide (*overflow*). | **100% Selaras** (Grand Theory Behavioral Finance, S-O-R, Pseudo-Set, Regulasi Diri; 5 variabel Y, X1, X2, X3, M). | Ubah layout kartu variabel menjadi grid proporsional yang bernapas lega, atau 5 kartu vertikal yang hanya memuat nama, esensi definisi 1 kalimat, dan skala ukur baku. Pindahkan detail rincian indikator ke tooltip/hover atau bullet ringkas 2 baris. |
| **5** | **Slide 5: Model & Hipotesis** | Tabel literatur di atas menekan diagram alur model di bawah. Diagram SVG digambar kaku seperti flowchart programmer dengan garis tipis kusam, dan 6 butir hipotesis berdesakan di sampingnya. | **100% Selaras** (4 rujukan empiris, model jalur MRA, 6 hipotesis terarah, persamaan Model 1 & 2). | Gunakan diagram jalur Canva yang tebal, jelas, bergradasi anggun dengan panah kontras. Tabel riset terdahulu dibuat bersih dengan warna latar lembut berselang-seling khas Canva. |
| **6** | **Slide 6: Metodologi** | Grid 2×2 dijejali teks teknis yang terlalu padat (banyak paragraf penuh), menyerupai halaman naskah Word yang dipindahkan ke kotak slide, bukan slide presentasi lisan. | **100% Selaras** (Purposive, WNI ≥17th, formula Green N≥111, Target 120–150 + Pilot 30, Mean-Centering, MRA OLS, tanpa autokorelasi). | Terapkan teknik *Canva Visual Chunking*: 4 kuadran bersih dengan ikon lembut, poin kunci 1 baris berhuruf tebal, badge angka formula Green, dan kotak penegasan Mean-Centering yang menonjol. |
| **7** | **Slide 7: Penutup & Q&A** | Dua kartu kontribusi dan kartu penutup terlihat generik dan kosong di bagian tengah, kurang memberikan kesan akhir yang memukau bagi dewan penguji. | **100% Selaras** (Kontribusi teoretis, kontribusi praktis, terima kasih, pembukaan forum Q&A). | Buat penutup bergaya Canva Executive: 2 kartu kontribusi bernilai tinggi dengan ilustrasi lencana akademis, dipadukan dengan podium penutup yang hangat dan percaya diri. |

---

## 🎯 2. Tujuan & Sasaran Produk (Goals & Acceptance Criteria)

### A. Sasaran Desain Visual (Canva Human-Designed Aesthetic)
1. **Zero Layout Overflow:** Tidak boleh ada teks, gambar, atau kartu yang terpotong atau keluar dari batas kanvas slide 16:9 pada resolusi layar apa pun.
2. **Crystal-Clear Visuals (Gambar Tajam & Terbaca):**
   - Logo universitas wajib transparan (bebas latar putih persegi).
   - Grafik empiris (Gambar 1.2 dan Gambar 1.3) wajib ditampilkan dengan ukuran yang proporsional sehingga sumbu, label kartu, dan batangnya terbaca jelas oleh mata penguji.
3. **Tipografi Editorial Canva:** Paduan font *Outfit* (bold untuk judul) dan *Plus Jakarta Sans* (elegan dan nyaman dibaca untuk teks). Bebas dari font monospace programmer di badan teks slide.
4. **Palet Warna Harmonis & Humanis:**
   - Latar: Pilihan Default **Canva Editorial Light** (`#FAF9F6` / Putih Gading Bersih) dengan bayangan lembut, serta opsi **Canva Navy Executive** (`#0F172A`) via toggle instan.
   - Aksen: Royal Navy (`#0F2642`), Warm Amber/Gold UKRIDA (`#D97706`), Ice Blue (`#0284C7`), Emerald (`#059669`), dan Rose (`#E11D48`).

### B. Sasaran Keselarasan Alur Ilmiah (Academic Alignment)
1. **Kesesuaian 100% Alur 7 Slide:** Wajib mematuhi urutan:
   - Slide 1: Identitas & Pembuka
   - Slide 2: Konteks Industri & Fenomena Pasar
   - Slide 3: Masalah Penelitian & Research Gap
   - Slide 4: Landasan Teori & 5 Variabel Baku
   - Slide 5: Riset Terdahulu, Model MRA & 6 Hipotesis
   - Slide 6: Rancangan Metodologi & Analisis Data (Mean-Centering)
   - Slide 7: Kontribusi Penelitian & Sesi Diskusi
2. **Kesesuaian Naskah Bicara (*Speaker Notes*):** Drawer catatan narasi (tombol `N`) wajib menyajikan naskah kata-per-kata yang persis sama dengan dokumen panduan [`ALUR_PRESENTASI_7_SLIDE_DETAIL.md`](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/02_Persiapan_Sidang/02_Rencana_PPT_Sempro_7_Slide/ALUR_PRESENTASI_7_SLIDE_DETAIL.md).

---

## 📐 3. Spesifikasi Arsitektur Tata Letak Baru (Per Slide)

### 🔹 Slide 1 — Cover
- **Struktur:** Canva Asymmetrical Hero Banner.
- **Elemen:**
  - Header: Logo UKRIDA transparan + Teks Institusi.
  - Judul: 3 baris bold kontras tinggi dengan penekanan warna lembut pada variabel $X$, $Y$, dan $M$.
  - Kartu Metadata: Mahasiswa (Arthur Reezan, NIM 312023002), Pembimbing (Dr. Fredella Colline lengkap dengan seluruh gelar), Forum (Seminar Proposal S1 Manajemen Keuangan 2026).

### 🔹 Slide 2 — Konteks Industri & Fenomena
- **Struktur:** 50% Visual Exhibit (Kiri) + 50% Poin Fenomena (Kanan).
- **Elemen:**
  - Kiri: 2 Kartu Metrik Pahlawan (`> US$ 100 Miliar` & `64,8 Miliar Kartu`) + Gambar 1.2 (Grafik Pertumbuhan Kumulatif Produksi TCG) berukuran besar dan tajam di dalam bingkai foto Canva.
  - Kanan: 3 Kartu Berurutan (`01 Ritel Modern Indonesia`, `02 Mekanisme Blind Pack Gacha`, `03 Asimetri Nilai & Spekulasi Kartu Langka`).

### 🔹 Slide 3 — Masalah Penelitian & Research Gap
- **Struktur:** 45% Kausalitas & Bukti (Kiri) + 55% Matriks Gap & Novelty (Kanan).
- **Elemen:**
  - Kiri: Alur Stepper 5 Tahap Kausalitas Masalah + Gambar 1.3 (Disparitas Harga PSA 10) dengan lebar proporsional (~280px) berlabel disclaimer jelas.
  - Kanan: 3 Kartu Kesenjangan Empiris (Gap Hedonis Pranggabayu vs Apidana; Gap Kelengkapan Barasz 2017; Gap Spekulasi Aryadi vs Colline 2024) + Kotak Hijau Kebaruan (*Novelty* Arthur).

### 🔹 Slide 4 — Tinjauan Pustaka & 5 Variabel Baku
- **Struktur:** Banner Teori Horisontal (Atas) + 5 Kartu Variabel Ringkas (Bawah).
- **Elemen:**
  - Atas: Grand Theory *Behavioral Finance* & 3 Supporting Theories (S-O-R, Pseudo-Set, Regulasi Diri).
  - Bawah: 5 Kartu Variabel ($Y, X_1, X_2, X_3, M$) dengan tata letak lapang, memuat definisi 1 kalimat padat, indikator esensial, dan nama skala ukur baku internasional (IBTS, Babin, Barasz, Keynes, BSCS).

### 🔹 Slide 5 — Riset Terdahulu, Model MRA & 6 Hipotesis
- **Struktur:** Tabel Komparasi Empiris (Atas) + Split Model & Hipotesis (Bawah).
- **Elemen:**
  - Atas: Tabel 4 rujukan empiris kunci dengan baris selang-seling warna lembut.
  - Bawah Kiri: Diagram jalur MRA bergaya Canva Flowchart (garis tebal, node lembut, panah interaksi putus-putus yang anggun).
  - Bawah Kanan: 6 Hipotesis bernomor tegas + Formula Persamaan MRA Model 2.

### 🔹 Slide 6 — Metodologi Penelitian & Ekonometrika
- **Struktur:** 4 Kuadran Eksekutif Seimbang (Grid 2×2).
- **Elemen:**
  - Kuadran 1: Desain Kuantitatif Asosiatif, Cross-Sectional, Likert 5 Poin, Skor Komposit.
  - Kuadran 2: Populasi Tak Terbatas, Purposive Sampling, Kaidah Green $N \ge 111$, Target 120–150 + Pilot 30.
  - Kuadran 3: Uji Instrumen (Pearson & Alpha $\ge 0,70$), Asumsi Klasik (KS, VIF, Glejser), Bebas Autokorelasi.
  - Kuadran 4: Ekonometrika MRA OLS, **Highlight Mutlak Mean-Centering**, Uji t, Uji F, $\Delta R^2$, Simple Slopes.

### 🔹 Slide 7 — Penutup & Sesi Q&A
- **Struktur:** 2 Kartu Kontribusi (Atas) + Podium Penutup & Forum Q&A (Bawah).
- **Elemen:**
  - Atas: Kontribusi Teoretis (*Behavioral Finance* komoditas hobi fisik) & Kontribusi Praktis (Edukasi proteksi finansial kolektor muda).
  - Bawah: Banner Penutup Formal dengan apresiasi kepada pembimbing dan dewan penguji, pill status Q&A Dibuka.

---

## 🛡️ 4. Batasan & Larangan (Guardrails)
1. **Dilarang memasukkan maskot kartun Pokémon.** Pertahankan citra akademis perguruan tinggi.
2. **Dilarang memperkecil gambar grafik secara berlebihan.** Gambar harus dapat dibaca atau didukung teks metrik pahlawan yang mewakilinya.
3. **Dilarang membuat teks meluap (*no overflow*).** Ketinggian setiap komponen harus dihitung secara fleksibel di dalam rasio 16:9.
4. **Dilarang mengubah parameter ilmiah skripsi** (X1, X2, X3, M, Y, 6 hipotesis, kaidah sampel Green, nama pembimbing).

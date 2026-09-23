# 📋 PRD: Pembuatan Slide Deck Seminar Proposal (Sempro) Ringkas 7 Slide
### *Skripsi S1 Manajemen Keuangan — FEB Universitas Kristen Krida Wacana (UKRIDA)*

> [!SUMMARY] Tujuan & Solusi Dokumen Ini
> - **Untuk Apa:** *Product Requirements Document* (PRD) komprehensif sebagai spesifikasi mutlak (*source of truth*) untuk diserahkan kepada AI lain (Claude, ChatGPT, Gamma, Cursor, PPTAgent, dll.) dalam men-generate slide deck presentasi Seminar Proposal 7 slide.
> - **Masalah yang Diselesaikan:** Mencegah AI menghasilkan slide dengan teks bertele-tele (*wall of text*), jumlah slide melar, salah variabel/teori, atau desain kuno; menjamin 100% kepatuhan pada arahan dosen pembimbing ([[07_Review_&_Audit/Revisi_Dosen/|Dr. Fredella Colline]]).
> - **Keputusan/Output:** Spesifikasi desain, konstelasi data ilmiah, struktur slide 1 s.d. 7, dan parameter teknis yang siap dieksekusi oleh sistem/AI perancang presentasi.

---

## 🎯 1. Ringkasan Eksekutif & Tujuan Produk

* **Pengguna Utama:** Arthur Reezan (NIM: 312023002) — Mahasiswa S1 Manajemen FEB UKRIDA.
* **Audiens Sasaran:** Dewan Penguji Seminar Proposal dan Dosen Pembimbing ([[07_Review_&_Audit/Revisi_Dosen/|Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A]]).
* **Alokasi Waktu Sidang:** 7 – 10 menit presentasi verbal (~1 hingga 1,5 menit per slide) + 20 menit tanya jawab.
* **Target Output:** 1 deck presentasi (format `.pptx` atau HTML slide deck interaktif) yang memuat **TEPAT 7 SLIDE**, memiliki keterbacaan tinggi, visual modern (FinTech Executive / Dark Mode), dan padat data.

---

## 🏛️ 2. Parameter Kunci Skripsi (Source of Truth Mutlak)

AI penerima dokumen ini **DILARANG KERAS** mengubah parameter riset di bawah ini:

| Parameter | Data Ilmiah Resmi |
|---|---|
| **Judul Skripsi** | *Pengaruh Hedonic Motivation ($X_1$), Desire for Completeness ($X_2$), dan Speculative Motive ($X_3$) terhadap Impulsive Buying ($Y$) Booster Pack Kartu Pokémon TCG dengan Self-Control ($Z$) sebagai Variabel Moderasi* |
| **Peneliti** | Arthur Reezan (NIM: 312023002) |
| **Dosen Pembimbing** | Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A |
| **Institusi** | Program Studi S1 Manajemen, Fakultas Ekonomi dan Bisnis, Universitas Kristen Krida Wacana (UKRIDA), Jakarta (2026) |
| **Variabel Dependen ($Y$)** | *Impulsive Buying* (Skala IBTS, Verplanken & Herabadi, 2001; Rook, 1987) |
| **Variabel Independen 1 ($X_1$)** | *Hedonic Motivation* (Arnold & Reynolds, 2003; Babin et al., 1994) |
| **Variabel Independen 2 ($X_2$)** | *Desire for Completeness* (Pseudo-Set Framing: Barasz et al., 2017; Gao, 2014) |
| **Variabel Independen 3 ($X_3$)** | *Speculative Motive* (Behavioral Finance: Shiller, 2000; Keynes, 1936; PSA 10 Arbitrage) |
| **Variabel Moderasi ($Z$)** | *Self-Control* (Brief Self-Control Scale / BSCS: Tangney et al., 2004; Baumeister, 2002) |
| **Pendekatan Metodologi** | Kuantitatif Asosiatif Kausal, Survei Kuesioner (Skala Likert 1–5) |
| **Populasi & Sampel** | Kolektor WNI Pokémon TCG, *Purposive Sampling*, target $N = 120$–$150$ responden (Usia $\ge 17$ tahun, beli booster pack fisik min. 1× dalam 12 bulan terakhir, diutamakan 6 bulan; pilot test $n = 30$) |
| **Alat Analisis Data** | *Moderated Regression Analysis (MRA)* dengan teknik *Mean-Centering* |

---

## 🎨 3. Prinsip Desain & Visual Guidelines

1. **Gaya Visual:** *FinTech Dark Mode* atau *Clean Modern Executive*.
   - Background Utama: Dark Slate / Navy Blue (`#0B0F19` atau `#0F172A`).
   - Warna Kartu Kontainer: Deep Slate (`#1E293B` dengan border halus `#334155`).
   - Teks Utama: Pure White (`#F8FAFC`) dan Teks Sekunder: Cool Grey (`#94A3B8`).
   - Aksen Warna (Penegas Kategori):
     - Cyan / Electric Blue (`#06B6D4` / `#38BDF8`): Variabel Independen ($X$) & Data.
     - Emerald Green (`#10B981`): Variabel Dependen ($Y$) & Hipotesis Positif.
     - Purple / Violet (`#8B5CF6`): Variabel Moderasi ($Z$).
     - Amber / Gold (`#F59E0B`): Fenomena Industri & Nilai Pasar.
2. **Struktur Layout Berbasis Kartu (*Card-Based Grid*):**
   - Dilarang membuat paragraf panjang.
   - Gunakan layout grid 2 atau 3 kolom berupa *cards/containers* dengan ikon, angka sorotan (*callout numbers*), dan teks ringkas (maksimal 2–3 baris per kartu).
3. **Tipografi:** Sans-serif modern berbobot kontras (Inter, Montserrat, Plus Jakarta Sans, atau Roboto). Ukuran heading 24–32 pt, sub-heading 18–20 pt, body 13–16 pt.

---

## 📑 4. Spesifikasi Fungsional Slide-by-Slide (7 Slide)

### 🔹 SLIDE 1: Pembuka & Identitas Riset
* **Tujuan:** Menampilkan citra akademis yang profesional, percaya diri, dan jelas.
* **Komponen Slide:**
  - Label Kategori: `PROPOSAL SKRIPSI S1 MANAJEMEN KEUANGAN`
  - Judul Lengkap (Bold, kontras tinggi): *Pengaruh Hedonic Motivation, Desire for Completeness, dan Speculative Motive terhadap Impulsive Buying Booster Pack Kartu Pokémon TCG dengan Self-Control sebagai Variabel Moderasi*
  - Badge Identitas Mahasiswa: **Arthur Reezan — NIM: 312023002**
  - Badge Dosen Pembimbing: **Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A**
  - Footer: Fakultas Ekonomi dan Bisnis, Universitas Kristen Krida Wacana, Jakarta 2026.
* **Catatan Presenter (*Speaker Notes*):** Salam pembuka resmi, perkenalkan diri, sebutkan judul skripsi dan nama dosen pembimbing dalam tempo tenang dan tegas (durasi: 40–45 detik).

---

### 🔹 SLIDE 2: Latar Belakang — Konteks Industri & Fenomena Masalah
* **Tujuan:** Memaparkan fenomena pasar dan urgensi masalah perilaku belanja irasional pada produk Pokémon TCG.
* **Layout:** 3 Kartu Horisontal / Vertikal Grid:
  - **Kartu 1 — Ledakan Industri Pokémon TCG:**
    - Metrik Sorotan: **> 64,8 Miliar Kartu** terjual global (The Pokémon Company, 2024).
    - Poin: Pergeseran dari sekadar permainan anak menjadi komoditas koleksi dan investasi bernilai tinggi; penetrasi pasar Indonesia pesat pasca rilis kartu berbahasa Indonesia (2019).
  - **Kartu 2 — Mekanisme Gacha / Blind-Box:**
    - Poin: Sistem *probabilistic reward* (ketidakpastian isi kartu). Konsumen membeli peluang acak demi sensasi dopamin, *near-miss effect*, dan perburuan kartu langka (*secret rare*).
  - **Kartu 3 — Masalah Finansial (Impulsive Buying):**
    - Poin: Konsumen melakukan pembelian spontan (*unplanned, spur-of-the-moment*), berulang, dan emosional; berpotensi mengorbankan alokasi keuangan pribadi. (JANGAN klaim dana darurat/paylater — tidak ada di naskah!)
* **Catatan Presenter (*Speaker Notes*):** Jelaskan bahwa Pokémon TCG bukan sekadar mainan melainkan komoditas bernilai tinggi dengan sistem pembelian blind-box/gacha yang memicu fenomena impulsive buying yang merugikan keuangan kolektor (durasi: 1,5 menit).

---

### 🔹 SLIDE 3: Latar Belakang — Research Gap & Kebaruan (*Novelty*)
* **Tujuan:** Membuktikan ada kesenjangan empiris dan kebaruan teoritis yang memvalidasi mengapa riset ini layak disidangkan.
* **Layout:** Split 2 Bagian (Kiri: Matriks Gap Empiris; Kanan: Kartu Novelty Riset Arthur):
  - **Kiri — Kesenjangan Temuan Terdahulu (Research Gap):**
    - *Gap $X_1$ (Hedonis):* Pranggabayu (2022) menemukan pengaruh positif, namun Apidana (2022) menemukan pada produk hobi bernilai mahal, rasionalitas utilitas tetap dominan.
    - *Gap $X_2$ (Kelengkapan):* Barasz et al. (2017) menemukan efek psikologis *pseudo-set framing*, namun belum diuji empiris pada produk fisik kartu koleksi di Indonesia.
    - *Gap $X_3$ (Spekulasi):* Aryadi & Lingga (2024) mencatat arbitrase grading PSA 10 memicu FOMO, sementara Colline (2024) menemukan investor rasional cenderung berhati-hati.
  - **Kanan — Kebaruan Penelitian (*Novelty* Arthur):**
    - Mengintegrasikan faktor psikologi kolektor ($X_2$) dan motif spekulasi finansial ($X_3$).
    - Menghadirkan **Self-Control ($Z$) sebagai Variabel Moderasi** untuk menguji apakah pengendalian diri mampu meredam belanja impulsif kartu berisiko acak.
* **Catatan Presenter (*Speaker Notes*):** Tekankan pertentangan hasil penelitian terdahulu dan tunjukkan bahwa kebaruan penelitian ini terletak pada pemaduan psikologi kolektor, motif pasar sekunder, serta peran moderasi Self-Control (durasi: 1,5 menit).

---

### 🔹 SLIDE 4: Tinjauan Pustaka — Landasan Teori & Konstelasi Variabel
* **Tujuan:** Memperlihatkan rigor teoritis dan operasionalisasi variabel berbasis instrumen baku.
* **Layout:** 2 Blok (Atas: Teori Rujukan; Bawah: 5 Kartu Variabel):
  - **Blok Teori:**
    - *Grand Theory:* **Behavioral Finance** (Simon, 1955; Kahneman & Tversky, 1979; Shiller, 2000; Thaler & Shefrin, 1981) — Bias psikologis dalam keputusan keuangan.
    - *Supporting Theories:* Teori Stimulus-Organism-Response / S-O-R (Mehrabian & Russell, 1974), Pseudo-Set Framing (Barasz et al., 2017), Teori Regulasi Diri (Baumeister, 2002).
  - **Blok Variabel:**
    - **$Y$ (Impulsive Buying):** Pembelian spontan tanpa evaluasi konsekuensi (Skala IBTS, Verplanken & Herabadi, 2001).
    - **$X_1$ (Hedonic Motivation):** Kesenangan, hiburan, dan pelarian stres (Arnold & Reynolds, 2003).
    - **$X_2$ (Desire for Completeness):** Hasrat melengkapi nomor urut master set (Barasz et al., 2017).
    - **$X_3$ (Speculative Motive):** Ekspektasi keuntungan finansial pasar sekunder (Keynes, 1936; Shiller, 2000).
    - **$Z$ (Self-Control / Moderasi):** Kapasitas menahan dorongan sesaat (BSCS, Tangney et al., 2004).
* **Catatan Presenter (*Speaker Notes*):** Uraikan hubungan antara grand theory keuangan perilaku dengan variabel yang diteliti serta sebutkan skala baku internasional yang digunakan (durasi: 1,5 menit).

---

### 🔹 SLIDE 5: Model Penelitian & Perumusan Hipotesis
* **Tujuan:** Menampilkan visualisasi konseptual model MRA dan 6 hipotesis operasional secara kristal (TEPAT 6 — dilarang H7).
* **Layout:** Kiri Diagram Model Jalur (Path Model), Kanan Daftar 6 Hipotesis (sinkron naskah Bab 1–2: H1–H6; koreksi 23 Sep 2026 — tidak ada H7):
  - **Diagram Model Jalur:**
    - Panah Langsung: $X_1, X_2, X_3 \rightarrow Y$ ($+$)
    - Panah Moderasi Interaksi: $X_1 \cdot Z, X_2 \cdot Z, X_3 \cdot Z \rightarrow Y$ (Meredam / $-$)
  - **6 Hipotesis Riset:**
    - **$H_1$:** Hedonic Motivation berpengaruh positif terhadap Impulsive Buying.
    - **$H_2$:** Desire for Completeness berpengaruh positif terhadap Impulsive Buying.
    - **$H_3$:** Speculative Motive berpengaruh positif terhadap Impulsive Buying.
    - **$H_4$:** Self-Control memoderasi (meredam) pengaruh Hedonic Motivation terhadap Impulsive Buying.
    - **$H_5$:** Self-Control memoderasi (meredam) pengaruh Desire for Completeness terhadap Impulsive Buying.
    - **$H_6$:** Self-Control memoderasi (meredam) pengaruh Speculative Motive terhadap Impulsive Buying.
* **Catatan Presenter (*Speaker Notes*):** Tunjukkan diagram model, jelaskan 3 pengaruh anteseden dan 3 efek moderasi yang dihipotesiskan memperlemah/meredam impulsivitas (durasi: 1,5 menit).

---

### 🔹 SLIDE 6: Metode Penelitian, Sampel & Analisis Data
* **Tujuan:** Menegaskan kelayakan pelaksanaan riset dan ketepatan metode statistik MRA.
* **Layout:** Grid 4 Kuadran / 4 Kartu Pilar Metodologi:
  - **Kuadran 1 — Desain & Pengukuran:**
    - Kuantitatif Asosiatif Kausal; Survei Kuesioner Daring (Google Forms).
    - Skala Likert 5 Poin (1 = Sangat Tidak Setuju s.d. 5 = Sangat Setuju).
  - **Kuadran 2 — Populasi & Sampling:**
    - Kolektor WNI, populasi infinite; *Purposive Sampling* target $N = 120$–$150$ responden (+ pilot test $n = 30$).
    - Kriteria: WNI domisili Indonesia, Usia $\ge 17$ tahun, beli booster pack fisik min. 1× dalam 12 bulan terakhir (diutamakan 6 bulan).
  - **Kuadran 3 — Uji Kualitas Data & Asumsi Klasik:**
    - Validitas Pearson ($r_{\text{hitung}} > r_{\text{tabel}}$) & Reliabilitas Cronbach's Alpha ($\alpha \ge 0,70$).
    - Uji Asumsi Klasik: Normalitas (Kolmogorov-Smirnov), Multikolinearitas (VIF < 10, Tolerance > 0,10), Heteroskedastisitas (Glejser).
  - **Kuadran 4 — Analisis Data & Pengujian Hipotesis:**
    - *Moderated Regression Analysis (MRA)* dengan teknik **Mean-Centering** untuk variabel prediktor dan moderator (mencegah multikolinearitas struktural).
    - Uji $t$ (parsial), Uji $F$ (simultan), Koefisien Determinasi ($R^2$ dan $\Delta R^2$).
* **Catatan Presenter (*Speaker Notes*):** Jelaskan purposive sampling, sampel $\ge 150$, instrumen valid & reliabel, serta ketepatan MRA dengan mean-centering (durasi: 1,5 menit).

---

### 🔹 SLIDE 7: Penutup & Sesi Tanya Jawab
* **Tujuan:** Menutup presentasi dengan profesional dan elegan, membuka forum diskusi penguji.
* **Komponen Slide:**
  - Header: `RINGKASAN & KONTRIBUSI RISET`
  - Kontribusi Teoretis: Memperkaya literatur *Behavioral Finance* pada produk alternatif/hobi bernilai koleksi.
  - Kontribusi Praktis: Menjadi acuan edukasi literasi keuangan dan pengendalian diri bagi generasi muda.
  - Callout Utama: **"Sekian Presentasi Usulan Proposal Skripsi. Terima Kasih atas Perhatian Dewan Penguji."**
  - Sub-callout: **Sesi Tanya Jawab (Q&A) Dibuka.**
  - Identitas Kontak: Arthur Reezan | Program Studi S1 Manajemen FEB UKRIDA.
* **Catatan Presenter (*Speaker Notes*):** Ucapkan terima kasih secara santun dan tegas, lalu serahkan waktu kembali kepada Ketua Sidang (durasi: 30 detik).

---

## ✅ 5. Kriteria Keberhasilan (*Acceptance Criteria*) AI

1. Jumlah slide **persis 7 slide** (tidak boleh 6 atau 8).
2. Tidak ada teks narasi panjang paragraf; seluruh poin disajikan dalam format *bulleted cards* yang padat dan mudah dipindai mata (*scannable*).
3. Menggunakan nama dosen pembimbing lengkap dengan gelar: **Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A**.
4. Semua istilah bahasa asing (*impulsive buying*, *booster pack*, *hedonic motivation*, *mean-centering*, dll.) dicetak miring (*italic*).
5. Tersedia naskah bicara presenter (*speaker notes*) untuk setiap slide.

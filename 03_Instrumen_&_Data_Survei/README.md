# 📊 INSTRUMEN PENELITIAN & DATA SURVEI LAPANGAN
### *Wadah Operasionalisasi Variabel, Kuesioner, Pilot Test, & Analisis SPSS MRA (Fase Pasca-Sempro)*

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Pusat pengelolaan instrumen pengumpulan data lapangan, draf kuesioner Google Forms, tabulasi pilot test 30 responden, data mentah survei ($N \ge 111$), serta berkas output olah data SPSS Moderated Regression Analysis (MRA).
> - **Masalah yang Diselesaikan:** Menjembatani proposal yang telah lolos seminar proposal menuju eksekusi penelitian lapangan secara terstruktur, mencegah tercecernya data mentah Excel, dan memastikan seluruh butir kuesioner 100% selaras dengan operasionalisasi variabel Bab III.
> - **Keputusan/Output:** Tersedia struktur direktori modular untuk kuesioner, tabulasi mentah, dan output statistik SPSS.

---

## 🏛️ 1. STRUKTUR DIREKTORI RISET LAPANGAN

```text
03_Instrumen_&_Data_Survei/
├── README.md                              <-- [Panduan ini] Cetak biru operasionalisasi & SOP survei
├── 📁 01_Kuesioner_Google_Forms/          <-- Draf naskah pertanyaan kuesioner & link Google Forms
├── 📁 02_Data_Mentah_Survei_Excel/        <-- Tabulasi data mentah (pilot test 30 responden & data final N=111-150)
└── 📁 03_Output_SPSS_MRA/                 <-- File syntax (.sps), dataset (.sav), dan output hasil olah data (.spv)
```

---

## 🎯 2. SPESIFIKASI OPERASIONALISASI VARIABEL & SKALA PENGUKURAN

Pengukuran menggunakan **Skala Likert 5-Poin** (1 = Sangat Tidak Setuju s.d. 5 = Sangat Setuju).

| Simbol | Variabel Penelitian | Dimensi / Indikator Kunci | Rujukan Skala Baku |
| :---: | :--- | :--- | :--- |
| **Y** | *Impulsive Buying* | Pembelian spontan tanpa rencana, dorongan emosional mendadak saat melihat booster pack | Verplanken & Herabadi (2001); Rook & Fisher (1995) |
| **X1** | *Hedonic Motivation* | Sensasi kesenangan membuka kemasan (*gacha thrill*), relaksasi, kepuasan visual kartu *holographic/secret rare* | Arnold & Reynolds (2003) |
| **X2** | *Desire for Completeness* | Hasrat melengkapi nomor urut binder set, sensasi ketidaknyamanan melihat slot binder kosong | Gao, Huang, & Simonson (2014); Belk (1995) |
| **X3** | *Speculative Motive* | Ekspektasi kenaikan harga sekunder, motivasi grading kartu (*PSA 10 Gem Mint*), potensi cuan alternatif | Aryadi & Lingga (2024); Baur et al. (2018) |
| **M** | *Self-Control* (Moderasi) | Kemampuan menahan impuls belanja berlebih, disiplin alokasi anggaran hobi, pengendalian diri finansial | Tangney, Baumeister, & Boone (2004); Thaler & Shefrin (1981) |

---

## 📈 3. TAHAP EKSEKUSI RISET LAPANGAN (ROADMAP)

1. **Penyusunan Kuesioner (Tahap 1):**
   * Finalisasi kalimat butir instrumen bahasa Indonesia yang komunikatif bagi komunitas TCG.
   * Penyisipan pertanyaan saringan (*screening questions*): WNI, usia $\ge 17$ tahun, pernah membeli booster pack fisik minimal 1x dalam 6–12 bulan terakhir.
2. **Uji Coba Pilot Test ($N=30$) (Tahap 2):**
   * Sebar kuesioner awal ke 30 responden kolektor di LGS (*Local Game Store*) / Discord.
   * Uji Validitas: Korelasi Bivariate Pearson ($r_{hitung} > r_{tabel} = 0,361$).
   * Uji Reliabilitas: *Cronbach's Alpha* $> 0,70$.
3. **Penyebaran Data Penuh ($N=111\text{--}150$) (Tahap 3):**
   * Pengumpulan sampel memenuhi kaidah Green (1991) formula $N \ge 104 + k = 111$ ($k=7$ prediktor MRA).
4. **Olah Data MRA 2-Tahap Hierarkis di SPSS (Tahap 4):**
   * Transformasi *Mean-Centering* untuk $X_1, X_2, X_3,$ dan $M$.
   * Model 1 (Baseline Langsung): $Y = \alpha + \beta_1 X_1^* + \beta_2 X_2^* + \beta_3 X_3^* + \beta_4 M^* + e$.
   * Model 2 (Interaksi Moderasi): $Y = \alpha + \beta_1 X_1^* + \beta_2 X_2^* + \beta_3 X_3^* + \beta_4 M^* + \beta_5 (X_1^* \cdot M^*) + \beta_6 (X_2^* \cdot M^*) + \beta_7 (X_3^* \cdot M^*) + e$.

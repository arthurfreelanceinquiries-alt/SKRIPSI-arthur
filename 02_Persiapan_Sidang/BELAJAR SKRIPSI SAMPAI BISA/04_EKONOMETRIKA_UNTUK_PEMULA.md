# 📊 EKONOMETRIKA DATA PANEL UNTUK PEMULA TOTAL
### *Dari nol sampai paham — tanpa rumus yang bikin pusing, pakai analogi kehidupan nyata*

---

> **Catatan:** Bagian ini menjelaskan konsep ekonometrika data panel yang digunakan di skripsi dengan bahasa sehari-hari dan analogi visual. Semua angka yang disebutkan tetap dari skripsi.

---

## 1. APA ITU DATA PANEL? (Analogi: Rapor Sekolah)

Bayangkan kamu punya **rapor** dari **4 siswa** selama **20 semester** (10 tahun sekolah).

| | Semester 1 | Semester 2 | ... | Semester 20 |
|---|---|---|---|---|
| **Siswa A** | 75 | 78 | ... | 88 |
| **Siswa B** | 82 | 80 | ... | 90 |
| **Siswa C** | 70 | 73 | ... | 85 |
| **Siswa D** | 88 | 90 | ... | 95 |

Ini namanya **data panel** — gabungan dari:
- **Cross-section:** Data dari beberapa individu (4 siswa) pada satu waktu → membandingkan antar individu
- **Time-series:** Data dari satu individu (1 siswa) sepanjang waktu → melihat tren

**Di skripsimu:**
- "Siswa" = **4 bank** (BBRI, BMRI, BBCA, BBNI)
- "Semester" = **20 kuartal** (Q1-2021 s.d. Q4-2025)
- "Nilai rapor" = **ROA** (yang ingin kita jelaskan)
- "Faktor yang memengaruhi nilai" = **Green Financing, NPL, CAR**
- Total data = 4 × 20 = **80 observasi**

### Kenapa Pakai Data Panel? (Bukan Cuma Cross-Section atau Time-Series Saja?)

| Jenis Data | Contoh | Kelemahan |
|---|---|---|
| **Cross-section saja** | Data 4 bank pada 1 kuartal saja | Hanya 4 titik data! Terlalu sedikit untuk analisis apapun |
| **Time-series saja** | Data 1 bank selama 20 kuartal | Tidak bisa membandingkan antar bank |
| **Data Panel** ✅ | Data 4 bank × 20 kuartal = 80 | Banyak data + bisa bandingkan antar bank + bisa lihat tren |

---

## 2. TIGA MODEL DATA PANEL (Analogi: Kelas Bimbel)

Bayangkan kamu mau meneliti: **"Apakah jam belajar mempengaruhi nilai ujian?"**

Kamu punya data 4 siswa selama 20 kali ujian. Masing-masing siswa punya jam belajar yang berbeda-beda setiap ujian. Nah, pertanyaannya: **bagaimana kamu memperlakukan perbedaan antar siswa?**

### Model 1: Common Effect Model (CEM) — "Semua Siswa Sama"

```
Analogi: Guru menyamakan semua murid.
         "Kalian semua sama aja, tidak ada yang lebih pintar atau lebih bodoh."
         Jadi rumus untuk semua siswa: Nilai = 50 + 2 × Jam Belajar
```

**Cara kerja:** CEM menganggap **tidak ada perbedaan** antar individu (bank). Semua bank diperlakukan seolah identik — punya intercept dan slope yang sama.

**Masalahnya:** Kita tahu bahwa BBCA dan BBRI itu **jelas berbeda** — budaya, basis nasabah, efisiensi, semuanya berbeda. Mengabaikan perbedaan ini bisa menghasilkan estimasi yang **bias**.

---

### Model 2: Fixed Effect Model (FEM) — "Setiap Siswa Unik, Tapi Uniknya Tetap" ✅ *TERPILIH*

```
Analogi: Guru mengakui setiap murid punya "kecerdasan dasar" berbeda.
         Si A memang dasarnya lebih pintar, si B biasa saja.
         Tapi guru ingin tahu: setelah faktor bakat dikontrol,
         apakah jam belajar TETAP berpengaruh ke nilai?

         Rumus si A: Nilai = 70 + 2 × Jam Belajar   (baseline-nya 70)
         Rumus si B: Nilai = 55 + 2 × Jam Belajar   (baseline-nya 55)
         Rumus si C: Nilai = 60 + 2 × Jam Belajar   (baseline-nya 60)
         Rumus si D: Nilai = 80 + 2 × Jam Belajar   (baseline-nya 80)

         → Slope-nya SAMA (2), tapi intercept-nya BEDA!
```

**Cara kerja:** FEM memberikan **intercept (titik awal) yang berbeda** untuk setiap bank, tapi koefisien variabel X-nya sama. "Fixed" artinya perbedaan antar-bank ini bersifat **tetap** (tidak berubah seiring waktu).

**Contoh di skripsi:**
- BBCA mungkin punya baseline ROA lebih tinggi karena manajemen biaya yang sangat efisien
- BBRI punya exposure UMKM yang berbeda dari BMRI
- Tapi **pengaruh NPL terhadap ROA** (koefisien -0,385) berlaku sama untuk semua bank

**Kapan dipilih?** Ketika Uji Hausman menunjukkan p < 0,05, artinya ada korelasi antara "keunikan bank" dengan variabel X → FEM lebih tepat.

---

### Model 3: Random Effect Model (REM) — "Setiap Siswa Berbeda, Tapi Secara Acak"

```
Analogi: Guru mengakui murid berbeda, tapi menganggap perbedaan itu
         ACAK (random) — bukan karena faktor sistematis.
         Seperti: "Si A kebetulan saja lebih pintar, bukan karena
         sekolah lamanya lebih bagus atau keluarganya lebih supportive."
```

**Cara kerja:** REM juga mengakui perbedaan antar bank, tapi menganggap perbedaan itu **acak** dan **tidak berkorelasi** dengan variabel independen (GF, NPL, CAR).

**Kapan dipilih?** Jika Uji Hausman menunjukkan p > 0,05 (tidak ada korelasi antara efek individual dan variabel X).

**Di skripsi ini:** Uji Hausman p = 0,0026 < 0,05 → **REM ditolak, FEM terpilih.**

---

### Perbandingan Visual:

```
           CEM                    FEM                      REM
    (Semua Bank Sama)     (Bank Beda, Tapi Tetap)    (Bank Beda, Acak)

ROA │                  ROA │     ╱ Bank A (intercept    ROA │     ╱ Bank A
    │      ╱               │    ╱   lebih tinggi)          │    ╱
    │     ╱  (1 garis      │   ╱                           │   ╱  (garis bisa
    │    ╱    untuk         │  ╱  ╱ Bank B                 │  ╱    berbeda tapi
    │   ╱     semua)        │ ╱  ╱                         │ ╱     perbedaannya
    │  ╱                    │╱  ╱  ╱ Bank C                │╱      dianggap acak)
    │ ╱                     │  ╱  ╱                        │
    │╱                      │ ╱  ╱  ╱ Bank D               │
    └──────── X             └──────── X                    └──────── X

    Slope SAMA              Slope SAMA                     Slope bisa
    Intercept SAMA          Intercept BEDA ← Inti FEM!     sedikit beda
```

---

## 3. UJI PEMILIHAN MODEL (Analogi: Turnamen Eliminasi)

Prosesnya seperti **turnamen olahraga** — model-model "bertanding" dan yang kalah tereliminasi:

```
        BABAK 1: Uji Chow                BABAK 2: Uji Hausman
    ┌────────────────────────┐       ┌────────────────────────┐
    │   CEM  vs  FEM         │       │   FEM  vs  REM         │
    │                        │       │                        │
    │   H0: Pilih CEM        │       │   H0: Pilih REM        │
    │   H1: Pilih FEM        │       │   H1: Pilih FEM        │
    │                        │       │                        │
    │   Prob F = 0,0000      │       │   Prob = 0,0026        │
    │   0,0000 < 0,05        │       │   0,0026 < 0,05        │
    │   → TOLAK H0           │       │   → TOLAK H0           │
    │   → FEM MENANG! ✅      │       │   → FEM MENANG! ✅      │
    └────────────────────────┘       └────────────────────────┘
                                              │
                                              ▼
                                    ┌──────────────────┐
                                    │  JUARA: FEM 🏆   │
                                    └──────────────────┘
```

**Aturan main sederhana:**
- **p-value < 0,05** → Tolak H₀ → Pilih yang di H₁
- **p-value > 0,05** → Gagal Tolak H₀ → Tetap di H₀

---

## 4. UJI ASUMSI KLASIK (Analogi: Tes Kesehatan Sebelum Bertanding)

Sebelum hasil regresi bisa dipercaya, model harus lolos "tes kesehatan" — yaitu **uji asumsi klasik**. Kalau tidak lolos, hasilnya bisa **bias** dan **tidak bisa dipercaya**.

### Uji 1: Normalitas Residual (Jarque-Bera)
```
❓ Pertanyaan: "Apakah 'sisa error' (residual) dari model kita 
                menyebar secara normal (seperti lonceng)?"

🩺 Alat Uji:   Jarque-Bera Test
📏 Syarat:      p-value > 0,05
📊 Hasil:       p = 0,398 > 0,05 → ✅ LOLOS (Normal)

💡 Analogi:     Bayangkan kamu melempar dadu 80 kali dan mencatat hasilnya.
                Jika distribusi hasilnya "wajar" (mengikuti pola tertentu),
                maka pengujian statistikmu valid. Jika distribusinya aneh
                (misal: selalu keluar angka 6), berarti ada masalah.
```

### Uji 2: Multikolinearitas (VIF)
```
❓ Pertanyaan: "Apakah variabel-variabel X saling 'tumpang tindih' 
                (berkorelasi sangat kuat satu sama lain)?"

🩺 Alat Uji:   Variance Inflation Factor (VIF)
📏 Syarat:      VIF < 10
📊 Hasil:       VIF_GF = 1,28 | VIF_NPL = 1,42 | VIF_CAR = 1,35 → ✅ LOLOS

💡 Analogi:     Bayangkan kamu riset pengaruh "jam belajar" dan "jumlah buku
                yang dibaca" terhadap nilai ujian. Kalau orang yang belajar 
                lama selalu juga baca banyak buku, maka kedua variabel itu 
                "tumpang tindih" — kita tidak bisa pisahkan pengaruh 
                masing-masing. VIF mendekati 1 = variabel-variabelnya 
                independen satu sama lain (ideal!).
```

### Uji 3: Heteroskedastisitas (Uji Glejser)
```
❓ Pertanyaan: "Apakah 'ukuran error' berubah-ubah tergantung nilai X?"

🩺 Alat Uji:   Uji Glejser (regresi |residual| terhadap X)
📏 Syarat:      p-value seluruh variabel > 0,05
📊 Hasil:       Semua p > 0,05 → ✅ LOLOS (Homoskedastisitas)

💡 Analogi:     Bayangkan kamu prediksi harga rumah berdasarkan luas tanah.
                Jika error prediksimu selalu ±Rp 50 juta (konsisten), itu 
                homoskedastis (bagus). Tapi jika untuk rumah kecil errornya 
                ±Rp 10 juta sedangkan rumah besar ±Rp 500 juta, itu 
                heteroskedastis (bermasalah) — presisimu tidak konsisten.
```

### Uji 4: Autokorelasi (Durbin-Watson)
```
❓ Pertanyaan: "Apakah error pada satu periode 'menular' ke periode 
                berikutnya (berkorelasi serial)?"

🩺 Alat Uji:   Durbin-Watson (DW)
📏 Syarat:      DW berada di antara dU (1,74) dan 4-dU (2,26)
📊 Hasil:       DW = 1,942 → Berada di antara 1,74 dan 2,26 → ✅ LOLOS

💡 Analogi:     Bayangkan suhu udara hari ini 35°C. Apakah itu memberitahu 
                kita bahwa besok pasti 34-36°C juga? Jika error di hari ini 
                "menular" ke besok, ada autokorelasi (bermasalah). Model 
                yang baik: error hari ini TIDAK bisa memprediksi error besok.

📐 Cara baca DW:
                0 ────── dL ── dU ─── 2 ─── 4-dU ── 4-dL ────── 4
                |  Auto+  |  ??  | BEBAS |  ??  |    Auto-    |
                               ↑
                            1,942 ← Skripsimu di sini (BEBAS ✅)
```

---

## 5. CARA BACA OUTPUT REGRESI (Langkah Demi Langkah)

Ketika kamu dapat output seperti ini:

| Variabel | Koefisien (β) | Std. Error | t-Statistik | p-value |
|---|---|---|---|---|
| Konstanta | 1,485 | 0,312 | 4,760 | 0,0000 |
| GF (X₁) | +0,042 | 0,011 | 3,818 | 0,0003 |
| NPL (X₂) | -0,385 | 0,076 | -5,066 | 0,0000 |
| CAR (X₃) | +0,074 | 0,016 | 4,625 | 0,0000 |

### Langkah 1: Lihat tanda koefisien (β)
- **Positif (+)** = hubungan searah (X naik → Y naik)
- **Negatif (-)** = hubungan berlawanan (X naik → Y turun)

### Langkah 2: Lihat p-value
- **< 0,05** → Signifikan (pengaruhnya nyata, bukan kebetulan) ✅
- **> 0,05** → Tidak signifikan (pengaruhnya mungkin hanya kebetulan) ❌

### Langkah 3: Interpretasi koefisien
"Setiap kenaikan 1 unit X, maka Y berubah sebesar β unit, **ceteris paribus** (variabel lain tetap)."

### Langkah 4: Periksa Std. Error dan t-Statistik
- **t-Statistik = β / Std. Error**
- Semakin besar |t|, semakin kuat pengaruh variabel tersebut
- Contoh: t NPL = -0,385 / 0,076 = -5,066 (sangat besar → sangat kuat)

### Langkah 5: Baca Adjusted R² dan Uji F
- **Adjusted R² = 0,702** → 70,2% variasi Y dijelaskan oleh semua X secara bersama
- **F = 32,450, p = 0,0000** → Model secara keseluruhan signifikan

---

## 6. RANGKUMAN VISUAL KESELURUHAN

```
                         ALUR ANALISIS DATA PANEL SKRIPSI

    ┌─────────────────┐
    │  Data Panel      │ 4 bank × 20 kuartal = 80 observasi
    │  (N=4, T=20)     │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Statistik       │ Mean, Median, Max, Min, Std.Dev
    │  Deskriptif      │ → ROA rata-rata 3,18%, NPL 2,42%, dst
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Estimasi 3      │ CEM, FEM, REM
    │  Model           │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Uji Pemilihan   │ Chow (CEM vs FEM) → FEM
    │  Model           │ Hausman (FEM vs REM) → FEM
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Uji Asumsi      │ Normalitas ✅ | Multikol ✅
    │  Klasik          │ Heterosk. ✅  | Autokol ✅
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Uji Hipotesis   │ Uji t (parsial): H1 ✅ H2 ✅ H3 ✅
    │                  │ Uji F (simultan): H4 ✅
    │                  │ Adjusted R² = 70,2%
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  KESIMPULAN      │ GF (+), NPL (-), CAR (+) → signifikan!
    └─────────────────┘
```

---

*Sekarang kamu sudah paham ekonometrika data panel dari A sampai Z. Kalau dosen tanya "kenapa FEM?", kamu bisa jawab pakai analogi siswa-siswa di atas — dijamin jawabanmu berkesan!* 🎓📈

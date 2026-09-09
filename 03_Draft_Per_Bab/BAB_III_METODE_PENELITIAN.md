# BAB III
# METODE PENELITIAN

## 3.1 Jenis dan Sumber Data

     Penelitian ini menggunakan pendekatan kuantitatif asosiatif dengan desain *cross-sectional* survei. Pendekatan kuantitatif dipilih karena penelitian ini bertujuan menguji hipotesis mengenai hubungan antarvariabel yang telah dirumuskan berdasarkan tinjauan pustaka dan teori yang relevan. Desain *cross-sectional* digunakan karena pengumpulan data dilakukan pada satu titik waktu tertentu, tanpa mengikuti perubahan variabel secara longitudinal.

     Jenis data yang digunakan dalam penelitian ini adalah data primer. Data primer diperoleh secara langsung dari responden melalui instrumen kuesioner daring (*online questionnaire*) yang didistribusikan menggunakan platform Google Forms. Kuesioner disusun dalam bentuk pernyataan tertutup (*closed-ended statements*) dengan menggunakan skala Likert 5 poin, di mana setiap pernyataan memiliki pilihan jawaban sebagai berikut:

**Tabel 3.1 Skala Pengukuran Likert 5 Poin**

| Skor | Keterangan |
|:---|:---|
| 1 | Sangat Tidak Setuju (STS) |
| 2 | Tidak Setuju (TS) |
| 3 | Netral (N) |
| 4 | Setuju (S) |
| 5 | Sangat Setuju (SS) |

*Sumber: Sugiyono (2019).*

     Selain data primer dari kuesioner, penelitian ini juga menggunakan data sekunder berupa literatur ilmiah, jurnal penelitian, buku teks, serta data dan laporan resmi dari lembaga terkait (seperti data OJK mengenai literasi keuangan Indonesia) sebagai pendukung kajian teori dan fenomena di Bab I dan Bab II.

---

## 3.2 Populasi dan Sampel

### 3.2.1 Populasi

     Populasi dalam penelitian ini adalah seluruh konsumen atau kolektor kartu *Pokemon Trading Card Game* (Pokemon TCG) fisik resmi di Indonesia. Populasi ini bersifat tidak terbatas (*infinite population*) karena jumlah pasti pembeli kartu Pokemon TCG di Indonesia tidak dapat diketahui secara pasti.

### 3.2.2 Sampel

     Teknik pengambilan sampel yang digunakan dalam penelitian ini adalah *purposive sampling* (sampel bertujuan), yaitu teknik penentuan sampel berdasarkan pertimbangan dan kriteria tertentu yang ditetapkan oleh peneliti. Kriteria inklusi responden dalam penelitian ini adalah sebagai berikut:

1. Warga Negara Indonesia (WNI) yang berdomisili di Indonesia.
2. Berusia minimal 17 tahun pada saat pengisian kuesioner.
3. Pernah melakukan pembelian *booster pack* kartu Pokemon TCG fisik resmi (berbahasa Indonesia) minimal satu kali dalam rentang waktu 6 hingga 12 bulan terakhir.

     Penentuan jumlah sampel minimum dalam penelitian ini mengacu pada formula Green (1991) yang direkomendasikan untuk analisis regresi berganda:

- **Untuk pengujian model keseluruhan (*multiple correlation*):**

  $$N \ge 50 + 8k \tag{3.1}$$

  Di mana $k$ = jumlah prediktor. Dalam model MRA penelitian ini, prediktor terdiri dari: $X_1$, $X_2$, $X_3$, $M$, $X_1 \cdot M$, $X_2 \cdot M$, $X_3 \cdot M$ = **7 prediktor**.

  $$N \ge 50 + 8(7) = 50 + 56 = 106\text{ responden}$$

- **Untuk pengujian prediktor individual (*partial correlation*):**

  $$N \ge 104 + k \tag{3.2}$$

  $$N \ge 104 + 7 = 111\text{ responden}$$

     Berdasarkan perhitungan di atas, jumlah sampel minimum yang diperlukan adalah 111 responden. Namun, untuk mengantisipasi kemungkinan data yang tidak lengkap atau tidak memenuhi syarat (*missing/invalid responses*) dan untuk meningkatkan kekuatan uji statistik (*statistical power*), peneliti menetapkan target jumlah sampel sebesar **120 hingga 150 responden**. Penetapan target ini juga sejalan dengan rekomendasi Cohen (1988) untuk mencapai *statistical power* sebesar 0,80 dengan *medium effect size* pada taraf signifikansi 0,05.

     Distribusi kuesioner dilakukan secara daring melalui komunitas-komunitas kolektor Pokemon TCG Indonesia yang aktif di berbagai platform digital, antara lain: grup Facebook (*Pokemon TCG Indonesia*, *Pasar Kartu Pokemon Indonesia*), server Discord komunitas TCG, forum Reddit (*r/PokemonTCG*), serta melalui jaringan toko hobi lokal (*Local Game Stores / LGS*) di kota-kota besar Indonesia.

> **Catatan keterbatasan:** Karena teknik sampling yang digunakan adalah *purposive sampling* (non-probabilitas), maka hasil penelitian ini hanya dapat digeneralisasikan secara terbatas pada sampel yang diteliti dan tidak dapat diklaim mewakili seluruh populasi pembeli kartu Pokemon TCG di Indonesia secara representatif.

---

## 3.3 Model Penelitian

     Model penelitian yang digunakan dalam penelitian ini adalah *Moderated Regression Analysis* (MRA), yaitu analisis regresi yang memasukkan variabel interaksi (*interaction term*) antara variabel independen dan variabel moderasi untuk menguji apakah variabel moderasi memperkuat atau memperlemah hubungan antara variabel independen dan variabel dependen.

     Model persamaan regresi dalam penelitian ini disusun dalam dua tahap:

**Model 1 — Regresi Berganda (Pengaruh Langsung):**

$$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + e \tag{3.3}$$

**Model 2 — *Moderated Regression Analysis* / MRA (Pengaruh Moderasi):**

$$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_4 M + \beta_5 (X_1 \cdot M) + \beta_6 (X_2 \cdot M) + \beta_7 (X_3 \cdot M) + e \tag{3.4}$$

Keterangan:
- $Y$ = *Impulsive Buying* (variabel dependen)
- $X_1$ = *Hedonic Motivation* (variabel independen 1)
- $X_2$ = *Need for Completion* (variabel independen 2)
- $X_3$ = *Speculative Motive* (variabel independen 3)
- $M$ = Literasi Keuangan (variabel moderasi)
- $X_1 \cdot M$ = Interaksi *Hedonic Motivation* $\times$ Literasi Keuangan
- $X_2 \cdot M$ = Interaksi *Need for Completion* $\times$ Literasi Keuangan
- $X_3 \cdot M$ = Interaksi *Speculative Motive* $\times$ Literasi Keuangan
- $\alpha$ = Konstanta
- $\beta_1 \dots \beta_7$ = Koefisien regresi
- $e$ = *Error term* (variabel pengganggu)

     Efek moderasi dinyatakan terbukti apabila koefisien regresi variabel interaksi ($\beta_5$, $\beta_6$, atau $\beta_7$) signifikan secara statistik pada taraf $\alpha = 0,05$.

```
                    Pengaruh Langsung
    ┌──────────────────────────────────────────────────────┐
    │                                                      │
    │   [ X1: Hedonic Motivation  ] ──── H1 (+) ───┐      │
    │                                               │      │
    │   [ X2: Need for Completion ] ──── H2 (+) ───┼──►  [ Y: Impulsive Buying ]
    │                                               │      │
    │   [ X3: Speculative Motive  ] ──── H3 (+) ───┘      │
    │                                                      │
    └──────────────────────────────────────────────────────┘
                                                    ▲
                                                    │
                         H4, H5, H6 (Memperlemah / -)
                                                    │
                                       [ M: Literasi Keuangan ]
                                       (Variabel Moderasi)
```

**Gambar 3.1 Model Penelitian**

---

## 3.4 Operasionalisasi Variabel

     Operasionalisasi variabel merupakan proses pendefinisian variabel-variabel penelitian secara spesifik dan terukur, sehingga setiap variabel dapat diukur melalui indikator-indikator yang jelas. Berikut adalah operasionalisasi variabel dalam penelitian ini:

**Tabel 3.2 Operasionalisasi Variabel**

### A. Variabel Dependen: *Impulsive Buying* (Y)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| *Impulsive Buying* (Y) | Kecenderungan membeli *booster pack* kartu Pokemon TCG secara tiba-tiba, tanpa perencanaan anggaran keuangan sebelumnya, dan didorong oleh dorongan emosional sesaat. | Kognitif | Y1. Saya sering membeli *booster pack* kartu Pokemon tanpa perencanaan sebelumnya. | Likert 1–5 |
| | | Kognitif | Y2. Saya tidak terlalu memikirkan konsekuensi finansial saat membeli *booster pack* kartu Pokemon. | Likert 1–5 |
| | | Afektif | Y3. Saya merasa terdorong kuat untuk membeli *booster pack* kartu Pokemon saat melihatnya di toko. | Likert 1–5 |
| | | Afektif | Y4. Saya merasa senang dan bersemangat saat membeli *booster pack* kartu Pokemon secara spontan. | Likert 1–5 |
| | | Kognitif | Y5. Saya sering membeli lebih banyak *booster pack* kartu Pokemon dari yang saya rencanakan. | Likert 1–5 |
| | | Afektif | Y6. Saya sulit menahan diri untuk tidak membeli *booster pack* kartu Pokemon ketika berada di toko atau melihat di *marketplace*. | Likert 1–5 |

**Sumber adaptasi:** Verplanken dan Herabadi (2001) — *Impulsive Buying Tendency Scale* (IBTS); Rook dan Fisher (1995).

---

### B. Variabel Independen 1: *Hedonic Motivation* (X1)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| *Hedonic Motivation* (X1) | Motivasi berbelanja *booster pack* kartu Pokemon TCG untuk mendapatkan kesenangan emosional, sensasi kejutan, dan hiburan psikologis. | *Adventure* | X1.1. Saya merasa berpetualang dan bersemangat saat membeli dan membuka *booster pack* kartu Pokemon. | Likert 1–5 |
| | | *Adventure* | X1.2. Pengalaman membuka bungkus *booster pack* kartu Pokemon memberikan sensasi kejutan yang menyenangkan bagi saya. | Likert 1–5 |
| | | *Gratification* | X1.3. Membeli *booster pack* kartu Pokemon merupakan cara saya untuk memanjakan diri atau menghilangkan stres. | Likert 1–5 |
| | | *Gratification* | X1.4. Saya merasa bahagia dan puas secara emosional setelah berhasil menarik kartu langka dari *booster pack*. | Likert 1–5 |
| | | *Idea* | X1.5. Saya senang mengikuti rilis seri kartu Pokemon terbaru dan menjelajahi desain kartu yang baru keluar. | Likert 1–5 |

**Sumber adaptasi:** Arnold dan Reynolds (2003) — *Hedonic Shopping Motivation Scale*; Babin, Darden, dan Griffin (1994).

---

### C. Variabel Independen 2: *Need for Completion* (X2)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| *Need for Completion* (X2) | Dorongan psikologis kuat untuk mengisi slot kartu yang masih kosong dalam album/*binder* koleksi satu seri kartu Pokemon TCG. | Set completion | X2.1. Saya merasa tidak nyaman ketika album/*binder* koleksi kartu Pokemon saya masih memiliki slot kosong. | Likert 1–5 |
| | | Set completion | X2.2. Saya terdorong untuk terus membeli *booster pack* agar dapat melengkapi seluruh kartu dalam satu seri. | Likert 1–5 |
| | | Cognitive tension | X2.3. Mengetahui ada kartu yang belum saya miliki dalam suatu seri membuat saya ingin segera membelinya. | Likert 1–5 |
| | | Mastery | X2.4. Melengkapi satu set penuh kartu Pokemon memberikan perasaan pencapaian dan kepuasan bagi saya. | Likert 1–5 |
| | | Cognitive tension | X2.5. Semakin sedikit kartu yang kurang dalam satu seri, semakin kuat dorongan saya untuk segera melengkapinya. | Likert 1–5 |

**Sumber adaptasi:** Belk (1995) — *Collecting in a Consumer Society*; Gao et al. (2014); konsep *Zeigarnik Effect* (Zeigarnik, 1927).

---

### D. Variabel Independen 3: *Speculative Motive* (X3)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| *Speculative Motive* (X3) | Pertimbangan nilai jual kembali (*resale value*) dan harapan memperoleh keuntungan finansial (*capital gain*) dari pembelian *booster pack* kartu Pokemon TCG. | Resale expectation | X3.1. Saya mempertimbangkan potensi nilai jual kembali kartu saat memutuskan membeli *booster pack*. | Likert 1–5 |
| | | Capital gain | X3.2. Saya berharap menarik kartu langka yang bernilai tinggi di pasar sekunder saat membeli *booster pack*. | Likert 1–5 |
| | | Overoptimism | X3.3. Saya merasa peluang untuk mendapatkan kartu bernilai mahal dari *booster pack* cukup besar. | Likert 1–5 |
| | | Investment view | X3.4. Saya melihat pembelian *booster pack* kartu Pokemon sebagai bentuk "investasi" yang berpotensi menguntungkan. | Likert 1–5 |
| | | Market awareness | X3.5. Saya sering memantau harga kartu Pokemon di pasar sekunder (*marketplace* daring) sebelum membeli *booster pack*. | Likert 1–5 |

**Sumber adaptasi:** Shiller (2000) — *Irrational Exuberance*; Keynes (1936) — *Speculative Motive*; Kahneman dan Tversky (1979) — *Prospect Theory*.

---

### E. Variabel Moderasi: Literasi Keuangan (M)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| Literasi Keuangan (M) | Tingkat pengetahuan, sikap, dan keterampilan finansial individu dalam mengelola keuangan pribadi, khususnya terkait penganggaran, pengendalian pengeluaran, dan pemahaman risiko. | Pengetahuan keuangan | M1. Saya memahami pentingnya menyusun anggaran (*budgeting*) untuk mengelola pengeluaran bulanan saya. | Likert 1–5 |
| | | Pengetahuan keuangan | M2. Saya memahami perbedaan antara kebutuhan (*needs*) dan keinginan (*wants*) dalam pengeluaran keuangan saya. | Likert 1–5 |
| | | Perilaku keuangan | M3. Saya secara rutin mencatat dan mengevaluasi pengeluaran keuangan pribadi saya. | Likert 1–5 |
| | | Perilaku keuangan | M4. Saya selalu mempertimbangkan kondisi keuangan saya sebelum melakukan pembelian yang tidak direncanakan. | Likert 1–5 |
| | | Sikap keuangan | M5. Saya percaya bahwa menabung dan mengelola keuangan dengan baik lebih penting daripada memenuhi keinginan sesaat. | Likert 1–5 |
| | | Pengetahuan keuangan | M6. Saya memahami konsep risiko finansial dan menyadari bahwa tidak semua pengeluaran menghasilkan keuntungan. | Likert 1–5 |

**Sumber adaptasi:** Chen dan Volpe (1998); OJK — Standar SNLIK (2023); OECD-INFE (2022).

---

## 3.5 Metode Analisis Data

     Data yang diperoleh dari kuesioner akan diolah dan dianalisis menggunakan perangkat lunak *Statistical Package for the Social Sciences* (SPSS). Analisis data dalam penelitian ini dilakukan melalui beberapa tahapan sebagai berikut:

### 3.5.1 Uji Validitas dan Reliabilitas

     Uji validitas dilakukan untuk memastikan bahwa setiap butir pernyataan dalam kuesioner benar-benar mengukur konstruk yang dimaksud. Teknik yang digunakan adalah korelasi *Pearson Product Moment*, di mana suatu butir pernyataan dinyatakan valid apabila nilai $r_{hitung} > r_{tabel}$ pada taraf signifikansi 0,05.

     Uji reliabilitas dilakukan untuk mengetahui konsistensi internal instrumen pengukuran. Teknik yang digunakan adalah *Cronbach's Alpha*, di mana suatu instrumen dinyatakan reliabel apabila nilai *Cronbach's Alpha* $\ge 0,60$ (Ghozali, 2018).

### 3.5.2 Uji Asumsi Klasik

     Sebelum melakukan analisis regresi, terlebih dahulu dilakukan uji asumsi klasik untuk memastikan bahwa model regresi memenuhi persyaratan BLUE (*Best Linear Unbiased Estimator*). Untuk data survei *cross-sectional*, uji asumsi klasik yang relevan dan dilakukan meliputi:

1. **Uji Normalitas:** Menguji apakah residual model regresi berdistribusi normal. Teknik yang digunakan adalah uji *Kolmogorov-Smirnov*, di mana data dinyatakan berdistribusi normal apabila nilai signifikansi $> 0,05$.

2. **Uji Multikolinearitas:** Menguji apakah terdapat korelasi yang tinggi antarvariabel independen dalam model regresi. Multikolinearitas tidak terjadi apabila nilai *Tolerance* $> 0,10$ dan nilai *Variance Inflation Factor* (VIF) $< 10$.

3. **Uji Heteroskedastisitas:** Menguji apakah terdapat ketidaksamaan varian residual dari satu pengamatan ke pengamatan lain. Teknik yang digunakan adalah uji Glejser, di mana heteroskedastisitas tidak terjadi apabila nilai signifikansi variabel independen terhadap absolut residual $> 0,05$.

### 3.5.3 Analisis Regresi Berganda

     Analisis regresi berganda digunakan untuk menguji pengaruh variabel independen ($X_1$, $X_2$, $X_3$) secara parsial dan simultan terhadap variabel dependen ($Y$). Model regresi berganda yang digunakan adalah:

$$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + e \tag{3.5}$$

Tahap ini bertujuan menguji hipotesis H1, H2, dan H3 mengenai pengaruh langsung masing-masing variabel independen terhadap *Impulsive Buying*.

### 3.5.4 *Moderated Regression Analysis* (MRA)

     *Moderated Regression Analysis* (MRA) digunakan untuk menguji apakah Literasi Keuangan ($M$) memoderasi (memperlemah) pengaruh variabel independen ($X_1$, $X_2$, $X_3$) terhadap *Impulsive Buying* ($Y$). Model MRA yang digunakan adalah:

$$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_4 M + \beta_5 (X_1 \cdot M) + \beta_6 (X_2 \cdot M) + \beta_7 (X_3 \cdot M) + e \tag{3.6}$$

     Efek moderasi dinyatakan terbukti dan signifikan apabila koefisien regresi variabel interaksi ($\beta_5$, $\beta_6$, dan/atau $\beta_7$) menunjukkan nilai signifikansi $p < 0,05$. Tahap ini bertujuan menguji hipotesis H4, H5, dan H6.

     Sebelum menghitung variabel interaksi, variabel independen dan variabel moderasi akan di-*center* terlebih dahulu (*mean centering*), yaitu mengurangi skor setiap responden dengan rata-rata (*mean*) variabel tersebut (Aiken & West, 1991; Ghozali, 2018). Prosedur ini dilakukan untuk mengatasi potensi multikolinearitas struktural antara variabel utama dan variabel interaksi.

### 3.5.5 Uji Koefisien Determinasi ($R^2$)

     Koefisien determinasi ($R^2$) digunakan untuk mengukur seberapa besar kemampuan model regresi dalam menjelaskan variasi variabel dependen. Nilai $R^2$ berkisar antara 0 hingga 1, di mana semakin mendekati 1 berarti model semakin baik dalam menjelaskan variasi *Impulsive Buying*. Dalam penelitian ini, perbandingan nilai $R^2$ antara Model 1 (tanpa moderasi) dan Model 2 (dengan moderasi) akan dianalisis untuk melihat peningkatan daya jelang model setelah memasukkan variabel interaksi.

### 3.5.6 Uji Hipotesis

**a. Uji t (Uji Parsial)**

     Uji t digunakan untuk menguji signifikansi pengaruh masing-masing variabel independen secara parsial terhadap variabel dependen. Kriteria pengujian: apabila nilai signifikansi $p < 0,05$, maka hipotesis diterima (terdapat pengaruh signifikan).

**b. Uji F (Uji Simultan)**

     Uji F digunakan untuk menguji signifikansi pengaruh seluruh variabel independen secara bersama-sama (simultan) terhadap variabel dependen. Kriteria pengujian: apabila nilai signifikansi $p < 0,05$, maka model regresi secara keseluruhan signifikan.

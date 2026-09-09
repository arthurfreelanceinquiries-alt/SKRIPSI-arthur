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

     Selain data primer dari kuesioner, penelitian ini juga menggunakan data sekunder berupa literatur ilmiah, jurnal penelitian internasional dan nasional bereputasi, buku teks manajemen keuangan dan perilaku konsumen, serta laporan industri pasar kartu koleksi global dan nasional sebagai pendukung kajian teori dan fenomena di Bab I dan Bab II.

---

## 3.2 Populasi dan Sampel

### 3.2.1 Populasi

     Populasi dalam penelitian ini adalah seluruh konsumen atau kolektor kartu *Pokémon Trading Card Game* (Pokémon TCG) fisik resmi di Indonesia. Populasi ini bersifat tidak terbatas (*infinite population*) karena jumlah pasti pembeli kartu Pokémon TCG di Indonesia tidak dapat diketahui secara pasti seiring luasnya jaringan distribusi ritel modern di seluruh Nusantara.

### 3.2.2 Sampel

     Teknik pengambilan sampel yang digunakan dalam penelitian ini adalah *purposive sampling* (sampel bertujuan), yaitu teknik penentuan sampel berdasarkan pertimbangan dan kriteria tertentu yang ditetapkan oleh peneliti. Kriteria inklusi responden dalam penelitian ini adalah sebagai berikut:

1. Warga Negara Indonesia (WNI) yang berdomisili di Indonesia.
2. Berusia minimal 17 tahun pada saat pengisian kuesioner.
3. Pernah melakukan pembelian *booster pack* kartu Pokémon TCG fisik resmi (berbahasa Indonesia) minimal satu kali dalam rentang waktu 6 hingga 12 bulan terakhir.

     Penentuan jumlah sampel minimum dalam penelitian ini mengacu pada formula Green (1991) yang direkomendasikan untuk analisis regresi berganda:

- **Untuk pengujian model keseluruhan (*multiple correlation*):**

  $$N \ge 50 + 8k \tag{3.1}$$

  Di mana $k$ = jumlah prediktor. Dalam model MRA penelitian ini, prediktor terdiri dari: $X_1$, $X_2$, $X_3$, $M$, $X_1 \cdot M$, $X_2 \cdot M$, $X_3 \cdot M$ = **7 prediktor**.

  $$N \ge 50 + 8(7) = 50 + 56 = 106\text{ responden}$$

- **Untuk pengujian prediktor individual (*partial correlation*):**

  $$N \ge 104 + k \tag{3.2}$$

  $$N \ge 104 + 7 = 111\text{ responden}$$

     Berdasarkan perhitungan di atas, jumlah sampel minimum yang diperlukan adalah 111 responden. Namun, untuk mengantisipasi kemungkinan data yang tidak lengkap atau tidak memenuhi syarat (*missing/invalid responses*) dan untuk meningkatkan kekuatan uji statistik (*statistical power*), peneliti menetapkan target jumlah sampel sebesar **120 hingga 150 responden**. Penetapan target ini juga sejalan dengan rekomendasi Cohen (1988) untuk mencapai *statistical power* sebesar 0,80 dengan *medium effect size* pada taraf signifikansi 0,05.

     Distribusi kuesioner dilakukan secara daring melalui komunitas-komunitas kolektor Pokémon TCG Indonesia yang aktif di berbagai platform digital, antara lain: grup Facebook (*Pokémon TCG Indonesia*, *Pasar Kartu Pokémon Indonesia*), server Discord komunitas TCG Indonesia, grup komunitas WhatsApp/Telegram kolektor, serta melalui jaringan toko hobi lokal (*Local Game Stores / LGS*) di kota-kota besar Indonesia.

> **Catatan keterbatasan:** Karena teknik sampling yang digunakan adalah *purposive sampling* (non-probabilitas), maka hasil penelitian ini hanya dapat digeneralisasikan secara terbatas pada sampel yang diteliti dan tidak dapat diklaim mewakili seluruh populasi pembeli kartu Pokémon TCG di Indonesia secara representatif.

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
- $X_2$ = *Desire for Completeness* (variabel independen 2)
- $X_3$ = *Speculative Motive* (variabel independen 3)
- $M$ = *Self-Control* (variabel moderasi)
- $X_1 \cdot M$ = Interaksi *Hedonic Motivation* $\times$ *Self-Control*
- $X_2 \cdot M$ = Interaksi *Desire for Completeness* $\times$ *Self-Control*
- $X_3 \cdot M$ = Interaksi *Speculative Motive* $\times$ *Self-Control*
- $\alpha$ = Konstanta
- $\beta_1 \dots \beta_7$ = Koefisien regresi
- $e$ = *Error term* (variabel pengganggu)

     Efek moderasi dinyatakan terbukti memperlemah apabila koefisien regresi variabel interaksi ($\beta_5$, $\beta_6$, atau $\beta_7$) bernilai negatif dan signifikan secara statistik pada taraf $\alpha = 0,05$.

```
                    PENGARUH LANGSUNG
     ┌─────────────────────────────────────────────────────────┐
     │                                                         │
     │   [ X1: Hedonic Motivation     ] ──── H1 (+) ────┐      │
     │                                                   │      │
     │   [ X2: Desire for Completeness] ──── H2 (+) ────┼──►  [ Y: Impulsive Buying ]
     │                                                   │      │
     │   [ X3: Speculative Motive     ] ──── H3 (+) ────┘      │
     │                                                         │
     └─────────────────────────────────────────────────────────┘
                                                         ▲
                                                         │
                              H4, H5, H6 (Memperlemah / -)
                                                         │
                                            [ M: Self-Control ]
                                            (Variabel Moderasi)
```

**Gambar 3.1 Model Penelitian (Moderated Regression Analysis)**

---

## 3.4 Operasionalisasi Variabel

     Operasionalisasi variabel merupakan proses pendefinisian variabel-variabel penelitian secara spesifik dan terukur, sehingga setiap variabel dapat diukur melalui indikator-indikator yang jelas. Berikut adalah operasionalisasi variabel dalam penelitian ini:

**Tabel 3.2 Operasionalisasi Variabel**

### A. Variabel Dependen: *Impulsive Buying* (Y)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| *Impulsive Buying* (Y) | Kecenderungan membeli *booster pack* kartu Pokémon TCG secara tiba-tiba, tanpa perencanaan anggaran keuangan sebelumnya, dan didorong oleh dorongan emosional sesaat. | Kognitif | Y1. Saya sering membeli *booster pack* kartu Pokémon tanpa perencanaan sebelumnya. | Likert 1–5 |
| | | Kognitif | Y2. Saya tidak terlalu memikirkan konsekuensi finansial saat membeli *booster pack* kartu Pokémon. | Likert 1–5 |
| | | Afektif | Y3. Saya merasa terdorong kuat untuk membeli *booster pack* kartu Pokémon saat melihatnya di toko. | Likert 1–5 |
| | | Afektif | Y4. Saya merasa senang dan bersemangat saat membeli *booster pack* kartu Pokémon secara spontan. | Likert 1–5 |
| | | Kognitif | Y5. Saya sering membeli lebih banyak *booster pack* kartu Pokémon dari yang saya rencanakan. | Likert 1–5 |
| | | Afektif | Y6. Saya sulit menahan diri untuk tidak membeli *booster pack* kartu Pokémon ketika berada di toko atau melihat di *marketplace*. | Likert 1–5 |

*Sumber adaptasi:* Verplanken dan Herabadi (2001) — *Impulsive Buying Tendency Scale* (IBTS); Rook dan Fisher (1995).

---

### B. Variabel Independen 1: *Hedonic Motivation* (X1)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| *Hedonic Motivation* (X1) | Motivasi berbelanja *booster pack* kartu Pokémon TCG untuk mendapatkan kesenangan emosional, sensasi kejutan, dan hiburan psikologis. | *Adventure* | X1.1. Saya merasa berpetualang dan bersemangat saat membeli dan membuka *booster pack* kartu Pokémon. | Likert 1–5 |
| | | *Adventure* | X1.2. Pengalaman membuka bungkus *booster pack* kartu Pokémon memberikan sensasi kejutan yang menyenangkan bagi saya. | Likert 1–5 |
| | | *Gratification* | X1.3. Membeli *booster pack* kartu Pokémon merupakan cara saya untuk memanjakan diri atau menghilangkan stres. | Likert 1–5 |
| | | *Gratification* | X1.4. Saya merasa bahagia dan puas secara emosional setelah berhasil menarik kartu langka dari *booster pack*. | Likert 1–5 |
| | | *Idea* | X1.5. Saya senang mengikuti rilis seri kartu Pokémon terbaru dan menjelajahi desain kartu yang baru keluar. | Likert 1–5 |

*Sumber adaptasi:* Arnold dan Reynolds (2003) — *Hedonic Shopping Motivation Scale*; Babin, Darden, dan Griffin (1994).

---

### C. Variabel Independen 2: *Desire for Completeness* (X2)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| *Desire for Completeness* (X2) | Dorongan psikologis dan motivasional internal individu untuk melengkapi seluruh nomor kartu yang masih kosong dalam album/*binder* koleksi satu seri kartu Pokémon TCG. | *Cognitive Tension* | X2.1. Saya merasa tidak nyaman dan terganggu ketika album/*binder* koleksi kartu Pokémon saya masih memiliki slot nomor kartu yang kosong. | Likert 1–5 |
| | | *Drive for Closure* | X2.2. Saya terdorong untuk terus membeli *booster pack* tambahan agar dapat melengkapi seluruh kartu dalam satu seri secara utuh. | Likert 1–5 |
| | | *Cognitive Tension* | X2.3. Mengetahui ada kartu yang belum saya miliki dalam suatu seri membuat saya berhasrat untuk segera mendapatkannya. | Likert 1–5 |
| | | *Sense of Wholeness* | X2.4. Melengkapi satu set penuh kartu Pokémon memberikan perasaan pencapaian, kepuasan, dan keutuhan bagi saya. | Likert 1–5 |
| | | *Drive for Closure* | X2.5. Semakin sedikit kartu yang kurang dalam satu seri, semakin kuat desakan saya untuk segera membeli pack demi melengkapinya. | Likert 1–5 |

*Sumber adaptasi:* Gao, Huang, dan Simonson (2014) — *The "Completing the Set" Effect*; Barasz, John, Keenan, dan Norton (2017) — *Pseudo-Set Framing*; Belk (1995); Zeigarnik (1927).

---

### D. Variabel Independen 3: *Speculative Motive* (X3)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| *Speculative Motive* (X3) | Pertimbangan nilai pasar sekunder, ekspektasi sertifikasi grading, dan harapan memperoleh keuntungan finansial (*capital gain*) dari penjualan kembali kartu langka hasil pembelian *booster pack*. | *Capital Gain* | X3.1. Saya mempertimbangkan potensi kenaikan harga jual kembali kartu di pasar sekunder saat memutuskan membeli *booster pack*. | Likert 1–5 |
| | | *Grading Arbitrage* | X3.2. Saya berharap menarik kartu langka berkondisi sempurna untuk dikirim ke lembaga grading (seperti PSA/BGS) agar nilainya berlipat ganda. | Likert 1–5 |
| | | *Overoptimism* | X3.3. Saya merasa peluang saya untuk mendapatkan kartu bernilai jutaan rupiah dari *booster pack* acak cukup besar. | Likert 1–5 |
| | | *Investment View* | X3.4. Saya memandang pembelian *booster pack* kartu Pokémon sebagai bentuk instrumen aset alternatif yang berpotensi menghasilkan keuntungan modal. | Likert 1–5 |
| | | *Market Awareness* | X3.5. Saya aktif memantau pergerakan harga kartu Pokémon di pasar sekunder (*marketplace* daring dan lelang komunitas) sebelum membeli pack. | Likert 1–5 |

*Sumber adaptasi:* Shiller (2000) — *Irrational Exuberance*; Keynes (1936) — *Speculative Motive*; Kahneman dan Tversky (1979) — *Prospect Theory*; Baur, Hong, dan Lee (2018).

---

### E. Variabel Moderasi: *Self-Control* (M)

| Variabel | Definisi Operasional | Dimensi | Indikator | Skala |
|:---|:---|:---|:---|:---|
| *Self-Control* (M) | Kapasitas volisional individu untuk menolak godaan belanja spontan, menunda kepuasan sesaat (*delay of gratification*), dan mendisiplinkan pengeluaran agar selaras dengan batasan anggaran keuangan pribadi. | *Resisting Temptation* | M1. Saya mampu menolak godaan membeli barang yang menarik sesaat jika barang tersebut di luar perencanaan anggaran saya. | Likert 1–5 |
| | | *Non-Impulsive Behavior* | M2. Saya terbiasa berpikir tenang dan mempertimbangkan dampak pengeluaran sebelum memutuskan untuk bertransaksi. | Likert 1–5 |
| | | *Delay of Gratification* | M3. Saya mampu menahan diri dari kesenangan belanja saat ini demi menjaga keamanan dan tujuan keuangan masa depan saya. | Likert 1–5 |
| | | *Self-Discipline* | M4. Saya memiliki disiplin diri yang kuat untuk tidak membeli barang secara mendadak saat berada di kasir toko. | Likert 1–5 |
| | | *Emotional Control* | M5. Saya tidak mudah terhanyut oleh suasana hati atau letupan kegembiraan sesaat dalam membelanjakan uang saya. | Likert 1–5 |
| | | *Adherence to Plan* | M6. Saya secara konsisten mematuhi alokasi batas pengeluaran hobi yang telah saya rencanakan sebelumnya. | Likert 1–5 |

*Sumber adaptasi:* Tangney, Baumeister, dan Boone (2004) — *Brief Self-Control Scale* (BSCS); Vohs dan Faber (2007); Sultan, Joireman, dan Sprott (2012).

---

## 3.5 Metode Analisis Data

     Data yang diperoleh dari kuesioner akan diolah dan dianalisis menggunakan perangkat lunak *Statistical Package for the Social Sciences* (IBM SPSS Statistics). Analisis data dalam penelitian ini dilakukan melalui beberapa tahapan sistematis sebagai berikut:

### 3.5.1 Uji Validitas dan Reliabilitas

     Uji validitas dilakukan untuk memastikan bahwa setiap butir pernyataan dalam kuesioner benar-benar mengukur konstruk yang dimaksud secara akurat. Teknik yang digunakan adalah korelasi *Pearson Product Moment*, di mana suatu butir pernyataan dinyatakan valid apabila nilai koefisien korelasi $r_{\text{hitung}} > r_{\text{tabel}}$ pada taraf signifikansi $\alpha = 0,05$ dengan uji dua sisi (*two-tailed*).

     Uji reliabilitas dilakukan untuk mengetahui konsistensi internal instrumen pengukuran antarbutir pernyataan. Teknik yang digunakan adalah koefisien *Cronbach's Alpha*, di mana suatu konstruk variabel dinyatakan reliabel apabila nilai *Cronbach's Alpha* $\ge 0,60$ (Ghozali, 2018).

### 3.5.2 Uji Asumsi Klasik

     Sebelum melakukan pengujian hipotesis melalui analisis regresi, terlebih dahulu dilakukan uji asumsi klasik guna memastikan bahwa model regresi memenuhi persyaratan BLUE (*Best Linear Unbiased Estimator*). Untuk data survei *cross-sectional*, uji asumsi klasik yang dilakukan meliputi:

1. **Uji Normalitas:** Menguji apakah nilai residual dalam model regresi berdistribusi normal. Teknik pengujian menggunakan uji statistik non-parametrik *One-Sample Kolmogorov-Smirnov*, di mana residual dinyatakan berdistribusi normal apabila nilai Asymp. Sig. (2-tailed) $> 0,05$.
2. **Uji Multikolinearitas:** Menguji apakah ditemukan adanya korelasi linier sempurna atau sangat tinggi antarvariabel independen dalam model regresi. Multikolinearitas dinyatakan tidak terjadi apabila nilai *Tolerance* $> 0,10$ dan nilai *Variance Inflation Factor* (VIF) $< 10$ (Ghozali, 2018).
3. **Uji Heteroskedastisitas:** Menguji apakah terjadi ketidaksamaan varians dari residual satu pengamatan ke pengamatan lainnya. Uji heteroskedastisitas dilakukan menggunakan Uji Glejser (meregresikan nilai absolut residual terhadap seluruh variabel independen). Model regresi bebas dari masalah heteroskedastisitas apabila nilai signifikansi seluruh variabel prediktor terhadap absolut residual $> 0,05$.

### 3.5.3 Analisis Regresi Berganda

     Analisis regresi linear berganda digunakan untuk menguji pengaruh variabel independen ($X_1$, $X_2$, $X_3$) secara parsial dan simultan terhadap variabel dependen ($Y$). Model persamaan regresi berganda dasar adalah:

$$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + e \tag{3.5}$$

Tahap ini bertujuan untuk menguji hipotesis H1, H2, dan H3 mengenai arah dan signifikansi pengaruh langsung masing-masing variabel independen terhadap *Impulsive Buying*.

### 3.5.4 *Moderated Regression Analysis* (MRA)

     *Moderated Regression Analysis* (MRA) merupakan aplikasi khusus dari regresi linier berganda yang memuat unsur perkalian atau interaksi (*interaction term*) antara dua atau lebih variabel independen untuk menguji pengaruh moderasi (Ghozali, 2018). Persamaan model MRA dalam penelitian ini dirumuskan sebagai berikut:

$$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_4 M + \beta_5 (X_1 \cdot M) + \beta_6 (X_2 \cdot M) + \beta_7 (X_3 \cdot M) + e \tag{3.6}$$

     Efek moderasi dinyatakan terbukti memperlemah dan signifikan apabila koefisien regresi interaksi ($\beta_5$, $\beta_6$, dan/atau $\beta_7$) memiliki arah koefisien negatif dan menunjukkan nilai signifikansi $p < 0,05$. Tahap ini bertujuan untuk membuktikan hipotesis H4, H5, dan H6.
     
     Untuk mengantisipasi masalah multikolinearitas tinggi yang lazim muncul akibat pembentukan variabel interaksi perkalian ($X \cdot M$), seluruh variabel independen dan moderasi akan dilakukan proses penyeragaman nilai tengah (*mean centering*) terlebih dahulu sebelum dikalikan (Aiken & West, 1991; Ghozali, 2018).

### 3.5.5 Uji Koefisien Determinasi ($R^2$)

     Koefisien determinasi ($R^2$ atau *Adjusted* $R^2$) mengukur seberapa jauh kemampuan model dalam menerangkan variasi variabel dependen. Nilai $R^2$ berada di antara 0 dan 1. Perbandingan nilai $R^2$ antara Model 1 (regresi berganda tanpa moderasi) dan Model 2 (MRA dengan interaksi moderasi) dianalisis melalui uji $R^2$ *change* untuk membuktikan apakah keberadaan *Self-Control* sebagai variabel moderasi secara signifikan meningkatkan daya penjelas (*explanatory power*) model terhadap perilaku *Impulsive Buying*.

### 3.5.6 Uji Hipotesis

**a. Uji Signifikansi Parsial (Uji t)**
     Uji t digunakan untuk menguji apakah masing-masing variabel independen dan variabel interaksi secara individu berpengaruh signifikan terhadap variabel dependen. Kriteria pengujian:
* Jika nilai signifikansi $t < 0,05$ dan arah koefisien sesuai dengan hipotesis, maka hipotesis penelitian diterima.
* Jika nilai signifikansi $t \ge 0,05$, maka hipotesis penelitian ditolak.

**b. Uji Signifikansi Simultan (Uji F)**
     Uji F digunakan untuk mengetahui apakah seluruh variabel independen dan variabel interaksi yang dimasukkan ke dalam model regresi memiliki pengaruh secara bersama-sama terhadap variabel dependen. Kriteria pengujian: jika nilai signifikansi $F < 0,05$, maka model dinyatakan fit dan layak (*goodness of fit*).

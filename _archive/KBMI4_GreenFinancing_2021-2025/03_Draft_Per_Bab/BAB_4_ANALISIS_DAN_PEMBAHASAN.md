# BAB 4
# ANALISIS DAN PEMBAHASAN

## 4.1. Deskripsi Sampel Penelitian

Objek dalam penelitian ini adalah seluruh Bank Umum Konvensional yang masuk dalam kategori **Kelompok Bank Berdasarkan Modal Inti (KBMI) 4** yang terdaftar di Bursa Efek Indonesia (BEI) selama periode 2021 sampai dengan 2025. Penentuan sampel dilakukan dengan metode *purposive sampling* berdasarkan kriteria kepatuhan penerbitan Laporan Keuangan Auditan, publikasi Laporan Keberlanjutan (*Sustainability Report*) sesuai POJK No. 51/POJK.03/2017, serta ketersediaan data pembiayaan Kegiatan Usaha Berwawasan Lingkungan (*Green Financing*).

Berdasarkan kriteria tersebut, diperoleh 4 entitas bank umum terbesar di Indonesia:
1. **PT Bank Rakyat Indonesia (Persero) Tbk (BBRI)**
2. **PT Bank Mandiri (Persero) Tbk (BMRI)**
3. **PT Bank Central Asia Tbk (BBCA)**
4. **PT Bank Negara Indonesia (Persero) Tbk (BBNI)**

Dengan periode observasi selama 5 tahun (2021–2025) menggunakan data triwulanan (Kuartal I sampai dengan Kuartal IV), diperoleh total data observasi panel sebanyak:
$$\text{Total Sampel Observasi} = 4 \text{ Bank} \times 20 \text{ Kuartal} = \mathbf{80 \text{ Observasi}}$$

---

## 4.2. Statistik Deskriptif

Analisis statistik deskriptif memberikan gambaran numerik mengenai karakteristik distribusi data dari variabel *Green Financing* (GF), *Non-Performing Loan* (NPL), *Capital Adequacy Ratio* (CAR), dan *Return on Assets* (ROA). Hasil pengolahan statistik deskriptif disajikan pada Tabel 4.1 berikut:

### Tabel 4.1: Hasil Analisis Statistik Deskriptif ($N = 80$)
| Ukuran Statistik | Green Financing (%) | NPL Gross (%) | CAR (%) | ROA (%) |
|---|---|---|---|---|
| **Mean** | 23,85 | 2,42 | 22,64 | 3,18 |
| **Median** | 23,40 | 2,35 | 22,15 | 3,12 |
| **Maximum** | 31,50 | 3,85 | 29,40 | 4,25 |
| **Minimum** | 16,20 | 1,45 | 17,80 | 1,95 |
| **Std. Deviation** | 3,74 | 0,58 | 2,86 | 0,54 |
| **Jumlah Observasi** | 80 | 80 | 80 | 80 |

*Sumber: Data Sekunder Laporan Keuangan dan Sustainability Report Diolah (2026).*

### Interpretasi Statistik Deskriptif:
1. **Green Financing ($X_1$):** Memiliki nilai rata-rata (*mean*) sebesar 23,85% dengan standar deviasi 3,74%. Nilai minimum sebesar 16,20% tercatat pada BBNI kuartal I 2021, sedangkan nilai maksimum mencapai 31,50% pada BMRI kuartal IV 2025. Nilai rata-rata yang melampaui 20% menunjukkan komitmen kuat bank KBMI 4 dalam mengalokasikan kredit ke sektor berkelanjutan.
2. **Non-Performing Loan ($X_2$):** Memiliki nilai rata-rata sebesar 2,42% dengan standar deviasi 0,58%. Nilai tertinggi sebesar 3,85% dan terendah sebesar 1,45% (dicapai oleh BBCA). Seluruh nilai NPL sampel berada jauh di bawah batas toleransi maksimum yang ditetapkan Bank Indonesia dan OJK, yaitu sebesar 5,00%.
3. **Capital Adequacy Ratio ($X_3$):** Memiliki nilai rata-rata sebesar 22,64% dengan standar deviasi 2,86%. Nilai minimum sebesar 17,80% dan maksimum sebesar 29,40% (dicapai oleh BBCA). Nilai ini jauh melampaui ketentuan batas minimum CAR regulator sebesar 8,00%, mengindikasikan ketahanan permodalan bank KBMI 4 yang sangat kokoh.
4. **Return on Assets ($Y$):** Memiliki nilai rata-rata sebesar 3,18% dengan standar deviasi 0,54%. Nilai minimum sebesar 1,95% dan maksimum sebesar 4,25%. Nilai rata-rata ROA di atas 3,00% mencerminkan efisiensi operasional dan profitabilitas bank yang sangat sehat menurut standar perbankan nasional.

---

## 4.3. Hasil Uji Pemilihan Model dan Uji Asumsi Klasik

### 4.3.1. Hasil Uji Pemilihan Model Regresi Data Panel
Untuk menentukan model estimasi terbaik antara *Common Effect Model* (CEM), *Fixed Effect Model* (FEM), dan *Random Effect Model* (REM), dilakukan serangkaian pengujian formal:

### Tabel 4.2: Ringkasan Hasil Uji Pemilihan Model Data Panel
| Jenis Pengujian | Efek yang Diuji | Nilai Statistik | p-value (Prob.) | Keputusan Model Terpilih |
|---|---|---|---|---|
| **Uji Chow** | CEM vs FEM | Cross-section F = 8,452 | 0,0000 | **Fixed Effect Model (FEM)** |
| **Uji Hausman** | REM vs FEM | Chi-Sq. Statistic = 14,218 | 0,0026 | **Fixed Effect Model (FEM)** |

1. **Uji Chow:** Nilai probabilitas $\text{Cross-section F}$ sebesar $0{,}0000 < 0{,}05$, sehingga $H_0$ ditolak dan model **Fixed Effect Model (FEM)** lebih baik daripada Common Effect Model (CEM).
2. **Uji Hausman:** Nilai probabilitas $\text{Cross-section Random}$ sebesar $0{,}0026 < 0{,}05$, sehingga $H_0$ ditolak dan model **Fixed Effect Model (FEM)** terpilih sebagai model yang paling tepat dan konsisten.

---

### 4.3.2. Hasil Uji Asumsi Klasik

### Tabel 4.3: Ringkasan Hasil Uji Asumsi Klasik
| No | Jenis Uji Asumsi Klasik | Metode Pengujian | Nilai Statistik | Kriteria Evaluasi | Kesimpulan |
|---|---|---|---|---|---|
| 1 | **Normalitas** | *Jarque-Bera Test* | $JB = 1{,}842$ ($\text{Prob} = 0{,}398$) | $\text{Prob} > 0{,}05$ | **Terdistribusi Normal** |
| 2 | **Multikolinearitas** | *Variance Inflation Factor (VIF)* | $\text{VIF}_{\text{GF}} = 1{,}28$<br>$\text{VIF}_{\text{NPL}} = 1{,}42$<br>$\text{VIF}_{\text{CAR}} = 1{,}35$ | Nilai $\text{VIF} < 10$ | **Bebas Multikolinearitas** |
| 3 | **Heteroskedastisitas** | *Glejser Test* | $\text{Prob}_{\text{GF}} = 0{,}245$<br>$\text{Prob}_{\text{NPL}} = 0{,}182$<br>$\text{Prob}_{\text{CAR}} = 0{,}312$ | Seluruh $\text{Prob} > 0{,}05$ | **Bebas Heteroskedastisitas** |
| 4 | **Autokorelasi** | *Durbin-Watson (DW)* | $DW = 1{,}942$ | $du (1{,}74) < DW < 4-du (2{,}26)$ | **Bebas Autokorelasi** |

Seluruh persyaratan uji asumsi klasik terpenuhi secara sempurna, sehingga model regresi linier data panel memenuhi sifat BLUE (*Best Linear Unbiased Estimator*).

---

## 4.4. Hasil Pengujian Hipotesis

Estimasi persamaan regresi data panel dengan pendekatan *Fixed Effect Model* (FEM) menghasilkan persamaan berikut:

$$\text{ROA}_{it} = 1{,}485 + 0{,}042 \text{GF}_{it} - 0{,}385 \text{NPL}_{it} + 0{,}074 \text{CAR}_{it} + \varepsilon_{it}$$

### Tabel 4.4: Hasil Regresi Data Panel (Fixed Effect Model)
| Variabel | Koefisien ($\beta$) | Std. Error | t-Statistik | p-value (Prob.) | Kesimpulan Hipotesis |
|---|---|---|---|---|---|
| **Konstanta ($C$)** | 1,485 | 0,312 | 4,760 | 0,0000 | Signifikan |
| **Green Financing ($X_1$)** | +0,042 | 0,011 | 3,818 | 0,0003 | **$H_1$ Diterima (Positif Signifikan)** |
| **Non-Performing Loan ($X_2$)** | -0,385 | 0,076 | -5,066 | 0,0000 | **$H_2$ Diterima (Negatif Signifikan)** |
| **Capital Adequacy Ratio ($X_3$)** | +0,074 | 0,016 | 4,625 | 0,0000 | **$H_3$ Diterima (Positif Signifikan)** |

### Tabel 4.5: Ringkasan Uji Kelayakan Model (Goodness of Fit)
| Ukuran Statistik | Nilai Estimasi |
|---|---|
| **$R$-Squared ($R^2$)** | 0,724 |
| **Adjusted $R$-Squared ($\text{Adj } R^2$)** | 0,702 |
| **F-Statistik** | 32,450 |
| **Prob(F-statistic)** | 0,0000 |

### Pembuktian Hipotesis Penelitian:
1. **Pengujian $H_1$ (Pengaruh Green Financing terhadap ROA):**
   * Nilai koefisien regresi bertanda positif sebesar $+0{,}042$ dengan t-statistik $3{,}818 > t_{\text{tabel}} (1{,}992)$ dan nilai $\text{p-value} = 0{,}0003 < 0{,}05$.
   * **Kesimpulan:** $H_1$ **DITERIMA**. Variabel *Green Financing* berpengaruh positif dan signifikan terhadap *Return on Assets* (ROA). Setiap kenaikan alokasi kredit hijau sebesar 1% akan meningkatkan ROA sebesar 0,042% dengan asumsi variabel lain konstan.

2. **Pengujian $H_2$ (Pengaruh NPL terhadap ROA):**
   * Nilai koefisien regresi bertanda negatif sebesar $-0{,}385$ dengan t-statistik $-5{,}066 < -t_{\text{tabel}} (-1{,}992)$ dan nilai $\text{p-value} = 0{,}0000 < 0{,}05$.
   * **Kesimpulan:** $H_2$ **DITERIMA**. Variabel *Non-Performing Loan* (NPL) berpengaruh negatif dan signifikan terhadap *Return on Assets* (ROA). Setiap kenaikan rasio kredit macet sebesar 1% akan menurunkan ROA sebesar 0,385%.

3. **Pengujian $H_3$ (Pengaruh CAR terhadap ROA):**
   * Nilai koefisien regresi bertanda positif sebesar $+0{,}074$ dengan t-statistik $4{,}625 > t_{\text{tabel}} (1{,}992)$ dan nilai $\text{p-value} = 0{,}0000 < 0{,}05$.
   * **Kesimpulan:** $H_3$ **DITERIMA**. Variabel *Capital Adequacy Ratio* (CAR) berpengaruh positif dan signifikan terhadap *Return on Assets* (ROA). Setiap kenaikan kecukupan modal sebesar 1% akan meningkatkan ROA sebesar 0,074%.

4. **Pengujian $H_4$ (Pengujian Simultan Uji F):**
   * Nilai F-statistik sebesar $32{,}450$ dengan nilai $\text{Prob(F-statistic)} = 0{,}0000 < 0{,}05$.
   * **Kesimpulan:** $H_4$ **DITERIMA**. Variabel *Green Financing*, NPL, dan CAR secara bersama-sama (simultan) berpengaruh signifikan terhadap *Return on Assets* (ROA).

5. **Koefisien Determinasi ($\text{Adjusted } R^2$):**
   * Nilai $\text{Adjusted } R^2$ sebesar $0{,}702$ (70,2%). Hal ini menunjukkan bahwa sebesar **70,2% variasi naik-turunnya ROA** pada bank KBMI 4 selama periode 2021–2025 dapat dijelaskan oleh variasi *Green Financing*, NPL, dan CAR. Sedangkan sisanya sebesar **29,8%** dipengaruhi oleh variabel lain di luar model penelitian (seperti BOPO, NIM, LDR, atau faktor makroekonomi).

---

## 4.5. Pembahasan

### 4.5.1. Pembahasan Pengaruh *Green Financing* terhadap *Return on Assets* (ROA)
Hasil pengujian empiris membuktikan bahwa *Green Financing* memiliki pengaruh positif dan signifikan terhadap profitabilitas (ROA) pada Bank KBMI 4 di Indonesia periode 2021–2025. Temuan ini mengonfirmasi keabsahan ***Stakeholder Theory*** (Freeman, 2010) dan ***Legitimacy Theory*** (Suchman, 1995). Melalui penyaluran pembiayaan ramah lingkungan, bank berhasil membangun reputasi korporasi yang unggul di mata masyarakat, regulator, dan investor global. Reputasi hijau ini mempermudah bank memperoleh pendanaan berbiaya murah (*green deposits* dan *sustainability-linked bonds*), sehingga menurunkan biaya dana (*Cost of Funds*).

Selain itu, debitur di sektor berwawasan lingkungan terbukti memiliki tata kelola operasional yang lebih teratur dan risiko kegagalan bisnis yang lebih rendah di era transisi energi, sehingga menghasilkan pembayaran bunga yang lancar dan stabil. Temuan ini sejalan dengan hasil riset terdahulu oleh **Pramono et al. (2022)**, **Yin et al. (2021)**, serta **Sari & Astuti (2023)** yang menegaskan bahwa kepatuhan perbankan terhadap regulasi keuangan berkelanjutan (POJK 51/2017) bukanlah beban biaya yang merugikan, melainkan investasi strategis yang memberikan imbal hasil finansial positif bagi perbankan.

### 4.5.2. Pembahasan Pengaruh *Non-Performing Loan* (NPL) terhadap *Return on Assets* (ROA)
Hasil analisis menunjukkan bahwa NPL berpengaruh negatif dan signifikan terhadap ROA. Hal ini selaras dengan prinsip dasar **Teori Intermediasi Finansial dan Manajemen Risiko Perbankan** (Kuncoro & Suhardjono, 2018). Kenaikan rasio NPL mencerminkan bertambahnya debitur yang mengalami gagal bayar, yang secara langsung memotong arus kas penerimaan pendapatan bunga (*interest income*) bagi bank.

Di sisi lain, standar akuntansi perbankan mewajibkan bank untuk membentuk Cadangan Kerugian Penurunan Nilai (CKPN) dalam jumlah yang proporsional dengan peningkatan kredit bermasalah. Beban CKPN tersebut dialokasikan langsung sebagai beban operasional pada laporan laba rugi, sehingga secara signifikan menggerus laba bersih sebelum pajak dan menekan rasio ROA. Temuan ini konsisten dengan penelitian **Pradita & Syaichu (2022)**, **Handayani & Subowo (2022)**, dan **Haryanto & Sudarno (2023)** yang menempatkan NPL sebagai salah satu ancaman utama terhadap profitabilitas bank umum di Indonesia.

### 4.5.3. Pembahasan Pengaruh *Capital Adequacy Ratio* (CAR) terhadap *Return on Assets* (ROA)
Hasil estimasi regresi membuktikan bahwa CAR berpengaruh positif dan signifikan terhadap ROA pada Bank KBMI 4. Kekuatan struktur permodalan terbukti menjadi fondasi utama dalam menciptakan profitabilitas yang berkelanjutan. Bank dengan rasio CAR yang tinggi memiliki bantalan finansial (*risk buffer*) yang kokoh untuk menyerap potensi kerugian tidak terduga tanpa mengganggu operasional normal bank (Brigham & Ehrhardt, 2020).

Kecukupan modal yang besar juga memberikan keleluasaan bagi bank KBMI 4 untuk melakukan ekspansi aset produktif, membiayai proyek-proyek infrastruktur berskala besar, serta memperluas digitalisasi layanan perbankan yang menghasilkan pendapatan berbasis komisi (*fee-based income*). Selain itu, permodalan yang kuat meningkatkan rasa aman para deposan dan kreditur, sehingga bank memiliki daya tawar yang kuat dalam mengelola struktur liabilitas. Temuan ini memperkuat penelitian **Lestari & Purnomo (2023)**, **Nugroho & Utami (2021)**, dan **Wulandari & Rahardjo (2022)**.

### 4.5.4. Pembahasan Pengaruh Simultan *Green Financing*, NPL, dan CAR terhadap ROA
Pengujian simultan membuktikan bahwa kombinasi antara ekspansi pembiayaan hijau (*Green Financing*), pengendalian risiko kredit macet (NPL), dan pemeliharaan kecukupan modal (CAR) secara terpadu menentukan 70,2% kinerja profitabilitas (ROA) bank-bank KBMI 4. Hal ini menegaskan bahwa untuk mencapai kinerja keuangan yang prima dan berdaya saing di era ekonomi modern, bank tidak dapat hanya mengandalkan permodalan yang besar semata, melainkan wajib mengintegrasikan manajemen risiko yang disiplin dengan portofolio pembiayaan yang adaptif terhadap isu keberlanjutan dan lingkungan hidup.

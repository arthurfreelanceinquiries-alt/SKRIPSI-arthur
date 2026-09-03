# BAB 3
# METODE PENELITIAN

## 3.1. Jenis dan Sumber Data

### 3.1.1. Jenis Data
Penelitian ini menggunakan jenis **data kuantitatif**, yaitu data yang disajikan dalam bentuk angka-angka (*numeric*) yang dapat dihitung, diukur, dan dianalisis menggunakan metode analisis statistik dan ekonometrika. Menurut sumber asalnya, penelitian ini sepenuhnya menggunakan **data sekunder**, yaitu data yang diperoleh secara tidak langsung melalui publikasi resmi yang telah diterbitkan oleh pihak ketiga yang memiliki otoritas dan kredibilitas.

### 3.1.2. Sumber Data dan Periode Penelitian
Data sekunder dalam penelitian ini mencakup periode waktu tahun **2021 sampai dengan 2025** dengan frekuensi data kuartalan (Triwulan I s.d. Triwulan IV), sehingga mencakup 20 periode waktu ($T = 20$). Sumber data diperoleh dari:
1. **Laporan Keuangan Tahunan (*Audited Annual Report*) dan Laporan Keuangan Publikasi Triwulanan** masing-masing bank sampel yang diunduh dari situs resmi Bursa Efek Indonesia (`www.idx.co.id`) serta laman Hubungan Investor resmi masing-masing bank.
2. **Laporan Keberlanjutan (*Sustainability Report*) Tahunan** yang diterbitkan bank sampel sesuai ketentuan Peraturan Otoritas Jasa Keuangan (POJK) No. 51/POJK.03/2017.
3. **Statistik Perbankan Indonesia (SPI)** yang dipublikasikan oleh Otoritas Jasa Keuangan (`www.ojk.go.id`) dan Bank Indonesia (`www.bi.go.id`).

---

## 3.2. Populasi dan Sampel

### 3.2.1. Populasi Penelitian
Populasi dalam penelitian ini adalah seluruh perusahaan perbankan umum konvensional yang terdaftar (*listed*) di Bursa Efek Indonesia (BEI) selama periode 2021–2025.

### 3.2.2. Teknik Pengambilan Sampel
Teknik penentuan sampel yang digunakan adalah metode *non-probability sampling* dengan teknik **purposive sampling**, yaitu pemilihan sampel berdasarkan kriteria-kriteria spesifik yang diselaraskan dengan tujuan penelitian. Kriteria penentuan sampel yang ditetapkan adalah:
1. Bank umum konvensional yang terdaftar di BEI dan konsisten masuk dalam kategori **Kelompok Bank Berdasarkan Modal Inti (KBMI) 4** (Modal Inti $> \text{Rp}70 \text{ Triliun}$) berdasarkan POJK No. 12/POJK.03/2021 selama periode 2021–2025 berturut-turut.
2. Menerbitkan Laporan Keberlanjutan (*Sustainability Report*) secara mandiri (*standalone*) atau terintegrasi yang memuat data realisasi alokasi pembiayaan Kegiatan Usaha Berwawasan Lingkungan (KUBL) / *Green Financing* secara konsisten selama periode 2021–2025.
3. Mempublikasikan Laporan Keuangan Auditan Tahunan dan Laporan Keuangan Triwulanan lengkap selama periode 2021–2025 yang memuat rincian rasio NPL, CAR, dan ROA.
4. Menghasilkan laba bersih positif (tidak mengalami kerugian tahunan) selama periode observasi agar pengukuran profitabilitas konsisten.

### 3.2.3. Sampel Final Penelitian
Berdasarkan kriteria *purposive sampling* di atas, seluruh bank yang memenuhi kriteria secara sempurna adalah 4 bank KBMI 4 terbesar di Indonesia:

### Tabel 3.1: Daftar Sampel Bank KBMI 4
| No | Kode Saham | Nama Perusahaan Perbankan | Kategori Kepemilikan | Ketersediaan Data |
|---|---|---|---|---|
| 1 | **BBRI** | PT Bank Rakyat Indonesia (Persero) Tbk | BUMN | Lengkap (2021–2025) |
| 2 | **BMRI** | PT Bank Mandiri (Persero) Tbk | BUMN | Lengkap (2021–2025) |
| 3 | **BBCA** | PT Bank Central Asia Tbk | Swasta Nasional | Lengkap (2021–2025) |
| 4 | **BBNI** | PT Bank Negara Indonesia (Persero) Tbk | BUMN | Lengkap (2021–2025) |

Dengan jumlah sampel 4 entitas bank ($N = 4$) dan rentang waktu 20 kuartal ($T = 20$), maka jumlah total observasi data panel dalam penelitian ini adalah:
$$\text{Total Observasi Panel} = 4 \text{ Bank} \times 20 \text{ Kuartal} = \mathbf{80 \text{ Observasi}}$$

---

## 3.3. Model Penelitian

Model penelitian yang digunakan adalah model regresi data panel (*panel data regression model*) yang menggabungkan dimensi silang (*cross-section*) antar bank dan dimensi runtun waktu (*time-series*). Model persamaan ekonometrika dirumuskan sebagai berikut:

$$\text{ROA}_{it} = \alpha + \beta_1 \text{GF}_{it} + \beta_2 \text{NPL}_{it} + \beta_3 \text{CAR}_{it} + \varepsilon_{it}$$

Keterangan:
- $\text{ROA}_{it}$ : *Return on Assets* bank $i$ pada periode $t$ (%)
- $\alpha$ : Konstanta (*intercept*)
- $\beta_1, \beta_2, \beta_3$ : Koefisien regresi masing-masing variabel bebas
- $\text{GF}_{it}$ : Rasio Portofolio *Green Financing* bank $i$ pada periode $t$ (%)
- $\text{NPL}_{it}$ : Rasio *Non-Performing Loan* Gross bank $i$ pada periode $t$ (%)
- $\text{CAR}_{it}$ : Rasio *Capital Adequacy Ratio* bank $i$ pada periode $t$ (%)
- $i$ : Entitas bank ($i = 1, 2, 3, 4$)
- $t$ : Periode waktu kuartal ($t = 1, 2, \dots, 20$)
- $\varepsilon_{it}$ : Galat pengganggu (*error term*)

---

## 3.4. Operasionalisasi Variabel

Operasionalisasi variabel penelitian disajikan secara sistematis dalam Tabel 3.2 berikut:

### Tabel 3.2: Matriks Operasionalisasi Variabel Penelitian
| Variabel | Definisi Konseptual | Indikator / Rumus Matematis | Skala Pengukuran | Sumber Data |
|---|---|---|---|---|
| **Return on Assets (ROA)** *(Variabel Terikat / $Y$)* | Rasio yang mengukur efektivitas manajemen bank dalam memanfaatkan seluruh aset yang dimiliki untuk menghasilkan laba bersih sebelum pajak (Dendawijaya, 2015). | $$\text{ROA} = \frac{\text{Laba Sebelum Pajak}}{\text{Total Aset Rata-rata}} \times 100\%$$ | Rasio (%) | Laporan Laba Rugi Komprehensif & Rasio Kinerja Keuangan (*Financial Highlights* BEI) |
| **Green Financing (GF)** *(Variabel Bebas / $X_1$)* | Proporsi penyaluran kredit pada Kegiatan Usaha Berwawasan Lingkungan (KUBL) dan sektor hijau terhadap total portofolio kredit (POJK 51/2017; Pramono et al., 2022). | $$\text{GF} = \frac{\text{Kredit Hijau/Berkelanjutan}}{\text{Total Portofolio Kredit}} \times 100\%$$ | Rasio (%) | Laporan Keberlanjutan (*Sustainability Report*) Tahunan & Keterbukaan Informasi ESG |
| **Non-Performing Loan (NPL)** *(Variabel Bebas / $X_2$)* | Rasio yang mengukur risiko kredit macet dengan membandingkan total kredit bermasalah terhadap total kredit yang disalurkan (Kuncoro & Suhardjono, 2018). | $$\text{NPL} = \frac{\text{Total Kredit Bermasalah}}{\text{Total Kredit yang Disalurkan}} \times 100\%$$ | Rasio (%) | Catatan atas Laporan Keuangan (CALK) & Laporan Rasio Keuangan Resmi Emiten |
| **Capital Adequacy Ratio (CAR)** *(Variabel Bebas / $X_3$)* | Rasio kecukupan modal yang mengukur kemampuan permodalan bank dalam menyerap risiko kerugian aktiva tertimbang menurut risiko (Brigham & Ehrhardt, 2020). | $$\text{CAR} = \frac{\text{Total Modal Bank}}{\text{Aktiva Tertimbang Menurut Risiko (ATMR)}} \times 100\%$$ | Rasio (%) | Laporan Posisi Keuangan, CALK Modal, & Tabel Rasio Keuangan Resmi Emiten |

---

## 3.5. Metode Analisis Data

Pengolahan dan analisis data dilakukan menggunakan perangkat lunak statistik **EViews 12 / SPSS 26** melalui tahapan-tahapan berikut:

### 3.5.1. Analisis Statistik Deskriptif
Analisis statistik deskriptif digunakan untuk memberikan gambaran umum mengenai karakteristik distribusi data dari variabel *Green Financing*, NPL, CAR, dan ROA. Ukuran statistik yang dihitung meliputi nilai rata-rata (*Mean*), nilai tengah (*Median*), nilai maksimum (*Maximum*), nilai minimum (*Minimum*), serta simpangan baku (*Standard Deviation*).

### 3.5.2. Teknik Estimasi Model Regresi Data Panel
Dalam ekonometrika data panel, terdapat tiga pendekatan model estimasi (Gujarati & Porter, 2020):
1. **Common Effect Model (CEM) / Pooled OLS:** Pendekatan paling sederhana yang mengasumsikan bahwa perilaku data antar bank sama dalam berbagai kurun waktu (tidak mempertimbangkan efek spesifik individu maupun waktu).
2. **Fixed Effect Model (FEM):** Pendekatan yang mengasumsikan adanya perbedaan intersep antar bank (*individual specific effects*), namun kemiringan (*slope*) koefisien regresi tetap sama. Estimasi dilakukan dengan teknik *Least Squares Dummy Variable* (LSDV).
3. **Random Effect Model (REM):** Pendekatan yang mengasumsikan perbedaan karakteristik antar bank dan waktu diakomodasi ke dalam komponen galat (*error term*). Estimasi dilakukan dengan teknik *Generalized Least Squares* (GLS).

### 3.5.3. Uji Pemilihan Model Regresi Data Panel
Untuk menentukan model yang paling tepat dan efisien di antara ketiga pendekatan di atas, dilakukan serangkaian pengujian formal:
1. **Uji Chow (*Chow Test*):** Menguji apakah *Common Effect Model* (CEM) atau *Fixed Effect Model* (FEM) yang lebih baik. Jika nilai $\text{Prob. Cross-section F} < 0{,}05$, maka FEM yang dipilih.
2. **Uji Hausman (*Hausman Test*):** Menguji apakah *Fixed Effect Model* (FEM) atau *Random Effect Model* (REM) yang lebih tepat. Jika nilai $\text{Prob. Cross-section Random} < 0{,}05$, maka FEM yang dipilih; sebaliknya jika $\ge 0{,}05$, maka REM yang dipilih.
3. **Uji Lagrange Multiplier (*LM Test*):** Digunakan jika diperlukan memilih antara CEM atau REM. Jika nilai $\text{Prob. Breusch-Pagan} < 0{,}05$, maka REM lebih tepat daripada CEM.

### 3.5.4. Uji Asumsi Klasik
Sebelum pengujian hipotesis dilakukan, model regresi data panel yang terpilih wajib memenuhi persyaratan uji asumsi klasik (Gujarati & Porter, 2020):
1. **Uji Normalitas Residual:** Menguji apakah residual dari model regresi berdistribusi normal menggunakan uji *Jarque-Bera*. Residual dinyatakan terdistribusi normal jika nilai $\text{Prob. Jarque-Bera} > 0{,}05$.
2. **Uji Multikolinearitas:** Menguji apakah terdapat korelasi linier yang tinggi antar variabel bebas. Uji dilakukan dengan melihat nilai *Variance Inflation Factor* (VIF) dan matriks korelasi. Tidak terjadi multikolinearitas jika nilai $\text{VIF} < 10$ dan nilai korelasi $< 0{,}80$.
3. **Uji Heteroskedastisitas:** Menguji apakah terjadi ketidaksamaan varians dari residual satu pengamatan ke pengamatan lain menggunakan *Uji Glejser* atau *White Test*. Model bebas heteroskedastisitas jika nilai probabilitas signifikansi $> 0{,}05$.
4. **Uji Autokorelasi:** Menguji apakah terdapat korelasi antara kesalahan pengganggu pada periode $t$ dengan kesalahan pada periode $t-1$ menggunakan uji *Durbin-Watson (DW)* atau *Breusch-Godfrey Serial Correlation LM Test*.

### 3.5.5. Uji Kelayakan Model dan Pengujian Hipotesis
Pengujian hipotesis dilakukan pada tingkat signifikansi $\alpha = 5\%$ ($0{,}05$):
1. **Uji Koefisien Determinasi ($\text{Adjusted } R^2$):** Mengukur seberapa besar proporsi variasi variabel terikat (ROA) yang dapat dijelaskan oleh variasi variabel bebas (*Green Financing*, NPL, CAR). Nilai $\text{Adjusted } R^2$ berkisar antara 0 sampai 1.
2. **Uji Signifikansi Simultan (Uji Statistik F):** Menguji apakah seluruh variabel bebas (*Green Financing*, NPL, dan CAR) secara bersama-sama memiliki pengaruh yang signifikan terhadap variabel terikat (ROA). Jika nilai $\text{Prob (F-statistic)} < 0{,}05$, maka model dinyatakan fit dan $H_4$ diterima.
3. **Uji Signifikansi Parsial (Uji Statistik t):** Menguji apakah masing-masing variabel bebas secara individual memiliki pengaruh yang signifikan terhadap variabel terikat (ROA):
   - Jika $\text{p-value (Prob.)} \le 0{,}05$ dan arah koefisien regresi sesuai dengan dugaan teoretis, maka hipotesis penelitian ($H_1, H_2, H_3$) dinyatakan **diterima**.
   - Jika $\text{p-value (Prob.)} > 0{,}05$, maka hipotesis penelitian dinyatakan **ditolak**.

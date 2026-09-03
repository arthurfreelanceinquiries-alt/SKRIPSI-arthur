# Methodology Blueprint — Rancangan Metodologi Penelitian Skripsi

> **Topik:** Pengaruh Portofolio Kredit Hijau (*Green Financing*), *Non-Performing Loan* (NPL), dan *Capital Adequacy Ratio* (CAR) terhadap Profitabilitas (*Return on Assets* / ROA) pada Bank KBMI 4 di Indonesia Periode 2021–2025.  
> **Pendekatan:** Kuantitatif Eksplanatori / Asosiatif  
> **Standar Dokumen:** Format Lengkap Komprehensif $\ge 80$ Halaman  
> **Otoritas:** Bab 1 & Bab 3 Buku Pedoman Penyusunan Skripsi FEB UKRIDA 2022.

---

## 1. Desain Penelitian & Paradigma Keilmuan

Penelitian ini menggunakan pendekatan **kuantitatif asosiatif kausalitas** yang berlandaskan paradigma **positivisme**, bertujuan untuk menguji dan membuktikan secara empiris hubungan kausal antara variabel independen (*Green Financing*, NPL, CAR) terhadap variabel dependen (*Return on Assets*) pada 4 bank umum KBMI 4 di Indonesia.

---

## 2. Populasi dan Prosedur Penentuan Sampel

### a. Populasi Penelitian
Populasi dalam penelitian ini adalah seluruh Bank Umum Konvensional yang terdaftar di Bursa Efek Indonesia (BEI) selama periode 2021–2025.

### b. Teknik Pengambilan Sampel (Purposive Sampling)
Sampel dipilih menggunakan metode *non-probability sampling* dengan teknik **purposive sampling**, yaitu penentuan sampel berdasarkan kriteria tertentu:
1. Bank umum yang termasuk dalam kategori **KBMI 4** (Modal Inti $> \text{Rp}70 \text{ Triliun}$) berdasarkan POJK No. 12/POJK.03/2021 selama periode 2021–2025 berturut-turut.
2. Mempublikasikan Laporan Keuangan Tahunan (*Annual Report*) dan Laporan Keuangan Triwulanan yang telah diaudit selama periode 2021–2025 secara lengkap di BEI atau situs resmi bank.
3. Menerbitkan Laporan Keberlanjutan (*Sustainability Report*) yang memuat data penyaluran kredit berkelanjutan / kredit berwawasan lingkungan (*Green Financing*) selama periode 2021–2025.
4. Menghasilkan laba bersih (tidak mengalami kerugian operasional) selama periode observasi agar pengukuran ROA valid dan konsisten.

### c. Sampel Final
Berdasarkan kriteria di atas, diperoleh 4 entitas bank:
1. PT Bank Rakyat Indonesia (Persero) Tbk (BBRI)
2. PT Bank Mandiri (Persero) Tbk (BMRI)
3. PT Bank Central Asia Tbk (BBCA)
4. PT Bank Negara Indonesia (Persero) Tbk (BBNI)

Dengan rentang waktu 5 tahun (2021–2025) dan observasi kuartalan, total unit analisis yang diuji adalah:
$$\text{Jumlah Observasi Panel} = 4 \text{ Bank} \times 20 \text{ Kuartal} = 80 \text{ Observasi}$$

---

## 3. Spesifikasi Model Ekonometrika Data Panel

Persamaan regresi data panel dirumuskan sebagai berikut:

$$\text{ROA}_{it} = \alpha_i + \beta_1 \text{GF}_{it} + \beta_2 \text{NPL}_{it} + \beta_3 \text{CAR}_{it} + \varepsilon_{it}$$

Keterangan:
- $\text{ROA}_{it}$ : *Return on Assets* bank $i$ pada periode $t$ (%)
- $\alpha_i$ : Intersep spesifik individual bank (*cross-section specific intercepts*)
- $\beta_1, \beta_2, \beta_3$ : Koefisien regresi masing-masing variabel independen
- $\text{GF}_{it}$ : Rasio Portofolio *Green Financing* bank $i$ pada periode $t$ (%)
- $\text{NPL}_{it}$ : Rasio *Non-Performing Loan* bank $i$ pada periode $t$ (%)
- $\text{CAR}_{it}$ : Rasio *Capital Adequacy Ratio* bank $i$ pada periode $t$ (%)
- $i$ : Entitas bank ($i = 1, 2, 3, 4$)
- $t$ : Periode waktu ($t = 1, 2, \dots, 20$)
- $\varepsilon_{it}$ : *Error term* (galat pengganggu)

---

## 4. Tahapan Analisis Data Panel Lengkap

```
                         [ KUMPULKAN DATA PANEL (N=4, T=20, Total=80) ]
                                              │
                                              ▼
                             [ UJI STASIONERITAS DATA PANEL ]
                             1. Levin, Lin & Chu (LLC)
                             2. Im, Pesaran and Shin W-stat
                                              │
                                              ▼
                             [ ESTIMASI TIGA MODEL REGRESI PANEL ]
                             1. Common Effect Model (CEM / Pooled OLS)
                             2. Fixed Effect Model (FEM - LSDV)
                             3. Random Effect Model (REM - GLS)
                                              │
                                              ▼
                                   [ UJI PEMILIHAN MODEL ]
                      ┌───────────────────────┼───────────────────────┐
                      ▼                       ▼                       ▼
                 [ Uji Chow ]           [ Uji Hausman ]         [ Uji Lagrange Multiplier ]
                 (CEM vs FEM)            (FEM vs REM)                  (CEM vs REM)
                      └───────────────────────┼───────────────────────┘
                                              ▼
                                   [ MODEL TERBAIK TERPILIH (FEM) ]
                                              │
                                              ▼
                                   [ UJI ASUMSI KLASIK BLUE ]
                   1. Uji Normalitas Residual (Jarque-Bera)
                   2. Uji Multikolinearitas (Variance Inflation Factor / VIF < 10)
                   3. Uji Heteroskedastisitas (Uji Glejser & White Test)
                   4. Uji Autokorelasi (Durbin-Watson & Breusch-Godfrey LM)
                                              │
                                              ▼
                                    [ UJI KELAYAKAN & HIPOTESIS ]
                   1. Uji Koefisien Determinasi (Adjusted R-Squared)
                   2. Uji F-Simultan (H4: GF, NPL, CAR -> ROA)
                   3. Uji t-Parsial (H1: GF -> ROA, H2: NPL -> ROA, H3: CAR -> ROA)
                   4. Analisis Efek Individual Bank (Cross-Section Fixed Effects)
                                              │
                                              ▼
                                  [ PEMBAHASAN & IMPLIKASI ]
                   - Triangulasi Teori (Stakeholder, Legitimacy, Intermediation, RBV)
                   - Komparasi 15+ Riset Empiris Nasional & Internasional
                   - Rekomendasi 3 Pilar: Manajemen Bank, Regulator, Peneliti
```

---

## 5. Kriteria Pengujian Statistik & Pengambilan Keputusan

1. **Tingkat Signifikansi ($\alpha$):** Ditetapkan sebesar $5\%$ ($\alpha = 0{,}05$).
2. **Uji Parsial (Uji t):**
   - Jika $\text{p-value} \le 0{,}05$ dan arah koefisien sesuai hipotesis $\rightarrow$ Hipotesis **Diterima** (berpengaruh signifikan).
   - Jika $\text{p-value} > 0{,}05 \rightarrow$ Hipotesis **Ditolak** (tidak berpengaruh signifikan).
3. **Uji Simultan (Uji F):**
   - Jika $\text{p-value } F \le 0{,}05 \rightarrow$ Variabel $X_1, X_2, X_3$ secara bersama-sama berpengaruh signifikan terhadap $Y$.
4. **Koefisien Determinasi ($\text{Adj } R^2$):**
   - Mengukur proporsi variasi $Y$ yang mampu dijelaskan oleh model regresi panel.

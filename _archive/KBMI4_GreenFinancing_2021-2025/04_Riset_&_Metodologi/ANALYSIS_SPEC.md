# Analysis Specification — Spesifikasi Ekonometrika Data Panel

> **Topik:** Pengaruh Portofolio Kredit Hijau (*Green Financing*), *Non-Performing Loan* (NPL), dan *Capital Adequacy Ratio* (CAR) terhadap Profitabilitas (*Return on Assets* / ROA) pada Bank KBMI 4 di Indonesia Periode 2021–2025.  
> **Target Analisis:** Data Panel 4 Bank $\times$ 20 Kuartal = 80 Observasi.  
> **Standar Dokumen:** Format Lengkap Komprehensif $\ge 80$ Halaman.  
> **Software Utama:** EViews 12 / STATA 17 / SPSS 26.

---

## 1. Spesifikasi Model Matematis & Ekonometrika

Model regresi data panel didefinisikan sebagai berikut:

$$\text{ROA}_{it} = \alpha + \beta_1 \text{GF}_{it} + \beta_2 \text{NPL}_{it} + \beta_3 \text{CAR}_{it} + \mu_i + \lambda_t + v_{it}$$

Di mana:
- $\text{ROA}_{it}$ : Kinerja profitabilitas bank $i$ pada kuartal $t$
- $\text{GF}_{it}$ : Rasio penyaluran *Green Financing* bank $i$ pada kuartal $t$
- $\text{NPL}_{it}$ : Rasio kredit bermasalah (*Non-Performing Loan*) bank $i$ pada kuartal $t$
- $\text{CAR}_{it}$ : Rasio kecukupan modal (*Capital Adequacy Ratio*) bank $i$ pada kuartal $t$
- $\mu_i$ : Efek spesifik individual bank yang tidak teramati (*unobserved bank-specific effect*)
- $\lambda_t$ : Efek spesifik waktu (*time-specific effect*)
- $v_{it}$ : Galat stokastik (*idiosyncratic error term*)

---

## 2. Pohon Keputusan Pemilihan Model (Model Selection Protocol)

```
                            [ Estimasi CEM dan FEM ]
                                       │
                                       ▼
                                 [ Uji Chow ]
                    H0: CEM lebih baik vs H1: FEM lebih baik
                                       │
                     ┌─────────────────┴─────────────────┐
                     ▼                                   ▼
             p-value >= 0.05                     p-value < 0.05
                  (CEM)                              (FEM)
                     │                                   │
                     ▼                                   ▼
          [ Estimasi CEM vs REM ]               [ Estimasi FEM vs REM ]
                     │                                   │
                     ▼                                   ▼
             [ Uji Lagrange ]                     [ Uji Hausman ]
        H0: CEM vs H1: REM                  H0: REM vs H1: FEM
                     │                                   │
          ┌──────────┴──────────┐             ┌──────────┴──────────┐
          ▼                     ▼             ▼                     ▼
     p >= 0.05              p < 0.05      p >= 0.05              p < 0.05
       [CEM]                  [REM]         [REM]                  [FEM]
```

---

## 3. Matriks Diagnostik Uji Asumsi Klasik

| No | Jenis Pengujian | Metode / Uji Statistik | Nilai Ambang Batas (Rule of Thumb) | Tindakan Koreksi Jika Melanggar |
|---|---|---|---|---|
| 1 | **Normalitas Residual** | *Jarque-Bera Test* | $\text{Prob } > 0{,}05$ (Residual terdistribusi normal) | Transformasi logaritmik natural atau penambahan observasi |
| 2 | **Multikolinearitas** | *Variance Inflation Factor* (VIF) & Matriks Korelasi | $\text{VIF} < 10$ dan Nilai Korelasi Antar-X $< 0{,}80$ | Menghapus variabel yang kolinier atau membuat indeks gabungan |
| 3 | **Heteroskedastisitas** | *Glejser Test* / *White Heteroskedasticity Test* | $\text{Prob } > 0{,}05$ (Homoskedastisitas terpenuhi) | Menggunakan estimasi *White's Heteroskedasticity-Consistent Standard Errors* |
| 4 | **Autokorelasi** | *Durbin-Watson (DW)* / *Breusch-Godfrey LM Test* | $du < d < 4 - du$ atau $\text{Prob Obs*R-squared} > 0{,}05$ | Menggunakan estimasi *Newey-West HAC Standard Errors* atau autoregresif AR(1) |

---

## 4. Templat Tabel Pelaporan Hasil Analisis (Bab 4)

### Tabel 4.X: Hasil Estimasi Regresi Data Panel (Fixed Effect Model)
| Variabel | Simbol | Koefisien ($\beta$) | Std. Error | t-Statistik | p-value (Prob.) | Kesimpulan Hipotesis |
|---|---|---|---|---|---|---|
| *Constant* | $C$ | 1,485 | 0,312 | 4,760 | 0,0000 | Signifikan |
| *Green Financing* | $\text{GF}$ | +0,042 | 0,011 | 3,818 | 0,0003 | **$H_1$ Diterima (+) Signifikan** |
| *Non-Performing Loan* | $\text{NPL}$ | -0,385 | 0,076 | -5,066 | 0,0000 | **$H_2$ Diterima (-) Signifikan** |
| *Capital Adequacy Ratio* | $\text{CAR}$ | +0,074 | 0,016 | 4,625 | 0,0000 | **$H_3$ Diterima (+) Signifikan** |

### Tabel 4.Y: Efek Spesifik Masing-Masing Bank (*Cross-Section Fixed Effects*)
| Kode Bank | Nama Entitas Bank KBMI 4 | Efek Individual ($\mu_i$) | Interpretasi Karakteristik Bank |
|---|---|---|---|
| **BBRI** | PT Bank Rakyat Indonesia (Persero) Tbk | +0,182 | Basis UMKM kuat & portofolio kredit hijau terbesar |
| **BMRI** | PT Bank Mandiri (Persero) Tbk | +0,045 | Portofolio korporasi hijau & sindikasi EBT |
| **BBCA** | PT Bank Central Asia Tbk | +0,215 | Efisiensi CASA tertinggi & rasio NPL terendah |
| **BBNI** | PT Bank Negara Indonesia (Persero) Tbk | -0,442 | Transformasi digital & ekspansi bertahap kredit hijau |

### Tabel 4.Z: Ringkasan Uji Kelayakan Model
| Ukuran Statistik | Nilai Hitung | Keterangan / Evaluasi |
|---|---|---|
| **$R$-Squared ($R^2$)** | 0,725 | Total proporsi variasi ROA yang dijelaskan model |
| **Adjusted $R$-Squared** | 0,702 | Daya penjelas model terkoreksi derajat kebebasan (70,2%) |
| **F-Statistik** | 32,450 | Uji signifikansi simultan model regresi |
| **Prob(F-statistic)** | 0,0000 | Model regresi fit dan sangat layak secara statistik ($p < 0{,}05$) |

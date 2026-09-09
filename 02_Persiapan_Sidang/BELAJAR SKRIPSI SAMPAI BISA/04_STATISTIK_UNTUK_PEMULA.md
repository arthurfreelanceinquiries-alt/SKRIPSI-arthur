# 📊 STATISTIK & MRA UNTUK PEMULA
### *Panduan Memahami Metode Analisis Data Proposal Skripsi Pokémon TCG*

---

> **Target Pembaca:** Mahasiswa S1 yang baru pertama kali menggunakan SPSS dan MRA. Panduan ini menjelaskan konsep statistik dengan bahasa sederhana dan analogi sehari-hari.

---

## 1. APA ITU REGRESI?

**Analogi:** Bayangkan kamu ingin tahu apakah "banyaknya nonton konten unboxing" (X) membuat kamu "lebih sering beli booster pack" (Y). Regresi = alat untuk mengukur seberapa kuat hubungan itu.

**Persamaan dasar:**
```
Y = a + bX + e
```
- `a` = konstanta (berapa Y saat X = 0)
- `b` = koefisien regresi (setiap X naik 1, Y berubah sebesar b)
- `e` = error (faktor lain yang tidak diukur)

**Regresi Berganda** = sama, tapi dengan banyak X:
```
Y = a + b₁X₁ + b₂X₂ + b₃X₃ + e
```

---

## 2. APA ITU MRA (Moderated Regression Analysis)?

**Analogi:** Kamu sudah tahu bahwa "senang merobek pack" (X1) → "beli impulsif" (Y). Tapi kamu curiga: apakah orang yang "paham keuangan" (M) akan **kurang** terpengaruh? MRA menguji apakah M mengubah kekuatan hubungan X→Y.

**Caranya:** Tambahkan variabel perkalian X×M (*interaction term*):
```
Y = a + b₁X₁ + b₂X₂ + b₃X₃ + b₄M + b₅(X₁×M) + b₆(X₂×M) + b₇(X₃×M) + e
```

**Interpretasi kunci:**
- Jika `b₅` negatif dan signifikan → Literasi Keuangan **memperlemah** pengaruh Hedonic Motivation terhadap Impulsive Buying ✅
- Jika `b₅` tidak signifikan → Literasi Keuangan **tidak** memoderasi hubungan tersebut ❌

---

## 3. LANGKAH-LANGKAH ANALISIS DI SPSS

### Langkah 1: Input Data
1. Buka SPSS → Variable View
2. Buat kolom: `Y`, `X1`, `X2`, `X3`, `M` (isi = total skor Likert per variabel)
3. Data View → Input skor dari 120-150 responden

### Langkah 2: Uji Validitas
1. Analyze → Correlate → Bivariate
2. Masukkan semua item + total skor variabel
3. Cek: Pearson Correlation tiap item terhadap total skor
4. **Valid** jika r-hitung > r-tabel (lihat tabel r dengan df = N-2, α = 0,05)

### Langkah 3: Uji Reliabilitas
1. Analyze → Scale → Reliability Analysis
2. Masukkan item-item satu variabel → Model: Alpha
3. **Reliabel** jika Cronbach's Alpha ≥ 0,60

### Langkah 4: Statistik Deskriptif
1. Analyze → Descriptive Statistics → Descriptives
2. Masukkan semua variabel → Centang Mean, Std. Deviation, Min, Max

### Langkah 5: Uji Asumsi Klasik

**a. Normalitas (Kolmogorov-Smirnov):**
1. Analyze → Nonparametric Tests → Legacy Dialogs → 1-Sample K-S
2. Masukkan residual model
3. **Normal** jika Asymp. Sig. > 0,05

**b. Multikolinearitas:**
1. Saat menjalankan regresi → Statistics → centang Collinearity diagnostics
2. **Aman** jika Tolerance > 0,10 DAN VIF < 10

**c. Heteroskedastisitas (Uji Glejser):**
1. Simpan residual dari regresi (Save → Unstandardized Residuals)
2. Hitung ABS(residual) → jadikan variabel dependen baru
3. Regresikan X₁, X₂, X₃ terhadap ABS_RES
4. **Aman** jika semua Sig. > 0,05

### Langkah 6: Regresi Berganda (Model 1)
1. Analyze → Regression → Linear
2. Dependent: Y | Independent: X1, X2, X3
3. Method: Enter
4. Lihat tabel Coefficients → Sig. < 0,05 = signifikan

### Langkah 7: MRA (Model 2)
1. **Mean-centering dulu!**
   - Transform → Compute Variable
   - `X1_c = X1 - mean(X1)`
   - `M_c = M - mean(M)`
   - Ulangi untuk X2_c, X3_c
2. **Buat interaction terms:**
   - `X1M = X1_c × M_c`
   - `X2M = X2_c × M_c`
   - `X3M = X3_c × M_c`
3. Analyze → Regression → Linear
   - Dependent: Y
   - Independent: X1_c, X2_c, X3_c, M_c, X1M, X2M, X3M
4. Lihat koefisien X1M, X2M, X3M → Sig. < 0,05 = moderasi terbukti

---

## 4. CARA MEMBACA OUTPUT SPSS

### Tabel Model Summary
| R | R Square | Adjusted R² | Std. Error |
|:---|:---|:---|:---|
| 0,756 | 0,572 | 0,548 | 2,341 |

**Artinya:** Model menjelaskan 57,2% variasi Y. Sisanya 42,8% oleh faktor lain.

### Tabel ANOVA
| | df | F | Sig. |
|:---|:---|:---|:---|
| Regression | 7 | 24,567 | 0,000 |

**Artinya:** Sig. < 0,05 → Model secara keseluruhan signifikan (Uji F diterima).

### Tabel Coefficients
| Variabel | B | Std. Error | t | Sig. |
|:---|:---|:---|:---|:---|
| X1_c | 0,342 | 0,089 | 3,843 | 0,000 |
| X1M | -0,156 | 0,045 | -3,467 | 0,001 |

**Artinya:**
- X1 → Y: positif signifikan (b = 0,342, Sig. = 0,000 < 0,05) → **H1 diterima**
- X1×M: negatif signifikan (b = -0,156, Sig. = 0,001 < 0,05) → **H4 diterima** (FL memperlemah pengaruh HM → IB)

---

## 5. TIPS PENTING

| ⚠️ Kesalahan Umum | ✅ Yang Benar |
|:---|:---|
| Tidak mean-centering sebelum MRA | **Selalu** mean-center X dan M sebelum membuat interaction term |
| Melihat R² biasa | Gunakan **Adjusted R²** (lebih akurat untuk multiple regression) |
| Lupa cek asumsi klasik | **Wajib** uji normalitas, multikolinearitas, heteroskedastisitas SEBELUM regresi |
| Menyimpulkan "berpengaruh" hanya dari arah koefisien | Harus cek **Sig. < 0,05** — koefisien positif tapi Sig. > 0,05 = TIDAK signifikan |
| Bingung VIF tinggi pada interaction term | VIF tinggi pada X×M itu **normal** — fokus pada VIF variabel utama (X1, X2, X3, M) |

---

## 6. GLOSARIUM SINGKAT OUTPUT SPSS

| Istilah | Arti |
|:---|:---|
| B (Unstandardized) | Koefisien regresi mentah — "setiap X naik 1, Y berubah sebesar B" |
| Beta (Standardized) | Koefisien terstandarisasi — untuk membandingkan kekuatan relatif antar-variabel |
| t | Rasio B/Std.Error — semakin besar, semakin signifikan |
| Sig. (p-value) | Probabilitas hasil terjadi secara kebetulan — < 0,05 = signifikan |
| R² | Proporsi variasi Y yang dijelaskan model |
| F | Uji signifikansi model keseluruhan |
| VIF | Variance Inflation Factor — > 10 = multikolinearitas bermasalah |
| Durbin-Watson | Uji autokorelasi — idealnya mendekati 2 *(PERINGATAN: HANYA untuk data runtun waktu/time series! TIDAK digunakan pada skripsi kuesioner cross-sectional ini)* |
| Tolerance | 1/VIF — > 0,10 = aman |

---

*Selamat belajar SPSS! Statistik itu tidak menakutkan kalau dipahami logikanya.* 📈

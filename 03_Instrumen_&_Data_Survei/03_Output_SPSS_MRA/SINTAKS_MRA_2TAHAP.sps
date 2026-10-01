* ============================================================.
* SINTAKS MRA 2 TAHAP HIERARKIS — Pokemon TCG Impulsive Buying.
* Model 1 : Y = a + b1X1* + b2X2* + b3X3* + b4M* + e.
* Model 2 : Model 1 + b5(X1*M*) + b6(X2*M*) + b7(X3*M*) + e.
* Tanda * = skor terpusat (mean-centering). H1-H3 : b1-b3 > 0.
* H4-H6 (moderasi memperlemah) : b5-b7 < 0, p < 0,05 (uji dua sisi).
* Variabel mentah (CSV) : Y1-Y6, X1_1-X1_5, X2_1-X2_5,
*   X3_1-X3_5, M1-M6, S1_WNI S2_Usia17 S3_Jakbar S4_Beli, INCLUDE.
* Filter : hanya baris INCLUDE = 1 yang dianalisis.
* Pilot : N = 30, r-tabel = 0,361 (df = 28, alfa 5% dua sisi),
*   reliabel bila Cronbach Alpha >= 0,70.
* Final : N = 111-150 (Green 1991 : 50+8k = 106, 104+k = 111, k = 7).
* Catatan : uji autokorelasi Durbin-Watson SENGAJA tidak dipakai
*   (hanya relevan untuk data time-series/panel, bukan survei
*   cross-sectional). Uji F-change df1 = 3, df2 = N - 8.
* ============================================================.

* ---------- 0. Filter inklusi dan penanganan missing ----------.
* Pastikan file aktif sudah berisi kolom sesuai kodebook.
FILTER BY INCLUDE.
* Analisis memakai listwise deletion (bawaan REGRESSION /MISSING LISTWISE).

* ---------- 1. SKOR KOMPOSIT (mean composite tiap konstruk) ----------.
* Skor = rata-rata butir VALID pada konstruknya. Angka setelah MEAN.
* = syarat jumlah butir valid (mis. MEAN.6 butuh 6 butir terisi).
* Komposit dihitung DULU karena dipakai sebagai pembanding uji validitas.
COMPUTE Y_mean  = MEAN.6(Y1, Y2, Y3, Y4, Y5, Y6).
COMPUTE X1_mean = MEAN.5(X1_1, X1_2, X1_3, X1_4, X1_5).
COMPUTE X2_mean = MEAN.5(X2_1, X2_2, X2_3, X2_4, X2_5).
COMPUTE X3_mean = MEAN.5(X3_1, X3_2, X3_3, X3_4, X3_5).
COMPUTE M_mean  = MEAN.6(M1, M2, M3, M4, M5, M6).
EXECUTE.
VARIABLE LABELS
  Y_mean  'Impulsive Buying (komposit)'
  X1_mean 'Hedonic Motivation (komposit)'
  X2_mean 'Desire for Completeness (komposit)'
  X3_mean 'Speculative Motive (komposit)'
  M_mean  'Self-Control (komposit)'.

* ---------- 2. UJI KUALITAS DATA : PILOT N = 30 ----------.
* 2a. Validitas butir : korelasi Pearson butir vs skor komposit konstruk.
* Jalankan pada DATA PILOT (N = 30) sebelum estimasi regresi.
* Kriteria : r-hitung > r-tabel 0,361 ; pendukung corrected item-total >= 0,30.

CORRELATIONS
  /VARIABLES = Y1 Y2 Y3 Y4 Y5 Y6 WITH Y_mean
  /PRINT = TWOTAIL NOSIG
  /MISSING = PAIRWISE.
CORRELATIONS
  /VARIABLES = X1_1 X1_2 X1_3 X1_4 X1_5 WITH X1_mean
  /PRINT = TWOTAIL NOSIG
  /MISSING = PAIRWISE.
CORRELATIONS
  /VARIABLES = X2_1 X2_2 X2_3 X2_4 X2_5 WITH X2_mean
  /PRINT = TWOTAIL NOSIG
  /MISSING = PAIRWISE.
CORRELATIONS
  /VARIABLES = X3_1 X3_2 X3_3 X3_4 X3_5 WITH X3_mean
  /PRINT = TWOTAIL NOSIG
  /MISSING = PAIRWISE.
CORRELATIONS
  /VARIABLES = M1 M2 M3 M4 M5 M6 WITH M_mean
  /PRINT = TWOTAIL NOSIG
  /MISSING = PAIRWISE.

* 2b. Reliabilitas konsistensi internal per konstruk (Alpha >= 0,70).
RELIABILITY
  /VARIABLES = Y1 Y2 Y3 Y4 Y5 Y6
  /SCALE('Y Impulsive Buying') ALL
  /MODEL = ALPHA
  /STATISTICS = DESCRIPTIVE SCALE CORR
  /SUMMARY = MEANS VARIANCE COV CORR.
RELIABILITY
  /VARIABLES = X1_1 X1_2 X1_3 X1_4 X1_5
  /SCALE('X1 Hedonic Motivation') ALL
  /MODEL = ALPHA
  /STATISTICS = DESCRIPTIVE SCALE CORR
  /SUMMARY = MEANS VARIANCE COV CORR.
RELIABILITY
  /VARIABLES = X2_1 X2_2 X2_3 X2_4 X2_5
  /SCALE('X2 Desire for Completeness') ALL
  /MODEL = ALPHA
  /STATISTICS = DESCRIPTIVE SCALE CORR
  /SUMMARY = MEANS VARIANCE COV CORR.
RELIABILITY
  /VARIABLES = X3_1 X3_2 X3_3 X3_4 X3_5
  /SCALE('X3 Speculative Motive') ALL
  /MODEL = ALPHA
  /STATISTICS = DESCRIPTIVE SCALE CORR
  /SUMMARY = MEANS VARIANCE COV CORR.
RELIABILITY
  /VARIABLES = M1 M2 M3 M4 M5 M6
  /SCALE('M Self-Control') ALL
  /MODEL = ALPHA
  /STATISTICS = DESCRIPTIVE SCALE CORR
  /SUMMARY = MEANS VARIANCE COV CORR.

* ---------- 3. MEAN-CENTERING prediktor dan pemoderasi ----------.
* Rerata besar (grand mean) diambil dari data sendiri via AGGREGATE
* agar sintaks portabel untuk pilot maupun final tanpa angka manual.
* Centering mereduksi multikolinearitas non-esensial prediktor-interaksi
* tanpa mengubah R2 maupun koefisien interaksi (Aiken & West ; Hayes).

AGGREGATE
  /OUTFILE = * MODE = ADDVARIABLES
  /Y_grand = MEAN(Y_mean)
  /X1_grand = MEAN(X1_mean)
  /X2_grand = MEAN(X2_mean)
  /X3_grand = MEAN(X3_mean)
  /M_grand = MEAN(M_mean)
  /M_sd = SD(M_mean).
COMPUTE Yc = Y_mean - Y_grand.
COMPUTE X1c = X1_mean - X1_grand.
COMPUTE X2c = X2_mean - X2_grand.
COMPUTE X3c = X3_mean - X3_grand.
COMPUTE Mc = M_mean - M_grand.
EXECUTE.
VARIABLE LABELS
  X1c 'X1 terpusat (X1*)' / X2c 'X2 terpusat (X2*)'
  / X3c 'X3 terpusat (X3*)' / Mc 'M terpusat (M*)'.

* ---------- 4. ISTILAH INTERAKSI moderasi ----------.
COMPUTE X1Mc = X1c * Mc.
COMPUTE X2Mc = X2c * Mc.
COMPUTE X3Mc = X3c * Mc.
EXECUTE.
VARIABLE LABELS
  X1Mc 'Interaksi X1*M* (H4)' / X2Mc 'Interaksi X2*M* (H5)'
  / X3Mc 'Interaksi X3*M* (H6)'.

* ---------- 5. REGRESI HIERARKIS MRA : Model 1 lalu Model 2 ----------.
* Blok 1 = Model 1 aditif baseline (H1-H3 + efek langsung M).
* Blok 2 = Model 2 interaksi penuh (H4-H6). Opsi CHANGE menghasilkan
* R2-change (Delta R2) dan F-change dengan df1 = 3, df2 = N - 8.
* COLLIN/TOL = cek multikolinearitas efek utama (syarat : Tol > 0,10,
* VIF < 10 pada Model 1). Simpan residual Model 2 untuk uji asumsi.

REGRESSION
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS CI(95) R ANOVA COLLIN TOL CHANGE
  /CRITERIA = PIN(.05) POUT(.10)
  /NOORIGIN
  /DEPENDENT Y_mean
  /METHOD = ENTER X1c X2c X3c Mc
  /METHOD = ENTER X1Mc X2Mc X3Mc
  /SCATTERPLOT = (*ZRESID, *ZPRED)
  /RESIDUALS HISTOGRAM(ZRESID) NORMPROB(ZRESID)
  /SAVE RESID(Res_M2) PRED(Pred_M2).

* ---------- 6. UJI ASUMSI KLASIK ----------.
* 6a. Normalitas residual Model 2 : Kolmogorov-Smirnov (normal bila p > 0,05).
NPAR TESTS
  /K-S(NORMAL) = Res_M2
  /MISSING ANALYSIS.

* 6b. Multikolinearitas : baca Tolerance (> 0,10) dan VIF (< 10) pada
* tabel Coefficients Model 1. VIF tinggi pada BLOK INTERAKSI Model 2 yang
* didorong teori bukan pelanggaran otomatis (korelasi struktural
* prediktor-interaksi bersifat ekspektasian ; centering hanya mereduksi
* komponen non-esensial).
* (Tidak ada perintah tambahan — output sudah dihasilkan perintah REGRESSION.)

* 6c. Heteroskedastisitas : uji Glejser — regresikan nilai absolut residual
* pada seluruh prediktor + interaksi ; bebas hetero bila semua p > 0,05.
COMPUTE AbsRes = ABS(Res_M2).
EXECUTE.
REGRESSION
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS R ANOVA
  /CRITERIA = PIN(.05) POUT(.10)
  /NOORIGIN
  /DEPENDENT AbsRes
  /METHOD = ENTER X1c X2c X3c Mc X1Mc X2Mc X3Mc.

* ---------- 7. SIMPLE SLOPES (kemiringan bersyarat, Hayes 2018) ----------.
* Arah moderasi memperlemah : slope Xi->Y mendatar pada M tinggi.
* Slope H4 : b1 + b5*Mc ; H5 : b2 + b6*Mc ; H6 : b3 + b7*Mc,
* dievaluasi pada Mc = -1SD (rendah), 0 (rata-rata), +1SD (tinggi).
* Ambil b1-b7 dari tabel Coefficients Model 2 dan M_sd dari AGGREGATE,
* lalu hitung manual / via PROCESS macro bila tersedia di instalasi SPSS.

DESCRIPTIVES VARIABLES = X1c X2c X3c Mc X1Mc X2Mc X3Mc
  /STATISTICS = MEAN STDDEV MIN MAX.

* CONTOH hitung manual slope H4 pada tiga level M (ganti b1 b5 dgn angka output) :
*   Slope_rendah = b1 + b5*(-1*M_sd).   Slope_rata = b1.   Slope_tinggi = b1 + b5*(+1*M_sd).
* Ulangi pola sama untuk H5 (b2,b6) dan H6 (b3,b7). Plot garis prediksi
* Y atas X pada tiga level M untuk visual pembuktian efek memperlemah.

* ---------- 8. RINGKASAN ATURAN KEPUTUSAN (dibaca di output) ----------.
* H1 didukung : b1 > 0 dan p < 0,05.  H2 : b2 > 0 dan p < 0,05.
* H3 didukung : b3 > 0 dan p < 0,05.  H4 : b5 < 0 dan p < 0,05.
* H5 didukung : b6 < 0 dan p < 0,05.  H6 : b7 < 0 dan p < 0,05.
* Blok moderasi bermakna : Delta R2 > 0 dengan F-change p < 0,05.
* Model layak : uji F simultan Model 2 p < 0,05.

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Panduan menjalankan SINTAKS_MRA_2TAHAP.sps dan daftar output yang wajib dikutip di Bab 4.
> - **Masalah yang Diselesaikan:** Mencegah langkah olah data terlewat (centering, hierarki, asumsi klasik, simple slopes).
> - **Keputusan/Output:** SOP 7 langkah plus checklist R2, Delta R2, F-change df(3,N-8), beta5-7<0, p<0,05.

# README OUTPUT — Cara Pakai Sintaks MRA 2 Tahap (SPSS)

> Pasangan operasional file `SINTAKS_MRA_2TAHAP.sps`. Model kanonis: Model 1 `Y = a + b1X1* + b2X2* + b3X3* + b4M* + e`; Model 2 tambah `b5(X1*M*) + b6(X2*M*) + b7(X3*M*) + e` (tanda `*` = terpusat/mean-centered). Hipotesis: H1–H3 `b1-b3 > 0`; H4–H6 moderasi memperlemah `b5-b7 < 0`, `p < 0,05` (uji dua sisi konservatif).

---

## 1. Cara pakai sintaks (7 langkah)

1. **Siapkan CSV** mengikuti `02_Data_Mentah_Survei_Excel/KODEBOOK_DAN_TEMPLATE_TABULASI.md` (nama kolom persis; pilot `data_pilot_N30.csv`, final `data_final_N.csv`). Pastikan hanya baris INCLUDE=1 yang dipertahankan untuk analisis (baris 0 pindah ke `log_eksklusi.csv`).
2. **Impor ke SPSS:** File > Open > Data > pilih CSV (atau drag-drop); pastikan tipe 27 butir = Numeric/Scale, S1–S4/P1–P5 = Nominal/Ordinal sesuai kodebook.
3. **Buka sintaks:** File > Open > Syntax > `SINTAKS_MRA_2TAHAP.sps`. Untuk data PILOT: sorot/blok §1–§2 (komposit + validitas-reliabilitas) lalu Run > Selection. Untuk data FINAL: jalankan seluruh sintaks (Run > All) setelah butir final dinyatakan valid-reliabel.
4. **Baca blok per blok** bila SPSS versi lama mengeluh: jalankan §1 (komposit) dulu agar Y_mean..M_mean terbentuk sebelum korelasi validitas; AGGREGATE centering menyesuaikan rerata data sendiri (portabel pilot vs final).
5. **Simpan output:** File > Save As `Pilot_N30.spv` / `MRA_Final_N.spv`; simpan dataset ber-residual sebagai `.sav` (kolom Res_M2, AbsRes ikut tersimpan via /SAVE).
6. **Butir gagal pilot** (r-hitung <= 0,361 atau Alpha < 0,70): revisi redaksi butir di Forms, sebar ulang 30 responden lulus baru, ulangi §1–§2. Jangan campur responden pilot ke sampel final.
7. **Simple slopes (Hayes 2018):** ambil b1–b7 Model 2 dari Coefficients + M_sd dari AGGREGATE/DESCRIPTIVES; hitung slope `b_i + b_j*(±1SD)`; plot tiga garis (M rendah/rata/tinggi) sebagai bukti visual efek memperlemah.

## 2. Checklist output yang WAJIB dilaporkan (Bab 4)

| # | Output (nama tabel SPSS) | Kriteria kelulusan/keputusan |
|---|---|---|
| 1 | Validitas pilot — Correlations (r-hitung tiap butir) | Tiap butir `r-hitung > r-tabel 0,361` (df=28); pendukung corrected item-total >=0,30 |
| 2 | Reliabilitas pilot — Reliability Statistics (Alpha per konstruk Y, X1, X2, X3, M) | `Cronbach Alpha >= 0,70` tiap konstruk |
| 3 | Model Summary — R2 Model 1 & Model 2, Adjusted R2 (deskriptif) | Laporkan keduanya; kontribusi murni moderasi = Delta R2 dari R2 biasa (bukan Adjusted) |
| 4 | Model Summary — **Delta R2 + F-change + Sig. F-change** | Blok moderasi bermakna bila `Delta R2 > 0` dan `p F-change < 0,05`, dengan `df1 = 3`, `df2 = N - 8` |
| 5 | ANOVA — uji F simultan Model 2 | Model layak bila `p < 0,05` |
| 6 | Coefficients Model 2 — **b1, b2, b3 (H1–H3)** | Didukung bila `b > 0` dan `p < 0,05` |
| 7 | Coefficients Model 2 — **b5, b6, b7 (H4–H6)** | Didukung bila **`b < 0`** (memperlemah) dan `p < 0,05` |
| 8 | Coefficients Model 1 — Tolerance & VIF | Lulus bila `Tolerance > 0,10` dan `VIF < 10` (blok interaksi Model 2 yang tinggi karena struktur teori bukan pelanggaran otomatis) |
| 9 | NPAR Tests — Kolmogorov-Smirnov residual (Res_M2) | Residual normal bila `p > 0,05` |
| 10 | Coefficients Glejser (DV = AbsRes) | Bebas heteroskedastisitas bila semua `p > 0,05` |
| 11 | Scatterplot ZRESID–ZPRED + Histogram/N-P Plot | Pola acak menyebar (tak ada corong/pola sistematis) sebagai pendukung visual |
| 12 | Simple slopes ±1 SD (Hayes 2018) | Slope Xi→Y mendatar pada M tinggi; laporkan 3 angka slope + grafik per H4/H5/H6 |

> Tanpa uji Durbin-Watson (sengaja dikecualikan untuk survei cross-sectional). Jika pemeriksa meminta PROCESS macro, estimasi setara: Model 1 Hayes dengan tiga interaksi simultan dan centering ON menghasilkan koefisien identik dengan sintaks ini.

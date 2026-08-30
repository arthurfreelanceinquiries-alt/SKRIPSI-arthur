# Spesifikasi Analisis Fase 3

> Versi kerja: 0.1, 10 Agustus 2026  
> Status: praspesifikasi kandidat; tidak memuat data atau hasil empiris  
> Finalisasi hanya setelah expert review, cognitive interview, pilot, software dry run, power, dan audit metodologi.

## 1. Estimand

Estimand ialah perbandingan model-based atas rerata rasio beban kewajiban pembayaran kontraktual historis menurut kategori buffer likuid saat survei, setelah penyesuaian kovariat, di antara rumah tangga eligible yang berhasil direkrut dan menyelesaikan data analitik melalui site penelitian (R=1).

Kriteria analitik utama:

1. consent;
2. usia minimal 18 tahun dan domisili/site sesuai;
3. informan mengetahui keuangan rumah tangga;
4. utang konsumtif non-KPR masih aktif saat survei;
5. ada kewajiban positif yang pertama kali jatuh tempo pada tiga bulan acuan;
6. X valid kode 1–5;
7. seluruh kontrak historis in-scope mempunyai tiga contract-month lengkap dan seluruh tiga income-month lengkap;
8. required_total_3m positif;
9. income_total_3m positif;
10. rekonsiliasi berhasil, tidak ada duplikasi, klasifikasi unresolved, atau raw-to-clean logic error.

Hasil hanya berlaku pada R=1. Y historis mendahului X saat survei dan dapat telah mengikis buffer; bahasa kausal dilarang.

## 2. Derivasi Variabel

- x_cat: kode X_duration 1–5.
- x_ge3m: 1 untuk x_cat 4–5; 0 untuk x_cat 1–3; sensitivitas.
- statement_required_total: total minimum/kontraktual kontrak sebelum alokasi.
- consumer_required_raw: statement total setelah alokasi bagian rumah tangga dan bagian tujuan konsumtif yang dapat ditelusuri.
- required_contract_month: consumer_required_raw dikurangi prior-arrears amount dan cross-contract amount hanya bila alokasi serta adjustment dapat diatribusikan; jika tidak, nilai clean missing.
- debt_window_complete: seluruh kontrak historis in-scope mempunyai tiga contract-month clean numerik; kontrak boleh sudah ditutup saat survei, tetapi household harus mempunyai minimal satu kontrak aktif saat survei.
- required_total_3m: jumlah required_contract_month hanya bila debt_window_complete=1; summation dilarang skip missing.
- income_month: total pendapatan kas bersih aktual rumah tangga, tidak termasuk pinjaman, penjualan aset, penarikan tabungan, dan transfer antar-rekening.
- income_window_complete: M3, M2, M1 masing-masing numerik, termasuk nol eksplisit.
- income_total_3m: jumlah income_month hanya bila income_window_complete=1; summation dilarang skip missing.
- y_ratio: required_total_3m / income_total_3m untuk nilai positif.
- ln_y: natural log y_ratio untuk distributional check.
- verified_record: seluruh nilai utama berasal dari statement/kontrak/aplikasi atau catatan kontemporer.
- site_cluster: unit ketergantungan rekrutmen yang nyata, bukan sekadar kota.

Setiap derivasi harus dapat ditelusuri ke field mentah. Nilai hasil edit manual tanpa audit trail dilarang.

## 3. Flow dan Eksklusi

Tampilkan jumlah pada setiap tahap: approached/invited, screened, eligible, consent, started, completed, X valid, debt-window complete, income-window complete, Y dapat dihitung, dan record analitik. Alasan eksklusi saling eksklusif sejauh mungkin: active-now gagal, historical-window gagal, informan tidak memadai, tujuan rumah/usaha, mixed/joint tidak terpisah, adjustment arrears/cross-contract tak terpisah, pendapatan nonpositif, missing X/Y, rekonsiliasi gagal, duplikasi, atau raw-to-clean logic error.

Jangan menyembunyikan kasus pendapatan nol/negatif; laporkan deskriptif terpisah dan jelaskan bahwa rasio tidak terdefinisi/layak untuk model utama.

## 4. Statistik Deskriptif Wajib

1. Flow keseluruhan dan per site/channel.
2. Karakteristik sampel dan missingness.
3. Proporsi lima kategori X.
4. Jumlah/jenis kontrak dan sumber angka.
5. Distribusi required_total_3m, income_total_3m, dan y_ratio keseluruhan serta per kategori X.
6. Flags: comprehension, arrears, restructure, mixed/joint exclusion, double count, dan verified record.
7. Median, IQR, mean, SD, minimum, maksimum, serta persentil yang dipraspesifikasikan untuk nilai kontinu; tidak hanya mean.

Tidak ada label “tinggi/rendah” tanpa ambang yang sudah dibenarkan.

## 5. Model Utama Kandidat

GLM Gamma dengan log link:

log(E[Y_i | X_i, C_i, R_i=1]) = alpha + beta_1 X2_i + beta_2 X3_i + beta_3 X4_i + beta_4 X5_i + gamma C_i.

Kategori referensi dan urutan X dibekukan sebelum survei utama. X diuji dengan uji global empat derajat bebas. Pelaporan:

- adjusted predicted mean Y setiap kategori;
- mean ratio dan confidence interval terhadap kategori referensi;
- global test;
- jumlah observasi, site/cluster, dan kovariat tiap model;
- ukuran efek serta ketidakpastian, bukan hanya p-value.

M0 tanpa adjustment; M1 memakai confounder yang dibekukan melalui DAG. Model tidak boleh ditambah/dikurangi berdasarkan p-value.

## 6. Audit Denominator Wajib

Outcome menjadi required_total_3m nominal. Kandidat analisis pendamping utama ialah Gamma-log dengan log pendapatan sebagai kovariat:

log(E[D_i]) = alpha + beta X_i + delta log(income_total_3m_i) + gamma C_i.

Delta diestimasi dan pendapatan tidak dipakai sebagai offset; hubungan tidak dipaksa proporsional satu-banding-satu. Gamma-log tetap harus didukung pilot/diagnostik. Bila tidak layak, fallback dibekukan sebelum data utama, misalnya OLS log nominal dengan HC3. Spline pendapatan hanya sensitivity bila nonlinieritas material sudah ditunjukkan sebelum analisis utama; knot/derajat harus dibekukan.

Jika model rasio berasosiasi tetapi model nominal setelah penyesuaian pendapatan tidak, kesimpulan hanya boleh menyatakan perbedaan burden relatif terhadap pendapatan.

## 7. Paket Pembanding Minimum

1. OLS pada ln_y dengan HC3 atau cluster-aware standard error yang feasible.
2. x_ge3m sebagai pembanding ambang NFCS, bukan outcome utama.
3. Complete core records versus verified_record subset bila ukuran memungkinkan.

Quantile regression, MI, CR2, wild bootstrap, atau model lain hanya digunakan bila dipraspesifikasikan setelah pilot dan secara teknis layak. Hasil tambahan harus dilabeli sensitivity/exploratory sesuai waktu keputusannya.

## 8. Cluster dan Standard Error

Cluster ditentukan dari proses rekrutmen nyata. Site fixed effect tidak menghilangkan ketergantungan. Jika cluster terlalu sedikit/besar, cluster-robust inference tidak boleh dipaksakan; desain rekrutmen harus diperbaiki atau inferensi dibatasi. Pilihan HC3, cluster-robust, CR2, atau wild bootstrap dicatat bersama jumlah cluster dan alasan.

## 9. Missing, Nilai Ekstrem, dan Diagnostik

- Kode tidak tahu dan menolak tetap terpisah.
- X/Y utama tidak diimputasi dengan mean/median/kategori.
- Missing kovariat ditangani complete-case pada model minimum; MI hanya bila ukuran, pola, MAR, software, dan kompetensi membenarkan.
- Rasio di atas satu tidak otomatis salah.
- Verifikasi sumber dan komponen sebelum koreksi; nilai ekstrem benar tidak dihapus/winsorize otomatis.
- Gamma: cek convergence, deviance/Pearson, dispersion, residual, leverage/influence, dan adequacy link/variance.
- OLS: residual pattern, heteroskedastisitas, multikolinearitas, leverage/influence; normalitas bukan syarat untuk setiap variabel mentah.
- Autokorelasi tidak diuji mekanis pada survei potong lintang.

## 10. Power dan Freeze

Power simulation memakai smallest effect substantif, proporsi X, dispersi Y, korelasi kovariat, jumlah/ukuran cluster, beberapa ICC, missing, nonresponse, dan eligibility. Hasil dipisah menjadi target screened, eligible, started, dan analytical complete. Satu angka Slovin atau rule-of-thumb dilarang.

Sebelum survei utama, bekukan: populasi, periode, codebook, derivasi, cleaning, estimand, M0/M1, denominator model, sensitivity minimum, cluster handling, missing handling, serta version hash.

## 11. Aturan Bahasa Hasil

Boleh: “berasosiasi”, “berbeda secara model-based”, “mean ratio”, “pada sampel eligible yang berhasil direkrut”, dan “burden kontraktual historis relatif terhadap pendapatan”.

Dilarang tanpa desain/bukti tambahan: “berpengaruh”, “menyebabkan”, “meningkatkan/menurunkan” secara kausal, “mewakili Jabodetabek”, “utang menopang konsumsi”, “makan tabungan”, atau “seluruh rumah tangga”.

Bab IV–V dan tabel angka tidak boleh diisi sebelum data nyata, cleaning log, output software, dan audit tersedia.

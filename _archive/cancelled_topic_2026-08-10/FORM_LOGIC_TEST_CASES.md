# Kasus Uji Logika Form dan Pipeline

> Seluruh nilai di dokumen ini **sintetis dan bukan responden/pilot**.  
> Tujuan: menguji skip logic, klasifikasi, derivasi, dan audit trail sebelum pengumpulan data.  
> Dilarang mengimpor kasus ini sebagai data penelitian atau mengutipnya sebagai hasil.

## Aturan Umum

Gunakan tiga bulan M3, M2, M1. Angka nominal adalah unit uji arbitrer. Expected output harus ditulis sebelum form/pipeline dijalankan. Setiap kegagalan dicatat sebagai defect: ID kasus, versi form/code, hasil aktual, hasil harapan, akar masalah, revisi, dan retest.

## Kasus Screening

| ID | Input sintetis | Expected flow |
|---|---|---|
| T01 | consent=0 | Stop; tidak menyimpan jawaban substantif |
| T02 | consent=1, age18=0 | Tidak eligible: usia |
| T03 | finance_role=3 | Tidak eligible: informan tidak mengetahui seluruh keuangan |
| T04 | active_now=0, required_window=1 | Tidak eligible: kontrak tidak aktif saat survei |
| T05 | active_now=1, required_window=0 | Tidak eligible utama: utang baru/tanpa kewajiban historis |
| T06 | active_now=1, required_window=1, income tiga bulan positif | Lanjut ke instrumen core |
| T07 | duplicate_status=1 | Exclude duplicate; household lama tidak ditimpa |

## Kasus X

| ID | Input sintetis | Expected output |
|---|---|---|
| T08 | x_comp_asset=2, x_comp_expense=1, x_duration=3 | x_comprehension_flag=1; x_cat=3; definisi standar ditampilkan sebelum duration |
| T09 | x_comp_asset=1, x_comp_expense=1, x_duration=8 | X missing_reason=DK; tidak masuk model utama |
| T10 | x_duration=4 | x_cat=4; x_ge3m=1 |
| T11 | x_duration=2 | x_cat=2; x_ge3m=0 |

## Kasus Y Sederhana

| ID | Input sintetis | Expected output |
|---|---|---|
| T12 | Satu KTA konsumtif aktif; required M3=100, M2=100, M1=100; income=1.000 tiap bulan | required_total_3m=300; income_total_3m=3.000; y_ratio=0,10 |
| T13 | KPR required=500 dan KTA required=100 tiap bulan; income=1.000 tiap bulan | KPR keluar dari Y; required_total_3m=300; y_ratio=0,10; housing=KPR |
| T14 | Kontrak usaha required=200 dan BNPL required=50 tiap bulan; income=1.000 tiap bulan | Usaha keluar; required_total_3m=150; y_ratio=0,05 |

## Double Count, Arrears, dan Restrukturisasi

| ID | Input sintetis | Expected output |
|---|---|---|
| T15 | BNPL required 100 tiap bulan dibayar melalui kartu; minimum kartu 150 tiap bulan termasuk 100 BNPL + 50 transaksi kartu asli | Kontrak BNPL=300; komponen kartu yang masuk=150 total (50×3); required_total_3m=450, bukan 750; double_count_flag=1 |
| T16 | Tagihan M3=200 seluruhnya first-due; M2=300 terdiri 200 first-due + 100 tunggakan M3; M1=200 | required clean=200+200+200=600; prior_arrears_flag M2=1; tunggakan M3 tidak dihitung dua kali |
| T17 | Jadwal lama 300/bulan direstrukturisasi sebelum M2 menjadi 150/bulan; M3 old due=300, M2=150, M1=150 | required_total_3m=600; jadwal lama M2/M1 tidak dihitung; restructure_flag=1 |
| T18 | Penalti hipotetis 50 belum dibebankan | Penalti keluar tanpa menunggu keputusan D15 |

## Mixed Purpose dan Joint Debt

| ID | Input sintetis | Expected output |
|---|---|---|
| T19 | Kontrak campuran: statement=300/bulan; household=300; dokumen mengalokasikan consumer=200 dan usaha=100 | consumer_required_raw=200/bulan; allocation_source_month=dokumen; mixed_allocation_known=1; hierarchy lolos |
| T20 | Kontrak campuran 300/bulan tanpa alokasi | contract_include_y=8 unresolved; consumer_required_raw missing; Y household missing; household tidak masuk analisis utama |
| T21 | Joint debt konsumtif: statement=400/bulan; perjanjian menetapkan household=150 | household_required_amount=150; consumer_required_raw=150; allocation_source_month=perjanjian; hierarchy lolos |
| T22 | Joint debt 400/bulan tanpa alokasi yang diketahui | contract_include_y=8 unresolved; household_required_amount missing; Y household missing; household tidak masuk analisis utama |

## Pendapatan dan Missing

| ID | Input sintetis | Expected output |
|---|---|---|
| T23 | Gaji 1.000 + pinjaman 500 + penarikan tabungan 200 tiap bulan | income clean=1.000/bulan; pinjaman/penarikan tidak masuk |
| T24 | income M3=1.000, M2=0, M1=0; total tiga bulan=1.000; required_total=300 | y_ratio=0,30 bila total periode positif; dua bulan nol tetap disimpan dan diberi konteks |
| T25 | income_total_3m=0; required_total=300 | y_ratio tidak dihitung; income_zero_flag=1; tetap pada flow/deskriptif |
| T26 | required M2 menolak; bulan lain lengkap | Y tidak lengkap untuk model utama; missing_reason=refuse; jangan mengisi nol |

## Rekonsiliasi dan Audit Trail

| ID | Input sintetis | Expected output |
|---|---|---|
| T27 | Subtotal kontrak tidak sama dengan subtotal bulan | logic_flag=1; form meminta review sebelum submit |
| T28 | Raw required 500 dikoreksi menjadi 300 karena 200 double count | Raw tetap 500; clean=300; adjustment=200; alasan dan kontrak sumber tersimpan |
| T29 | Nilai y_ratio=1,20 dengan komponen yang konsisten | Tidak dihapus/winsorize; flag review selesai dan nilai dipertahankan |
| T30 | Dua record token sama dari household yang sama | Record kedua tidak menjadi household analitik baru; resolution log dibuat tanpa PII |

## Kriteria Lulus Dry Run

Semua expected flow/output harus cocok; tidak ada nilai sintetis yang bercampur dengan data aktual; raw fields tidak berubah; setiap adjustment terlacak; kode DK/refuse tidak dibaca sebagai nominal; dan laporan flow dapat direproduksi dari tabel mentah. “Sebagian besar berhasil” tidak cukup bila defect menyentuh consent, eligibility, double count, denominator, atau privasi.

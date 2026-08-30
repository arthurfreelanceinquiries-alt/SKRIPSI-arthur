# Kamus Data dan Skema Relasional

> Versi kerja: 0.2, 10 Agustus 2026  
> Status: kandidat sebelum form/pilot; nama dan tipe dibekukan ulang setelah expert/cognitive review  
> Prinsip: data mentah tidak ditimpa, derived fields dibuat terpisah, dan tidak ada PII/identitas finansial.

## 1. Struktur Tabel

Gunakan empat tabel yang terhubung oleh household_id acak:

1. household: consent, screening, X, kovariat, flags, dan status analitik.
2. debt_contract: satu baris per kontrak/akun.
3. debt_month: satu baris per kontrak × bulan acuan.
4. income_month: satu baris per rumah tangga × bulan acuan.

Recruitment flow dapat disimpan pada tabel agregat site-day yang tidak memuat identitas individu. Kontak insentif, bila ada, berada di penyimpanan terpisah dan tidak memakai household_id analitik secara langsung.

## 2. Kunci dan Metadata

| Field | Tabel | Tipe | Aturan |
|---|---|---|---|
| household_id | semua | string acak | Unik, bukan turunan nama/telepon/alamat; mekanisme final masih blocker |
| contract_id | debt_contract/debt_month | string internal | Unik dalam household; satu kontrak/akun |
| month_code | debt_month/income_month | kategori | M3, M2, M1 yang dipetakan ke nama bulan final |
| instrument_version | household | string | Nomor versi yang benar-benar digunakan |
| cluster_id | household | kategori proyek | Turunan dari unit ketergantungan rekrutmen nyata; mapping site/channel/recruitment chain dibekukan sebelum survei dan tidak memuat PII |
| cluster_rule_version | household | string | Versi tabel mapping cluster |
| site_id | household/flow | kategori | Unit rekrutmen nyata |
| channel_id | household/flow | kategori | Cara distribusi/rekrutmen |
| started_at/completed_at | household | datetime | Untuk durasi; presisi dibatasi sesuai etik |

## 3. Consent dan Screening

| Field | Tipe/nilai | Peran |
|---|---|---|
| consent | 1 ya; 0 tidak | Stop bila 0; jangan simpan jawaban substantif |
| age18 | 1/0 | Eligibility |
| domicile_code | daftar final | Eligibility/batas geografis |
| finance_role | 1 utama; 2 ikut dan tahu; 3 sebagian; 4 tidak tahu | 1–2 eligible |
| shared_finance | 1 sendiri; 2 bersama; 3 terpisah | Definisi rumah tangga |
| duplicate_status | 0 tidak; 1 ya; 8 tidak tahu | 1 dikeluarkan; 8 quality review |
| active_now | 1/0/8/9 | Wajib 1 |
| required_window | 1/0/8/9 | Wajib 1 |
| eligibility_final | 1/0 | Derived dari semua gate |
| exclusion_reason | kategori tunggal utama | Audit flow |

Kode 8 = tidak tahu dan 9 = menolak hanya untuk item kategorikal yang memang mendefinisikannya. Pada field nominal, simpan nilai kosong dan missing_reason terpisah; jangan menulis 8/9 sebagai rupiah.

## 4. Konstruk X

| Field | Tipe/nilai | Aturan |
|---|---|---|
| x_comp_asset | 1 benar; 2/3 salah; 8 tidak tahu | Comprehension |
| x_comp_expense | 1 benar; 2/3 salah; 8 tidak tahu | Comprehension |
| x_comprehension_flag | 1 ada salah; 0 keduanya benar | Derived |
| x_duration | 1 <1 minggu; 2 1mgg–<1bln; 3 1–<3bln; 4 3–<6bln; 5 ≥6bln; 8 DK; 9 refuse | X mentah |
| x_confidence | 1–4; 9 refuse | Quality/deskriptif |
| x_cat | 1–5 | Sama dengan x_duration valid |
| x_ge3m | 1 bila 4–5; 0 bila 1–3 | Sensitivitas |

Jangan membentuk saldo buffer nominal karena core instrument tidak mengumpulkannya.

## 5. Debt Contract

| Field | Tipe/nilai | Aturan |
|---|---|---|
| product_type | 1 KTA formal; 2 P2P; 3 kendaraan; 4 barang; 5 kartu revolving; 6 cicilan kartu; 7 BNPL; 8 informal; 9 lain | Satu jenis per kontrak |
| purpose | konsumsi umum; kendaraan; barang; medis; pendidikan; rumah; usaha; campuran; lain; DK | Tujuan, bukan produk |
| joint_flag | 1/0 | Pihak di luar household |
| joint_allocation_known | 1/0/NA | Derived; 1 hanya bila aturan, nilai/bagian per bulan, dan sumber alokasi tersedia |
| joint_allocation_rule | NA; seluruh household; nominal tetap; persentase tetap; bervariasi; tidak diketahui | Dasar menentukan bagian kewajiban household; dilarang mengasumsikan 50:50 |
| joint_allocation_value | rupiah, proporsi 0–1, atau NA | Unit mengikuti rule; bila bervariasi, nilai aktual wajib dicatat pada debt_month |
| mixed_allocation_known | 1/0/NA | Derived; 1 hanya bila aturan, nilai/bagian konsumtif per bulan, dan sumber alokasi tersedia |
| mixed_allocation_rule | NA; seluruh konsumtif; nominal tetap; persentase tetap; bervariasi; tidak diketahui | Dasar menentukan bagian tujuan konsumtif |
| mixed_allocation_value | rupiah, proporsi 0–1, atau NA | Unit mengikuti rule; bila bervariasi, nilai aktual wajib dicatat pada debt_month |
| allocation_source_contract | perjanjian/statement; catatan bersama; keterangan pihak terkait; lain; DK; NA | Sumber aturan alokasi tingkat kontrak; bukan pengganti nilai per bulan |
| restructure_flag | 1/0 | Status kontrak |
| active_contract_now | 1/0 | Household wajib mempunyai minimal satu kontrak aktif, tetapi kontrak historis yang membentuk Y boleh sudah ditutup |
| closed_before_survey | 1/0 | Kontrak historis ditutup/lunas setelah/dalam jendela tetapi sebelum survei |
| opened_after_window | 1/0 | Kontrak aktif baru setelah M1; tidak membentuk Y, hanya menjelaskan active-now |
| payment_channel | langsung; kartu; pinjaman lain; lain; DK | Flag double count |
| contract_include_y | 1 in-scope resolved; 0 out-of-scope; 8 in-scope unresolved | Derived dari kewajiban historis, purpose, allocation, dan rules; tidak mensyaratkan active_contract_now=1; status 8 memblokir Y household |
| contract_exclusion_reason | kategori | Rumah/usaha, mixed/joint tak terpisah, DK, lainnya; bedakan out-of-scope dari in-scope unresolved |

Nama kreditur, nomor akun, dan identitas peminjam dilarang.

## 6. Debt Month

| Field | Tipe | Aturan |
|---|---|---|
| statement_required_total | rupiah nonnegatif/kosong | Total minimum/kontraktual kontrak yang tampil/wajib sebelum alokasi; nol harus eksplisit |
| household_required_amount | rupiah nonnegatif/kosong | Bagian statement yang menjadi tanggung jawab household; sama dengan statement bila bukan joint debt |
| consumer_required_raw | rupiah nonnegatif/kosong | Bagian konsumtif dari household required; sama dengan household required bila seluruh tujuan konsumtif |
| allocation_source_month | statement/perjanjian; catatan; keterangan pihak terkait; lain; DK; NA | Sumber nominal/proporsi alokasi bulan itu |
| allocation_complete | 1/0 | 1 hanya bila rantai statement→household→consumer numerik, bersumber, dan konsisten |
| allocation_missing_reason | joint tak terpisah; mixed tak terpisah; sumber tidak memadai; DK; refuse; logic error; NA | Terpisah dari nilai nominal |
| prior_arrears_flag | 1/0/8/9 | Apakah total memuat tunggakan lama |
| prior_arrears_amount | rupiah nonnegatif/kosong | Wajib numerik bila flag=1 dan dapat diatribusikan; jika tak terpisah, clean missing |
| cross_contract_flag | 1/0/8/9 | Apakah raw memuat bagian kontrak lain yang sudah dienumerasi |
| cross_contract_amount | rupiah nonnegatif/kosong | Hanya dari statement/kontrak/catatan yang dapat mengatribusikan bagian tersebut |
| amount_source | statement/aplikasi/kontrak; catatan; ingatan; DK; refuse | Quality |
| required_amount_clean | rupiah nonnegatif/kosong | consumer_required_raw - prior_arrears_amount - cross_contract_amount bila alokasi dan semua adjustment terselesaikan |
| debt_month_complete | 1/0 | 1 hanya bila alokasi lengkap, hierarchy nominal valid, dan seluruh adjustment yang diperlukan terselesaikan |
| debt_month_missing_reason | allocation tak lengkap; DK; refuse; arrears tak terpisah; cross-contract tak terpisah; logic error; NA | Terpisah dari nilai |

Setiap kontrak historis in-scope wajib mempunyai tiga debt_month row, termasuk kontrak yang alokasinya akhirnya unresolved. Berlaku hierarchy `0 ≤ consumer_required_raw ≤ household_required_amount ≤ statement_required_total`; pelanggaran membuat logic error, bukan koreksi otomatis. required_amount_clean tidak boleh negatif. Jika flag adjustment=0, amount adjustment ditetapkan nol; jika flag=1 tetapi amount tidak diketahui, clean tetap missing. Nilai transaksi BNPL tidak boleh otomatis dikurangkan dari minimum due kartu. Setiap alokasi dan adjustment menyimpan bukti/sumber, alasan, dan nilai asal.

## 7. Income Month

| Field | Tipe | Aturan |
|---|---|---|
| income_total_raw | rupiah/kosong | Pendapatan kas bersih aktual rumah tangga |
| income_source_check | multi-select | Gaji, usaha bersih tersedia, pensiun, bantuan nonutang, transfer, lain |
| income_record_source | aplikasi/catatan; ingatan; DK; refuse | Quality |
| income_total_clean | rupiah/kosong | Setelah rekonsiliasi; pinjaman/asset sale/savings withdrawal/inter-account transfer keluar |
| income_missing_reason | DK; refuse; logic error; NA | Terpisah dari nilai |

Pendapatan nol/negatif disimpan dan dilaporkan pada flow, tetapi tidak menghasilkan y_ratio utama.
Setiap household wajib mempunyai tiga income_month row dengan nilai eksplisit termasuk nol; satu bulan missing membuat income_total_3m missing.

## 8. Kovariat dan Flags

| Field | Tipe | Catatan |
|---|---|---|
| area_code | kategori | Kota/kabupaten aktual yang dicakup |
| age_band_or_year | final sebelum pilot | Hindari detail identifikasi berlebih |
| education | kategori | Daftar final |
| employment | kategori | Daftar final |
| hh_size | integer nonnegatif | Anggota household |
| dependents | integer nonnegatif | Tidak boleh > hh_size tanpa klarifikasi |
| housing | KPR; milik tanpa KPR; sewa; menumpang; lain | Status, bukan nominal KPR |
| income_instability | INACTIVE placeholder | Jangan buat field pada form sampai sumber/definisi/threshold/timing disahkan |
| pre_shock_type/time | INACTIVE placeholder | Jangan buat field pada form sampai shock, besar, tanggal, dan overlap rule disahkan |
| arrears_flag/restructure_flag/double_count_flag | 1/0 | Deskriptif/quality, bukan kontrol otomatis |
| verified_record | 1/0 | 1 bila seluruh nilai kewajiban/pendapatan utama berbasis record kontemporer; X tetap self-report dan tidak membentuk flag ini |
| logic_flag | 1/0 + reason | Algoritma final wajib terdokumentasi |
| cluster_mapping_flag | 1/0 | 1 bila site/channel tidak dapat dipetakan ke cluster yang dipraspesifikasikan |

## 9. Derived Household Outcomes

- debt_window_complete = 1 hanya bila tidak ada contract_include_y=8 dan setiap contract_include_y=1 mempunyai tiga row dengan seluruh debt_month_complete=1; explicit zero sah, missing tidak.
- income_window_complete = 1 hanya bila M3, M2, M1 masing-masing mempunyai income_total_clean numerik; explicit zero sah, missing tidak.
- required_total_3m = jumlah required_amount_clean hanya bila debt_window_complete=1; fungsi sum dilarang skip missing.
- income_total_3m = jumlah tiga income_total_clean hanya bila income_window_complete=1; fungsi sum dilarang skip missing.
- y_ratio = required_total_3m / income_total_3m bila keduanya positif.
- ln_y = natural log y_ratio bila y_ratio positif.
- analysis_complete = consent/eligibility valid, x_cat 1–5, active-now household terpenuhi, debt_window_complete=1, income_window_complete=1, required_total_3m>0, income_total_3m>0, reconciliation=1, tanpa duplikasi, tanpa kontrak in-scope yang klasifikasinya unresolved, dan tanpa raw-to-clean logic error.
- R = 1 hanya untuk eligible completer yang masuk dataset analitik; flow sebelum R tetap dilaporkan agregat.

## 10. Pemeriksaan Logika Minimum

1. Hanya tiga month_code unik per household/contract.
2. Minimal satu active_contract_now=1 pada household.
3. contract_include_y tidak tergantung active_contract_now; kontrak historis yang sudah tutup tetap dapat membentuk Y.
4. Minimal satu required_amount_clean>0 dalam jendela historis.
5. Semua contract_include_y=1 mempunyai tepat tiga contract-month numerik; setiap contract_include_y=8 atau row/angka yang kurang membuat household tidak complete.
6. Tiga income month wajib numerik; tidak ada skip-missing.
7. Kontrak rumah/usaha tidak boleh contract_include_y=1.
8. Mixed/joint wajib mempunyai rule, nilai nominal/proporsi, dan sumber; tanpa itu klasifikasi tetap unresolved dan household tidak analysis_complete.
9. Pada setiap contract-month berlaku `0 ≤ consumer_required_raw ≤ household_required_amount ≤ statement_required_total`; T19 dan T21 harus dapat dihitung langsung dari field ini.
10. Adjustment arrears/cross-contract yang ditandai harus numerik dan teratribusi; bila tidak, clean missing.
11. Subtotal kontrak, subtotal bulan, dan total tiga bulan harus rekonsiliasi.
12. Tidak ada BNPL/card component yang dihitung dua kali.
13. income_total_3m sama dengan jumlah tiga bulan.
14. x_cat hanya 1–5; kode 8/9 menjadi missing dengan alasan.
15. hh_size, dependents, nilai nominal, dan tanggal melewati range check yang dipraspesifikasikan.
16. Semua perubahan dari statement ke household, consumer raw, dan clean mempunyai audit reason serta sumber.

Kamus final harus menyertakan label lengkap, format file, valid range, missing reason, formula, source item, dan version hash.

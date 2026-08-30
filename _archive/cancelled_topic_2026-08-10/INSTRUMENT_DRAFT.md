# Draf Instrumen Survei dan Codebook

> Status: draf Fase 3 untuk expert review, cognitive interview, dan field pilot; bukan kuesioner final  
> Unit: satu rumah tangga; informan: pengelola/anggota yang mengetahui keuangan rumah tangga  
> Jangan menyebarkan sebagai survei utama sebelum periode, klasifikasi utang, dan izin etik disahkan.

## A. Parameter yang Diisi Sebelum Survei

- Bulan survei: `[S]`.
- Bulan acuan lengkap: `[M-3]`, `[M-2]`, `[M-1]`.
- Wilayah/site yang diizinkan: `[DAFTAR FINAL]`.
- Aturan pembulatan nominal: `[FINAL SETELAH PILOT]`.
- Contact person etik/peneliti: `[FINAL]`.
- Perkiraan durasi: `[DIISI DARI COGNITIVE/FIELD PILOT]`.
- Insentif: `[ADA/TIDAK; NILAI DAN MEKANISME FINAL]`.
- Jadwal retensi/penghapusan data dan kontak: `[FINAL SESUAI ETIK]`.
- Status/contact person persetujuan etik: `[JANGAN DIKLAIM SEBELUM ADA]`.

## B. Pembukaan dan Persetujuan

**Teks pembuka kerja**

Survei ini meneliti kondisi penyangga likuid dan kewajiban pembayaran utang konsumtif pada tingkat rumah tangga. Jawaban bersifat sukarela. Pertanyaan nominal utang dan pendapatan dapat menimbulkan rasa tidak nyaman; Anda boleh melewati pertanyaan sensitif atau berhenti kapan saja tanpa konsekuensi. Kami tidak meminta NIK, alamat rinci, nomor rekening, nama akun, kredensial, atau tangkapan layar. Anda boleh membuka catatan pribadi untuk membantu mengingat, tetapi tidak perlu mengunggah atau menyerahkannya. Durasi, insentif, penyimpanan/penghapusan data, kontak peneliti, dan informasi etik harus diisi dari parameter final sebelum teks ini digunakan. Data hanya digunakan untuk kepentingan akademik dan dilaporkan secara agregat.

`C0_consent` Apakah Anda memahami penjelasan dan bersedia berpartisipasi?

- 1 Ya.
- 0 Tidak -> selesai, jangan menyimpan jawaban substantif.

## C. Screening dan Deduplikasi

`S1_age18` Apakah usia Anda sekurang-kurangnya 18 tahun?

- 1 Ya.
- 0 Tidak -> tidak eligible.

`S2_domicile` Di kota/kabupaten mana rumah tangga ini berdomisili?

- Kode hanya dari daftar wilayah final.
- Di luar cakupan -> tidak eligible.

`S3_finance_role` Seberapa jauh Anda mengetahui pendapatan, aset likuid, dan seluruh utang konsumtif rumah tangga ini?

- 1 Saya pengelola/pengambil keputusan utama dan mengetahui ketiganya.
- 2 Saya ikut mengelola dan mengetahui ketiganya.
- 3 Saya hanya mengetahui sebagian.
- 4 Saya tidak mengetahuinya.

Kode 1-2 eligible; 3-4 tidak eligible.

`S4_shared_finance` Apakah Anda tinggal sendiri atau tinggal bersama orang lain yang mengelola makanan dan kebutuhan pokok bersama?

- 1 Tinggal sendiri.
- 2 Tinggal bersama dan mengelola kebutuhan pokok bersama.
- 3 Tinggal bersama tetapi keuangan/kebutuhan pokok terpisah.

Gunakan jawaban untuk menerapkan definisi rumah tangga secara konsisten pada seluruh survei.

`S5_duplicate` Apakah anggota lain dari rumah tangga yang sama sudah mengisi survei ini?

- 0 Tidak.
- 1 Ya -> jangan membuat record kedua.
- 9 Tidak tahu -> verifikasi hanya melalui mekanisme token anonim yang telah diuji; sebelum itu, perlakukan sebagai risiko duplikasi tanpa meminta identitas.

`S6_active_now` Pada hari ini, apakah rumah tangga masih memiliki sedikitnya satu kontrak/akun utang konsumtif selain KPR/KPA dan selain utang usaha yang belum ditutup atau belum dilunasi seluruhnya?

- 1 Ya.
- 0 Tidak -> tidak eligible.
- 8 Tidak tahu -> tidak eligible untuk model utama; catat outcome screening.
- 9 Menolak -> selesai.

`S7_required_window` Pada `[M-3]` sampai `[M-1]`, apakah rumah tangga mempunyai sedikitnya satu kewajiban minimum/kontraktual positif dari seluruh utang konsumtif non-KPR pada periode itu, termasuk kontrak yang mungkin sudah lunas/ditutup sebelum hari ini?

- 1 Ya.
- 0 Tidak -> tidak eligible untuk model utama meskipun utang baru aktif pada bulan survei.
- 8 Tidak tahu -> tidak eligible untuk model utama; catat outcome screening.
- 9 Menolak -> selesai.

## D. Definisi yang Ditampilkan

**Utang konsumtif non-KPR** adalah kewajiban rumah tangga untuk kebutuhan pribadi/rumah tangga, bukan pembelian rumah dan bukan modal/operasional usaha. Contoh: KTA konsumtif, pinjaman daring konsumtif, cicilan kendaraan rumah tangga, cicilan barang, kartu kredit, atau BNPL/PayLater.

**Penyangga likuid** adalah uang/aset milik rumah tangga yang secara legal dapat dipakai dalam paling lama tujuh hari tanpa pinjaman baru dan tanpa kehilangan pokok yang material.

Yang masuk ialah uang tunai, saldo rekening transaksi/tabungan, uang elektronik, serta deposito yang memenuhi aturan tujuh hari. Yang tidak masuk ialah limit kredit/pinjaman baru, saham, kripto, emas, kendaraan, properti, dana usaha/titipan/jaminan, dan pensiun terikat.

**Kebutuhan esensial** meliputi pangan dasar, utilitas, transportasi dasar, kesehatan esensial, biaya tanggungan, dan sewa atau KPR. Pembayaran utang konsumtif non-KPR tidak termasuk ketika menjawab bagian penyangga likuid.

## E. Konstruk X

`X_comp_asset` Menurut definisi di atas, kelompok mana yang boleh dipakai untuk menilai penyangga likuid?

- 1 Uang tunai, tabungan/rekening transaksi, uang elektronik, dan deposito yang memenuhi aturan tujuh hari. **Benar.**
- 2 Kelompok pada pilihan 1 ditambah emas, saham, kendaraan, dan properti.
- 3 Limit kartu kredit dan pinjaman baru.
- 8 Tidak tahu.

`X_comp_expense` Ketika menilai berapa lama rumah tangga dapat bertahan, pembayaran mana yang sengaja tidak dimasukkan ke kebutuhan esensial?

- 1 Seluruh cicilan utang konsumtif non-KPR seperti KTA, pinjol, kendaraan/barang, kartu, dan BNPL. **Benar.**
- 2 Sewa atau KPR.
- 3 Pangan dan utilitas pokok.
- 8 Tidak tahu.

Jika salah satu jawaban tidak benar, tampilkan kembali definisi standar sebelum `X_duration` dan simpan `x_comprehension_flag=1`. Jangan mengubah definisi secara spontan per responden. Cognitive interview tetap menguji apakah latihan singkat ini menimbulkan bias atau justru diperlukan.

`X_duration` Jika sumber pendapatan utama rumah tangga berhenti hari ini, berapa lama rumah tangga dapat menutup kebutuhan esensial menggunakan penyangga likuid yang memenuhi definisi di atas, tanpa mengganti pendapatan yang hilang dengan pendapatan baru, pinjaman baru, menjual aset besar, pindah rumah, atau bantuan yang belum pasti?

- 1 Kurang dari satu minggu.
- 2 Satu minggu hingga kurang dari satu bulan.
- 3 Satu hingga kurang dari tiga bulan.
- 4 Tiga hingga kurang dari enam bulan.
- 5 Enam bulan atau lebih.
- 8 Tidak tahu.
- 9 Menolak.

`X_confidence` Seberapa yakin Anda terhadap jawaban tadi?

- 1 Tidak yakin sama sekali.
- 2 Kurang yakin.
- 3 Cukup yakin.
- 4 Sangat yakin.
- 9 Menolak.

Range check aset/pengeluaran dan blok literasi tidak dimasukkan pada pilot pertama. Keduanya hanya boleh ditambahkan pada versi berikutnya bila waktu pengisian core instrument layak dan ada tujuan validasi/analitik yang dipraspesifikasikan.

## F. Roster Utang dan Konstruk Y

`D0_product_roster` Centang produk yang memiliki kewajiban positif pada sedikitnya satu bulan `[M-3]` sampai `[M-1]`.

Daftarkan seluruh kontrak in-scope pada periode historis, termasuk yang sudah lunas/ditutup sebelum tanggal survei. Household tetap harus memiliki minimal satu kontrak non-KPR aktif saat survei, tetapi kontrak aktif tersebut tidak harus kontrak yang sama. Simpan flag perubahan komposisi kontrak agar dapat dideskripsikan.

- 1 KTA/pinjaman personal formal konsumtif.
- 2 Pinjaman daring/P2P konsumtif.
- 3 Kredit kendaraan untuk penggunaan rumah tangga.
- 4 Cicilan barang/elektronik.
- 5 Kartu kredit revolving.
- 6 Cicilan kartu kredit.
- 7 BNPL/PayLater.
- 8 Pinjaman informal dengan kewajiban yang disepakati.
- 9 Kontrak konsumtif lain, jelaskan jenis tanpa menyebut identitas kreditur.

Medis dan pendidikan dicatat sebagai tujuan, bukan jenis produk; restrukturisasi dicatat sebagai status kontrak. Kategori 8-9 tetap keputusan terbuka sampai expert review. Satu baris selalu mewakili satu kontrak/akun, bukan satu tujuan atau satu kanal pembayaran.

### Ulangi untuk setiap kontrak/akun produk

`Dk_type` Jenis produk.  
`Dk_purpose` Tujuan: konsumsi umum rumah tangga / kendaraan / barang / medis / pendidikan / rumah / usaha / campuran / lainnya / tidak tahu.  
`Dk_joint` Apakah kewajiban dibagi dengan pihak di luar rumah tangga? ya/tidak; jika ya, catat aturan/sumber alokasi bagian rumah tangga dan jangan memakai pembagian otomatis.  
`Dk_restructured` Apakah jadwal telah direstrukturisasi sebelum/dalam periode?  
`Dk_channel` Apakah pembayaran produk ini dilakukan melalui kartu/pinjaman lain? Ini flag double count, bukan produk baru.  
`Dk_status_now` Apakah kontrak/akun historis ini masih aktif pada tanggal survei? Jika tidak, catat bahwa kontrak ditutup/lunas sebelum survei. Kontrak yang baru aktif setelah `[M-1]` dicatat hanya untuk memenuhi/menjelaskan active-now dan tidak membentuk Y historis.  

Kontrak bertujuan rumah/usaha benar-benar out-of-scope dan dikeluarkan. Untuk tujuan campuran atau utang bersama, bagian yang relevan hanya boleh masuk bila nominal/proporsi dan sumber alokasinya dapat ditelusuri pada setiap bulan. Bila alokasi in-scope tidak terselesaikan, tandai kontrak sebagai unresolved, buat Y household missing, dan keluarkan household dari analisis utama sambil tetap melaporkannya pada flow; jangan menghapus kontrak tersebut lalu menghitung Y dari kontrak lain saja.

Untuk setiap kontrak historis dan setiap bulan `[M-3]`, `[M-2]`, `[M-1]`, buat satu baris. Nol harus dipilih eksplisit bila dipastikan tidak ada kewajiban pada bulan itu; kosong berarti missing, bukan nol. Urutan core instrument:

- `Dk_m_statement_required`: total minimum/kontraktual kontrak yang ditampilkan atau diwajibkan untuk bulan tersebut.
- `Dk_m_household_required`: bagian dari statement required yang secara kontraktual/disepakati menjadi tanggung jawab rumah tangga; sama dengan statement required bila bukan joint debt.
- `Dk_m_consumer_required_raw`: bagian konsumtif dari household required; sama dengan household required bila tujuan sepenuhnya konsumtif. Untuk mixed purpose, nominal/proporsi dan sumber alokasinya wajib dapat ditelusuri.
- `Dk_m_allocation_source`: kontrak/statement, kesepakatan tercatat, catatan kontemporer, ingatan konsisten, tidak tahu, atau menolak.
- `Dk_m_prior_arrears_flag` dan `Dk_m_prior_arrears_amount`: apakah consumer raw memuat kewajiban yang pertama kali jatuh tempo sebelumnya; nominal wajib diisi bila flag ya.
- `Dk_m_cross_contract_flag` dan `Dk_m_cross_contract_amount`: apakah consumer raw memuat bagian kontrak lain yang sudah dienumerasi; nominal hanya diisi bila dapat diatribusikan dari statement/kontrak/catatan yang jelas.
- `Dk_m_source`: aplikasi/statement/kontrak, catatan kontemporer, ingatan, tidak tahu, atau menolak.

Pokok, bunga, biaya, pembayaran aktual, dan status pembayaran rinci bukan core instrument. Nilai clean dihitung sebagai consumer required raw dikurangi prior-arrears amount dan cross-contract amount yang benar-benar teridentifikasi. Jika alokasi joint/mixed atau adjustment yang diperlukan tidak dapat dinominalkan, contract-month menjadi missing untuk Y utama; jangan mengurangkan nilai transaksi/BNPL secara mekanis dari minimum due kartu dan jangan menganggap missing sebagai nol.

`Y_reconcile` Setelah sistem menampilkan ulang raw amount, adjustment, clean amount, subtotal per kontrak, subtotal per bulan, dan total tiga bulan, apakah ringkasan tersebut sudah mencakup semua kewajiban konsumtif non-KPR rumah tangga pada periode acuan tanpa perhitungan ganda?

- 1 Ya.
- 0 Tidak -> kembali ke roster.
- 8 Tidak tahu -> quality flag.
- 9 Menolak.

## G. Pendapatan Denominator

Untuk setiap `[M-3]`, `[M-2]`, `[M-1]`:

- `I_m_total`: total pendapatan kas bersih rumah tangga yang benar-benar tersedia pada bulan tersebut.
- `I_m_source`: catatan/aplikasi, catatan pribadi, ingatan, tidak tahu, menolak.

`I_sources_check` Untuk tiga bulan acuan, sumber yang dipertimbangkan: gaji/upah bersih, pendapatan usaha bersih yang tersedia bagi rumah tangga, pensiun, bantuan nonutang, transfer/remitansi nonutang, dan pendapatan kas sah lainnya. Rincian per sumber hanya menjadi prompt rekonsiliasi bila total tidak konsisten, bukan seluruhnya wajib diisi.

Jangan hitung pinjaman, penjualan aset, penarikan tabungan, atau transfer antar-rekening sebagai pendapatan. Pendapatan nol/negatif ditandai; record tidak masuk model rasio tetapi tetap masuk flow deskriptif.

Ketiga bulan wajib mempunyai nilai numerik eksplisit, termasuk nol yang benar. Jika satu bulan tidak tahu/menolak/tidak terselesaikan, income_total_3m dan Y utama menjadi missing; sistem dilarang menjumlahkan dua bulan yang tersedia seolah-olah tiga bulan.

## H. Covariate Kandidat

`C_site` recruitment site/channel.  
`C_area` kota/kabupaten.  
`C_age` usia pengelola keuangan dalam tahun atau band praspesifik.  
`C_education` pendidikan tertinggi.  
`C_employment` status pekerjaan utama.  
`C_hhsize` jumlah anggota rumah tangga.  
`C_dependents` jumlah anggota tanpa pendapatan yang ditanggung.  
`C_housing` milik dengan KPR / milik tanpa KPR / sewa / menumpang / lainnya.  
`C_income_stability` **belum menjadi butir aktif**. Sebelum dipakai, tetapkan sumber item, periode 12 bulan pra-M3, definisi pendapatan pembanding, threshold/mapping, opsi jawaban, dan timing.  
`C_pre_shock` **belum menjadi butir aktif**. Sebelum dipakai, tetapkan jenis guncangan, definisi “pengeluaran besar”, tanggal mulai/akhir, serta aturan kejadian yang berlanjut ke jendela Y.

Blok literasi/kapabilitas hanya ditambahkan bila menggunakan butir berlisensi/terbuka yang sumber dan terjemahannya diverifikasi, expert review menyetujui, dan waktu pengisian pilot masih layak.

Kedua placeholder kovariat tidak boleh muncul pada form lapangan atau M1 sampai decision log menutup definisi dan cognitive review membuktikan proses responsnya.

## I. Derived Variables

`x_cat` = `X_duration` kode 1-5.  
`x_ge3m` = 1 bila `x_cat` 4-5; sensitivitas saja.  
`Dk_m_required_clean` = `Dk_m_consumer_required_raw - Dk_m_prior_arrears_amount - Dk_m_cross_contract_amount` hanya bila alokasi household/mixed dan semua adjustment yang ditandai terselesaikan.  
`debt_window_complete` = 1 bila seluruh kontrak historis in-scope mempunyai tiga clean amount numerik, termasuk nol eksplisit.  
`required_total_3m` = jumlah clean amount hanya bila `debt_window_complete=1`; jangan skip missing.  
`income_window_complete` = 1 bila ketiga `I_m_total` numerik; `income_total_3m` hanya dijumlahkan bila lengkap.  
`y_ratio` = `required_total_3m / income_total_3m`, hanya bila keduanya positif.  
`ln_y` = ln(`y_ratio`) untuk sensitivitas OLS.  
`verified_record` = 1 bila seluruh nilai kewajiban dan pendapatan utama bersumber dari aplikasi/statement/kontrak atau catatan kontemporer.  
`x_comprehension_flag` = 1 bila responden salah pada sedikitnya satu comprehension item sebelum X.  
`duplicate_risk_flag`, `arrears_flag`, `restructure_flag`, `income_zero_flag`, dan `logic_flag` disimpan terpisah.

## J. Validasi dan Stop Rules Pilot

Catat waktu penyelesaian, drop-off per bagian, missing per item, refusal nominal, penggunaan statement, jenis salah paham, frekuensi comprehension flag, rekonsiliasi roster, ketimpangan kategori X, dan nilai Y yang memerlukan klarifikasi.

Instrumen kembali ke revisi bila ditemukan salah satu kondisi substantif berikut:

- responden tetap tidak memahami pengecualian cicilan non-KPR dari X setelah definisi standar dan comprehension item;
- kartu/BNPL sering dihitung ganda;
- kewajiban bulanan tidak dapat dipisahkan dari pembayaran sukarela atau tunggakan lama;
- informan tidak mengetahui seluruh keuangan rumah tangga;
- refusal/missing membuat Y tidak dapat dihitung pada bagian besar pilot;
- satu/lebih kategori X terlalu jarang untuk model dummy yang direncanakan;
- waktu atau sensitivitas survei tidak layak secara etis/praktis.

Tidak ada persentase stop rule yang dinyatakan sebagai baku universal. Ambang numerik harus diputuskan dengan alasan, ukuran pilot, dan penyebut yang eksplisit sebelum pilot.

## K. Catatan Integritas

- Jangan mengisi data simulasi sebagai responden aktual.
- Jangan mengubah kategori, periode, numerator, kontrol, atau model setelah melihat hasil utama tanpa melabelinya eksploratori.
- Jangan menghapus nilai ekstrem yang benar.
- Jangan menyebut instrumen ini tervalidasi sebelum review dan pilot aktual selesai.
- Jangan menyebut hasil mewakili Jabodetabek bila desain rekrutmen tidak probabilistik.

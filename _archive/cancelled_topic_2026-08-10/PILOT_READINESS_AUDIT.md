# Audit Kesiapan Operasional Sebelum Pilot — Fase 3

> Status: audit mahasiswa peneliti terhadap `SOURCE_OF_TRUTH.md`, `METHODOLOGY_BLUEPRINT.md`, dan `INSTRUMENT_DRAFT.md` per 6 Agustus 2026. Dokumen ini tidak mengesahkan gerbang Data/Metodologi dan tidak memuat hasil responden.
> **Snapshot historis:** temuan ini dibuat sebelum koreksi 10 Agustus 2026. Penyelesaian kanonis dan keputusan yang masih terbuka harus dibaca pada SOURCE_OF_TRUTH.md serta DECISION_LOG.md; isi lama di bawah dipertahankan sebagai jejak audit, bukan status terbaru.  


## 1. Kesimpulan singkat

Pertanyaan penelitian, unit analisis, desain potong lintang, pengukuran Y dengan tiga bulan kalender historis yang sama, pengecualian KPR dari Y, serta larangan klaim kausal sudah konsisten. Instrumen belum boleh masuk field pilot karena bulan/site belum diisi, klasifikasi kontrak belum dibekukan, jalur etik dan expert reviewer belum nyata, cognitive interview belum dilakukan, kemampuan perangkat lunak belum dibuktikan, dan parameter prevalensi/power belum tersedia.

## 2. Ketidaksesuaian atau keputusan yang belum ditutup

| Prioritas | Temuan konkret | Bukti dokumen | Tindakan manusia yang diperlukan |
|---|---|---|---|
| Kritis | Skenario X tidak identik: sumber kanonis menyebut **sumber pendapatan utama hilang**, sedangkan blueprint/instrumen menyebut **seluruh pendapatan rutin berhenti**. Keduanya dapat menghasilkan jawaban durasi berbeda. | `SOURCE_OF_TRUTH.md` §6; `METHODOLOGY_BLUEPRINT.md` §4; `INSTRUMENT_DRAFT.md` E–`X_duration` | Dosen/metodolog menetapkan satu skenario; uji pemahamannya dalam expert review dan cognitive interview. |
| Kritis | Kategori roster 8–12 belum diputuskan. “Utang medis” dan “utang pendidikan” adalah tujuan, sedangkan “restrukturisasi” adalah status, bukan jenis kontrak; ini berisiko menggandakan akun yang sama. | `INSTRUMENT_DRAFT.md` F–`D0_product_roster`; `Dk_purpose`; `Dk_restructured` | Bekukan arsitektur **satu baris per kontrak/akun**; simpan tujuan dan restrukturisasi sebagai atribut. Putuskan perlakuan utang informal dan tujuan campuran. |
| Kritis | KPR wajib dikeluarkan dari Y dan “dicatat terpisah”, tetapi instrumen hanya mencatat status hunian/KPR; nominal biaya hunian/KPR tidak direkam secara terpisah. | `SOURCE_OF_TRUTH.md` §5–6; `INSTRUMENT_DRAFT.md` D, E, H–`C_housing` | Tentukan arti “dicatat terpisah”: minimal status KPR, atau juga cicilan hunian. Jika nominal tidak diperlukan karena X berupa durasi langsung, revisi source of truth agar tidak menjanjikan data yang tidak dikumpulkan. |
| Mayor | Periode masih placeholder dan fieldwork belum dikunci satu bulan. | `INSTRUMENT_DRAFT.md` A; `SOURCE_OF_TRUTH.md` §9 dan §11 | Tetapkan tanggal buka/tutup survei dan tulis tiga nama bulan kalender secara eksplisit di setiap layar/item. |
| Mayor | Perlakuan reksa dana pasar uang, pembulatan nominal, penalti, arrears, jadwal tidak bulanan, utang bersama, dan kontrak tujuan campuran belum final. | `SOURCE_OF_TRUTH.md` §6 dan §11; `METHODOLOGY_BLUEPRINT.md` §4–5; `INSTRUMENT_DRAFT.md` E–F | Dosen, ahli isi, dan mahasiswa menandatangani decision log sebelum cognitive interview final. |
| Mayor | Consent belum berisi durasi, potensi ketidaknyamanan, insentif bila ada, jadwal retensi/penghapusan kontak, identitas/contact person, dan nomor/persetujuan etik bila diwajibkan kampus. | `INSTRUMENT_DRAFT.md` A–B; `METHODOLOGY_BLUEPRINT.md` §10 | Konfirmasi format etik UKRIDA dan lengkapi informasi yang benar; jangan membuat nomor persetujuan. |
| Mayor | Token anonim untuk deduplikasi disebutkan, tetapi cara membuat token yang konsisten pada anggota rumah tangga yang berbeda belum ada. | `INSTRUMENT_DRAFT.md` C–`S5_duplicate`; `METHODOLOGY_BLUEPRINT.md` §10 | Pilih mekanisme teknis yang tidak mengumpulkan identitas, uji false match/non-match, dan pisahkan data kontak insentif. |
| Mayor | GLM Gamma, cluster-aware inference, quantile regression, multiple imputation, adjusted predictions, dan power simulation belum dikaitkan dengan perangkat lunak yang benar-benar dikuasai. | `SOURCE_OF_TRUTH.md` §10–12; `METHODOLOGY_BLUEPRINT.md` §7–9 | Pilih satu software/versi/lisensi. Lakukan dry run seluruh pipeline memakai data sintetis yang jelas dilabeli, bukan data responden. |
| Mayor | Prevalensi eligible, proporsi lima kategori X, dispersi Y, ICC, ukuran cluster, nonresponse, dan missingness belum diketahui; karena itu kebutuhan sampel utama belum dapat dihitung secara jujur. | `SOURCE_OF_TRUTH.md` §10–12; `METHODOLOGY_BLUEPRINT.md` §9 | Catat data screening dan cluster pada field pilot; gunakan skenario untuk perencanaan awal dan simulasi berbasis parameter pilot untuk keputusan akhir. |

## 3. Item instrumen yang ambigu atau terlalu berat

### Ambigu/berisiko salah klasifikasi

1. `X_check_assets` dan `X_check_expenses` berbunyi “yang Anda pertimbangkan ketika menjawab”, padahal ditempatkan **sebelum** `X_duration`. Instruksi “minta responden menjawab ulang X” juga tidak cocok dengan urutan ini. Pilih salah satu: pertanyaan durasi dahulu lalu comprehension check, atau daftar definisi dahulu tanpa frasa “menjawab ulang”.
2. “Tanpa kehilangan pokok yang material”, “kebutuhan esensial”, “transportasi dasar”, “kesehatan esensial”, dan “biaya tanggungan” memerlukan padanan bahasa responden dan contoh terbatas; kata “material” tidak memiliki ambang operasional.
3. `X_check_assets` opsi E, “dana yang sudah diniatkan untuk cicilan”, dapat terasa kontradiktif karena cicilan non-KPR dikeluarkan dari kebutuhan X. Maksud yang diuji ialah fungibilitas dana, tetapi bahasanya perlu cognitive probing.
4. `S4_shared_finance` belum menentukan perlakuan penghuni serumah yang sebagian kebutuhan pokoknya bersama tetapi pendapatan/utang terpisah; definisi rumah tangga harus disertai contoh kasus batas.
5. `Dk_purpose` kategori “campuran” tidak mempunyai aturan inklusi atau pembagian kewajiban. Jangan menyerahkan keputusan ini kepada enumerator secara spontan.
6. `Dk_joint` meminta “bagian rumah tangga” tanpa cara alokasi bila tidak ada perjanjian nominal. Tentukan apakah memakai kewajiban yang benar-benar menjadi tanggung jawab rumah tangga, proporsi yang disepakati, atau mengecualikan bila tidak diketahui.
7. `Dk_channel` belum cukup untuk mencegah double count. BNPL yang dibayar melalui kartu dapat masuk sebagai kontrak BNPL dan kemudian muncul di minimum due kartu; perlu layar rekonsiliasi kontrak-bulan dan aturan penelusuran sumber transaksi.
8. `Dk_m_required` dan `Dk_m_prior_arrears` dapat tumpang tindih. Instrumen perlu membedakan kewajiban yang **pertama kali jatuh tempo** pada bulan tersebut dari total tagihan yang memuat tunggakan lama.
9. `Y_reconcile` menanyakan apakah total sudah lengkap tetapi tidak menampilkan total per bulan/per kontrak. Responden tidak dapat merekonsiliasi angka yang tidak diperlihatkan kembali.
10. `C_income_stability` belum memiliki pembanding dan ambang penurunan; `C_pre_shock` “pengeluaran besar” juga belum memiliki definisi/waktu yang cukup presisi.
11. `verified_record`, `logic_flag`, dan flag lain belum mempunyai algoritma codebook yang dapat direplikasi.

### Terlalu berat untuk bentuk sekarang

1. Untuk setiap kontrak, instrumen meminta enam atribut awal dan tujuh isian untuk masing-masing dari tiga bulan. Satu kontrak dapat menghasilkan sekitar 27 respons; tiga kontrak dapat melampaui 80 respons sebelum blok pendapatan.
2. Komponen `principal`, `interest`, dan `fee` tidak dipakai untuk menghitung outcome utama bila `required` sudah mencerminkan minimum/kontraktual. Banyak pemegang kartu/BNPL juga tidak mengetahui pemisahannya. Jadikan breakdown opsional/audit, bukan wajib, kecuali ahli isi membuktikan perlunya.
3. `Dk_m_paid` dan `Dk_m_status` hanya deskriptif, sensitif, dan menambah beban. Pertahankan hanya jika mempunyai tujuan analitik/quality-control yang dipraspesifikasikan.
4. Blok pendapatan meminta enam komponen plus total dan sumber untuk setiap bulan. Pertimbangkan total pendapatan bersih per bulan sebagai butir utama dengan checklist sumber sekali, lalu lakukan rincian hanya saat rekonsiliasi; keputusan ini harus diuji, bukan langsung diasumsikan lebih valid.
5. Range check X dan blok literasi sebaiknya tidak dimasukkan sekaligus pada pilot pertama sebelum waktu penyelesaian roster dan pendapatan diketahui.

## 4. Checklist eksekusi minimum

### A. Sebelum cognitive interview

- [ ] **Akses nyata:** isi daftar kota/kabupaten, minimal satu site/gatekeeper yang telah menyatakan dapat membantu, kanal rekrutmen, perkiraan arus orang yang dapat diskrining, dan larangan gatekeeper mengetahui peserta/jawaban. Bukti: nama organisasi/komunitas, contact person, bentuk izin, wilayah, tanggal konfirmasi.
- [ ] **Batas inferensi:** sepakati apakah cakupan tetap multisitus Jabodetabek atau dipersempit mengikuti akses nyata; larang kata “representatif”.
- [ ] **Kalender:** tetapkan satu bulan fieldwork `[S]`, tanggal buka/tutup, serta tiga bulan lengkap `[M-3]`–`[M-1]`. Jika survei melampaui `[S]`, tetapkan aturan stop/restart; jangan menggeser bulan per responden.
- [ ] **Decision log konstruk:** selesaikan skenario kehilangan pendapatan pada X, instrumen pasar uang, kontrak campuran, utang informal/medis/pendidikan, restrukturisasi, arrears, penalti, jadwal tidak bulanan, utang bersama, pemeriksaan statement, dan pembulatan.
- [ ] **Etik/privasi:** konfirmasi jalur persetujuan UKRIDA, format consent, retensi data, insentif, dan contact person; jangan mencantumkan persetujuan yang belum ada.
- [ ] **Expert review nyata:** tetapkan nama, kompetensi, konflik kepentingan, dokumen yang dinilai, formulir komentar, dan decision log. Domain minimum yang harus tercakup: keuangan rumah tangga/utang, metodologi survei/statistik, serta etik/privasi. Jumlah reviewer mengikuti keputusan pembimbing/etik, bukan angka buatan agen.
- [ ] **Versi cognitive draft:** perbaiki urutan comprehension check, arsitektur roster satu kontrak-satu baris, dan ringkas field bulanan; beri nomor versi/tanggal.
- [ ] **Software:** nyatakan `software + versi + akses/lisensi + tingkat kemampuan`. Dry run: import/reshape roster, aturan double count/arrears, hitung X/Y, GLM Gamma-log, uji global X, adjusted means/ratios, diagnosis, cluster-aware SE bila relevan, dan simulasi power. Jika SPSS tidak menutup pipeline, sepakati penyederhanaan atau kesiapan belajar R sebelum pengumpulan utama.

### B. Cognitive interview aktual sebelum field pilot

- [ ] Rekrut peserta yang memenuhi atau mendekati profil eligible melalui jalur yang etis; jangan mencatat mereka sebagai data pilot kuantitatif.
- [ ] Uji dengan think-aloud/probing: definisi rumah tangga, “pendapatan berhenti”, aset tujuh hari, pengecualian cicilan dari X, minimum due, tunggakan lama, restrukturisasi, pembayaran BNPL lewat kartu, bagian utang bersama, pendapatan usaha bersih, dan tiga bulan recall.
- [ ] Catat kutipan/parafrase masalah, butir, revisi, alasan menerima/menolak revisi, durasi, serta versi instrumen. Lakukan putaran ulang sampai isu kritis teratasi; jangan mengarang jumlah wawancara atau hasil.
- [ ] Minta expert reviewer memeriksa ulang perubahan material dan bekukan versi field-pilot.

### C. Persiapan dan data yang wajib keluar dari field pilot

- [ ] Form elektronik menerapkan skip logic, satu kontrak-satu baris, recap per bulan, kode `tidak tahu` terpisah dari `menolak`, token deduplikasi, serta log site/cluster tanpa identitas finansial.
- [ ] Tetapkan definisi denominator untuk setiap indikator operasional sebelum peluncuran: completion, refusal nominal, missing Y, double count, contamination X, dan penggunaan statement.
- [ ] Catat per site: jumlah diundang/didatangi, disaring, eligible, menolak, mulai, lengkap, dan dapat dihitung X/Y. **Prevalensi eligible aktual = eligible / seluruh yang benar-benar disaring**, dilaporkan per site dan total dengan penyebut eksplisit.
- [ ] Kumpulkan parameter perencanaan: proporsi lima kategori X, distribusi/mean-variance Y positif, korelasi kovariat, jumlah dan ukuran cluster, ICC bila dapat diestimasi secara masuk akal, missingness, nonresponse, completion time, serta kemampuan responden melihat statement. Jangan memperlakukan estimasi pilot kecil sebagai presisi tinggi.
- [ ] Putuskan stop/revisi berdasarkan masalah substantif dan ambang yang dipraspesifikasikan; jangan mencari model yang paling signifikan.

### D. Setelah pilot, sebelum survei utama

- [ ] Pembimbing menetapkan *smallest effect of interest* yang bermakna secara ekonomi dan jumlah kontrol final dari DAG sebelum melihat hasil utama.
- [ ] Jalankan simulasi power model final memakai skenario yang mencakup proporsi X, dispersi Y, korelasi kovariat, ICC, ukuran/ketimpangan cluster, dan effect size. Laporkan seluruh asumsi dan sensitivitas, bukan satu angka N tanpa konteks.
- [ ] Inflasikan kebutuhan record analitik untuk design effect, missing X/Y, nonresponse, dan prevalensi eligible aktual; pisahkan target `orang disaring`, `eligible`, dan `record analitik lengkap`.
- [ ] Bekukan codebook, model utama, sensitivitas, aturan cleaning, periode, serta version hash sebelum survei utama.

## 5. Keputusan audit

- **Siap expert review:** YA, setelah decision log awal dan versi instrumen diringkas.
- **Siap cognitive interview:** BELUM; skenario X dan arsitektur roster belum final.
- **Siap field pilot:** BELUM; gatekeeper/site, kalender, etik, cognitive evidence, software dry run, dan form logic belum tersedia.
- **Siap power final/survei utama:** BELUM; prevalensi eligible dan distribusi nyata dari pilot belum tersedia.


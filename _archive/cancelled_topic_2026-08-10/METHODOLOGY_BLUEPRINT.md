# Blueprint Metodologi Fase 3

> Status: draf audit; belum mengesahkan gerbang Data atau Metodologi  
> Pertanyaan kanonis: Apakah kecukupan penyangga likuid rumah tangga berasosiasi dengan beban pembayaran utang konsumtif non-KPR pada rumah tangga yang memiliki utang konsumtif aktif di Jabodetabek?

## 1. Estimand dan Batas Inferensi

Estimand adalah perbandingan model-based atas rerata rasio beban kewajiban pembayaran kontraktual historis menurut kategori durasi penyangga likuid saat survei, setelah penyesuaian kovariat, di antara rumah tangga yang memenuhi syarat, berhasil direkrut, dan menyelesaikan data analitik melalui situs penelitian (R=1). Desain observasional potong lintang tidak mengidentifikasi arah sebab akibat, dan adjusted predictions tidak mengubah sampel nonprobabilitas menjadi representatif.

Pembatasan pada pemegang utang aktif dapat menciptakan selection atau collider bias. Hasil tidak boleh digeneralisasikan kepada seluruh rumah tangga Jabodetabek dan tidak menjelaskan kemungkinan rumah tangga mulai berutang.

Y merangkum kewajiban yang pertama kali jatuh tempo selama tiga bulan kalender selesai sebelum survei, sedangkan X dinilai pada tanggal survei. Karena Y secara waktu mendahului X dan dapat telah mengikis aset likuid, model tidak boleh ditafsirkan sebagai efek X terhadap Y; estimand tetap asosiasi antara buffer saat survei dan burden historis.

## 2. Unit Analisis dan Informan

- Unit analisis: satu rumah tangga.
- Rumah tangga: satu orang atau kelompok orang yang tinggal dalam tempat tinggal yang sama dan mengelola makanan serta kebutuhan hidup pokok secara bersama.
- Informan: orang dewasa yang menjadi pengelola atau benar-benar mengetahui pendapatan, aset likuid, dan seluruh kewajiban utang konsumtif rumah tangga.
- Hanya satu jawaban per rumah tangga.

### Inklusi

1. Usia sekurang-kurangnya 18 tahun.
2. Berdomisili pada wilayah penelitian yang benar-benar dicakup rekrutmen.
3. Memenuhi definisi informan keuangan rumah tangga.
4. Memiliki sedikitnya satu utang konsumtif non-KPR yang masih aktif pada tanggal survei.
5. Memiliki kewajiban minimum/kontraktual positif yang pertama kali jatuh tempo dalam jendela Y.
6. Memiliki total pendapatan kas bersih rumah tangga positif dalam jendela denominator.
7. Bersedia merinci kewajiban per produk dan pendapatan per bulan tanpa menyerahkan identitas finansial.

### Eksklusi

- KPR/KPA dan utang modal atau operasional usaha, walau kontraknya atas nama pribadi.
- Responden yang hanya mengetahui utangnya sendiri ketika keuangan rumah tangga digabung.
- Duplikasi anggota rumah tangga.
- Pinjaman, pencairan aset, dan transfer antar-rekening yang keliru dilaporkan sebagai pendapatan.
- Observasi yang terbukti salah input. Nilai ekstrem yang benar tidak dikeluarkan hanya karena besar.

## 3. Sampling yang Realistis

Rancangan kerja adalah purposive multisite quota sampling dengan screening, kecuali mahasiswa memperoleh kerangka sampel dengan probabilitas pemilihan yang dapat dihitung. Istilah site dan quota hanya menunjukkan diversifikasi rekrutmen, bukan stratifikasi probabilistik populasi.

1. Tetapkan hanya kota/kabupaten dan kanal yang benar-benar dapat diakses.
2. Gunakan beberapa jenis lokasi netral: komunitas lingkungan, tempat kerja, pusat kegiatan masyarakat, dan kanal umum; jangan hanya merekrut dari kampus, teman, atau komunitas pengguna BNPL.
3. Praspesifikasikan site, channel, quota variasi wilayah/demografis, dasar targetnya, serta unit cluster sebenarnya sebelum melihat hasil; quota populasi umum tidak otomatis sesuai dengan populasi pemegang utang aktif.
4. Catat per site: diundang/disaring, eligible, menolak, tidak lengkap, dan lengkap.
5. Batasi konsentrasi responden dari satu jaringan sosial atau tempat kerja.
6. Simpan recruitment site dan channel dalam data untuk audit ketergantungan cluster.
7. Jangan memakai istilah representatif dan jangan membuat bobot tanpa probabilitas pemilihan atau target kalibrasi resmi yang sah.

Rumus Slovin dan aturan sepuluh responden per variabel tidak diterima sebagai power analysis.

## 4. X: Kategori Durasi Penyangga Likuid

Untuk tetap dekat dengan skenario OECD/INFE, pertanyaan meminta responden membayangkan sumber pendapatan utama rumah tangga berhenti pada tanggal survei. Responden menilai berapa lama kebutuhan esensial dapat ditutup dari aset yang secara legal dapat digunakan dalam paling lama tujuh hari, tanpa mengganti pendapatan yang hilang dengan pendapatan baru, pinjaman baru, menjual aset besar, pindah rumah, atau bantuan yang belum pasti. Adaptasi unit dari individu ke rumah tangga serta pengecualian cicilan non-KPR tetap harus disebut dan diuji.

### Aset yang masuk

- Uang tunai.
- Saldo rekening transaksi/tabungan dan uang elektronik.
- Deposito yang dapat digunakan dalam tujuh hari tanpa kehilangan pokok yang material.
- Instrumen lain hanya jika benar-benar dapat digunakan dalam tujuh hari tanpa berutang atau penalti material.
- Dana yang secara mental dialokasikan untuk cicilan tetap masuk bila secara legal fungible dan tersedia; earmarking mental tidak mengubah likuiditas.

### Aset yang keluar

- Dana usaha, dana titipan, aset yang dijaminkan, dan pensiun terikat.
- Saham, kripto, emas, kendaraan, dan properti pada definisi utama.
- Limit kartu kredit atau pinjaman baru.
- Bantuan keluarga yang belum pasti.

### Pengeluaran esensial

Masuk: pangan dasar, utilitas, transportasi dasar, kesehatan esensial, biaya tanggungan, dan biaya hunian aktual termasuk sewa atau KPR. Keluar: seluruh pembayaran utang konsumtif non-KPR yang membentuk Y.

Kategori utama:

1. Kurang dari satu minggu.
2. Satu minggu hingga kurang dari satu bulan.
3. Satu hingga kurang dari tiga bulan.
4. Tiga hingga kurang dari enam bulan.
5. Enam bulan atau lebih.

Tidak tahu dan menolak adalah missing. X adalah adaptasi OECD/INFE QF13, bukan instrumen asli yang tervalidasi. Cronbach alpha tidak relevan untuk satu pertanyaan keadaan finansial; bukti yang diperlukan adalah validitas isi, proses respons, konsistensi logika, dan bila mungkin test-retest pada kondisi rumah tangga yang tidak berubah.

## 5. Y: Beban Kewajiban Pembayaran Kontraktual Historis

### Opsi kerja yang direkomendasikan

Gunakan tiga bulan kalender lengkap yang telah selesai sebelum bulan survei. Untuk setiap produk dan bulan, kumpulkan kewajiban minimum atau kontraktual yang pertama kali jatuh tempo pada bulan itu, bukan jumlah sukarela yang dibayar lebih cepat. Denominator memakai pendapatan kas bersih aktual pada tiga bulan kalender yang sama.

Y_i = jumlah kewajiban minimum atau kontraktual utang konsumtif non-KPR selama tiga bulan / jumlah pendapatan kas bersih rumah tangga selama tiga bulan.

Alasan: semua tagihan kartu revolving dan pendapatan pada periode yang sama sudah terbentuk saat survei. Versi forward tiga bulan ditolak sebagai model utama karena minimum kartu kredit bulan kedua dan ketiga belum diketahui.

### Numerator

Masukkan bila kontrak mempunyai kewajiban pada jendela historis dan tujuan/portion-nya in-scope, meskipun kontrak sudah ditutup sebelum survei. Household secara terpisah wajib mempunyai minimal satu utang non-KPR aktif saat survei; kontraknya tidak harus sama.

- KTA atau pinjaman personal konsumtif.
- Pinjaman daring/P2P konsumtif.
- Kredit kendaraan untuk penggunaan rumah tangga.
- Cicilan barang atau elektronik.
- Kartu kredit revolving dan cicilan kartu.
- BNPL/PayLater.
- Kontrak konsumtif lain yang lolos klasifikasi praspesifik.

Catat per kontrak dan bulan: statement required total; bagian tanggung jawab rumah tangga; bagian tujuan konsumtif; adjustment tunggakan lama; adjustment cross-contract; serta sumber angka/alokasi. Pokok, bunga, biaya, actual paid, dan status rinci bukan core instrument. Jangan meminta satu angka total rumah tangga tanpa enumerasi kontrak.

Aturan wajib:

- KPR/KPA dan utang usaha dikeluarkan.
- Pembayaran sukarela di atas minimum, pelunasan dipercepat, dan penalti hipotetis dikeluarkan dari numerator utama.
- Penalti yang sudah dibebankan dan wajib pada bulan acuan dicatat terpisah; keputusan memasukkannya dipraspesifikasikan.
- Arrears yang berasal dari sebelum jendela dicatat terpisah agar kewajiban yang sama tidak dihitung berulang.
- BNPL yang dibayar melalui kartu tidak dihitung dua kali; kontrak sumber adalah unit enumerasi, kanal pembayaran hanya atribut.
- Restrukturisasi mengikuti jadwal kontrak yang berlaku pada bulan acuan; jadwal lama tidak ikut dihitung.
- Utang bersama di luar rumah tangga hanya memasukkan bagian kewajiban rumah tangga yang dapat dibuktikan atau diketahui.

### Denominator

Pendapatan kas bersih aktual yang tersedia bagi rumah tangga per bulan: gaji bersih, pendapatan usaha bersih yang benar-benar ditarik untuk rumah tangga, pensiun, bantuan, dan transfer nonutang. Keluarkan pinjaman, penjualan aset, penarikan tabungan, dan transfer antar-rekening.

Pendapatan nol atau negatif tidak dipaksa masuk model rasio. Jumlah kasusnya dilaporkan sebagai bagian flow responden dan dianalisis deskriptif terpisah.

### Hipotesis Statistik Kandidat

Pedoman UKRIDA meminta pengembangan hipotesis untuk penelitian kuantitatif. Karena teori dan coholding mechanisms tidak mendukung arah deterministik, hipotesis kandidat bersifat dua sisi dan diuji secara global:

- H0: conditional mean beban kewajiban pembayaran kontraktual historis sama pada seluruh kategori durasi penyangga likuid setelah adjustment yang dipraspesifikasikan.
- H1: sekurang-kurangnya satu conditional mean berbeda.

H1 tidak menyatakan pengaruh kausal atau arah positif/negatif. Formulasi final memerlukan persetujuan DPS manusia dan harus konsisten dengan uji global empat derajat bebas.

## 6. DAG dan Kontrol

```text
Kapasitas ekonomi/life cycle ----> X
Kapasitas ekonomi/life cycle ----> Y
Guncangan pendapatan/kesehatan ---> X
Guncangan pendapatan/kesehatan ---> Y
Literasi/self-control ------------> X
Literasi/self-control ------------> Y

X ----?---- Y
Y ----?---- X
```

Model disajikan bertingkat:

- M0: X tanpa penyesuaian.
- M1a kandidat: site/wilayah, usia pengelola, pendidikan, dan status pekerjaan.
- M1b kandidat menambahkan status hunian/KPR, ukuran rumah tangga, dan jumlah tanggungan; model ini mengubah estimand menjadi perbandingan pada komposisi household yang setara.
- Ketidakstabilan pendapatan dan guncangan pra-periode hanya boleh ditambahkan setelah sumber item, periode, definisi, threshold/mapping, dan timing disahkan expert/cognitive review.
- Ukuran literasi/kapabilitas hanya bila memakai butir terbuka/berizin yang tervalidasi, beban survei layak, dan DAG membenarkan.

Ukuran rumah tangga, tanggungan, dan hunian turut membentuk kebutuhan esensial X; penyesuaian atasnya mengubah estimand menjadi asosiasi pada komposisi rumah tangga yang setara. Aset likuid, pengeluaran esensial, pembayaran, jumlah produk, saldo utang, BNPL use, tunggakan, dan distress tidak menjadi kontrol utama karena merupakan komponen atau kemungkinan akibat X/Y.

Pendapatan adalah penyebut Y. Karena risiko denominator bias, analisis pendamping wajib memakai required_total_3m nominal sebagai outcome. Kandidat utama pendamping adalah Gamma-log dengan log(income_total_3m) sebagai kovariat yang koefisiennya diestimasi, bukan offset sehingga elastisitas tidak dipaksa satu. Spline hanya sensitivitas bila pilot/diagnostik sebelum analisis utama menunjukkan nonlinieritas yang material.

## 7. Model Statistik

Model kandidat utama setelah pilot: generalized linear model Gamma dengan log link, X sebagai empat dummy dari lima kategori. Model ini hanya disahkan jika Y positif dan mean-variance pattern pilot mendukung Gamma.

Pelaporan utama:

- distribusi numerator nominal dan denominator pendapatan pada setiap kategori X;
- uji global empat derajat bebas untuk X;
- adjusted predicted mean Y tiap kategori;
- mean ratio beserta confidence interval;
- estimasi, ketidakpastian, dan ukuran efek, bukan hanya p-value;
- bahasa asosiasi buffer saat survei dengan burden historis, bukan pengaruh kausal.

Paket analisis minimum yang dipraspesifikasikan:

1. Gamma-log pada rasio sebagai model utama kandidat.
2. Pembayaran nominal sebagai outcome Gamma-log dengan log pendapatan sebagai kovariat terestimasi untuk analisis pendamping wajib; spline hanya sensitivity yang dipraspesifikasikan bila layak.
3. OLS pada log(Y) dengan HC3 atau standard error cluster-aware yang layak sebagai distributional check.
4. X biner kurang dari tiga bulan versus sekurang-kurangnya tiga bulan, hanya sebagai pembanding NFCS.

Median quantile regression, uji tren ordinal, multiple imputation, CR2/wild-cluster bootstrap, dan subset record terverifikasi hanya dipakai bila data, jumlah cluster, perangkat lunak, missingness, dan kapasitas mahasiswa membenarkan. Analisis tambahan tidak boleh menjadi dekorasi metodologis.

Jangan membuat dummy beban utang tinggi tanpa ambang regulator/literatur yang sepadan. Jangan memilih model karena memberi hasil paling signifikan.

## 8. Cluster, Missing, dan Nilai Ekstrem

- Jika rekrutmen berkelompok, prioritaskan banyak cluster kecil.
- CR2/GEE atau cluster-robust digunakan bila jumlah cluster memadai; cluster sedikit memerlukan inferensi small-sample atau wild-cluster bootstrap dan tetap dibatasi.
- Fixed effect wilayah tidak menghilangkan ketergantungan cluster.
- Tidak tahu dan menolak disimpan sebagai kode berbeda.
- X/Y hilang tidak diimputasi dengan mean, median, atau kategori terendah.
- Model utama dapat complete-case pada X/Y; tampilkan flow dan bandingkan kasus lengkap versus tidak lengkap.
- Missing covariate dapat diimputasi multipel hanya dengan model yang memasukkan X, Y, site, dan prediktor missingness.
- Rasio di atas satu mungkin benar. Verifikasi komponen; jangan hapus atau winsorize otomatis.
- Leverage, Cook distance, DFBETA, residual, dispersion, dan link diperiksa sebagai diagnosis, bukan alasan mekanis membuang data.

## 9. Pilot dan Power

Urutan wajib:

1. Expert content review atas definisi rumah tangga, X, klasifikasi produk, dan periode Y.
2. Cognitive interview untuk menguji pemahaman istilah, pengecualian cicilan non-KPR dari X, recall tagihan, dan risiko double count.
3. Field pilot aktual untuk completion time, refusal, missing, konsistensi X, ketersediaan statement, proporsi kategori X, distribusi Y, prevalensi eligible, dan konsentrasi cluster.
4. Bekukan codebook dan minimum effect yang bermakna secara ekonomi sebelum survei utama.
5. Simulasikan power model final dengan proporsi X, dispersion Y, korelasi covariate, ICC, ukuran cluster, dan minimum effect dari keputusan substantif/pilot.
6. Inflasikan kebutuhan analitis untuk design effect, missing, nonresponse, dan tingkat eligibility aktual.

Design effect kasar: DEFF = 1 + (mbar - 1)ICC. Untuk cluster tidak seimbang: DEFF sekitar 1 + {((CV_m)^2 + 1)mbar - 1}ICC. Rumus ini pemeriksaan awal; simulasi model final lebih utama.

Pilot tidak boleh dipakai untuk mencari spesifikasi yang signifikan. Hasil pilot aktual tidak boleh dibuat oleh agen. Responden pilot tidak digabungkan otomatis dengan survei utama; penggabungan hanya dapat dipertimbangkan bila kriterianya dipraspesifikasikan dan instrumen, scoring, populasi, serta prosedur tidak berubah material.

## 10. Privasi dan Integritas

- Tidak mengumpulkan NIK, alamat rinci, nomor rekening, kredensial, nama akun, atau unggahan screenshot.
- Responden boleh membuka catatan pribadi tanpa menyerahkannya.
- Nilai dapat dibulatkan dengan aturan seragam yang ditetapkan sebelum survei.
- Token deduplikasi acak dipisahkan dari data jawaban.
- Kontak insentif disimpan terpisah dan dihapus sesuai jadwal retensi.
- Gatekeeper tidak mengetahui siapa yang ikut atau isi jawaban.
8. Definisi final income instability/pre-shock dan keputusan set kovariat M1 melalui DAG.
- Informed consent menjelaskan sensitivitas data, hak berhenti, dan penggunaan akademik.

## 11. Blocker Sebelum Gerbang Lulus

1. Daftar wilayah, site, komunitas, dan gatekeeper yang benar-benar dapat diakses.
2. Penerimaan batas inferensi nonprobabilitas atau penyempitan populasi.
3. Persetujuan atas jendela trailing tiga bulan dan perlakuan utang informal, medis, pendidikan, restrukturisasi, tunggakan, serta penalti.
4. Keputusan apakah pemeriksaan aplikasi/statement diminta atau hanya dianjurkan.
5. Software yang benar-benar dikuasai atau akan dipelajari: SPSS, R, Stata, atau lainnya.
6. Nama/kapasitas calon expert reviewer dan jalur persetujuan etik kampus.
7. Cognitive interview serta field pilot aktual untuk parameter power.

Gerbang Metodologi dan Data tetap REVISI sampai blocker tersebut diselesaikan dan auditor menyatakan lulus.

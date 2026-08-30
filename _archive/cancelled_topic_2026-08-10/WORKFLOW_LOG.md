# Workflow Log Bimbingan Skripsi

Dokumen ini mencatat perubahan material secara kronologis. Status kanonis terbaru selalu berada di `SOURCE_OF_TRUTH.md`.

## 6 Agustus 2026

### Inisialisasi

- Seluruh `skills.md` dan `review-*.md` di folder `skripsi` dibaca.
- Pedoman FEB UKRIDA 2022 ditetapkan sebagai otoritas tertinggi.
- Persona bimbingan empat fase ditetapkan: fenomena, masalah penelitian, kelayakan, lalu judul.
- Larangan membuat judul sebelum Fase 3 lulus dikunci.

### Perubahan Fokus

- Minat awal Pasar Modal dinilai terlalu luas.
- Fokus sempat berpindah ke Kewirausahaan, tetapi fenomena dan bukti awal tidak cukup.
- Fokus dikembalikan ke Keuangan/Finance.
- Fenomena awal `dissaving/makan tabungan` diuji dengan data BI.
- Data BI 2025 menunjukkan fluktuasi, bukan penurunan konsisten: rasio tabungan terendah 13,7% pada Juli-September dan pulih menjadi 14,9% pada Desember.
- Klaim BI Juli 2026 sebesar 13,7% ditolak karena tidak terverifikasi; publikasi yang tersedia saat pemeriksaan adalah Juni 2026 sebesar 17,0%.

### Fase 1

- Fenomena dipertajam menjadi koeksistensi belanja yang bertahan, tabungan segmen tertentu yang melemah, dan pembiayaan konsumtif yang tumbuh.
- Sumber primer Mandiri, BI, dan OJK diverifikasi.
- Dosen menyatakan Fase 1 `LULUS` dengan batas bahwa koeksistensi agregat bukan hubungan kausal.

### Fase 2

- Masalah awal menanyakan apakah gejala agregat tercermin pada rumah tangga yang sama.
- Auditor menemukan rumusan belum berbentuk pertanyaan dan belum menyebut objek; alur dikembalikan ke Fase 2.
- Objek calon ditetapkan sebagai rumah tangga Jabodetabek dengan informan dewasa pengelola keuangan.
- Hubungan sempat difokuskan pada kapasitas menabung dan penggunaan kredit/BNPL.
- Dosen menemukan ketidakselarasan antara istilah dan ukuran.
- Pengguna memilih fokus `beban pembayaran utang rumah tangga`.
- Rumusan kemudian memakai tingkat tabungan bersih dan beban utang, tetapi ditolak karena kedua rasio menggunakan pendapatan sebagai penyebut bersama.
- Pengukuran X diubah menjadi perubahan saldo likuid nominal yang independen; Y tetap beban pembayaran utang terhadap pendapatan.
- Dosen menyatakan rumusan final Fase 2 `LULUS`.

### Fase 3

- Mahasiswa menyusun rancangan survei tiga bulan, literatur, relevansi, dan metode.
- Relevansi ekonomi dinyatakan `LULUS`.
- Data, research gap, dan metodologi berstatus `REVISI`.
- Pilot aktual, power analysis, akses gatekeeper, periode fieldwork, protokol data sensitif, dan akses SPSS menjadi blocker.
- Tidak ada judul yang dibuat.

### Sistem Multiagen

- Dibentuk `mahasiswa_peneliti`, `dosen_pembimbing`, dan `auditor_kepatuhan`.
- Auditor membaca contoh skripsi kakak tingkat secara lengkap dan menetapkannya sebagai comparator non-otoritatif.
- Setiap keputusan fase berikutnya memerlukan audit substantif dan kepatuhan.

### Google Docs

- Pengguna menetapkan dokumen akhir harus dibuat di Google Docs.
- Format final wajib mengikuti Pedoman UKRIDA secara presisi.
- Audit visual final wajib dilakukan melalui ekspor PDF.

### Source of Truth

- `SOURCE_OF_TRUTH.md` dibuat sebagai status kanonis yang dapat dibaca ulang setiap saat.
- `WORKFLOW_LOG.md` dibuat sebagai catatan kronologis.
- Kedua dokumen wajib diperbarui setelah setiap keputusan atau hasil material berikutnya.


### Pembatalan Rumusan Lama dan Pengesahan Ulang Fase 2

- Audit membuktikan bahwa perubahan saldo likuid selama periode secara identitas mengandung pengurangan pembayaran utang, sedangkan variabel beban utang juga memakai pembayaran utang.
- Kelulusan Fase 2 lama dibatalkan karena hubungan antarkonstruk berisiko terbentuk secara mekanis.
- Tiga keluarga pengganti diuji: kecukupan penyangga likuid, surplus kas pra-utang, dan perilaku menabung aktif.
- Mahasiswa dan dosen memilih kecukupan penyangga likuid sebagai kandidat paling relevan dan layak untuk survei S1.
- Auditor menemukan konstruk baru bebas tautologi langsung setelah X tidak lagi mengurangi dana likuid yang hanya dialokasikan secara mental untuk cicilan.
- Rujukan X dikoreksi ke OECD/INFE Toolkit 2026 QF13; NFCS J5 hanya mendukung ambang tiga bulan.
- X dikunci sebagai kategori durasi yang dilaporkan, bukan rasio nominal yang dihitung.
- Y dikunci secara konsep sebagai kewajiban utang konsumtif non-KPR terjadwal yang telah diketahui saat survei relatif terhadap pendapatan historis; ini bukan realisasi pembayaran masa depan.
- Dosen dan auditor menyatakan Fase 2 LULUS dengan rumusan: "Apakah kecukupan penyangga likuid rumah tangga berasosiasi dengan beban pembayaran utang konsumtif non-KPR pada rumah tangga yang memiliki utang konsumtif aktif di Jabodetabek?"
- Hubungan wajib disebut asosiasi; BNPL menjadi bagian operasional dari utang konsumtif non-KPR; kelayakan cakupan Jabodetabek tetap harus dibuktikan pada Fase 3.
- Fase 3 dibuka kembali, sedangkan Fase 4 dan pembuatan judul tetap ditutup.

### Koreksi Teknis Source of Truth

- apply_patch gagal pada koordinator dan subagen karena sandbox Windows tidak dapat menangani dua writable root.
- Setelah kegagalan terulang dan utilitas bawaan tidak dapat dieksekusi, pembaruan dilakukan dengan patch unified atomik cadangan lalu diverifikasi; tidak ada dokumen pedoman atau comparator yang diubah.

### Blueprint Metodologi dan Instrumen Fase 3

- METHODOLOGY_BLUEPRINT.md dan INSTRUMENT_DRAFT.md dibuat sebagai artefak terpisah yang dapat diambil ulang.
- X tetap kategori durasi penyangga likuid adaptasi OECD/INFE 2026; seluruh pembayaran utang konsumtif non-KPR pembentuk Y dikeluarkan dari pengeluaran yang ditutup X dan wajib diuji lewat expert review serta cognitive interview.
- Y direvisi dari pembayaran tiga bulan mendatang berbanding pendapatan historis menjadi kewajiban minimum/kontraktual yang pertama kali jatuh tempo dalam tiga bulan kalender selesai berbanding pendapatan aktual pada tiga bulan yang sama.
- Perubahan Y dilakukan karena minimum due kartu kredit bulan kedua/ketiga di masa depan belum terbentuk dan karena keselarasan periode numerator–denominator lebih defensibel.
- Model kandidat utama adalah GLM Gamma log link dengan empat dummy X, uji global, adjusted predicted means, dan mean ratios; keputusan final tetap menunggu distribusi pilot.
- OLS log dengan galat robust/cluster, regresi kuantil median, ambang X tiga bulan, tren ordinal, serta outcome pembayaran nominal dengan pendapatan sebagai kovariat disiapkan sebagai sensitivitas.
- Sampling realistis dikunci sebagai nonprobability multisitus berstrata/berkuota kecuali kerangka probabilitas nyata tersedia; klaim representatif Jabodetabek dilarang.

### Audit Literatur Kedua dan Koreksi

- Auditor kedua memberi status REVISI dengan delapan temuan: hasil pencarian aktual, crosswalk log–matriks, n Stavins, full text Salignac, perlakuan tesis/disertasi, landasan teori, posisi Arsyianti, dan denominator bias.
- Crossref API dijalankan pada 6 Agustus 2026 untuk lima kueri: 100 rekod teratas diperiksa dan menghasilkan 93 DOI unik; hanya empat studi dari kanal ini masuk matriks setelah verifikasi.
- Total hasil Crossref yang sangat besar dicatat sebagai universe fuzzy mesin, bukan artikel relevan; batas top-20 per kueri dinyatakan sehingga review tidak disamarkan sebagai systematic review.
- SEARCH_LOG.md kini mencatat platform, tanggal, kueri, filter, total, jumlah disaring, deduplikasi, inklusi, alasan eksklusi, keterbatasan Garuda/SINTA, dan belum tersedianya akses Scopus/Web of Science.
- LITERATURE_MATRIX.md diperluas menjadi 44 sumber dan direkonsiliasi dua arah dengan SEARCH_LOG.md.
- Stavins (2021) dikoreksi menjadi 2.793 partisipan dan 2.775 observasi tidak hilang pada ukuran emergency savings; n per model tidak diklaim.
- Arsyianti dan Beik (2015) diakui sudah mengeluarkan pinjaman rumah; novelty tidak boleh diletakkan pada DSR, lokasi Jakarta, atau pengecualian KPR.
- Landasan precautionary/buffer-stock saving ditetapkan sebagai jangkar teori; financial margin hanya kerangka ukur, sedangkan coholding, akses kredit, mental accounting, self-control, dan dukungan sosial menjadi mekanisme pesaing.
- PDF penuh Salignac et al. (2022) tidak dapat diakses secara legal karena langganan penerbit dan proteksi anti-bot HAL. Metadata, halaman, abstrak/preview, konteks IFLS, dan konstruk terverifikasi; gelombang, n, bobot, serta model tetap dilarang diklaim.
- Skripsi mahasiswa tetap dilarang sebagai referensi; tesis/disertasi repositori resmi tidak dilarang Pedoman UKRIDA tetapi ditempatkan sebagai sumber tambahan, bukan prioritas.
- Research gap dan seluruh Fase 3 tetap REVISI sampai audit ketiga serta blocker data/metodologi selesai.

### Audit Substantif dan Penyederhanaan 10 Agustus 2026

- Dosen memberi verdict: Data REVISI, Research Gap LULUS TERBATAS, Relevansi Ekonomi LULUS, Metodologi REVISI; Fase 3 keseluruhan tetap REVISI dan Fase 4 tetap tertutup.
- Gap hanya boleh disebut contextual/measurement extension pada korpus terdokumentasi, bukan penelitian pertama, novelty absolut, atau kebaruan berbasis Indonesia/Jabodetabek/DSR/pengecualian KPR secara sendiri.
- Auditor ketiga gagal menyelesaikan turn karena batas penggunaan akun; tidak ada verdict auditor yang direkayasa. Audit pengganti tetap wajib.
- Audit kesiapan operasional disimpan sebagai PILOT_READINESS_AUDIT.md dan kemudian diberi label snapshot historis setelah koreksi.
- Estimand dikoreksi menjadi perbandingan model-based pada rumah tangga eligible yang berhasil direkrut dan menyelesaikan data melalui site (R=1); adjusted predictions tidak menciptakan representativitas.
- Urutan waktu dikunci: Y adalah kewajiban kontraktual historis tiga bulan selesai, sedangkan X adalah buffer saat survei. Y dapat telah mengikis X sehingga tidak ada klaim bahwa X mendahului atau menyebabkan Y.
- Eligibility dipisah menjadi utang non-KPR masih aktif pada tanggal survei dan kewajiban positif yang pertama kali jatuh tempo pada jendela Y; keduanya wajib untuk sampel utama.
- Skenario X diselaraskan pada hilangnya sumber pendapatan utama rumah tangga agar lebih dekat dengan OECD/INFE; adaptasi rumah tangga dan pengecualian cicilan non-KPR tetap memerlukan expert/cognitive review.
- Sampling dikoreksi dari istilah berstrata menjadi purposive multisite quota sampling; site/quota hanya diversifikasi rekrutmen.
- Analisis numerator dengan fungsi log/spline pendapatan menjadi pendamping wajib untuk mengaudit denominator bias; numerator/denominator juga dideskripsikan menurut X.
- Paket analisis S1 dipangkas menjadi Gamma-log kandidat, numerator analysis, OLS log-ratio, dan ambang X tiga bulan; teknik lanjutan hanya jika layak.
- Instrumen screening kini membedakan active-now dan positive-historical-window.
- Roster memakai satu baris per kontrak/akun; jenis produk, tujuan, restrukturisasi, status aktif, dan kanal pembayaran dipisahkan.
- Medis/pendidikan dipindah menjadi tujuan, restrukturisasi menjadi status, serta kontrak campuran/joint yang tak dapat dialokasikan dikeluarkan dari Y utama.
- Core roster dipangkas menjadi required amount, tunggakan lama, dan sumber angka per bulan; breakdown pokok/bunga/biaya/actual paid/status rinci tidak wajib.
- Pendapatan dipangkas menjadi total kas bersih per bulan dengan prompt rekonsiliasi sumber.
- Comprehension item X distandardisasi sebelum pertanyaan durasi; range check/literasi ditunda dari pilot pertama.
- Consent diberi placeholder eksplisit untuk durasi, insentif, retensi, contact person, dan etik agar tidak ada fakta yang dikarang.
- DECISION_LOG.md dibuat untuk memisahkan keputusan kerja terkunci dari blocker pengguna/expert/etik/pilot.
- PILOT_EXECUTION_PACKAGE.md dibuat untuk expert review, cognitive interview, gate field pilot, uji form, flow denominator, output pilot, power, dan freeze.
- Pilot dilarang otomatis digabung dengan survei utama jika terjadi perubahan material.
- Source of truth diperbarui ke 10 Agustus 2026; judul dan Bab IV–V empiris tetap dilarang.

### Audit Pengganti dan Penutupan Tiga Celah Internal

- Auditor pengganti menyatakan Research Gap LULUS TERBATAS, Relevansi Ekonomi LULUS, Kepatuhan Fase LULUS, Data REVISI, dan Metodologi REVISI.
- Auditor menegaskan Fase 4 tetap tertutup; tidak ditemukan judul, data/pilot/hasil rekaan, klaim kausal, atau pelompatan fase.
- Kontrak historis in-scope yang sudah lunas/ditutup tetap membentuk Y; household wajib mempunyai minimal satu kontrak aktif saat survei, tetapi tidak harus kontrak yang sama.
- Kontrak yang baru aktif setelah jendela tidak membentuk Y dan hanya menjelaskan active-now.
- Raw required amount didefinisikan sebagai total minimum/kontraktual sebelum adjustment.
- Clean amount hanya mengurangi prior arrears dan cross-contract component yang nominalnya dapat diatribusikan; flag tanpa nominal membuat contract-month missing.
- Pengurangan mekanis nilai transaksi/BNPL dari minimum due kartu dilarang.
- Setiap kontrak historis in-scope wajib mempunyai tiga contract-month numerik, termasuk nol eksplisit; setiap household wajib mempunyai tiga income-month numerik.
- Fungsi penjumlahan dilarang skip missing; analysis_complete kini mempunyai quality gate deterministik.
- Hipotesis kandidat dua sisi/global ditambahkan untuk memenuhi Pedoman UKRIDA tanpa memaksakan arah: H1 sekurang-kurangnya satu conditional mean berbeda.
- Validitas/reliabilitas direkonsiliasi: Cronbach alpha tidak tepat untuk X satu butir dan Y hasil perhitungan; bukti melalui expert/cognitive/logic/record verification dan test-retest bila layak.
- DATA_DICTIONARY.md diperbarui dengan active/closed/opened flags, raw/clean adjustment, window completeness, cluster mapping, dan logic checks.
- ANALYSIS_SPEC.md diperbarui agar flow, completeness, dan eksklusi raw-to-clean eksplisit.
- FORM_LOGIC_TEST_CASES.md dibuat dengan 30 kasus sintetis berlabel; file dilarang dipakai sebagai data penelitian.
- Source of truth kini mencatat audit Research Gap selesai; dua gerbang yang masih menahan Fase 3 adalah Data dan Metodologi.
- Blocker yang tidak dapat diselesaikan agen: site/gatekeeper/geografi, bulan acuan, etik/consent final, expert/cognitive review, keputusan klasifikasi terbuka, definisi kovariat, software dry run, pilot, effect size, power, dan ukuran sampel.

### Re-audit Rantai Alokasi dan Register Bukti Manusia — 10 Agustus 2026

- Rantai numerator diperjelas menjadi statement required total → bagian tanggung jawab household → bagian tujuan konsumtif → pengurangan prior arrears/cross-contract teratribusi → clean amount.
- DATA_DICTIONARY.md kini mempunyai field rule, nilai nominal/proporsi, dan sumber alokasi joint/mixed tingkat kontrak serta nominal alokasi tingkat contract-month.
- Berlaku hierarchy 0 ≤ consumer required raw ≤ household required ≤ statement required; pelanggaran menjadi logic error dan tidak dikoreksi otomatis.
- Kontrak in-scope joint/mixed yang unresolved diberi contract_include_y=8, memblokir Y household, dan tidak boleh dihapus selektif agar Y dapat dihitung dari kontrak lain.
- T19–T22 direvisi agar keluaran alokasi dan missing dapat dihitung langsung dari field yang tersedia.
- Re-audit independen menyatakan koreksi internal PASS dan tidak menemukan kontradiksi material baru pada dokumen kanonis.
- PASS hanya berlaku untuk konsistensi rancangan internal; Data dan Metodologi tetap REVISI karena site, periode, etik, expert/cognitive review, form dry run, software, pilot, cluster, effect size, power, dan freeze belum dibuktikan.
- PHASE3_HUMAN_INPUTS.md dibuat sebagai register kanonis untuk semua input/bukti manusia; seluruh status awal TERBUKA.
- Tidak ada judul, data responden, hasil pilot, hasil statistik, persetujuan etik, atau nama reviewer yang dibuat-buat.

### Penolakan Fabrikasi Data — 10 Agustus 2026

- Permintaan membuat sub-agent untuk mengarang data responden dan mengaudit realism ditolak sebagai pelanggaran integritas akademik.
- D39 mengunci bahwa data sintetis hanya boleh dipakai untuk dry run teknis yang berlabel dan tidak pernah menjadi data pilot, hasil empiris, Bab IV–V, atau dasar kelulusan Fase 3.

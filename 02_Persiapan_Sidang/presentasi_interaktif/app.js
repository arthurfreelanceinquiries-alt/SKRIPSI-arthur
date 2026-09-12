// PANDUAN BELAJAR SKRIPSI FEB UKRIDA - APPLICATION ENGINE

const SLIDES = [{"id": 1, "tag": "COVER & IDENTITAS", "title": "Proposal Penelitian Skripsi", "subtitle": "S1 Manajemen Keuangan — Fakultas Ekonomi dan Bisnis UKRIDA", "content_type": "cover", "speaker_notes": "Buka presentasi dengan salam formal kepada Dosen Pembimbing/Penguji. Sebutkan judul dengan tegas dan artikulatif. Tekankan konsentrasi Manajemen Keuangan dan fokus pada objek kartu fisik Pokémon TCG."}, {"id": 2, "tag": "LATAR BELAKANG & FENOMENA", "title": "Fenomena Lapangan & Tiga Anomali Pasar", "subtitle": "Transformasi Produk Hobi Menjadi Komoditas Spekulatif Likuid", "content_type": "fenomena", "speaker_notes": "Jelaskan bahwa kartu Pokémon TCG bukan lagi sekadar mainan anak-anak. Sebutkan 3 anomali: penetrasi kasir ritel modern, mekanisme blind-pack mystery, dan disparitas harga SAR ekstrem (Rp25rb vs Rp3jt)."}, {"id": 3, "tag": "JUSTIFIKASI OBJEK", "title": "Mengapa Memilih Kartu Koleksi (TCG)?", "subtitle": "Konvergensi Nilai Emosional, Hasrat Kelengkapan, dan Likuiditas Pasar Fisik", "content_type": "justifikasi_tcg", "speaker_notes": "Antisipasi pertanyaan dosen: kenapa TCG bukan video game? Jawab: video game dibeli 1x (one-off), sedangkan TCG dibeli berulang (repetitive purchase) dengan ketidakpastian tinggi dan likuiditas pasar sekunder 64,8 miliar kartu."}, {"id": 4, "tag": "INDUSTRI GRADING", "title": "Lembaga Sertifikasi Grading & Arbitrase", "subtitle": "Mekanisme PSA, BGS, CGC dalam Menetapkan Likuiditas & Nilai Investasi", "content_type": "grading_arbitrage", "speaker_notes": "Jelaskan peran PSA/BGS/CGC: skala 1-10 Gem Mint, tamper-evident slab, population report, dan fenomena grading arbitrage yang memicu speculative motive."}, {"id": 5, "tag": "OPERASIONALISASI VARIABEL", "title": "Bedah 5 Variabel Penelitian (3X, 1Y, 1M)", "subtitle": "Definisi Konseptual, Dimensi, Indikator, dan Adaptasi Skala Baku", "content_type": "variabel_table", "speaker_notes": "Tunjukkan ketelitian metodologis: X1 (Hedonic - Arnold & Reynolds), X2 (Desire for Completeness - Gao et al. 2014 & Zeigarnik), X3 (Speculative - Keynes & Shiller), Y (Impulsive - Rook & Verplanken), M (Self-Control - Tangney et al. & Baumeister)."}, {"id": 6, "tag": "RERANGKA KONSEPTUAL", "title": "Model Penelitian & Persamaan MRA", "subtitle": "Pengaruh Langsung (H1–H3) dan Efek Moderasi Memperlemah (H4–H6)", "content_type": "mra_framework", "speaker_notes": "Paparkan diagram alur. Jelaskan perbedaan Model 1 (Main Effects) dan Model 2 (Interaction Terms). Tekankan bahwa hipotesis moderasi dirumuskan memperlemah (-)."}, {"id": 7, "tag": "LANDASAN TEORETIS", "title": "Grand Theory & Supporting Theories", "subtitle": "Behavioral Finance sebagai Payung Utama dan 3 Teori Pendukung", "content_type": "teori_struktur", "speaker_notes": "Tegaskan Grand Theory: Behavioral Finance (Simon Bounded Rationality, Kahneman-Tversky Prospect Theory, Shiller Irrational Exuberance, Thaler-Shefrin Planner-Doer). Teori pendukung: S-O-R, Completing the Set Effect, Self-Regulation Theory."}, {"id": 8, "tag": "TELAAH EMPIRIS", "title": "Matriks 10 Penelitian Terdahulu (2021–2025)", "subtitle": "Pemetaan Anteseden Impulsive Buying & Posisi Kebaruan (Novelty)", "content_type": "jurnal_matrix", "speaker_notes": "Tunjukkan 10 jurnal rujukan terbaru termasuk riset Dosen FEB UKRIDA (Colline, 2024), jurnal Scopus Q1 (Gong et al., 2024 Heliyon; Katauke et al., 2023), dan riset komunitas TCG Jakarta (Aryadi & Lingga, 2024)."}, {"id": 9, "tag": "HIPOTESIS PENELITIAN", "title": "Logika Kausalitas & 4-Tier Pembuktian Hipotesis", "subtitle": "Struktur Baku: Teori → Empiris → Objek Pokémon TCG → Rumusan Hipotesis", "content_type": "hipotesis_tiers", "speaker_notes": "Jelaskan struktur 4-tier: dosen menuntut agar setiap hipotesis dikaitkan secara eksplisit dengan objek fisik kartu Pokémon TCG. H1-H3 berpengaruh positif (+), H4-H6 memoderasi memperlemah (-)."}, {"id": 10, "tag": "METODOLOGI PENELITIAN", "title": "Desain Penelitian, Sampling, & Mean-Centering", "subtitle": "Kuantitatif Asosiatif, Purposive Sampling (N=120-150), & Regresi OLS SPSS", "content_type": "metodologi_mra", "speaker_notes": "Pertahankan formula Green (1991): N >= 50 + 8k = 106; target 120-150 responden (Cohen power 0.80). Jelaskan prosedur mean-centering untuk eliminasi multikolinearitas struktural, dan alasan tidak perlunya uji autokorelasi."}, {"id": 11, "tag": "SIMULASI SIDANG", "title": "Simulasi Pertanyaan Kritis Bimbingan & Sidang", "subtitle": "Kuasai Logika Pertanyaan Jebakan Dosen Pembimbing & Penguji", "content_type": "tanya_jawab_preview", "speaker_notes": "Tunjukkan kesiapan menjawab 16 pertanyaan bimbingan dan 5 pertanyaan jebakan tingkat tinggi, terutama seputar penggantian variabel moderasi, konsistensi 6 rumusan masalah, dan justifikasi teori."}, {"id": 12, "tag": "PENUTUP & ACTION PLAN", "title": "Cheat Sheet Kilat & Checklist Menjelang Sidang", "subtitle": "Rangkuman 1 Halaman: Logika Kuat, Mental Tenang, Penyampaian Percaya Diri", "content_type": "penutup_cheatsheet", "speaker_notes": "Tutup dengan ringkasan 1 halaman. Sampaikan komitmen penyelesaian bab demi bab sesuai Buku Pedoman FEB UKRIDA."}];
const FLASHCARDS = [{"id": 1, "cat": "var", "color": "blue", "title": "Impulsive Buying (Y)", "term": "Impulsive Buying", "author": "Rook (1987); Verplanken & Herabadi (2001)", "desc": "Pembelian mendadak, spontan, dan tanpa perencanaan anggaran sebelumnya yang didorong oleh stimulus lingkungan dan desakan emosional sesaat.", "hint": "Variabel Dependen (Y) — Dimensi Kognitif & Afektif"}, {"id": 2, "cat": "var", "color": "blue", "title": "Hedonic Motivation (X1)", "term": "Hedonic Motivation", "author": "Arnold & Reynolds (2003); Babin et al. (1994)", "desc": "Dorongan berbelanja demi kesenangan emosional, sensasi petualangan (*adventure*), letupan kegembiraan (*gratification*), dan pelarian stres.", "hint": "Variabel Independen 1 (X1) — Sensasi merobek pack"}, {"id": 3, "cat": "var", "color": "blue", "title": "Desire for Completeness (X2)", "term": "Desire for Completeness", "author": "Gao, Huang, & Simonson (2014); Barasz et al. (2017)", "desc": "Dorongan psikologis untuk menuntaskan himpunan koleksi yang belum lengkap, dipicu oleh ketegangan kognitif melihat celah slot kosong pada binder.", "hint": "Variabel Independen 2 (X2) — The Completing the Set Effect"}, {"id": 4, "cat": "var", "color": "blue", "title": "Speculative Motive (X3)", "term": "Speculative Motive", "author": "Keynes (1936); Shiller (2000); Baur et al. (2018)", "desc": "Tindakan mengakuisisi aset dengan ekspektasi menjualnya kembali di pasar sekunder untuk meraih keuntungan modal (*capital gain*) dari kenaikan harga.", "hint": "Variabel Independen 3 (X3) — Ekspektasi cuan kartu langka"}, {"id": 5, "cat": "var", "color": "blue", "title": "Self-Control (M)", "term": "Self-Control (Kontrol Diri)", "author": "Tangney et al. (2004); Baumeister (2002); Sultan et al. (2012)", "desc": "Kapasitas volisional individu untuk menolak godaan belanja spontan, menunda kepuasan (*delay of gratification*), dan menegakkan batas anggaran.", "hint": "Variabel Moderasi (M) — Rem volisional / Planner-Doer"}, {"id": 6, "cat": "theory", "color": "green", "title": "Grand Theory", "term": "Behavioral Finance", "author": "Herbert Simon (1955); Kahneman & Tversky (1979); Shiller (2000)", "desc": "Paradigma keuangan yang mengkaji bias psikologis dan batasan kognitif (*bounded rationality*) manusia yang menyebabkan anomali keputusan pasar tidak rasional.", "hint": "Grand Theory Skripsi — Menolak Efficient Market Hypothesis"}, {"id": 7, "cat": "theory", "color": "green", "title": "Planner-Doer Model", "term": "Dual-System Planner-Doer", "author": "Thaler & Shefrin (1981)", "desc": "Model pertarungan psikologis antara 'Doer' (sisi impulsif pencari kenikmatan jangka pendek) dan 'Planner' (sisi rasional perencana jangka panjang).", "hint": "Landasan peran Self-Control sebagai moderator"}, {"id": 8, "cat": "theory", "color": "green", "title": "S-O-R Framework", "term": "Stimulus-Organism-Response", "author": "Mehrabian & Russell (1974)", "desc": "Stimulus lingkungan ritel (S) mempengaruhi kondisi internal emosi/kognisi individu (O) yang akhirnya memicu respons tindakan konsumsi (R).", "hint": "Supporting Theory 1 — Pajangan kasir -> Emosi -> Beli"}, {"id": 9, "cat": "theory", "color": "green", "title": "Zeigarnik Effect", "term": "Zeigarnik Effect", "author": "Bluma Zeigarnik (1927)", "desc": "Kecenderungan kognitif manusia untuk lebih mengingat dan merasa terganggu oleh tugas yang belum tuntas dibanding tugas yang sudah selesai.", "hint": "Akar psikologi hasrat menuntaskan nomor binder"}, {"id": 10, "cat": "theory", "color": "green", "title": "Completing the Set Effect", "term": "The 'Completing the Set' Effect", "author": "Gao, Huang, & Simonson (2014, JMR)", "desc": "Fenomena di mana motivasi akuisisi konsumen melonjak drastis secara non-linier ketika himpunan koleksi mendekati batas kelengkapan penuh.", "hint": "Istilah ilmiah baku rujukan jurnal pemasaran Q1"}, {"id": 11, "cat": "theory", "color": "green", "title": "Self-Regulation Theory", "term": "Self-Regulation Theory & Ego Depletion", "author": "Baumeister (2002); Vohs & Faber (2007)", "desc": "Kontrol diri dipandang sebagai sumber daya energi mental terbatas (*ego depletion*). Ketika energi ini habis, manusia rentan melakukan belanja impulsif.", "hint": "Supporting Theory 3 — Kekuatan rem volisional"}, {"id": 12, "cat": "theory", "color": "green", "title": "Prospect Theory", "term": "Prospect Theory & Lottery Effect", "author": "Kahneman & Tversky (1979)", "desc": "Kecenderungan manusia melebih-lebihkan probabilitas kecil untuk meraih keuntungan sangat besar, persis seperti harapan menarik kartu SAR dari booster pack.", "hint": "Bias optimisme berlebihan di balik pembelian pack"}, {"id": 13, "cat": "tcg", "color": "yellow", "title": "Trading Card Game", "term": "Pokémon TCG Fisik", "author": "Nintendo / Creatures Inc. (1996)", "desc": "Permainan kartu koleksi strategis fisik yang telah mencetak lebih dari 64,8 miliar lembar kartu di seluruh dunia dan memiliki pasar sekunder sangat aktif.", "hint": "Objek Penelitian Skripsi"}, {"id": 14, "cat": "tcg", "color": "yellow", "title": "Blind-Pack Mystery", "term": "Booster Pack & Blind-Pack", "author": "Mekanisme Produk", "desc": "Kemasan foil tertutup kedap cahaya berisi kartu acak (biasanya 5–10 lembar) di mana pembeli tidak mengetahui isinya sebelum bungkus dirobek.", "hint": "Pemicu sensasi gacha & rasa penasaran"}, {"id": 15, "cat": "tcg", "color": "yellow", "title": "SAR Card", "term": "Special Illustration Rare (SAR)", "author": "Kategori Kelangkaan", "desc": "Tingkat kelangkaan kartu tertinggi dengan gambar ilustrasi penuh (*full-art*). Memiliki pull rate sangat kecil (<1-3%) dan harga termahal di pasar sekunder.", "hint": "Target utama kolektor & spekulan (Rp500rb - Rp3jt+)"}, {"id": 16, "cat": "tcg", "color": "yellow", "title": "Sertifikasi Grading", "term": "Lembaga Grading (PSA, BGS, CGC)", "author": "Third-Party Authentication", "desc": "Lembaga independen terakreditasi internasional yang memeriksa keaslian dan kondisi fisik kartu secara objektif dengan skala 1 (Poor) sampai 10 (Gem Mint).", "hint": "Pemberi legitimasi likuiditas aset kartu fisik"}, {"id": 17, "cat": "tcg", "color": "yellow", "title": "Tamper-Evident Slab", "term": "Slab & Population Report", "author": "Standar Keamanan Grading", "desc": "Cangkang plastik sonik kedap udara berlabel barcode/QR yang mengunci kartu secara permanen, didukung basis data populasi (*Pop Report*) tingkat kelangkaan.", "hint": "Kemasan pelindung kartu bersertifikat grade 10"}, {"id": 18, "cat": "tcg", "color": "yellow", "title": "Grading Arbitrage", "term": "Arbitrase Grading (Grading Arbitrage)", "author": "Mekanisme Keuangan Pasar", "desc": "Strategi membeli kartu mentah seharga ratusan ribu rupiah, mengirimnya untuk di-grading, dan menjualnya kembali di harga jutaan rupiah jika meraih PSA 10.", "hint": "Pemicu utama Speculative Motive di komunitas TCG"}, {"id": 19, "cat": "stat", "color": "red", "title": "Teknik Analisis", "term": "Moderated Regression Analysis (MRA)", "author": "Aiken & West (1991); Ghozali (2018)", "desc": "Aplikasi khusus regresi linier berganda yang menyertakan istilah perkalian/interaksi (X·M) untuk menguji apakah moderator memperkuat atau memperlemah hubungan.", "hint": "Metode Statistik Utama Penelitian"}, {"id": 20, "cat": "stat", "color": "red", "title": "Uji Asumsi Multikol", "term": "Prosedur Mean-Centering", "author": "Aiken & West (1991); Cohen et al. (2003)", "desc": "Mengurangi nilai variabel dengan nilai rata-ratanya (X* = X - X̄) sebelum dikalikan untuk mengeliminasi multikolinearitas struktural tanpa mengubah signifikansi.", "hint": "Solusi ilmiah jika VIF interaksi melonjak tinggi"}, {"id": 21, "cat": "stat", "color": "red", "title": "Teknik Sampling", "term": "Purposive Sampling", "author": "Sekaran & Bougie (2016); Sugiyono (2019)", "desc": "Teknik penentuan sampel non-acak dengan pertimbangan kriteria inklusi tertentu agar responden memiliki pemahaman dan pengalaman relevan terhadap objek.", "hint": "Kriteria: WNI >=17 thn, pernah beli pack resmi 6-12 bln"}, {"id": 22, "cat": "stat", "color": "red", "title": "Formula Sampel", "term": "Kaidah Green (1991) & Cohen (1988)", "author": "Green (1991); Cohen (1988)", "desc": "Formula N >= 50 + 8k (k=7 -> N >= 106). Target penelitian: 120-150 responden untuk menjamin statistical power >= 0.80 pada medium effect size f2=0.15.", "hint": "Justifikasi jumlah kecukupan sampel S1"}, {"id": 23, "cat": "stat", "color": "red", "title": "Uji Asumsi Klasik", "term": "Alasan Tiadanya Uji Autokorelasi", "author": "Ghozali (2018); Gujarati (2009)", "desc": "Uji autokorelasi (Durbin-Watson) hanya berlaku untuk data deret waktu (time-series). Pada data survei cross-sectional, antar-responden independen sehingga uji ini tidak relevan.", "hint": "Jawaban tangkas atas pertanyaan jebakan penguji"}, {"id": 24, "cat": "stat", "color": "red", "title": "Uji Kelayakan Model", "term": "Uji F (Simultan) & Koefisien Determinasi R²", "author": "Ghozali (2018)", "desc": "Uji F menilai apakah seluruh variabel independen secara simultan berpengaruh signifikan terhadap Y. R² (atau R² Change pada MRA) mengukur persentase varians Y yang dijelaskan.", "hint": "Uji ketepatan model regresi"}, {"id": 25, "cat": "stat", "color": "red", "title": "Uji Hipotesis Parsial", "term": "Uji t (Parsial)", "author": "Ghozali (2018)", "desc": "Menguji signifikansi pengaruh masing-masing variabel independen dan interaksi secara individual terhadap Y (diterima jika p-value < 0,05 dan t-hitung > t-tabel).", "hint": "Pengujian H1 sampai H6 secara parsial"}, {"id": 26, "cat": "stat", "color": "red", "title": "Instrumen Pengukuran", "term": "Skala Likert 5 Poin & Uji Instrumen", "author": "Hair et al. (2019); Nunnally (1978)", "desc": "Skala 1 (Sangat Tidak Setuju) s.d. 5 (Sangat Setuju). Diuji dengan Uji Validitas (Korelasi Pearson Product Moment r >= 0,30) dan Uji Reliabilitas (Cronbach's Alpha >= 0,60).", "hint": "Standar kelayakan kuesioner penelitian"}, {"id": 27, "cat": "stat", "color": "red", "title": "Konsistensi Metodologi", "term": "Hukum 1-to-1: RM = TP = Hipotesis", "author": "Pedoman Penulisan Skripsi FEB UKRIDA", "desc": "Prinsip keselarasan simetris 1-to-1 di mana 6 butir Rumusan Masalah selaras penuh dengan 6 butir Tujuan Penelitian dan 6 Hipotesis (H1–H3 efek langsung, H4–H6 efek moderasi MRA).", "hint": "Benang merah ilmiah (Golden Thread) proposal"}];
const QUESTIONS = [{"id": 1, "type": "bimbingan", "badge": "Revisi Kunci 9 Sep", "question": "Mengapa Anda mengubah variabel moderasi dari Literasi Keuangan menjadi Self-Control?", "keywords": ["Knowledge-to-behavior gap", "Rem volisional", "Planner-Doer Model", "Thaler & Shefrin (1981)", "Sultan et al. (2012)"], "answer": "Terima kasih atas pertanyaannya. Perubahan ini dilakukan berdasarkan hasil telaah literatur dan arahan Ibu Pembimbing pada bimbingan 9 September 2026. Pertama, literasi keuangan berlandaskan domain kognitif (pengetahuan), di mana studi empiris (Fernandes et al., 2014) kerap menemukan 'knowledge-to-behavior gap' — orang yang paham teori keuangan belum tentu mampu menahan diri saat berbelanja. Sebaliknya, Self-Control (Kontrol Diri) merupakan kapasitas volisional eksekutif yang bekerja langsung sebagai 'rem perilaku'. Dalam teori Planner-Doer (Thaler & Shefrin, 1981) dan studi empiris Sultan et al. (2012), kontrol diri secara konsisten terbukti memperlemah dorongan belanja impulsif."}, {"id": 2, "type": "bimbingan", "badge": "Istilah Ilmiah Baku", "question": "Mengapa Anda mengganti istilah 'Need for Completion' menjadi 'Desire for Completeness'?", "keywords": ["Gao, Huang, & Simonson (2014)", "Journal of Marketing Research", "The Completing the Set Effect", "Barasz et al. (2017)", "Zeigarnik Effect (1927)"], "answer": "Istilah 'Need for Completion' bersifat informal dan belum dibakukan dalam konteks perilaku konsumen. Dalam literatur pemasaran terkemuka (Journal of Marketing Research), konstruk ini telah diformalkan oleh Gao, Huang, & Simonson (2014) sebagai 'The Completing the Set Effect' dan oleh Barasz et al. (2017) sebagai 'Desire for Completeness'. Landasan psikologinya berakar kokoh pada Zeigarnik Effect (1927) mengenai ketegangan kognitif akibat tugas yang belum selesai. Penggunaan istilah Desire for Completeness memberikan rujukan jurnal internasional Q1 yang sangat kredibel."}, {"id": 3, "type": "bimbingan", "badge": "Konsentrasi Keuangan", "question": "Mengapa Grand Theory yang digunakan adalah Behavioral Finance, bukan teori pemasaran murni?", "keywords": ["Manajemen Keuangan", "Aset alternatif spekulatif", "Bounded Rationality", "Prospect Theory & Lottery Effect", "Irrational Exuberance"], "answer": "Penelitian ini diajukan pada Program Studi S1 Manajemen Konsentrasi Manajemen Keuangan. Objek kartu Pokémon TCG saat ini telah bertransformasi menjadi aset alternatif bernilai spekulatif dengan pasar sekunder yang sangat likuid. Grand Theory Behavioral Finance (Simon, 1955; Kahneman & Tversky, 1979; Shiller, 2000; Thaler & Shefrin, 1981) secara tepat membedah anomali keputusan keuangan konsumen muda yang irasional: adanya ilusi probabilitas (lottery effect), bias optimisme menarik kartu mahal bernilai PSA 10, serta konflik antara kesenangan sesaat (Doer) dan perencanaan anggaran jangka panjang (Planner)."}, {"id": 4, "type": "bimbingan", "badge": "Struktur Naskah", "question": "Mengapa di BAB II variabel Dependen (Y) dibahas terlebih dahulu sebelum variabel Independen (X)?", "keywords": ["Masalah inti penelitian", "Alur logis", "Standar telaah pustaka", "Fenomena yang dipengaruhi"], "answer": "Sesuai kaidah penulisan ilmiah yang logis dan arahan Dosen Pembimbing, variabel dependen (Y - Impulsive Buying) merupakan masalah utama atau fenomena inti yang ingin diselesaikan dalam penelitian ini. Dengan membedah definisi, dimensi, dan batasan operasional Y terlebih dahulu, kita membangun standar pemahaman yang jelas tentang apa yang sedang dipengaruhi, sebelum kemudian menganalisis faktor-faktor pemicunya (X1, X2, X3) dan variabel pemoderasinya (M)."}, {"id": 5, "type": "bimbingan", "badge": "Kaitan Objek Fisik", "question": "Bagaimana kaitan sertifikasi grading (PSA, BGS, CGC) dengan variabel Speculative Motive?", "keywords": ["Skala 1-10 Gem Mint", "Tamper-evident slab", "Population report", "Grading arbitrage", "Disparitas harga modal vs jual"], "answer": "Lembaga grading profesional seperti PSA menilai keaslian dan kondisi fisik kartu pada skala 1-10 (Gem Mint 10) lalu menyegelnya dalam tamper-evident slab. Kartu bersertifikat PSA 10 memiliki harga pasar puluhan kali lipat dari kartu mentah karena didukung population report resmi yang membuktikan kelangkaannya. Disparitas harga inilah yang menciptakan fenomena grading arbitrage — pembeli memborong booster pack dengan spekulasi memperoleh kartu berkondisi sempurna yang dapat di-grade dan dijual kembali demi capital gain."}, {"id": 6, "type": "bimbingan", "badge": "Hipotesis Moderasi", "question": "Mengapa hipotesis moderasi (H4, H5, H6) dirumuskan memperlemah (-), bukan memperkuat?", "keywords": ["Self-Regulation Theory", "Planner-Doer Model", "Rem volisional", "Delay of gratification", "Meredam dampak X terhadap Y"], "answer": "Karena variabel moderasi yang digunakan adalah Self-Control (Kontrol Diri). Menurut Self-Regulation Theory (Baumeister, 2002) dan model Planner-Doer (Thaler & Shefrin, 1981), kontrol diri adalah rem volisional. Ketika kontrol diri konsumen tinggi, mereka memiliki kapasitas untuk menunda kepuasan (delay of gratification) dan menahan dorongan belanja spontan, sehingga efek rangsangan emosional (X1), hasrat kelengkapan (X2), dan motif spekulasi (X3) terhadap Impulsive Buying (Y) berhasil diredam atau diperlemah."}, {"id": 7, "type": "jebakan", "badge": "Jebakan Penguji ⭐⭐⭐⭐⭐", "question": "Saudara menggunakan Zeigarnik Effect dari tahun 1927 — itu hampir 100 tahun lalu. Apakah teori itu masih relevan? Ada bukti terbaru?", "keywords": ["Replikasi modern", "Gao et al. (2014, JMR)", "Gong et al. (2024, Heliyon Scopus Q1)", "Tan & Adyantari (2024)", "Validasi konteks blind box"], "answer": "Zeigarnik Effect memang dicetuskan pada 1927, namun mekanisme psikologisnya telah direplikasi dan dikonfirmasi berulang kali dalam literatur perilaku konsumen modern. Dalam konteks pemasaran, Gao, Huang, & Simonson (2014) di Journal of Marketing Research membuktikannya sebagai The Completing the Set Effect. Studi terbaru oleh Gong et al. (2024) di jurnal Heliyon (Scopus Q1) serta Tan & Adyantari (2024) membuktikan bahwa ketidakpastian himpunan pada produk blind box modern memicu rasa ingin tahu dan ketegangan penyelesaian set yang secara signifikan mendorong impulsive buying. Jadi mekanisme psikologisnya telah divalidasi penuh dalam konteks produk koleksi kontemporer."}, {"id": 8, "type": "jebakan", "badge": "Jebakan Penguji ⭐⭐⭐⭐⭐", "question": "Speculative motive dicetuskan Keynes (1936) untuk pasar uang/obligasi. Bukankah menggunakannya untuk kartu mainan adalah peregangan teori yang berlebihan?", "keywords": ["Esensi capital gain", "Robert Shiller (2000) Irrational Exuberance", "Baur et al. (2018) Alternative Assets", "Pasar sekunder likuid", "Koleksi sebagai instrumen investasi"], "answer": "Memang benar Keynes awalnya membahas motif spekulasi dalam konteks preferensi likuiditas pasar uang. Namun esensi dari speculative motive — yaitu mengakuisisi aset dengan ekspektasi memperoleh keuntungan modal (capital gain) dari apresiasi harga di masa depan — bersifat universal. Robert Shiller (2000) memperluasnya ke berbagai kelas aset dalam Irrational Exuberance, dan Baur et al. (2018) secara eksplisit mengkaji barang koleksi (collectibles) sebagai alternative tangible assets. Kartu Pokémon TCG saat ini memiliki pasar sekunder terorganisir, standar sertifikasi grading (PSA 10), dan omzet lelang jutaan dolar, sehingga secara empiris memenuhi seluruh karakteristik aset spekulatif."}, {"id": 9, "type": "jebakan", "badge": "Jebakan Penguji ⭐⭐⭐⭐⭐", "question": "Bukankah ketiga variabel X Anda berpotensi multikolinear tinggi? Misalnya pembeli yang hedonis juga ingin melengkapi koleksi.", "keywords": ["Process-oriented vs Goal-oriented vs Profit-oriented", "Uji validitas diskriminan", "Korelasi antar-variabel r < 0.80", "Uji VIF < 10"], "answer": "Secara fenomenologis ketiganya bisa dirasakan bersamaan, namun secara konseptual memiliki fokus yang sangat berbeda: Hedonic Motivation berorientasi pada proses (process-oriented / sensasi merobek pack); Desire for Completeness berorientasi pada pencapaian target (goal-oriented / menuntaskan slot binder); sedangkan Speculative Motive berorientasi pada imbal hasil finansial (profit-oriented / resale value & grading). Secara statistik, kami akan menerapkan uji validitas diskriminan, analisis korelasi antar-variabel (memastikan r < 0,80), dan uji VIF untuk memastikan tidak ada multikolinearitas yang melanggar asumsi regresi."}, {"id": 10, "type": "jebakan", "badge": "Jebakan Penguji ⭐⭐⭐⭐⭐", "question": "Mengapa Anda tidak melakukan uji autokorelasi (Durbin-Watson) pada penelitian ini?", "keywords": ["Data survei cross-sectional", "Bukan time series", "Pengamatan independen antar-individu", "Ghozali (2018) & Gujarati (2009)"], "answer": "Uji autokorelasi (seperti Durbin-Watson) tidak dilakukan karena secara metodologis dan ekonometrika (Ghozali, 2018; Gujarati, 2009), autokorelasi hanya relevan untuk data deret waktu (time-series) di mana terdapat ketergantungan residual antar-periode waktu. Pada data primer kuesioner dengan desain survei cross-sectional, responden mengisi kuesioner secara independen pada satu titik waktu, sehingga asumsi non-autokorelasi terpenuhi secara alami. Uji asumsi klasik yang wajib dipenuhi adalah uji normalitas, multikolinearitas, dan heteroskedastisitas."}, {"id": 11, "type": "metodologi", "badge": "Metodologi Sampel", "question": "Berapa target sampel Anda dan apa justifikasi akademisnya?", "keywords": ["Formula Green (1991)", "N >= 50 + 8k", "Minimal 106 responden", "Target 120-150 responden", "Cohen (1988) power 0.80 medium effect size"], "answer": "Target sampel ditetapkan sebanyak 120 hingga 150 responden. Angka ini didasarkan pada formula Green (1991) untuk regresi berganda dengan k=7 prediktor: N >= 50 + 8(7) = 106 responden. Target 120-150 responden juga memenuhi kaidah Cohen (1988) untuk mencapai statistical power sebesar 0,80 pada alpha = 0,05 dengan medium effect size (f2 = 0,15), serta mengantisipasi potensi kuesioner yang tidak lengkap atau tidak lolos screening."}, {"id": 12, "type": "metodologi", "badge": "Teknik Sampling", "question": "Mengapa Anda menggunakan teknik Purposive Sampling, bukan Random Sampling?", "keywords": ["Non-Probability Purposive Sampling", "Kriteria inklusi spesifik", "Populasi tak terbatas (infinite)", "Screening questions"], "answer": "Purposive sampling digunakan karena penelitian ini memerlukan responden yang memiliki kriteria pengalaman spesifik terhadap objek penelitian. Jika digunakan random sampling pada populasi umum, mayoritas responden mungkin tidak pernah membeli booster pack Pokémon TCG sehingga data yang terkumpul tidak valid. Kriteria inklusi kami menetapkan: WNI, usia minimal 17 tahun, dan pernah membeli booster pack fisik resmi berbahasa Indonesia minimal 1 kali dalam 6-12 bulan terakhir."}, {"id": 13, "type": "metodologi", "badge": "Statistik MRA", "question": "Apa fungsi prosedur Mean-Centering pada model MRA?", "keywords": ["Eliminasi multikolinearitas struktural", "Aiken & West (1991)", "X* = X - X̄ dan M* = M - M̄", "Nilai interaksi dan p-value tetap identik"], "answer": "Pada model regresi moderasi, mengalikan dua variabel (X · M) secara otomatis menciptakan korelasi tinggi antara variabel interaksi dengan variabel aslinya (multikolinearitas struktural). Prosedur mean-centering (mengurangi setiap skor variabel dengan nilai rata-ratanya sebelum dikalikan) berhasil mengeliminasi multikolinearitas struktural ini sehingga nilai VIF turun di bawah 10, tanpa mengubah koefisien esensial, standard error terstandarisasi, maupun signifikansi p-value uji interaksi (Aiken & West, 1991; Ghozali, 2018)."}, {"id": 14, "type": "teori", "badge": "Kontribusi Akademik", "question": "Apa novelty (kebaruan) utama dari penelitian ini dibandingkan penelitian sebelumnya?", "keywords": ["Integrasi 3 pemicu simultan", "Aset alternatif fisik likuid", "Self-Control sebagai moderator volisional", "Pionir TCG Indonesia FEB UKRIDA"], "answer": "Kebaruan utama penelitian ini terletak pada: (1) Mengintegrasikan secara simultan pemicu emosional (Hedonic), bias psikologi koleksi (Desire for Completeness / Zeigarnik Effect), dan motif spekulasi finansial (Speculative Motive / Behavioral Finance) pada komoditas hobi fisik dengan pasar sekunder aktif; (2) Memposisikan Self-Control sebagai rem volisional pemoderasi perilaku konsumtif; dan (3) Menjadi studi empiris pionir di lingkungan FEB UKRIDA yang meneliti perilaku konsumsi kartu Pokémon TCG resmi berbahasa Indonesia."}, {"id": 15, "type": "teori", "badge": "Manfaat Penelitian", "question": "Apa manfaat praktis penelitian ini bagi mahasiswa, masyarakat, dan regulator keuangan?", "keywords": ["Edukasi finansial Gen Z", "Risiko kerugian terselubung", "Peran kontrol diri", "Masukan literasi keuangan OJK"], "answer": "Secara praktis, penelitian ini memberikan penyadaran bagi konsumen muda (khususnya Gen Z) bahwa di balik sensasi menyenangkan membuka pack dan ilusi keuntungan spekulasi harga pasar, terdapat risiko kerugian finansial akibat pembelian impulsif yang tidak terencana. Hasil riset ini menegaskan pentingnya penguatan Self-Control dalam alokasi belanja hobi serta memberikan masukan kontekstual bagi OJK dan lembaga keuangan dalam merancang literasi keuangan berbasis perilaku."}, {"id": 16, "type": "bimbingan", "badge": "Konsistensi RM & Hipotesis", "question": "Mengapa Rumusan Masalah dan Tujuan Penelitian Anda ada 6 butir? Apakah referensi jurnal perlu bertambah seiring ekspansi ini?", "keywords": ["Hukum Simetris 1-to-1", "Benang Merah (Golden Thread)", "H1-H3 Pengaruh Langsung", "H4-H6 Efek Moderasi MRA", "72 Referensi Lengkap"], "answer": "Penelitian ini memiliki 3 variabel independen dan 1 variabel moderasi (Self-Control). Perumusan 6 butir di BAB 1 merupakan penegasan benang merah ilmiah (golden thread) dengan prinsip simetris 1-to-1 antara Rumusan Masalah (1–6), Tujuan Penelitian (1–6), dan Pengembangan Hipotesis (H1–H6 di BAB 2): Butir 1–3 menguji pengaruh langsung (direct effect: Hedonic, Completeness, Speculative terhadap Impulsive Buying), sedangkan butir 4–6 menguji efek interaksi moderasi Self-Control melalui MRA. Penambahan butir ini TIDAK memerlukan penambahan referensi baru, karena seluruh landasan teori moderasi (Self-Regulation Theory, Planner-Doer) dan kajian empiris pendukung H4–H6 (Apidana & Kholifah, 2022; Lienardy & Panasea, 2024; Artadita & Firmialy, 2024; Sultan et al., 2012; dsb.) sudah tercakup secara lengkap dan komprehensif dalam 72 referensi ilmiah di naskah dan daftar pustaka."}];
const QUIZ = [{"id": 1, "q": "Berdasarkan rujukan jurnal pemasaran internasional (Gao et al., 2014), apa istilah ilmiah baku yang menggantikan 'Need for Completion' dalam penelitian ini?", "options": ["A. Need for Achievement", "B. Desire for Completeness", "C. Compulsive Buying Tendency", "D. Fear of Missing Out (FOMO)"], "ans": 1, "exp": "Sesuai arahan Dosen Pembimbing (9 Sep 2026) dan publikasi Gao, Huang, & Simonson (2014) di Journal of Marketing Research, istilah yang dibakukan adalah 'Desire for Completeness' yang berlandaskan pada 'The Completing the Set Effect' dan Zeigarnik Effect (1927)."}, {"id": 2, "q": "Variabel moderasi dalam penelitian ini resmi ditetapkan sebagai Self-Control (Kontrol Diri). Apa alasan utama penggantian dari Literasi Keuangan?", "options": ["A. Literasi keuangan terlalu sulit dihitung di SPSS", "B. Self-Control bertindak sebagai rem volisional eksekutif untuk mengatasi 'knowledge-to-behavior gap'", "C. Literasi keuangan tidak memiliki skala pengukuran internasional", "D. Tidak ada teori yang menghubungkan literasi keuangan dengan belanja"], "ans": 1, "exp": "Berdasarkan studi Fernandes et al. (2014) dan teori Planner-Doer Thaler & Shefrin (1981), literasi keuangan seringkali mengalami knowledge-to-behavior gap (tahu teori tapi tetap impulsif). Self-Control bertindak sebagai rem volisional eksekutif yang secara langsung menahan dorongan belanja spontan."}, {"id": 3, "q": "Grand Theory yang menjadi payung utama penelitian skripsi S1 Manajemen Keuangan ini adalah...", "options": ["A. Efficient Market Hypothesis (Fama, 1970)", "B. Classical Economic Theory (Adam Smith)", "C. Behavioral Finance (Simon, 1955; Kahneman-Tversky, 1979; Shiller, 2000)", "D. Technology Acceptance Model (Davis, 1989)"], "ans": 2, "exp": "Grand Theory yang ditetapkan adalah Behavioral Finance (Keuangan Perilaku) yang menentang asumsi rasionalitas sempurna neoklasik dan membedah anomali bias psikologis serta rasionalitas terbatas (bounded rationality) dalam pengambilan keputusan keuangan."}, {"id": 4, "q": "Lembaga grading profesional seperti PSA menilai kartu fisik pada skala...", "options": ["A. Skala 1 (Poor) sampai 10 (Gem Mint)", "B. Skala Likert 1 sampai 5", "C. Skala Persentase 0% sampai 100%", "D. Skala Huruf A, B, C, D"], "ans": 0, "exp": "Lembaga grading independen seperti PSA (Professional Sports Authenticator) menggunakan skala penilaian objektif dari 1 (Poor) hingga 10 (Gem Mint) yang disegel dalam tamper-evident slab."}, {"id": 5, "q": "Mekanisme di mana kolektor membeli kartu mentah (raw card), mengirimkannya ke lembaga grading, dan menjualnya kembali dengan harga berlipat jika memperoleh nilai PSA 10 disebut...", "options": ["A. Market Cannibalization", "B. Grading Arbitrage (Arbitrase Grading)", "C. Short Selling", "D. Price Dumping"], "ans": 1, "exp": "Fenomena ini disebut Grading Arbitrage, yaitu motif spekulasi finansial memanfaatkan disparitas harga ekstrem antara kartu mentah yang belum dinilai dengan kartu bersertifikat PSA 10 Gem Mint di pasar lelang sekunder."}, {"id": 6, "q": "Mengapa hipotesis moderasi H4, H5, dan H6 dirumuskan dengan arah 'memperlemah' (-)?", "options": ["A. Karena kuesioner menggunakan skala Likert negatif", "B. Karena Self-Control yang tinggi bertindak sebagai rem kognitif yang meredam dampak rangsangan emosional dan motif spekulasi terhadap pembelian impulsif", "C. Karena jumlah responden di bawah 100 orang", "D. Karena dosen tidak mengizinkan hipotesis positif"], "ans": 1, "exp": "Self-Regulation Theory (Baumeister, 2002) dan model Planner-Doer (Thaler & Shefrin, 1981) menjelaskan bahwa individu berkontrol diri tinggi memiliki kapasitas menunda kepuasan (delay of gratification), sehingga memperlemah pengaruh X1, X2, dan X3 terhadap Impulsive Buying."}, {"id": 7, "q": "Berapa ukuran sampel minimum yang disyaratkan oleh formula Green (1991) untuk model penelitian dengan k = 7 prediktor?", "options": ["A. N >= 30 responden", "B. N >= 106 responden (N >= 50 + 8k)", "C. N >= 250 responden", "D. N >= 500 responden"], "ans": 1, "exp": "Formula Green (1991) menyatakan N >= 50 + 8k. Untuk k = 7 prediktor (3X, 1M, dan 3 istilah interaksi X*M), ukuran sampel minimum adalah 50 + 8(7) = 106 responden. Target penelitian ditetapkan 120-150 responden."}, {"id": 8, "q": "Apa tujuan utama dilakukannya prosedur 'Mean-Centering' sebelum mengalikan variabel independen dengan pemoderasi pada MRA?", "options": ["A. Mengubah data ordinal menjadi data interval", "B. Mengeliminasi multikolinearitas struktural antar-istilah interaksi dengan variabel aslinya", "C. Menaikkan nilai R-squared secara artifisial", "D. Menggantikan uji normalitas residual"], "ans": 1, "exp": "Mean-centering (X* = X - X̄ dan M* = M - M̄) mengeliminasi multikolinearitas struktural yang timbul akibat perkalian variabel, sehingga nilai VIF turun ke batas aman tanpa mengubah substansi signifikansi moderasi (Aiken & West, 1991)."}, {"id": 9, "q": "Mengapa uji autokorelasi (Durbin-Watson) TIDAK diperlukan dalam penelitian skripsi ini?", "options": ["A. Karena software SPSS tidak memiliki fitur autokorelasi", "B. Karena autokorelasi hanya berlaku untuk data deret waktu (time-series), sedangkan data survei primer cross-sectional bersifat independen antar-individu", "C. Karena data tidak berdistribusi normal", "D. Karena penelitian menggunakan moderasi MRA"], "ans": 1, "exp": "Sesuai kaidah ekonometrika (Ghozali, 2018), autokorelasi mengukur korelasi residual antar-waktu pada data time-series. Pada penelitian survei cross-sectional dengan data primer, pengamatan antar-individu independen sehingga autokorelasi tidak relevan."}, {"id": 10, "q": "Efek psikologis dari tugas yang belum tuntas yang memicu ketegangan kognitif untuk mencari penyelesaian (closure) pertama kali diteliti oleh...", "options": ["A. B.F. Skinner (1938)", "B. Bluma Zeigarnik (1927)", "C. Philip Kotler (2000)", "D. Robert Shiller (2000)"], "ans": 1, "exp": "Zeigarnik Effect ditemukan oleh psikolog Bluma Zeigarnik pada 1927, yang membuktikan bahwa pikiran manusia secara persisten mengingat tugas belum tuntas dan menuntut penuntasan (closure)."}, {"id": 11, "q": "Apa karakteristik utama yang membedakan booster pack Pokémon TCG dari produk Pokémon lainnya seperti video game atau tiket bioskop?", "options": ["A. Video game dibeli berulang kali setiap minggu", "B. Booster pack memiliki mekanisme blind-pack mystery yang dibeli berulang (repetitive purchase) dengan ketidakpastian isi kartu", "C. Kartu Pokémon tidak bisa dijual kembali", "D. Booster pack hanya bisa dibeli di Jepang"], "ans": 1, "exp": "Video game atau tiket film adalah one-off purchase (dibeli sekali selesai). Sebaliknya, booster pack adalah repetitive purchase yang dipicu oleh ketidakpastian blind-pack mystery (probabilitas gacha/lotre)."}, {"id": 12, "q": "Dalam sistematika penulisan BAB II Tinjauan Pustaka sesuai arahan Dosen Pembimbing, urutan pembahasan variabel yang benar adalah...", "options": ["A. Variabel Moderasi (M) lebih dulu -> Variabel Independen (X) -> Variabel Dependen (Y)", "B. Variabel Dependen (Y - Impulsive Buying) lebih dulu -> Variabel X1, X2, X3 -> Variabel Moderasi (M) -> Pengembangan Hipotesis", "C. Hipotesis lebih dulu -> Definisi Teori -> Data Lapangan", "D. Variabel X1 langsung ke hipotesis tanpa membahas Y"], "ans": 1, "exp": "Arahan Dosen Pembimbing menetapkan variabel dependen (Y - Impulsive Buying) dibahas terlebih dahulu sebagai masalah inti penelitian, disusul variabel penjelas (X1, X2, X3), variabel pemoderasi (M), dan sintesis pengembangan hipotesis 4-tier."}, {"id": 13, "q": "Kriteria inklusi responden dalam teknik Purposive Sampling penelitian ini adalah...", "options": ["A. Siapa saja yang bermain game Pokémon di Nintendo Switch", "B. WNI, usia minimal 17 tahun, dan pernah membeli booster pack fisik resmi minimal 1x dalam 6-12 bulan terakhir", "C. Warga negara asing yang tinggal di Jakarta", "D. Anak-anak usia di bawah 12 tahun yang ditemani orang tua"], "ans": 1, "exp": "Kriteria inklusi spesifik: WNI, usia >= 17 tahun (memiliki kapasitas hukum dan pertimbangan finansial mandiri), dan pernah membeli booster pack fisik resmi berbahasa Indonesia minimal 1x dalam 6-12 bulan terakhir."}, {"id": 14, "q": "Berdasarkan meta-analisis Amos et al. (2014), pemicu pembelian impulsif dikelompokkan ke dalam 3 klaster faktor. Variabel apa yang mewakili faktor kognitif kolektor?", "options": ["A. Hedonic Motivation (X1)", "B. Speculative Motive (X3)", "C. Desire for Completeness (X2)", "D. Self-Control (M)"], "ans": 2, "exp": "Amos et al. (2014) memetakan 3 klaster: Afektif/Emosional diwakili Hedonic Motivation (X1); Kognitif Kolektor diwakili Desire for Completeness (X2); dan Situasional/Ekonomi diwakili Speculative Motive (X3)."}, {"id": 15, "q": "Tingkat kelangkaan kartu Pokémon TCG resmi Indonesia yang memiliki nilai pasar sekunder termahal dan menjadi target utama arbitrase grading adalah...", "options": ["A. Common (C)", "B. Uncommon (U)", "C. Special Illustration Rare (SAR)", "D. Basic Energy"], "ans": 2, "exp": "Special Illustration Rare (SAR) merupakan kartu kelangkaan puncak dengan karya seni eksklusif penuh (full-art), pull rate sangat kecil (<1-3%), dan diperdagangkan antara Rp500.000 hingga lebih dari Rp3.000.000."}, {"id": 16, "q": "Berdasarkan prinsip keselarasan ilmiah ('Hukum 1-to-1: RM = TP = Hipotesis'), mengapa Rumusan Masalah dan Tujuan Penelitian proposal Arthur dirumuskan menjadi 6 butir?", "options": ["A. Karena ada 6 variabel independen dalam penelitian ini", "B. Karena menyelaraskan secara simetris 3 butir pengaruh langsung (H1-H3) dan 3 butir efek moderasi Self-Control (H4-H6)", "C. Karena disyaratkan minimal 6 butir oleh Kementerian Pendidikan", "D. Karena kuesioner hanya terdiri dari 6 pertanyaan"], "ans": 1, "exp": "Enam butir Rumusan Masalah dan Tujuan Penelitian mencerminkan 'benang merah ilmiah' (golden thread) yang simetris 1-to-1 dengan hipotesis: Butir 1–3 menguji efek langsung (H1-H3), dan Butir 4–6 menguji efek moderasi Self-Control (H4-H6). Penambahan butir ini tidak membutuhkan referensi baru karena seluruh landasan teoritis dan empiris moderasi sudah lengkap di BAB 2."}];

// App State
let currentSlideIndex = 0;
let currentFcIndex = 0;
let currentFcCategory = 'all';
let currentFcList = [...FLASHCARDS];
let fcMasteredSet = new Set(JSON.parse(localStorage.getItem('fc_mastered') || '[]'));

let currentQuizIndex = 0;
let quizScore = 0;
let quizAnswered = false;

let timerSeconds = 15 * 60; // 15 mins default
let timerInterval = null;
let timerRunning = false;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initSlideDeck();
  initFlashcards();
  initDefenseQuestions();
  initQuiz();
  initMRACalculator();
  initTimer();
  initShortcuts();
});

// Tab Navigation
function initNavigation() {
  const navBtns = document.querySelectorAll('.nav-tab-btn');
  const sections = document.querySelectorAll('.tab-section');

  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.dataset.tab;
      navBtns.forEach(b => b.classList.remove('active'));
      sections.forEach(s => s.classList.remove('active'));

      btn.classList.add('active');
      const targetSection = document.getElementById(tabId);
      if (targetSection) targetSection.classList.add('active');
    });
  });
}

// 1. SLIDE DECK ENGINE
function initSlideDeck() {
  renderSlide(currentSlideIndex);

  document.getElementById('deck-prev-btn').addEventListener('click', prevSlide);
  document.getElementById('deck-next-btn').addEventListener('click', nextSlide);
  document.getElementById('notes-toggle-btn').addEventListener('click', toggleNotes);
}

function renderSlide(index) {
  const slide = SLIDES[index];
  const container = document.getElementById('slide-render-area');
  
  document.getElementById('slide-tag').textContent = slide.tag;
  document.getElementById('slide-title').textContent = slide.title;
  document.getElementById('slide-subtitle').textContent = slide.subtitle;
  document.getElementById('slide-num-text').textContent = (index + 1) + ' / ' + SLIDES.length;
  
  const progressPercent = ((index + 1) / SLIDES.length) * 100;
  document.getElementById('deck-progress-fill').style.width = progressPercent + '%';
  document.getElementById('deck-progress-label').textContent = Math.round(progressPercent) + '% SELESAI';

  document.getElementById('notes-text').textContent = slide.speaker_notes || 'Tidak ada catatan pembicara.';

  document.getElementById('deck-prev-btn').disabled = (index === 0);
  document.getElementById('deck-next-btn').disabled = (index === SLIDES.length - 1);

  container.innerHTML = getSlideBodyHTML(slide);
}

function nextSlide() {
  if (currentSlideIndex < SLIDES.length - 1) {
    currentSlideIndex++;
    renderSlide(currentSlideIndex);
  }
}

function prevSlide() {
  if (currentSlideIndex > 0) {
    currentSlideIndex--;
    renderSlide(currentSlideIndex);
  }
}

function toggleNotes() {
  const drawer = document.getElementById('notes-drawer');
  drawer.classList.toggle('open');
}

function getSlideBodyHTML(slide) {
  switch (slide.content_type) {
    case 'cover':
      return `
        <div class="cover-layout">
          <div class="cover-badge-top">🎓 PROPOSAL SKRIPSI S1 MANAJEMEN KEUANGAN FEB UKRIDA</div>
          <h1 class="cover-main-title">
            PENGARUH <span class="cover-highlight">HEDONIC MOTIVATION</span>, <span class="cover-highlight">DESIRE FOR COMPLETENESS</span>, DAN <span class="cover-highlight">SPECULATIVE MOTIVE</span> TERHADAP <span class="cover-highlight">IMPULSIVE BUYING</span> DENGAN <span class="cover-highlight">SELF-CONTROL</span> SEBAGAI MODERASI
          </h1>
          <p style="color: var(--text-secondary); max-width: 750px; font-size: 1.05rem;">
            Studi Empiris pada Pembeli Booster Pack Kartu Fisik Pokémon Trading Card Game (TCG) Resmi di Indonesia
          </p>
          <div class="cover-meta-grid">
            <div class="cover-meta-card">
              <label>Penyusun</label>
              <p>Arthur Reezan</p>
              <span style="font-size:0.8rem; color: var(--text-muted);">NIM: 322015175</span>
            </div>
            <div class="cover-meta-card">
              <label>Dosen Pembimbing</label>
              <p>Dr. Fredella Colline, S.E., M.M.</p>
              <span style="font-size:0.8rem; color: var(--text-muted);">CFP®, PFM, CHCP-A</span>
            </div>
            <div class="cover-meta-card">
              <label>Institusi & Waktu</label>
              <p>FEB UKRIDA Jakarta</p>
              <span style="font-size:0.8rem; color: var(--text-muted);">September 2026</span>
            </div>
          </div>
        </div>
      `;

    case 'fenomena':
      return `
        <div class="slide-grid-3">
          <div class="feature-card gold">
            <div class="feature-header">
              <div class="feature-icon">🏪</div>
              <div class="feature-title">Penetrasi Minimarket</div>
            </div>
            <div class="feature-body">
              Kartu resmi Indonesia didistribusikan di kasir Indomaret dan Alfamart seharga Rp20.000–Rp30.000. Lokasi kasir menjadi pemicu stimulus lingkungan fisik (S) langsung.
            </div>
          </div>
          <div class="feature-card blue">
            <div class="feature-header">
              <div class="feature-icon">❓</div>
              <div class="feature-title">Blind-Pack Mystery</div>
            </div>
            <div class="feature-body">
              Kemasan foil kedap cahaya menyimpan misteri isi acak. Probabilitas acak (<1-3% kartu SAR) menciptakan <em>lottery effect</em> yang memicu lonjakan dopamin dan rasa penasaran persisten.
            </div>
          </div>
          <div class="feature-card emerald">
            <div class="feature-header">
              <div class="feature-icon">📈</div>
              <div class="feature-title">Disparitas Harga 100x</div>
            </div>
            <div class="feature-body">
              Modal pack Rp25.000 berpeluang menarik kartu Special Illustration Rare (SAR) yang diperjualbelikan Rp500.000 s.d. Rp3.000.000+ di Tokopedia dan komunitas Facebook/Discord.
            </div>
          </div>
        </div>
        <div class="callout-box" style="margin-top: 1.5rem;">
          <div class="callout-title">Rumusan Masalah Inti:</div>
          <div class="callout-desc">Bagaimana dorongan kesenangan emosional, desakan melengkapi binder, dan ekspektasi cuan lelang memicu pembelian impulsif, serta mampukah Kontrol Diri (Self-Control) bertindak sebagai rem volisional?</div>
        </div>
      `;

    case 'justifikasi_tcg':
      return `
        <div class="slide-grid-2">
          <div class="feature-card gold">
            <div class="feature-header">
              <div class="feature-icon">🏆</div>
              <div class="feature-title">Ekosistem Waralaba >$100 Miliar</div>
            </div>
            <ul class="feature-list">
              <li>Pokémon adalah waralaba media dengan pendapatan kotor tertinggi di dunia (>USD 100 miliar).</li>
              <li>Pilar video game (Game Boy hingga Switch) melahirkan slogan <em>"Gotta Catch 'Em All!"</em>.</li>
              <li>Anime TV 25 tahun dan film layar lebar (Detective Pikachu) memperluas basis audiens lintas generasi.</li>
            </ul>
          </div>
          <div class="feature-card emerald">
            <div class="feature-header">
              <div class="feature-icon">🃏</div>
              <div class="feature-title">Mengapa Harus Memilih TCG?</div>
            </div>
            <ul class="feature-list">
              <li><strong>64,8 Miliar Lembar Kartu:</strong> Pangsa pasar fisik terbesar di dunia dengan likuiditas luar biasa tinggi.</li>
              <li><strong>Repetitive vs One-Off Purchase:</strong> Video game dibeli sekali selesai; booster pack dibeli berulang kali karena ketidakpastian.</li>
              <li><strong>Konvergensi 3 Pemicu:</strong> Menyatukan sensasi hedonis merobek bungkus, hasrat menuntaskan nomor binder, dan spekulasi aset bernilai grading.</li>
            </ul>
          </div>
        </div>
      `;

    case 'grading_arbitrage':
      return `
        <div class="slide-grid-2">
          <div class="feature-card blue">
            <div class="feature-header">
              <div class="feature-icon">🛡️</div>
              <div class="feature-title">Lembaga Grading Independen</div>
            </div>
            <div class="feature-body">
              <p>Perusahaan pihak ketiga terakreditasi internasional (<strong>PSA, BGS, CGC</strong>) menilai keaslian dan kondisi fisik kartu pada skala 1–10 (<em>Gem Mint 10</em>).</p>
              <ul class="feature-list" style="margin-top: 0.75rem;">
                <li><strong>Tamper-Evident Slab:</strong> Disegel sonik permanen kedap udara.</li>
                <li><strong>Population Report:</strong> Sensus publik tingkat kelangkaan resmi.</li>
              </ul>
            </div>
          </div>
          <div class="feature-card gold">
            <div class="feature-header">
              <div class="feature-icon">💎</div>
              <div class="feature-title">Grading Arbitrage di Pasar Sekunder</div>
            </div>
            <div class="feature-body">
              <p>Kolektor membeli kartu mentah (<em>raw card</em>) seharga ratusan ribu rupiah, mengirimnya ke PSA, dan jika memperoleh grade 10, menjualnya kembali seharga jutaan rupiah.</p>
              <div class="callout-box emerald" style="margin-top: 0.75rem;">
                <strong>Kaitan Finansial:</strong> Ekspektasi keuntungan modal (capital gain) inilah yang memicu <em>Speculative Motive</em> dan aksi borong spontan di kasir toko.
              </div>
            </div>
          </div>
        </div>
      `;

    case 'variabel_table':
      return `
        <div class="data-table-wrapper">
          <table class="modern-table">
            <thead>
              <tr>
                <th>Variabel & Simbol</th>
                <th>Definisi Singkat</th>
                <th>Dimensi Utama</th>
                <th>Rujukan Baku</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong style="color:#fff;">Impulsive Buying (Y)</strong></td>
                <td>Pembelian spontan tanpa rencana anggaran akibat stimulus emosi sesaat.</td>
                <td>(1) Kognitif<br>(2) Afektif</td>
                <td>Rook (1987); Verplanken & Herabadi (2001)</td>
              </tr>
              <tr>
                <td><strong style="color:#fbbf24;">Hedonic Motivation (X1)</strong></td>
                <td>Kesenangan emosional, sensasi petualangan, dan letupan kegembiraan saat membuka pack.</td>
                <td>(1) Adventure<br>(2) Gratification<br>(3) Idea Shopping</td>
                <td>Arnold & Reynolds (2003); Babin et al. (1994)</td>
              </tr>
              <tr>
                <td><strong style="color:#60a5fa;">Desire for Completeness (X2)</strong></td>
                <td>Hasrat menuntaskan himpunan koleksi akibat ketegangan kognitif celah slot kosong.</td>
                <td>(1) Cognitive Tension<br>(2) Drive for Closure<br>(3) Wholeness</td>
                <td>Gao et al. (2014); Zeigarnik (1927)</td>
              </tr>
              <tr>
                <td><strong style="color:#34d399;">Speculative Motive (X3)</strong></td>
                <td>Ekspektasi keuntungan modal (capital gain) dari kenaikan harga kartu langka.</td>
                <td>(1) Ekspektasi Cuan<br>(2) Likuiditas<br>(3) Arbitrase Grading</td>
                <td>Keynes (1936); Shiller (2000); Baur (2018)</td>
              </tr>
              <tr>
                <td><strong style="color:#a78bfa;">Self-Control (M - Moderasi)</strong></td>
                <td>Kapasitas volisional menolak godaan belanja spontan dan menunda kepuasan.</td>
                <td>(1) Tahan Godaan<br>(2) Non-Impulsif<br>(3) Disiplin Anggaran</td>
                <td>Tangney et al. (2004); Baumeister (2002)</td>
              </tr>
            </tbody>
          </table>
        </div>
      `;

    case 'mra_framework':
      return `
        <div class="slide-grid-2">
          <div class="diagram-container">
            <svg class="mra-svg" viewBox="0 0 500 320" xmlns="http://www.w3.org/2000/svg">
              <rect x="20" y="30" width="160" height="40" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
              <text x="100" y="55" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">X1: Hedonic Motivation</text>

              <rect x="20" y="100" width="160" height="40" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
              <text x="100" y="125" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">X2: Completeness</text>

              <rect x="20" y="170" width="160" height="40" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
              <text x="100" y="195" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">X3: Speculative Motive</text>

              <rect x="330" y="100" width="150" height="50" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
              <text x="405" y="125" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">Y: Impulsive Buying</text>
              <text x="405" y="140" fill="#94a3b8" font-size="10" text-anchor="middle">Booster Pack TCG</text>

              <rect x="175" y="260" width="150" height="40" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
              <text x="250" y="285" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">M: Self-Control</text>

              <line x1="180" y1="50" x2="330" y2="110" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>
              <line x1="180" y1="120" x2="330" y2="125" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)"/>
              <line x1="180" y1="190" x2="330" y2="140" stroke="#10b981" stroke-width="2" marker-end="url(#arrow)"/>

              <path d="M 250 260 L 250 145" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4" marker-end="url(#arrow-purple)"/>
              <text x="260" y="210" fill="#a78bfa" font-size="11" font-weight="bold">H4, H5, H6 (-)</text>
              <text x="260" y="225" fill="#94a3b8" font-size="9">Memperlemah</text>
              
              <defs>
                <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                  <path d="M 0 0 L 10 5 L 0 10 z" fill="#f8fafc"/>
                </marker>
                <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                  <path d="M 0 0 L 10 5 L 0 10 z" fill="#8b5cf6"/>
                </marker>
              </defs>
            </svg>
          </div>
          <div class="feature-card purple">
            <div class="feature-title" style="color: #fff;">Persamaan Model Regresi MRA</div>
            <div style="font-family: var(--font-mono); font-size: 0.85rem; color: #e2e8f0; line-height: 1.7; background: rgba(0,0,0,0.3); padding: 1rem; border-radius: var(--radius-sm);">
              <strong>Model 1 (Efek Utama):</strong><br>
              Y = α + β₁X₁ + β₂X₂ + β₃X₃ + e<br><br>
              <strong>Model 2 (MRA Moderasi Interaksi):</strong><br>
              Y = α + β₁X₁ + β₂X₂ + β₃X₃ + β₄M +<br>
              &nbsp;&nbsp;&nbsp;&nbsp;β₅(X₁·M) + β₆(X₂·M) + β₇(X₃·M) + e
            </div>
            <p style="font-size:0.85rem; color: var(--text-secondary); margin-top: 0.5rem;">
              *Catatan: X dan M menjalani prosedur <em>mean-centering</em> (X* = X - X̄) sebelum dikalikan untuk mencegah multikolinearitas struktural.
            </p>
          </div>
        </div>
      `;

    case 'teori_struktur':
      return `
        <div class="slide-grid-2">
          <div class="feature-card gold">
            <div class="feature-header">
              <div class="feature-icon">🏛️</div>
              <div class="feature-title">Grand Theory: Behavioral Finance</div>
            </div>
            <ul class="feature-list">
              <li><strong>Herbert Simon (1955):</strong> <em>Bounded Rationality</em> — batas kognitif memaksa manusia menggunakan heuristik instan.</li>
              <li><strong>Kahneman & Tversky (1979):</strong> <em>Prospect Theory</em> — overoptimism bias dan ilusi probabilitas (lottery effect).</li>
              <li><strong>Robert Shiller (2000):</strong> <em>Irrational Exuberance</em> — pasar spekulatif didorong histeria emosi, bukan fundamental.</li>
              <li><strong>Thaler & Shefrin (1981):</strong> <em>Planner-Doer Model</em> — konflik antara nafsu belanja instan (Doer) vs perencana anggaran (Planner).</li>
            </ul>
          </div>
          <div class="feature-card blue">
            <div class="feature-header">
              <div class="feature-icon">📚</div>
              <div class="feature-title">Supporting Theories</div>
            </div>
            <ul class="feature-list">
              <li><strong>Model S-O-R (Mehrabian & Russell, 1974):</strong> Stimulus kasir & blind pack (S) memicu reaksi afektif/kognitif (O) yang melahirkan Impulsive Buying (R).</li>
              <li><strong>The "Completing the Set" Effect (Gao et al., 2014) & Zeigarnik Effect (1927):</strong> Ketegangan kognitif melihat celah slot binder mendorong penyelesaian set.</li>
              <li><strong>Self-Regulation Theory (Baumeister, 2002):</strong> Kontrol diri sebagai rem volisional terbatas (ego depletion) penahan godaan belanja.</li>
            </ul>
          </div>
        </div>
      `;

    case 'jurnal_matrix':
      return `
        <div class="data-table-wrapper" style="max-height: 420px; overflow-y: auto;">
          <table class="modern-table">
            <thead>
              <tr>
                <th>Peneliti & Tahun</th>
                <th>Variabel yang Diteliti</th>
                <th>Temuan Kunci Penelitian</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Colline (2024)</strong><br><span style="color:var(--accent-gold); font-size:0.75rem;">Dosen FEB UKRIDA</span></td>
                <td>Overconfidence, Herding, Keputusan Finansial</td>
                <td>Membuktikan tingginya bias optimisme dan perilaku ikut-ikutan spekulatif pada generasi muda Indonesia.</td>
              </tr>
              <tr>
                <td><strong>Gong et al. (2024)</strong><br><span style="color:#60a5fa; font-size:0.75rem;">Heliyon (Scopus Q1)</span></td>
                <td>Blind Box, Curiosity, Impulsive Buying</td>
                <td>Kemasan acak blind box membangkitkan rasa penasaran afektif yang langsung mendorong impulse buying.</td>
              </tr>
              <tr>
                <td><strong>Aryadi & Lingga (2024)</strong><br><span style="color:#34d399; font-size:0.75rem;">Springer Nature</span></td>
                <td>Motivasi Kolektor, Investasi TCG Jakarta</td>
                <td>Membuktikan komunitas TCG Jakarta menjadikan kartu fisik sebagai instrumen aset alternatif bernilai spekulatif.</td>
              </tr>
              <tr>
                <td><strong>Artadita & Firmialy (2024)</strong><br><span style="color:#a78bfa; font-size:0.75rem;">BBR (Scopus Q3/SINTA 1)</span></td>
                <td>Shopping Enjoyment, Mod: Self-Control, Impulsive</td>
                <td>Kesenangan belanja game berpengaruh kuat; kontrol diri memoderasi dan menahan dorongan belanja spontan.</td>
              </tr>
              <tr>
                <td><strong>Katauke et al. (2023)</strong><br><span style="color:#f87171; font-size:0.75rem;">Sustainability (Scopus Q1)</span></td>
                <td>Regulasi Finansial, Impulsivity</td>
                <td>Kapasitas regulasi diri dan kontrol finansial secara signifikan menekan impulsivitas konsumsi.</td>
              </tr>
            </tbody>
          </table>
        </div>
      `;

    case 'hipotesis_tiers':
      return `
        <div class="slide-grid-2">
          <div class="feature-card gold">
            <div class="feature-title">Pengaruh Langsung (H1, H2, H3: Positif +)</div>
            <ul class="feature-list" style="gap: 0.8rem;">
              <li><strong>H1 (+): Hedonic Motivation → Impulsive Buying</strong><br>
                <span style="font-size:0.8rem; color:var(--text-muted);">Sensasi merobek pack foil dan letupan dopamin memicu belanja spontan di kasir toko.</span>
              </li>
              <li><strong>H2 (+): Desire for Completeness → Impulsive Buying</strong><br>
                <span style="font-size:0.8rem; color:var(--text-muted);">Slot kosong bernomor di album binder memicu ketegangan kognitif untuk terus memborong pack.</span>
              </li>
              <li><strong>H3 (+): Speculative Motive → Impulsive Buying</strong><br>
                <span style="font-size:0.8rem; color:var(--text-muted);">Potensi cuan kartu PSA 10 bernilai jutaan rupiah melumpuhkan kehati-hatian anggaran.</span>
              </li>
            </ul>
          </div>
          <div class="feature-card purple">
            <div class="feature-title">Efek Moderasi (H4, H5, H6: Memperlemah -)</div>
            <ul class="feature-list" style="gap: 0.8rem;">
              <li><strong>H4 (-): Self-Control Memperlemah Hedonic → Impulsive</strong><br>
                <span style="font-size:0.8rem; color:var(--text-muted);">Fungsi Planner aktif menunda kepuasan dan menolak kenikmatan sesaat.</span>
              </li>
              <li><strong>H5 (-): Self-Control Memperlemah Completeness → Impulsive</strong><br>
                <span style="font-size:0.8rem; color:var(--text-muted);">Sadar probabilitas gacha kecil, dialihkan ke beli kartu satuan (singles) terencana.</span>
              </li>
              <li><strong>H6 (-): Self-Control Memperlemah Speculative → Impulsive</strong><br>
                <span style="font-size:0.8rem; color:var(--text-muted);">Disiplin memahami risiko modal dan biaya grading meredam ambisi spekulatif.</span>
              </li>
            </ul>
          </div>
        </div>
      `;

    case 'metodologi_mra':
      return `
        <div class="slide-grid-3">
          <div class="feature-card blue">
            <div class="feature-header">
              <div class="feature-icon">🎯</div>
              <div class="feature-title">Populasi & Sampel</div>
            </div>
            <div class="feature-body">
              <strong>Purposive Sampling</strong><br>
              Kriteria: WNI, usia ≥ 17 thn, pernah beli booster pack resmi minimal 1x dalam 6–12 bulan terakhir.<br><br>
              <strong>Formula Green (1991):</strong><br>
              N ≥ 50 + 8(7) = 106.<br>
              <strong>Target:</strong> 120–150 responden (Cohen power 0.80).
            </div>
          </div>
          <div class="feature-card emerald">
            <div class="feature-header">
              <div class="feature-icon">⚖️</div>
              <div class="feature-title">Mean-Centering MRA</div>
            </div>
            <div class="feature-body">
              Sebelum variabel X dikalikan dengan M, dilakukan standarisasi rata-rata:<br>
              <code style="color:var(--accent-gold-light);">X* = X - X̄ dan M* = M - M̄</code><br><br>
              Menghilangkan multikolinearitas struktural tanpa mengubah nilai esensial uji moderasi (Aiken & West, 1991).
            </div>
          </div>
          <div class="feature-card rose">
            <div class="feature-header">
              <div class="feature-icon">🛡️</div>
              <div class="feature-title">Uji Asumsi Klasik</div>
            </div>
            <div class="feature-body">
              Wajib: Normalitas Residual, Multikolinearitas (VIF < 10), dan Heteroskedastisitas (Glejser).<br><br>
              <strong>Autokorelasi TIDAK dilakukan</strong> karena data survei primer cross-sectional bersifat independen antar-individu (Ghozali, 2018).
            </div>
          </div>
        </div>
      `;

    case 'tanya_jawab_preview':
      return `
        <div class="callout-box" style="margin-bottom: 1.5rem;">
          <div class="callout-title">Simulasi Sidang & Bimbingan Terintegrasi</div>
          <div class="callout-desc">Telah disiapkan 15 Skenario Bimbingan Dosen + 5 Pertanyaan Jebakan Sidang Sulit Level ⭐⭐⭐⭐⭐. Buka tab <strong>"🎯 Simulasi Sidang"</strong> pada menu atas untuk latihan interaktif dengan kata kunci wajib!</div>
        </div>
        <div class="slide-grid-2">
          <div class="feature-card gold">
            <div class="feature-title">Pertanyaan Dosen Pembimbing</div>
            <ul class="feature-list">
              <li>Justifikasi penggantian variabel moderasi ke Self-Control</li>
              <li>Pembakuan istilah ilmiah Desire for Completeness</li>
              <li>Justifikasi Grand Theory Behavioral Finance</li>
              <li>Alur Bab II: Mengapa variabel Y dibahas terlebih dahulu</li>
              <li>Kaitan PSA Grading dengan Speculative Motive</li>
            </ul>
          </div>
          <div class="feature-card rose">
            <div class="feature-title">Pertanyaan Jebakan Penguji</div>
            <ul class="feature-list">
              <li>Relevansi Zeigarnik Effect (1927) di era modern</li>
              <li>Penerapan Speculative Motive Keynes pada kartu hobi</li>
              <li>Uji validitas diskriminan antar 3 variabel X</li>
              <li>Justifikasi tidak perlunya uji autokorelasi cross-sectional</li>
              <li>Penanganan selection bias komunitas online</li>
            </ul>
          </div>
        </div>
      `;

    case 'penutup_cheatsheet':
      return `
        <div class="feature-card gold" style="padding: 1.5rem;">
          <div class="feature-title" style="font-size:1.25rem; color:#fff; text-align:center; margin-bottom:1rem;">
            RANGKUMAN HAFALAN KILAT 1 HALAMAN (CHEAT SHEET)
          </div>
          <div style="font-family: var(--font-mono); font-size: 0.85rem; color: #cbd5e1; line-height: 1.7; background: rgba(0,0,0,0.4); padding: 1.25rem; border-radius: var(--radius-sm);">
            <strong>1. Model:</strong> 3X (Hedonic, Completeness, Speculative) -> Y (Impulsive) dimoderasi M (Self-Control memperlemah -)<br>
            <strong>2. Grand Theory:</strong> Behavioral Finance (Herbert Simon, Kahneman-Tversky, Shiller, Thaler-Shefrin Planner-Doer)<br>
            <strong>3. Rujukan Kunci:</strong> Gao et al. (2014 JMR), Zeigarnik (1927), Keynes (1936), Tangney et al. (2004), Colline (2024)<br>
            <strong>4. Metode:</strong> Kuantitatif Asosiatif | Purposive Sampling (N=120-150) | MRA Mean-Centering OLS SPSS<br>
            <strong>5. Aturan Asumsi:</strong> Uji Autokorelasi TIDAK relevan untuk data primer survei cross-sectional (Ghozali, 2018)
          </div>
          <div style="text-align:center; margin-top: 1.25rem; color: var(--accent-gold-light); font-weight:700;">
            🎓 Siap Maju Bimbingan & Seminar Proposal Skripsi FEB UKRIDA!
          </div>
        </div>
      `;

    default:
      return '<p>Konten slide sedang dimuat...</p>';
  }
}

// 2. FLASHCARD STUDIO ENGINE
function initFlashcards() {
  renderFlashcardFilter();
  renderCurrentFlashcard();

  const cardElement = document.getElementById('main-flashcard');
  cardElement.addEventListener('click', () => {
    cardElement.classList.toggle('flipped');
  });

  document.getElementById('fc-prev-btn').addEventListener('click', () => {
    if (currentFcIndex > 0) {
      currentFcIndex--;
      renderCurrentFlashcard();
    }
  });

  document.getElementById('fc-next-btn').addEventListener('click', () => {
    if (currentFcIndex < currentFcList.length - 1) {
      currentFcIndex++;
      renderCurrentFlashcard();
    }
  });

  document.getElementById('fc-repeat-btn').addEventListener('click', () => {
    const card = currentFcList[currentFcIndex];
    fcMasteredSet.delete(card.id);
    saveMasteredSet();
    nextFc();
  });

  document.getElementById('fc-master-btn').addEventListener('click', () => {
    const card = currentFcList[currentFcIndex];
    fcMasteredSet.add(card.id);
    saveMasteredSet();
    nextFc();
  });
}

function nextFc() {
  if (currentFcIndex < currentFcList.length - 1) {
    currentFcIndex++;
  } else {
    currentFcIndex = 0;
  }
  renderCurrentFlashcard();
}

function saveMasteredSet() {
  localStorage.setItem('fc_mastered', JSON.stringify([...fcMasteredSet]));
  updateMasteryProgress();
}

function updateMasteryProgress() {
  const percent = Math.round((fcMasteredSet.size / FLASHCARDS.length) * 100);
  const progressBar = document.getElementById('fc-progress-fill');
  if (progressBar) progressBar.style.width = percent + '%';
  const label = document.getElementById('fc-mastery-label');
  if (label) label.textContent = fcMasteredSet.size + ' / ' + FLASHCARDS.length + ' DIKUASAI (' + percent + '%)';
}

function renderFlashcardFilter() {
  const filterContainer = document.getElementById('fc-filter-group');
  const filters = [
    { id: 'all', label: 'Semua (26)' },
    { id: 'var', label: 'Variabel (5)' },
    { id: 'theory', label: 'Teori (7)' },
    { id: 'tcg', label: 'TCG & Grading (6)' },
    { id: 'stat', label: 'Statistik (8)' }
  ];

  filterContainer.innerHTML = filters.map(f => `
    <button class="filter-btn ${f.id === currentFcCategory ? 'active' : ''}" data-cat="${f.id}">
      ${f.label}
    </button>
  `).join('');

  filterContainer.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      currentFcCategory = btn.dataset.cat;
      filterContainer.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      if (currentFcCategory === 'all') {
        currentFcList = [...FLASHCARDS];
      } else {
        currentFcList = FLASHCARDS.filter(c => c.cat === currentFcCategory);
      }
      currentFcIndex = 0;
      renderCurrentFlashcard();
    });
  });
}

function renderCurrentFlashcard() {
  const cardElement = document.getElementById('main-flashcard');
  cardElement.classList.remove('flipped');

  if (currentFcList.length === 0) {
    document.getElementById('fc-front-term').textContent = "Tidak ada kartu.";
    return;
  }

  const card = currentFcList[currentFcIndex];
  const badgeClass = card.color;

  document.getElementById('fc-badge-front').className = 'card-badge ' + badgeClass;
  document.getElementById('fc-badge-front').textContent = card.title;
  document.getElementById('fc-front-term').textContent = card.term;

  document.getElementById('fc-badge-back').className = 'card-badge ' + badgeClass;
  document.getElementById('fc-badge-back').textContent = card.title;
  document.getElementById('fc-back-author').textContent = card.author;
  document.getElementById('fc-back-desc').textContent = card.desc;

  document.getElementById('fc-indicator').textContent = (currentFcIndex + 1) + ' / ' + currentFcList.length;

  const isMastered = fcMasteredSet.has(card.id);
  document.getElementById('fc-status-pill').textContent = isMastered ? 'Sudah Dikuasai ✅' : 'Belum Dikuasai ⏳';
  document.getElementById('fc-status-pill').style.color = isMastered ? '#34d399' : '#f59e0b';

  updateMasteryProgress();
}

// 3. DEFENSE SIMULATOR ENGINE
function initDefenseQuestions() {
  const listContainer = document.getElementById('qa-list-container');
  const searchInput = document.getElementById('qa-search-input');

  function renderQA(items) {
    listContainer.innerHTML = items.map(q => `
      <div class="qa-card" data-id="${q.id}">
        <div class="qa-header">
          <div class="qa-title-wrapper">
            <span class="qa-badge ${q.type === 'jebakan' ? 'danger' : ''}">${q.badge}</span>
            <div class="qa-question">❓ ${q.question}</div>
          </div>
          <span style="font-size:1.2rem; color:var(--text-muted);" class="qa-chevron">▼</span>
        </div>
        <div class="qa-body">
          <div class="keywords-tag-container">
            <span class="must-say-label">Kata Kunci Wajib:</span>
            ${q.keywords.map(kw => `<span class="kw-badge">${kw}</span>`).join('')}
          </div>
          <div class="qa-answer-text">
            <strong>💡 Rekomendasi Jawaban:</strong><br>
            ${q.answer}
          </div>
        </div>
      </div>
    `).join('');

    listContainer.querySelectorAll('.qa-header').forEach(header => {
      header.addEventListener('click', () => {
        const card = header.closest('.qa-card');
        card.classList.toggle('open');
        const chevron = header.querySelector('.qa-chevron');
        chevron.textContent = card.classList.contains('open') ? '▲' : '▼';
      });
    });
  }

  renderQA(QUESTIONS);

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase();
      const filtered = QUESTIONS.filter(q => 
        q.question.toLowerCase().includes(query) || 
        q.answer.toLowerCase().includes(query) ||
        q.keywords.some(k => k.toLowerCase().includes(query))
      );
      renderQA(filtered);
    });
  }
}

// 4. INTERACTIVE QUIZ ENGINE
function initQuiz() {
  renderQuizQuestion();

  document.getElementById('quiz-next-btn').addEventListener('click', () => {
    if (currentQuizIndex < QUIZ.length - 1) {
      currentQuizIndex++;
      quizAnswered = false;
      renderQuizQuestion();
    } else {
      showQuizResult();
    }
  });

  document.getElementById('quiz-restart-btn').addEventListener('click', () => {
    currentQuizIndex = 0;
    quizScore = 0;
    quizAnswered = false;
    document.getElementById('quiz-result-view').style.display = 'none';
    document.getElementById('quiz-active-view').style.display = 'block';
    renderQuizQuestion();
  });
}

function renderQuizQuestion() {
  const q = QUIZ[currentQuizIndex];
  document.getElementById('quiz-progress-label').textContent = 'Soal ' + (currentQuizIndex + 1) + ' dari ' + QUIZ.length;
  document.getElementById('quiz-progress-fill').style.width = (((currentQuizIndex + 1) / QUIZ.length) * 100) + '%';
  
  document.getElementById('quiz-question-text').textContent = q.q;
  document.getElementById('quiz-explanation-box').classList.remove('show');
  document.getElementById('quiz-next-btn').style.display = 'none';

  const optionsContainer = document.getElementById('quiz-options-container');
  optionsContainer.innerHTML = q.options.map((opt, idx) => `
    <button class="quiz-opt-btn" data-index="${idx}">
      ${opt}
    </button>
  `).join('');

  optionsContainer.querySelectorAll('.quiz-opt-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      if (quizAnswered) return;
      quizAnswered = true;
      const selectedIndex = parseInt(btn.dataset.index);

      if (selectedIndex === q.ans) {
        btn.classList.add('correct');
        quizScore++;
      } else {
        btn.classList.add('wrong');
        optionsContainer.querySelector('[data-index="' + q.ans + '"]').classList.add('correct');
      }

      optionsContainer.querySelectorAll('.quiz-opt-btn').forEach(b => b.disabled = true);

      document.getElementById('quiz-exp-text').textContent = q.exp;
      document.getElementById('quiz-explanation-box').classList.add('show');
      document.getElementById('quiz-next-btn').style.display = 'inline-flex';
    });
  });
}

function showQuizResult() {
  document.getElementById('quiz-active-view').style.display = 'none';
  const resultView = document.getElementById('quiz-result-view');
  resultView.style.display = 'block';

  const finalScore = Math.round((quizScore / QUIZ.length) * 100);
  document.getElementById('quiz-final-score').textContent = finalScore;
  
  let gradeText = "";
  if (finalScore >= 85) {
    gradeText = "Luar Biasa! Pemahaman materi proposal Anda sangat matang (Nilai A). Siap Sidang!";
  } else if (finalScore >= 70) {
    gradeText = "Bagus! Anda sudah memahami sebagian besar konsep. Ulas kembali beberapa butir soal.";
  } else {
    gradeText = "Perlu Pengulangan! Disarankan membuka kembali Flashcard dan Slide Presentasi.";
  }
  document.getElementById('quiz-grade-text').textContent = gradeText;
}

// 5. MRA MODERATION SLOPES CALCULATOR
function initMRACalculator() {
  const slider = document.getElementById('mra-mod-slider');
  const varSelect = document.getElementById('mra-var-select');

  if (!slider || !varSelect) return;

  function updatePlot() {
    const modValue = parseFloat(slider.value);
    const varType = varSelect.value;
    
    document.getElementById('mra-mod-val-label').textContent = 
      modValue < -0.3 ? 'Rendah (Low Self-Control)' : 
      modValue > 0.3 ? 'Tinggi (High Self-Control)' : 'Rata-Rata (Mean)';

    const svg = document.getElementById('mra-slopes-svg');
    if (!svg) return;

    const baseSlope = 0.65;
    const interaction = -0.30;
    const currentSlope = baseSlope + (interaction * modValue);

    const x1 = 60, y1 = 220;
    const x2 = 360, y2 = 220 - (currentSlope * 200);

    svg.innerHTML = `
      <line x1="50" y1="240" x2="380" y2="240" stroke="#64748b" stroke-width="2"/>
      <line x1="50" y1="240" x2="50" y2="30" stroke="#64748b" stroke-width="2"/>

      <text x="210" y="270" fill="#94a3b8" font-size="12" text-anchor="middle">Tingkat ${varType} (X)</text>
      <text x="30" y="130" fill="#94a3b8" font-size="12" text-anchor="middle" transform="rotate(-90 30 130)">Impulsive Buying (Y)</text>

      <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#f59e0b" stroke-width="4"/>
      
      <circle cx="${x1}" cy="${y1}" r="6" fill="#f59e0b"/>
      <circle cx="${x2}" cy="${y2}" r="6" fill="#f59e0b"/>

      <text x="${x2 - 20}" y="${y2 - 15}" fill="#fbbf24" font-size="11" font-weight="bold">
        Kemiringan (Slope): ${currentSlope.toFixed(2)}
      </text>
    `;

    document.getElementById('mra-slope-desc').textContent = 
      modValue > 0.3 ? 
      "Ketika Self-Control TINGGI, kemiringan garis regresi melandai. Ini membuktikan secara visual bahwa Self-Control MEMPERLEMAH efek positif variabel X terhadap Impulsive Buying." :
      modValue < -0.3 ?
      "Ketika Self-Control RENDAH, kemiringan garis regresi menjadi sangat curam. Pembeli tanpa rem kognitif sangat rentan terjerumus dalam belanja impulsif." :
      "Pada tingkat Self-Control RATA-RATA, pengaruh variabel X terhadap Impulsive Buying berada pada tingkat moderat.";
  }

  slider.addEventListener('input', updatePlot);
  varSelect.addEventListener('change', updatePlot);
  updatePlot();
}

// 6. TIMER & KEYBOARD SHORTCUTS
function initTimer() {
  const timeDisplay = document.getElementById('timer-display');
  const toggleBtn = document.getElementById('timer-toggle-btn');
  const resetBtn = document.getElementById('timer-reset-btn');

  function updateDisplay() {
    const mins = Math.floor(timerSeconds / 60);
    const secs = timerSeconds % 60;
    timeDisplay.textContent = String(mins).padStart(2, '0') + ':' + String(secs).padStart(2, '0');
  }

  toggleBtn.addEventListener('click', () => {
    if (timerRunning) {
      clearInterval(timerInterval);
      timerRunning = false;
      toggleBtn.textContent = '▶';
    } else {
      timerInterval = setInterval(() => {
        if (timerSeconds > 0) {
          timerSeconds--;
          updateDisplay();
        } else {
          clearInterval(timerInterval);
          timerRunning = false;
          toggleBtn.textContent = '▶';
          alert('Waktu latihan presentasi 15 menit telah habis!');
        }
      }, 1000);
      timerRunning = true;
      toggleBtn.textContent = '⏸';
    }
  });

  resetBtn.addEventListener('click', () => {
    clearInterval(timerInterval);
    timerRunning = false;
    timerSeconds = 15 * 60;
    toggleBtn.textContent = '▶';
    updateDisplay();
  });

  updateDisplay();
}

function initShortcuts() {
  window.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

    if (e.key === 'ArrowRight' || e.key === ' ') {
      if (document.getElementById('tab-presentation').classList.contains('active')) {
        nextSlide();
      }
    } else if (e.key === 'ArrowLeft') {
      if (document.getElementById('tab-presentation').classList.contains('active')) {
        prevSlide();
      }
    } else if (e.key.toLowerCase() === 'n') {
      toggleNotes();
    } else if (e.key.toLowerCase() === 'f') {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    }
  });
}

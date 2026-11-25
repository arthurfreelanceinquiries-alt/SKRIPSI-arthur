> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Spesifikasi baku Google Forms survei utama — menjadi acuan Tunggal pelaksanaan revisi D45.
> - **Masalah yang Diselesaikan:** Menyelaraskan redaksi S3 (anti-kebingungan komuter), P5 (kanal marketplace), dan **urutan kode indikator X3** agar identik dengan Tabel 3.2 proposal.
> - **Keputusan/Output:** 1 butir consent + 4 screening + 5 profil + 27 butir Likert, beserta skrip penerap `CREATE_GFORM_AUTOMATION.gs`.

# DRAF KUESIONER GOOGLE FORMS — Impulsive Buying Booster Pack Pokemon TCG (Jakarta Barat)

> **Acuan kanonis:** Tabel 3.2 Operasionalisasi Variabel (`01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex` baris 1100), `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` (D06/D31/D45), dan `07_Review_&_Audit/Revisi_Dosen/2026-11-17_Revisi_Fredella_Colline_Validasi_Kuesioner_dan_Kanal_Belanja.md`.
> **Status:** Revisi D45 **SUDAH DITERAPKAN** langsung pada form live (`1W23UT6NnR1xchMGuQK_cIVctXGI3xPfPAUwsUJ7Z0Ws`) per 25 Nov 2026 — judul S3, opsi S3, judul P5, dan 5 opsi P5 terverifikasi lewat `viewform`. Catatan anti-komuter S3 ditempatkan pada **deskripsi section "Penyaringan — S3"** (bukan help text per-butir, yang tidak dapat diisi pada build Forms tersebut).

---

## A. Judul & Deskripsi Formulir

**Judul Forms:**

> Survei Perilaku Pembelian Booster Pack Kartu Pokémon TCG — Konsumen Jakarta Barat

**Deskripsi (Section 1):**

> Perkenalkan, saya Arthur Reezan, mahasiswa S1 Manajemen FEB UKRIDA. Survei ini mendukung penelitian mengenai pengaruh Hedonic Motivation, Desire for Completeness, dan Speculative Motive terhadap Impulsive Buying Booster Pack Kartu Pokémon TCG dengan Self-Control sebagai Variabel Moderasi (Studi pada Konsumen di Jakarta Barat).
>
> Partisipasi bersifat sukarela. Peneliti tidak meminta nama, NIM, email, nomor telepon, atau alamat rumah. Jawaban digunakan untuk keperluan akademik dan dilaporkan secara agregat. Anda dapat berhenti dengan menutup formulir sebelum mengirim jawaban.
>
> **Kriteria:** WNI, berusia minimal 17 tahun, memiliki **minimal salah satu** keterkaitan dengan Jakarta Barat, dan pernah membeli booster pack fisik resmi Pokémon TCG berbahasa Indonesia dalam 12 bulan terakhir.

---

## B. Butir C0 — Persetujuan (Consent)

| Kode | Pertanyaan | Opsi | Logika |
|---|---|---|---|
| C0 | Saya telah membaca informasi penelitian di atas dan bersedia berpartisipasi secara sukarela. | Ya, saya setuju berpartisipasi / Tidak, saya tidak setuju berpartisipasi | Setuju → Section S1. Tidak setuju → **Keluar** (tanpa mengisi apa pun) |

---

## C. Bagian 1 — Screening (S1–S4)

Semua bertipe **pilihan ganda, wajib isi**. Opsi diskualifikasi mengarah ke halaman **Penutup — Kriteria partisipasi belum terpenuhi** (`INCLUDE=0`).

| Kode | Pertanyaan | Opsi | Inklusi |
|---|---|---|---|
| S1 | Apakah Anda Warga Negara Indonesia (WNI)? | Ya / Tidak | WNI |
| S2 | Apakah usia Anda sudah mencapai 17 tahun atau lebih? | Ya, 17 tahun atau lebih / Tidak, di bawah 17 tahun | Usia ≥17 th |
| **S3** | **Apakah Anda memiliki MINIMAL SALAH SATU keterkaitan dengan wilayah Jakarta Barat berikut?** (Contoh: tinggal/kost di Jakbar, ATAU kuliah/bekerja di Jakbar seperti kampus UKRIDA/Untar/kantor Jakbar, ATAU pernah atau rutin berbelanja/bermain kartu Pokemon di toko/mall/LGS wilayah Jakbar) | **Ya (memenuhi minimal salah satu kriteria di atas)** / **Tidak (sama sekali tidak memiliki keterkaitan dengan Jakarta Barat)** | Keterkaitan Jakbar (D31 & D45) |
| S4 | Kapan TERAKHIR kali Anda membeli booster pack fisik resmi Pokémon TCG berbahasa Indonesia? | Dalam 6 bulan terakhir / Lebih dari 6 bulan s.d. 12 bulan terakhir / Lebih dari 12 bulan lalu atau belum pernah | Pembelian ≤12 bulan |

> **Catatan S3 (inti revisi D45):** redaksi sengaja memakai *"minimal salah satu"* agar responden komuter tidak salah diskualifikasi. Lokasi tinggal, kuliah/kerja, dan tempat bermain **boleh berbeda wilayah**; cukup satu di antaranya berada di Jakarta Barat. Bantuan (help text) butir S3 wajib menegaskan hal ini.

> **Catatan S4:** label *"berbahasa Indonesia"* dipertahankan karena menandai pasar ritel resmi Indonesia (harga eceran pack ± Rp20.000, sesuai Bab 1). Opsi *"lebih dari 12 bulan lalu"* dan *"belum pernah"* digabung agar tidak ada responden yang tertahan tanpa opsi.

---

## D. Bagian 2 — Profil Responden (P1–P5)

| Kode | Pertanyaan | Opsi | Wajib |
|---|---|---|---|
| P1 | Jenis kelamin | Laki-laki / Perempuan | Tidak |
| P2 | Kelompok usia | 17–20 / 21–25 / 26–30 / Lebih dari 30 tahun | Tidak |
| P3 | Kecamatan aktivitas utama di Jakarta Barat | Cengkareng / Grogol Petamburan / Kalideres / Kebon Jeruk / Kembangan / Palmerah / Taman Sari / Tambora | Tidak |
| P4 | Frekuensi pembelian booster pack dalam 6 bulan terakhir | 0 kali / 1 kali / 2–3 kali / 4–6 kali / Lebih dari 6 kali | Ya |
| **P5** | **Kanal/tempat pembelian utama yang paling sering Anda gunakan** | **Marketplace daring / E-commerce (Tokopedia, Shopee, TikTok Shop, Blibli, dll.)** / Local Game Store (LGS) resmi (Tanjung Duren/Central Park/Mall Taman Anggrek/Puri Indah) / Minimarket atau toko buku (Indomaret/Alfamart/Gramedia/Toys Kingdom) / Transaksi langsung / COD komunitas / Lainnya | Tidak |

> **Catatan P3:** help text wajib menulis *"Tanjung Duren termasuk Kecamatan Grogol Petamburan"* — kampus UKRIDA berada di sana.
> **Catatan P4:** help text wajib menulis *"Jika pembelian terakhir Anda lebih dari 6 bulan lalu, pilih 0 kali."* Agar konsisten dengan S4, responden yang lolos (S4 ≤12 bulan) tetap boleh menjawab 0 kali bila pembeliannya 7–12 bulan lalu.
> **Catatan P5 (inti revisi D45):** opsi **Marketplace daring ditempatkan di urutan pertama** dengan nama platform disebut eksplisit (Tokopedia, Shopee, TikTok Shop, Blibli).

---

## E. Bagian 3–7 — Butir Likert (27 butir, wajib isi)

Petunjuk (di setiap section): *"Berilah penilaian sesuai pengalaman Anda. 1 = Sangat Tidak Setuju; 2 = Tidak Setuju; 3 = Netral; 4 = Setuju; 5 = Sangat Setuju. Tidak ada jawaban benar atau salah."*

Tipe: **Skala linear 1–5**, label kiri "Sangat Tidak Setuju", label kanan "Sangat Setuju". Urutan butir **tetap** (jangan acak) agar pemetaan ke kodebook konsisten. Seluruh butir **favorabel** — tanpa reverse-scoring.

### E1. Y — Impulsive Buying (6 butir) · Section "Pengalaman pembelian"

| Kode | Indikator Tabel 3.2 | Teks butir |
|---|---|---|
| Y1 | 1. Ketiadaan perencanaan belanja sebelumnya | Saya membeli booster pack Pokémon TCG tanpa merencanakan pembelian tersebut sebelumnya. |
| Y2 | 2. Pengabaian pertimbangan konsekuensi finansial | Saya tidak mempertimbangkan dampak keuangan saat membeli booster pack Pokémon TCG. |
| Y3 | 3. Pembelian melebihi niat awal | Saya membeli booster pack Pokémon TCG lebih banyak daripada yang semula saya niatkan. |
| Y4 | 4. Dorongan belanja spontan saat melihat produk di etalase | Saya terdorong membeli booster pack Pokémon TCG secara spontan saat melihatnya di etalase toko. |
| Y5 | 5. Perasaan gembira dan antusias saat memutuskan membeli seketika | Saya merasa gembira dan antusias ketika memutuskan membeli booster pack Pokémon TCG secara mendadak. |
| Y6 | 6. Kesulitan menahan hasrat saat rilis produk baru | Saya sulit menahan keinginan membeli booster pack Pokémon TCG saat seri baru dirilis. |

> *Sumber Indikator: Verplanken dan Herabadi (2001); Rook (1987).*

### E2. X1 — Hedonic Motivation (5 butir) · Section "Pengalaman dan kesenangan berbelanja"

| Kode | Indikator Tabel 3.2 | Teks butir |
|---|---|---|
| X1_1 | 1. Adventure shopping | Saya merasa senang dan penasaran saat membuka kemasan booster pack Pokémon TCG. |
| X1_2 | 2. Gratification shopping | Membeli booster pack Pokémon TCG menjadi cara saya menghibur diri dan meredakan stres. |
| X1_3 | 3. Social shopping | Saya menikmati interaksi dan kebersamaan dengan teman sehobi saat berbelanja booster pack Pokémon TCG. |
| X1_4 | 4. Role shopping | Saya senang membeli booster pack Pokémon TCG untuk dihadiahkan atau dinikmati bersama orang lain. |
| X1_5 | 5. Idea shopping | Saya antusias mengikuti tren rilis seri dan pembaruan desain kartu Pokémon TCG. |

> *Sumber Indikator: Arnold dan Reynolds (2003); Babin et al. (1994).*

### E3. X2 — Desire for Completeness (5 butir) · Section "Kelengkapan koleksi"

| Kode | Indikator Tabel 3.2 | Teks butir |
|---|---|---|
| X2_1 | 1. Perasaan tidak nyaman melihat celah kosong | Saya merasa tidak nyaman melihat bagian yang masih kosong dalam satu seri koleksi kartu Pokémon TCG. |
| X2_2 | 2. Ketidaktenangan pikiran saat ada unit belum dimiliki | Saya merasa tidak tenang saat mengetahui masih ada kartu yang belum saya miliki dalam satu seri koleksi Pokémon TCG. |
| X2_3 | 3. Dorongan menambah unit demi melengkapi | Saya terdorong untuk terus menambah kartu demi melengkapi satu seri koleksi Pokémon TCG. |
| X2_4 | 4. Kepuasan batin saat set lengkap | Saya merasa puas ketika berhasil melengkapi satu set kartu Pokémon TCG. |
| X2_5 | 5. Desakan meningkat saat sisa semakin sedikit | Semakin sedikit kartu yang belum saya miliki dalam satu seri, semakin kuat dorongan saya untuk berbelanja demi melengkapinya. |

> *Sumber Indikator: Barasz et al. (2017); Gao et al. (2014).*

### E4. X3 — Speculative Motive (5 butir) · Section "Pertimbangan nilai kartu"

> **PENTING — koreksi urutan indikator.** Draf sebelumnya menukar posisi indikator 2 dan 4 sehingga kode butir tidak lagi sejajar dengan Tabel 3.2. Tabel di bawah ini **mengikuti urutan Tabel 3.2 apa adanya**.

| Kode | Indikator Tabel 3.2 (urutan baku) | Teks butir |
|---|---|---|
| X3_1 | 1. Ekspektasi memperoleh unit langka bernilai jual tinggi | Saya membeli booster pack Pokémon TCG dengan harapan memperoleh kartu langka yang bernilai jual tinggi di masa depan. |
| **X3_2** | **2. Penilaian kelayakan biaya pembelian vs potensi keuntungan** | Saya menilai biaya membeli booster pack Pokémon TCG sebanding dengan potensi keuntungan dari kartu yang diperoleh di masa depan. |
| X3_3 | 3. Pandangan produk sebagai aset alternatif yang dapat terapresiasi | Saya memandang kartu Pokémon TCG sebagai aset alternatif yang nilainya dapat meningkat di masa depan. |
| X3_4 | 4. Persepsi likuiditas dan kemudahan penjualan kembali | Saya menilai kartu Pokémon TCG mudah dan cepat dijual kembali di pasar sekunder. |
| X3_5 | 5. Ketertarikan pada kartu bersertifikasi resmi | Saya tertarik pada kartu Pokémon TCG bersertifikasi resmi (grading) karena berpotensi memiliki harga jual kembali yang lebih tinggi. |

> *Sumber Indikator: Colline (2024); Aryadi dan Lingga (2026).*

#### E4.1 Pemetaan Sitasi Colline (2024) — jawaban atas pertanyaan Dosen Pembimbing

Colline (2024) *"Biases in Indonesian Stock Investor Behavior"* tidak menyediakan skala psikometri kartu. Perannya adalah **landasan teoretis Behavioral Finance** tentang bias ekspektasi imbal hasil (*capital gain*), optimisme berlebih, dan ilusi keuntungan cepat pada pelaku transaksi di Indonesia. Peran itu masuk ke instrumen pada **dua butir**, bukan kelima butir:

| Butir | Indikator | Peran Colline (2024) |
|---|---|---|
| **X3_2** | 2. Kelayakan biaya vs potensi keuntungan | **Operasionalisasi utama.** Inti artikel Colline adalah kalkulasi untung-rugi yang bias — persis logika "biaya pembelian sebanding potensi keuntungan". |
| X3_1 | 1. Ekspektasi unit langka bernilai tinggi | **Dukungan konseptual.** Bias ekspektasi *return* menjelaskan mengapa pembeli membayangkan kartu langka bernilai tinggi. |
| X3_3, X3_4, X3_5 | 3, 4, 5 | Tidak bersumber dari Colline. Disokong Baur et al. (2018) untuk aset alternatif, Aryadi dan Lingga (2026) untuk likuiditas serta *grading* di komunitas TCG Jabodetabek. |

> **Rumusan satu kalimat untuk dijelaskan ke Dosen:** *"Bu Colline, artikel 2024 Bu Colline dipakai sebagai payung teori behavioral finance soal bias ekspektasi keuntungan. Yang paling tepat mewakili itu indikator ke-2 — penilaian biaya versus potensi untung — dan indikator ke-1 sebagai pendukung. Tiga indikator lainnya bersumber dari Baur et al. (2018) dan Aryadi dan Lingga (2026)."*

### E5. M — Self-Control (6 butir, moderasi) · Section "Pengendalian diri saat berbelanja"

| Kode | Indikator Tabel 3.2 | Teks butir |
|---|---|---|
| M1 | 1. Kemampuan menolak godaan di luar rencana anggaran | Saya mampu menolak godaan berbelanja di luar anggaran yang sudah saya rencanakan. |
| M2 | 2. Kebiasaan mempertimbangkan konsekuensi keuangan | Saya terbiasa mempertimbangkan konsekuensi keuangan sebelum bertransaksi. |
| M3 | 3. Disiplin diri menahan dorongan belanja spontan | Saya mampu menahan dorongan untuk membeli secara spontan saat melihat barang yang menarik. |
| M4 | 4. Kemampuan menunda kesenangan demi tujuan jangka panjang | Saya mampu menunda kesenangan berbelanja saat ini demi tujuan jangka panjang. |
| M5 | 5. Kemampuan menahan diri dari pengaruh suasana toko | Saya mampu menahan diri agar tidak mudah terpengaruh oleh suasana di toko saat berbelanja. |
| M6 | 6. Konsistensi mematuhi batas anggaran | Saya konsisten mematuhi batas anggaran pengeluaran yang telah saya tetapkan. |

> *Sumber Indikator: Tangney et al. (2004).*

---

## F. Halaman Penutup (2 jalur)

1. **Penutup — Kriteria partisipasi belum terpenuhi** (dari S1/S2/S3/S4 gagal): *"Terima kasih atas kesediaan Anda. Survei ini dikhususkan untuk responden WNI, berusia minimal 17 tahun, memiliki keterkaitan dengan Jakarta Barat, dan pernah membeli booster pack fisik resmi Pokémon TCG berbahasa Indonesia dalam 12 bulan terakhir. Anda tidak perlu mengisi butir penelitian berikutnya."* → **Submit**.
2. **Keluar — Tidak menyetujui partisipasi** (dari C0): halaman penutup tanpa submit; responden diminta menutup formulir.

---

## G. Penerapan & Verifikasi

**Status penerapan (25 Nov 2026):** seluruh perubahan S3 dan P5 sudah aktif di form live. Verifikasi dilakukan dengan membaca `FB_PUBLIC_LOAD_DATA_` dari `viewform` — judul, opsi, keterangan section, dan logika cabang C0/S1–S4 semuanya sesuai. 27 butir Likert utuh berurutan Y1..M6.

**Cara menerapkan ulang (bila formulir diganti / tanpa OAuth):**

1. Buka **https://script.google.com** → **New project**.
2. Tempel seluruh isi `03_Instrumen_&_Data_Survei/01_Kuesioner_Google_Forms/CREATE_GFORM_AUTOMATION.gs`.
3. Pilih fungsi **`perbaikiKuesionerRevisiD45`** → **Run** → izinkan akses saat diminta.
4. Buka **Execution log** untuk melihat ringkasan.
5. Jalankan **`verifikasiKuesioner`** untuk memastikan S3, P5, dan urutan 27 butir sudah benar.

**Yang diubah skrip pada form live (`1W23UT6NnR1xchMGuQK_cIVctXGI3xPfPAUwsUJ7Z0Ws`):**

| Butir | Sebelum | Sesudah |
|---|---|---|
| S3 | "Apakah Anda berdomisili ATAU rutin beraktivitas/bertransaksi (kuliah, kerja, COD, turnamen/LGS) di wilayah Jakarta Barat?" — opsi Ya/Tidak | Formula *"minimal salah satu keterkaitan"* + help text anti-komuter; opsi diperjelas |
| P5 | 4 opsi, "Marketplace daring" di urutan **terakhir**, tanpa contoh platform | 5 opsi, "Marketplace daring / E-commerce (Tokopedia, Shopee, TikTok Shop, Blibli, dll.)" di urutan **pertama** |
| C0, S1, S2, S4, P1–P4, 27 butir Likert | — | **Tidak diubah** (sudah benar) |

---

## H. Catatan Setting Google Forms (wajib)

1. **Wajib isi:** C0, S1–S4, P4, dan seluruh 27 butir Likert. P1–P3 dan P5 opsional.
2. **Validasi Likert:** gunakan tipe "Skala linear" 1–5; jangan "Respons singkat" bernomor.
3. **Section logic:** aktifkan "Go to section based on answer" pada C0, S1–S4. Aktifkan "Show progress bar".
4. **Satu respons per orang:** pertimbangkan "Limit to 1 response" bila sebar daring; bila sebar luring di LGS, matikan limit tetapi pastikan "Collect email addresses = OFF" dan cek duplikasi lewat pola P1–P5.
5. **Anti-bias:** matikan "Shuffle question order" agar urutan Y1..M6 tetap sesuai kodebook.
6. **Uji coba:** sebelum pilot N=30, kirim *preview link* ke 2–3 kolektor; uji jalur diskualifikasi S1–S4 dan jalur consent "tidak setuju".
7. **Ekspor:** unduh CSV/Excel, tabulasi mengikuti `02_Data_Mentah_Survei_Excel/KODEBOOK_DAN_TEMPLATE_TABULASI.md` dengan nama kolom persis.

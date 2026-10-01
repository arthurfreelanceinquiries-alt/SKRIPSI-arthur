> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Draf struktur Google Forms survei utama (screening, profil, 27 butir Likert) siap disalin ke Google Forms.
> - **Masalah yang Diselesaikan:** Mencegah butir lapangan menyimpang dari Tabel 3.2 proposal dan kriteria inklusi D06/D31.
> - **Keputusan/Output:** 27 butir berkode (Y=6, X1=5, X2=5, X3=5, M=6) plus setting wajib-isi, validasi, dan section logic.

# DRAF KUESIONER GOOGLE FORMS — Impulsive Buying Booster Pack Pokemon TCG (Jakarta Barat)

> Acuan kanonis: Tabel 3.2 Operasionalisasi Variabel (`01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md` Subbab 3.4 / `.tex` Tab. operasionalisasi), `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` (D06/D07/D31), dan `03_Instrumen_&_Data_Survei/README.md`. Seluruh redaksi butir di bawah disalin verbatim dari Tabel 3.2 (tanpa parafrasa) agar selaras 100%.

---

## A. Judul & Deskripsi Formulir (teks pembuka Forms)

**Judul Forms:**

> Survei Perilaku Pembelian Booster Pack Kartu Pokemon TCG — Konsumen Jakarta Barat

**Deskripsi (tampilkan di Section 1):**

> Perkenalkan, saya Arthur Reezan (S1 Manajemen, FEB UKRIDA). Formulir ini adalah instrumen Tugas Akhir berjudul *"Pengaruh Hedonic Motivation, Desire for Completeness, dan Speculative Motive terhadap Impulsive Buying Booster Pack Kartu Pokemon TCG dengan Self-Control sebagai Variabel Moderasi (Studi pada Konsumen di Jakarta Barat)"*.
>
> Partisipasi bersifat **sukarela dan anonim**. **Data PII minimal: kami TIDAK meminta nama, NIM, alamat email, nomor HP, atau alamat rumah.** Jawaban hanya dipakai untuk keperluan akademik dan dilaporkan secara agregat. Anda boleh berhenti kapan saja tanpa konsekuensi. Estimasi waktu pengisian: 5–7 menit. Dengan menekan "Berikutnya" dan mengisi kuesioner ini, Anda menyatakan telah membaca informasi ini dan **menyetujui berpartisipasi (informed consent)**.
>
> Kriteria partisipan: (1) WNI; (2) usia minimal 17 tahun (cakap memberi persetujuan mandiri, kepemilikan KTP); (3) berdomisili atau beraktivitas/bertransaksi aktif di Jakarta Barat; (4) pernah membeli *booster pack* fisik resmi minimal 1x dalam 12 bulan terakhir (diutamakan 6 bulan terakhir agar memori pembelian masih segar).

**Catatan etik (cantumkan di deskripsi/penutup):** survei risiko-minimal; tanpa data identitas; responden dapat mundur kapan pun; data tersimpan hanya untuk analisis akademik.

---

## B. Bagian 1 — Screening / Penyaringan Awal (WAJIB, Section 1, logic aktif)

Instruksi section: *"Bagian ini menentukan kelayakan Anda sebagai responden. Mohon jawab jujur."* Semua S1–S4 bertipe **Pilihan ganda (wajib isi)**. Responden yang menjawab "Tidak" pada SALAH SATU butir diarahkan otomatis ke **Section Penutup-Diskualifikasi** (lihat Bagian E) dan datanya tidak dianalisis (`INCLUDE=0` di kodebook).

| Kode | Pertanyaan (teks Forms) | Opsi jawaban | Kriteria inklusi yang diuji |
|---|---|---|---|
| S1 | Apakah Anda Warga Negara Indonesia (WNI)? | Ya / Tidak | Kewarganegaraan WNI |
| S2 | Apakah usia Anda sudah mencapai 17 tahun atau lebih? | Ya, >=17 tahun / Tidak, <17 tahun | Usia >=17 th (KTP, diskresi keuangan mandiri) |
| S3 | Apakah Anda berdomisili ATAU rutin beraktivitas/bertransaksi (kuliah, kerja, COD, turnamen/LGS) di wilayah Jakarta Barat? | Ya / Tidak | Domisili/aktivitas Jakarta Barat (D31) |
| S4 | Apakah Anda pernah membeli *booster pack* fisik resmi Pokemon TCG minimal 1 kali dalam 12 bulan terakhir? (diutamakan 6 bulan terakhir) | Ya, dalam 6 bulan terakhir / Ya, dalam 6–12 bulan terakhir / Tidak | Pembelian aktif >=1x dalam 6–12 bulan (anti *recall bias*) |

> Aturan: S4 = dua opsi "Ya..." diperlakukan sebagai LULUS (kode 1); opsi "Tidak" = GAGAL (kode 0). Rincian 6 vs 6–12 bulan dipakai untuk cek kesegaran recall, bukan untuk menggugurkan.

---

## C. Bagian 2 — Profil Responden (opsional, non-PII, Section 2)

Hanya tampil bila lolos screening. Semua bertipe pilihan ganda, **tidak wajib** kecuali Frekuensi (disarankan wajib untuk kontrol deskriptif). Tanpa nama/kontak dalam bentuk apa pun.

| Kode | Pertanyaan | Opsi |
|---|---|---|
| P1 | Jenis kelamin | Laki-laki / Perempuan |
| P2 | Kelompok usia | 17–20 / 21–25 / 26–30 / >30 tahun |
| P3 | Kecamatan aktivitas utama di Jakarta Barat | Cengkareng / Grogol Petamburan / Kalideres / Kebon Jeruk / Kembangan / Palmerah / Taman Sari / Tanjung Duren (Grogol Petamburan) / Lainnya-Jakbar |
| P4 | Frekuensi pembelian *booster pack* 6 bulan terakhir | 1x / 2–3x / 4–6x / >6x |
| P5 | Kanal pembelian utama | LGS (Tanjung Duren/Central Park/Mall Taman Anggrek/Puri Indah) / Minimarket-toko buku (Indomaret/Alfamart/Gramedia) / COD komunitas Jakbar / Marketplace daring |

---

## D. Bagian 3–7 — Butir Likert (WAJIB ISI SEMUA, skala linear 1–5)

Petunjuk umum (tampilkan di awal Section 3): *"Berilah penilaian 1 = Sangat Tidak Setuju, 2 = Tidak Setuju, 3 = Netral, 4 = Setuju, 5 = Sangat Setuju, sesuai pengalaman Anda membeli booster pack Pokemon TCG."* Tipe: **Skala linear 1–5, wajib isi, tanpa opsi kosong.** Urutan butir TETAP (jangan acak/shuffle) agar pemetaan kode Y1..M6 ke kodebook konsisten. Seluruh butir searah positif (favorabel) — skor 5 = konstruk tertinggi, tanpa reverse-scoring.

### D1. Y — Impulsive Buying (6 butir; sumber skala: IBTS Verplanken & Herabadi 2001 / Rook & Fisher 1995; dimensi Kognitif/Afektif)

| Kode | Dimensi | Teks butir (verbatim Tabel 3.2) |
|---|---|---|
| Y1 | Kognitif | Saya sering membeli *booster pack* kartu Pokemon tanpa rencana anggaran sebelumnya. |
| Y2 | Kognitif | Saya tidak mempertimbangkan dampak finansial saat membeli kartu Pokemon di toko. |
| Y3 | Afektif | Saya merasa terdorong secara spontan untuk membeli *pack* saat melihatnya di etalase toko. |
| Y4 | Afektif | Saya merasakan kegembiraan sesaat ketika memutuskan membeli kartu secara mendadak. |
| Y5 | Kognitif | Saya sering membeli *pack* lebih banyak dari yang semula saya niatkan. |
| Y6 | Afektif | Saya sulit menahan hasrat berbelanja kartu Pokemon saat rilis seri baru. |

### D2. X1 — Hedonic Motivation (5 butir; sumber skala: Arnold & Reynolds 2003; dimensi Adventure/Gratification/Social/Role/Idea — dimensi Value Shopping sengaja tidak dipakai karena harga eceran pack pasti/seragam)

| Kode | Dimensi | Teks butir (verbatim Tabel 3.2) |
|---|---|---|
| X1_1 | Adventure | Membuka kemasan *booster pack* memberikan sensasi petualangan dan kejutan mendebarkan. |
| X1_2 | Gratification | Membeli kartu Pokemon adalah cara saya menghibur diri dan meredakan stres. |
| X1_3 | Social | Berbelanja kartu Pokemon mempererat ikatan dan kebersamaan dengan sesama teman sehobi. |
| X1_4 | Role | Saya menikmati berbelanja kartu Pokemon untuk dihadiahkan atau dimainkan bersama teman dan keluarga sehobi. |
| X1_5 | Idea | Saya senang mengikuti tren rilis seri kartu Pokemon dan inovasi desain terbarunya. |

### D3. X2 — Desire for Completeness (5 butir; sumber skala: Gao, Huang, & Simonson 2014; Barasz et al. 2017; Belk 1995 — efek Zeigarnik)

| Kode | Dimensi | Teks butir (verbatim Tabel 3.2) |
|---|---|---|
| X2_1 | Cognitive Tension | Saya merasa tidak nyaman ketika album koleksi kartu Pokemon saya memiliki celah (*slot*) kosong. |
| X2_2 | Drive for Closure | Hasrat melengkapi seluruh seri kartu dalam album *binder* mendorong saya untuk terus menambah koleksi. |
| X2_3 | Cognitive Tension | Mengetahui ada kartu yang belum saya miliki dalam suatu seri membuat saya ingin segera membelinya. |
| X2_4 | Wholeness | Melengkapi satu set penuh kartu Pokemon memberikan perasaan pencapaian dan kepuasan batin. |
| X2_5 | Drive for Closure | Semakin sedikit kartu yang kurang dalam satu seri, semakin kuat desakan psikologis saya untuk menuntaskannya. |

### D4. X3 — Speculative Motive (5 butir; sumber skala: motif spekulasi Shiller/Keynes; Baur et al.; Colline 2024 — konteks apresiasi harga pasar sekunder & grading)

| Kode | Dimensi | Teks butir (verbatim Tabel 3.2) |
|---|---|---|
| X3_1 | Apresiasi Modal | Saya membeli kartu dengan ekspektasi menarik kartu langka bernilai jual tinggi. |
| X3_2 | Likuiditas | Saya yakin kartu Pokemon langka memiliki likuiditas tinggi sehingga mudah dan cepat dijual kembali menjadi uang tunai di pasar sekunder. |
| X3_3 | Tren Nilai | Saya memandang kartu Pokemon langka sebagai aset alternatif yang nilainya dapat naik di masa depan. |
| X3_4 | Potensi Nilai | Saya memandang biaya pembelian kartu sebanding dengan potensi apresiasi keuntungan di pasar sekunder. |
| X3_5 | Grading Value | Saya tertarik dengan sertifikasi kondisi fisik dan keaslian (*grading*) kartu demi menaikkan nilai jual lelang di pasar sekunder. |

### D5. M — Self-Control / Kontrol Diri, variabel moderasi (6 butir; sumber skala: BSCS Tangney, Baumeister, & Boone 2004; Thaler & Shefrin; Vohs & Faber)

| Kode | Dimensi | Teks butir (verbatim Tabel 3.2) |
|---|---|---|
| M1 | Tahan Godaan | Saya mampu menolak godaan berbelanja jika barang tersebut berada di luar rencana anggaran saya. |
| M2 | Non-Impulsif | Saya terbiasa berpikir tenang dan mempertimbangkan konsekuensi keuangan sebelum memutuskan bertransaksi. |
| M3 | Tunda Kepuasan | Saya mampu menahan diri dari kesenangan belanja saat ini demi menjaga stabilitas keuangan masa depan. |
| M4 | Disiplin Diri | Saya memiliki pengendalian diri yang kokoh untuk menahan dorongan membeli barang secara spontan saat melihat barang menarik. |
| M5 | Kontrol Emosi | Saya tidak mudah terhanyut oleh emosi sesaat dalam membelanjakan uang pribadi. |
| M6 | Taat Anggaran | Saya secara konsisten mematuhi alokasi batas anggaran pengeluaran hobi yang telah saya tetapkan. |

---

## E. Section Penutup (2 jalur logic)

1. **Penutup-LULUS** (tampil bila S1–S4 semua "Ya"): *"Terima kasih! Jawaban Anda tercatat dan sangat berarti bagi penelitian ini."*
2. **Penutup-DISKUALIFIKASI** (tampil bila ada "Tidak"): *"Terima kasih atas kesediaan Anda. Mohon maaf, survei ini khusus untuk responden yang memenuhi kriteria (WNI, >=17 th, aktif di Jakarta Barat, membeli pack 12 bulan terakhir), sehingga kuesioner Anda cukup sampai di sini."*

---

## F. Catatan Setting Google Forms (wajib diterapkan)

1. **Wajib isi:** S1–S4 dan seluruh 27 butir Likert set "Required = ON"; profil P1–P5 opsional (kecuali P4 disarankan wajib).
2. **Validasi:** semua Likert memakai tipe "Skala linear" min 1 label "Sangat Tidak Setuju", maks 5 label "Sangat Setuju"; tidak ada validasi angka bebas agar tidak ada input liar.
3. **Section logic (Go to section based on answer):** setiap opsi "Tidak" pada S1/S2/S3/S4 → lompat ke Section Penutup-DISKUALIFIKASI (Submit); opsi "Ya" → lanjut ke section berikutnya. Aktifkan "Show progress bar".
4. ** Satu respons per orang:** aktifkan "Limit to 1 response" (butuh login Google) ATAU, bila sebar via LGS luring khawatir hambatan login, matikan limit tetapi aktifkan "Collect email addresses = OFF" + cek duplikasi manual via pola P1–P5 di tabulasi. PII tetap minimal (tanpa nama/HP).
5. **Urutan & anti-bias:** matikan "Shuffle question order" (urutan Y1..M6 tetap sesuai kodebook); pisahkan tiap konstruk dalam section berbeda (Y, X1, X2, X3, M) dengan judul section jelas.
6. **Uji coba tautan:** sebelum pilot N=30, kirim *preview link* ke 2–3 kolektor untuk cek redaksi, waktu isi, dan logic lompatan; catat revisi (bila ada) di log, bukan di naskah proposal.
7. **Ekspor:** respons diunduh sebagai CSV/Excel lalu ditabulasi ulang mengikuti `02_Data_Mentah_Survei_Excel/KODEBOOK_DAN_TEMPLATE_TABULASI.md` (nama kolom persis Y1..M6, S1..S4, INCLUDE).

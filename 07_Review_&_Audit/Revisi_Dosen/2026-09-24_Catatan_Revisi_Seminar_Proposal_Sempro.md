> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Mendokumentasikan secara komprehensif seluruh arahan revisi dari dosen penguji pada Seminar Proposal (Sempro) tanggal 24 September 2026.
> - **Masalah yang Diselesaikan:** Menghilangkan risiko lupa konteks bimbingan pasca-sempro; memetakan 4 butir masukan penguji ke dalam analisis akar masalah (*root cause*), justifikasi ilmiah, dan rencana aksi konkret (*action plan*).
> - **Keputusan/Output:** Rujukan resmi penyusunan revisi proposal skripsi Arthur Reezan sebelum bimbingan pasca-sempro ke [[Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A]].

# 🎓 Catatan Revisi Seminar Proposal (Sempro) — 24 September 2026
### *Naskah Proposal Tugas Akhir S1 Manajemen Keuangan FEB UKRIDA*
**Mahasiswa:** Arthur Reezan (NIM: 312023002)  
**Dosen Pembimbing:** [[Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A]]  
**Status Naskah:** Proposal Selesai Diseminarkan; Memasuki Tahap Perbaikan Pasca-Sempro

---

## 📋 1. Ringkasan Matriks Revisi Dosen Penguji

| No | Butir Arahan Dosen Penguji | Status Eksekusi | Prioritas & Area File |
|:---:|:---|:---:|:---|
| **1** | **Bentuk Model Rerangka Konseptual Wajib Elips:** Bentuk kotak pada Gambar 2.1 harus diubah menjadi elips karena melambangkan konstruk laten teoretis. | **SELESAI (100% PASS)** | Master TeX, Gambar PNG, DOCX, MD |
| **2** | **Rasio Kemutakhiran Jurnal 80/20:** Jurnal tua di atas 10 tahun harus dikurangi drastis; proporsi wajib 80% jurnal baru ($\le 10$ tahun, idealnya $\le 5$ tahun ke belakang), 20% boleh literatur tua jika sangat fundamental/seminal. | **DICATAT (Perencanaan)** | Bab 1, Bab 2, [[01_Naskah_Utama/references.bib\|references.bib]] |
| **3** | **Narasi Alur Hubungan $X \rightarrow Y \rightarrow Z$ di Bab 1:** Alur logika antar-variabel kurang dijelaskan secara naratif mengalir; saat ini terkesan hanya berbentuk tabel sehingga membingungkan pembaca yang awam Pokémon. **Tabel 1.1 jangan dihapus (sudah baik)**, tetapi perlu narasi penghubung yang mudah dipahami. | **DICATAT (Perencanaan)** | Bab 1 (Latar Belakang & Research Gap) |
| **4** | **Eliminasi Istilah/Bahasa "Grand Theory":** Ditegur penguji bahwa pelabelan kaku *Grand Theory* sudah tidak relevan dan terlalu tua untuk konteks skripsi ini; bahasa tersebut perlu dihilangkan atau disesuaikan. | **DICATAT (Perencanaan)** | Bab 2 (§2.1.1 Landasan Teori) |

---

## 🔬 2. Bedah Analisis & Rencana Aksi Per Butir

### 📌 Butir 1: Model Rerangka Konseptual Berbentuk Elips
* **Status:** **Tuntas Dikerjakan pada Sesi 30.**
* **Dasar Metodologi:**
  - Konvensi pemodelan diagram jalur & SEM (*Bollen, 1989; Kline, 2015; Hair et al., 2010/2021*):
    * **Kotak (*Rectangle*):** Khusus variabel manifes / data observasi langsung (*observed variables*).
    * **Elips (*Ellipse*):** Khusus konstruk laten teoretis (*unobserved/latent variables*) yang diukur multi-item.
* **Hasil Eksekusi:**
  - Node TikZ di [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex]] diubah ke `ellipse`.
  - Berkas resolusi tinggi 300 DPI disimpan di [[01_Naskah_Utama/images/gambar_rerangka_penelitian.png]] dan disinkronkan ke aset slide sempro.
  - Kompilasi PDF dan DOCX lulus uji gerbang paritas 7/7 PASS.

---

### 📌 Butir 2: Rasio Kemutakhiran Pustaka 80/20 (Maksimal 10 Tahun, Prioritas $\le 5$ Tahun)
* **Inti Arahan Penguji:**
  - Referensi jurnal tua ($>10$ tahun) dikurangi secara signifikan.
  - Komposisi rujukan:
    * **80% Literatur Mutakhir:** Terbit dalam rentang 10 tahun terakhir (2016–2026), dengan bobot terbesar pada 5 tahun terakhir (2021–2026).
    * **Maksimal 20% Literatur Klasik/Seminal:** Hanya diperbolehkan untuk buku metodologi standar atau paper penemu teori awal yang benar-benar tidak dapat digantikan (*irreplaceable*).
* **Audit Awal Bibliografi Saat Ini (54 Referensi):**
  - Literatur seminal yang **wajib dipertahankan (kuota 20%)**:
    1. Rook (1987) — Pencetus teori *Impulsive Buying*.
    2. Babin, Darden, & Griffin (1994) — Pencetus instrumen *Hedonic Shopping Value*.
    3. Barasz et al. (2017) — Teori *Pseudo-Set Framing* ($X_2$).
    4. Tangney et al. (2004) — Skala *Brief Self-Control Scale* ($M$).
    5. Verplanken & Herabadi (2001) — Skala IBTS ($Y$).
    6. Aiken & West (1991) — Rujukan baku metode MRA & *mean-centering*.
    7. Cohen (1988) & Green (1991) — Kaidah baku *statistical power* penentuan ukuran sampel.
    8. Sugiyono (2019) / Ghozali (2018) / Hair et al. (2019) — Buku teks metode penelitian.
  - Literatur tua yang **dapat di-upgrade ke jurnal empiris 2018–2026**:
    - Kutipan artikel pendukung era 1970–2010 yang bukan penemu teori utama (misalnya studi pendukung lama yang membahas hedonis ritel umum atau spekulasi saham klasik) akan diganti dengan jurnal empiris terbaru terindeks SINTA/Scopus (2020–2025) yang membahas perilaku belanja impulsif, barang hobi, *blind-box*, atau aset digital/koleksi.
* **Rencana Implementasi:**
  - Lakukan inventarisasi tahun terbit dari 54 referensi di [[01_Naskah_Utama/references.bib]].
  - Identifikasi artikel berusia $>10$ tahun yang sifatnya hanya mengonfirmasi temuan (bukan skala baku).
  - Lakukan substitusi presisi 1-ke-1 dengan jurnal 2021–2025 tanpa mengganggu sitasi in-text dan tetap menjaga paritas 1:1 Mendeley.

---

### 📌 Butir 3: Narasi Alur Hubungan $X \rightarrow Y \rightarrow Z$ di Bab 1 bagi Orang Awam
* **Inti Arahan Penguji:**
  - Tabel 1.1 (Matriks Research Gap) dinilai **sudah sangat baik dan jangan dihapus**.
  - Namun, alur cerita (*storytelling*) latar belakang sebelum masuk ke tabel terasa melompat. Penguji yang tidak mengikuti kultur Pokémon TCG kesulitan menangkap logika psikologis mengapa variabel-variabel tersebut saling berkaitan.
* **Akar Masalah Narasi:**
  - Penjelasan fenomena di Bab 1 saat ini sangat padat data pasar makro (Statista $100B, produksi 64,8 Miliar kartu, disparitas PSA 10), lalu langsung menyajikan Tabel 1.1 gap antarpeneliti.
  - Hilang benang merah naratif yang menjelaskan **pengalaman psikologis konsumen (*the human journey*)**:
* **Konsep Alur Cerita Awam yang Akan Ditambahkan (Jembatan Narasi):**
  1. **Langkah 1 (Sensasi Hobi - $X_1$ *Hedonic Motivation*):** Konsumen membeli *booster pack* seharga Rp20.000 bukan sekadar membeli kertas bergambar, melainkan membeli sensasi kejutan (*unboxing thrill*) dan luapan dopamin saat merobek kemasan foil acak.
  2. **Langkah 2 (Obsesi Menuntaskan Binder - $X_2$ *Desire for Completeness*):** Setiap kartu memiliki nomor urut seri (misal No. 001 s.d. 150). Ketika dimasukkan ke dalam album/binder koleksi dan terdapat 2–3 slot kosong, timbul ketegangan kognitif (*Zeigarnik effect*) yang membuat kolektor tidak tahan melihat koleksinya belum lengkap. Dorongan melengkapi ini memicu hasrat membeli kemasan baru lagi.
  3. **Langkah 3 (Godaan Keuntungan Spekulatif - $X_3$ *Speculative Motive*):** Di pasar sekunder, kartu bergambar langka (*Secret Rare*) yang berkondisi sempurna dan disertifikasi *grading* PSA 10 harganya melonjak drastis hingga puluhan kali lipat (mencapai jutaan rupiah). Fenomena ini menciptakan ilusi optimisme bahwa dengan modal sebungkus Rp20.000, pembeli berpeluang mendapatkan "harta karun" bernilai fantastis.
  4. **Langkah 4 (Bermuara ke Perilaku - $Y$ *Impulsive Buying*):** Ketika ketiga dorongan ini hadir bersamaan saat konsumen berdiri di depan rak kasir minimarket, pertimbangan rasional lumpuh. Terjadilah keputusan belanja seketika tanpa perencanaan (*impulsive buying*).
  5. **Langkah 5 (Peran Rem Volisional - $Z / M$ *Self-Control*):** Di sinilah kontrol diri memainkan peran krusial. Konsumen dengan regulasi diri yang kuat mampu mengabaikan godaan visual kemasan dan menahan dorongan emosional belanja spontan; sebaliknya ketika kontrol diri lemah, dorongan hedonis, obsesi kelengkapan, dan spekulasi akan meledak menjadi transaksi berulang tanpa kendali.
* **Rencana Implementasi:**
  - Sisipkan 2–3 paragraf narasi mengalir yang membumi dan elegan tepat sebelum pemaparan Tabel 1.1 di Subbab 1.1 Latar Belakang.

---

### 📌 Butir 4: Eliminasi Bahasa / Pelabelan Kaku "Grand Theory"
* **Inti Arahan Penguji:**
  - Pelabelan formal "Grand Theory: Keuangan Perilaku (*Behavioral Finance*)" di Bab 2 dinilai tidak relevan, kaku, dan terlalu usang untuk riset skripsi S1 terapan.
* **Akar Masalah:**
  - Tradisi membagi teori secara hierarkis kaku (*Grand Theory* $\rightarrow$ *Middle Range Theory* $\rightarrow$ *Applied Theory*) sering dianggap dosen penguji sebagai formalitas teoretis yang memaksakan teori-teori makro abad lalu ke dalam fenomena mikro kontemporer.
* **Rencana Perbaikan:**
  - Ubah judul subbab di Bab 2 (§2.1.1) dari:
    - *Lama:* `2.1.1 Grand Theory: Keuangan Perilaku (Behavioral Finance)`
    - *Baru:* `2.1.1 Landasan Teoretis: Pendekatan Keuangan Perilaku (Behavioral Finance)` atau `2.1.1 Teori Perilaku Konsumen dan Keuangan Perilaku`
  - Hapus penyebutan istilah kata "Grand Theory" pada teks pengantar narasi Bab 2, dan ganti dengan frasa yang lebih mengalir seperti: *"Penelitian ini berpijak pada kerangka pendekatan keuangan perilaku (behavioral finance) dan teori stimulus-respons..."*.
  - Hilangkan label "Supporting Theory" pada subbab 2.1.2–2.1.4, cukup sebutkan nama teorinya secara proporsional.

---

## 🛠️ 3. Roadmap Eksekusi Selanjutnya (Sesuai Permintaan Pengguna)

Sesuai instruksi pengguna, butir 2, 3, dan 4 saat ini **disimpan dan dibekukan sebagai catatan Second Brain**.  
Ketika pengguna siap melakukan eksekusi penulisan, urutan kerja yang akan dijalankan adalah:

1. **Fase 1 (Bab 2):** Penyesuaian judul subbab teori & pembersihan frasa "Grand Theory" di Bab 2 (pekerjaan paling cepat, zero risk).
2. **Fase 2 (Bab 1):** Penulisan 2–3 paragraf narasi alur $X \rightarrow Y \rightarrow Z$ yang awam-friendly sebelum Tabel 1.1.
3. **Fase 3 (Bibliografi):** Audit proporsi tahun terbit 54 referensi, pemetaan artikel pengganti $\le 5$ tahun, dan penataan ulang berkas BibTeX/RIS.
4. **Fase 4 (Kompilasi & Paritas):** Rebuild DOCX + compile TeX PDF + verifikasi 7/7 gerbang paritas.

---
*Catatan ini resmi tercatat di Obsidian Second Brain Repositori Skripsi Arthur Reezan.* 🎯

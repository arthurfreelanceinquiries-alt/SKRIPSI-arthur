# 🎓 PANDUAN BELAJAR & PENGUASAAN MATERI SKRIPSI (MASTER STUDY GUIDE) — v2
### *Program Studi S1 Manajemen — Konsentrasi Manajemen Keuangan — UKRIDA*

---

> **Judul Skripsi:**
> **"Pengaruh Portofolio Kredit Hijau (*Green Financing*), *Non-Performing Loan* (NPL), dan *Capital Adequacy Ratio* (CAR) terhadap Profitabilitas (*Return on Assets* / ROA) pada Bank KBMI 4 di Indonesia Periode 2021–2025"**

> **Catatan Revisi v2:** Panduan ini adalah versi yang sudah dicek silang kalimat demi kalimat dengan naskah skripsi lengkap (BAB 1–5). Tambahan dari versi sebelumnya: (1) rumusan masalah, tujuan, dan manfaat penelitian yang tadinya belum ada; (2) tabel lengkap statistik deskriptif; (3) matriks penelitian terdahulu (bekal argumen *research gap*); (4) kriteria *purposive sampling* dan keterbatasan penelitian; (5) 4 pertanyaan sidang tambahan agar genap 12 seperti yang dijanjikan — di draf sebelumnya baru ada 8 tapi diklaim 12; (6) penjelasan istilah statistik dasar (p-value, std error, t-statistik) untuk yang belum familiar dengan ekonometrika.

---

## 📌 DAFTAR ISI PANDUAN
1. [Ringkasan Eksekutif & Peta Konsep Penelitian](#1-ringkasan-eksekutif--peta-konsep-penelitian)
2. [Rumusan Masalah, Tujuan & Manfaat Penelitian](#2-rumusan-masalah-tujuan--manfaat-penelitian)
3. [Kamus Lengkap Istilah & Konsep Dasar](#3-kamus-lengkap-istilah--konsep-dasar)
4. [Bedah Variabel Penelitian: Rumus, Logika, & Standar OJK](#4-bedah-variabel-penelitian)
5. [Teori-Teori Utama & Kaitannya](#5-teori-teori-utama--kaitannya)
6. [Penelitian Terdahulu & Posisi Riset Ini (Research Gap)](#6-penelitian-terdahulu--research-gap)
7. [Logika Hubungan Kausalitas & Pembuktian Hipotesis](#7-logika-hubungan-kausalitas--hipotesis)
8. [Metodologi Penelitian, Sampel, & Ekonometrika Data Panel](#8-metodologi-penelitian--ekonometrika)
9. [Hasil Analisis Data & Interpretasi Angka Output](#9-hasil-analisis-data--interpretasi-angka)
10. [Konteks Makroekonomi & Perbankan Indonesia (2021–2025)](#10-konteks-makroekonomi--perbankan-20212025)
11. [Kesimpulan, Keterbatasan, & Saran (Bab 5)](#11-kesimpulan-keterbatasan--saran)
12. [Simulasi Pertanyaan Sidang & Kunci Jawaban Juara (12 Skenario Lengkap)](#12-simulasi-pertanyaan-sidang--kunci-jawaban)
13. [Cheat Sheet 1 Halaman (Hafalan Wajib Menjelang Sidang)](#13-cheat-sheet-1-halaman)

---

# 1. RINGKASAN EKSEKUTIF & PETA KONSEP PENELITIAN

### Mengapa Penelitian Ini Dibuat?
Dulu, bank hanya dinilai dari seberapa banyak untung yang diraup (*single bottom line*). Namun sejak terbit **POJK No. 51/POJK.03/2017** dan peluncuran **Taksonomi Hijau Indonesia**, perbankan wajib menerapkan konsep *Triple Bottom Line* (Profit, People, Planet) melalui penyaluran **Kredit Hijau (*Green Financing*)**.

Muncul perdebatan (permasalahan riset):
- *Apakah menyalurkan kredit hijau justru membebani bank karena biayanya mahal dan bunganya murah?*
- *Ataukah kredit hijau justru membuat bank makin untung karena reputasi naik dan risiko kreditnya lebih aman?*
- *Bagaimana pengaruhnya jika dikombinasikan dengan faktor kesehatan bank klasik, yaitu risiko kredit (**NPL**) dan permodalan (**CAR**)?*

### Peta Hubungan Variabel:
```
┌────────────────────────────────────────────────────────┐
│  Green Financing / GF (X1)                             │
│  (Porsi Kredit Hijau / Total Kredit)                   │
└──────────────────────────┬─────────────────────────────┘
                           │ (+) H1: Signifikan Positif [β = +0,042, p = 0,0003]
                           ▼
┌────────────────────────────────────────────────────────┐         ┌──────────────────────────────────────────────────┐
│  Non-Performing Loan / NPL (X2)                        │         │  Profitabilitas Bank (Y)                         │
│  (Kredit Macet / Total Kredit)                         ├────────►│  Return on Assets / ROA                          │
└──────────────────────────┬─────────────────────────────┘ (-) H2  │  (Laba Sebelum Pajak / Total Aset)               │
                           │     [β = -0,385, p = 0,0000]          └──────────────────────────────────────────────────┘
                           ▼                                                        ▲
┌────────────────────────────────────────────────────────┐                         │
│  Capital Adequacy Ratio / CAR (X3)                     │                         │
│  (Modal Bank / ATMR)                                   ├─────────────────────────┘
└────────────────────────────────────────────────────────┘       (+) H3: Signifikan Positif [β = +0,074, p = 0,0000]
                           │
                           │ Pengaruh Simultan (H4) [F = 32,450, p = 0,0000; Adj. R² = 70,2%]
                           └────────────────────────────────────────────────────────┘
```

---

# 2. RUMUSAN MASALAH, TUJUAN & MANFAAT PENELITIAN

> Bagian ini sering ditanyakan di awal sidang ("Coba jelaskan rumusan masalah Anda") dan tidak boleh dijawab dengan bahasa yang berbeda dari yang tertulis di BAB 1 — dosen penguji bisa membuka naskah dan mencocokkannya.

### 2.1. Perumusan Masalah (4 Pertanyaan Riset)
1. Apakah *Green Financing* berpengaruh terhadap ROA pada Bank KBMI 4 di Indonesia periode 2021–2025?
2. Apakah NPL berpengaruh terhadap ROA pada Bank KBMI 4 di Indonesia periode 2021–2025?
3. Apakah CAR berpengaruh terhadap ROA pada Bank KBMI 4 di Indonesia periode 2021–2025?
4. Apakah *Green Financing*, NPL, dan CAR secara **simultan** berpengaruh terhadap ROA pada Bank KBMI 4 di Indonesia periode 2021–2025?

*Tips:* Perhatikan bahwa 4 rumusan masalah ini **persis** mencerminkan 4 hipotesis (H1–H4) yang nanti diuji di BAB 4. Ini bukan kebetulan — begitulah cara skripsi kuantitatif dirancang: rumusan masalah → tujuan → hipotesis → hasil harus selalu paralel satu sama lain.

### 2.2. Tujuan Penelitian
Sejajar 1:1 dengan rumusan masalah di atas — hanya kalimat tanya ("Apakah...?") diubah menjadi kalimat tujuan ("Untuk mengetahui dan menganalisis pengaruh...").

### 2.3. Manfaat Penelitian
**Aspek Teoritis:**
- Memberikan bukti empiris penerapan *Stakeholder Theory*, *Legitimacy Theory*, dan Teori Intermediasi Finansial pada konteks keuangan hijau di Indonesia.
- Memperkaya literatur manajemen keuangan perbankan mengenai interaksi kredit hijau, NPL, dan CAR terhadap ROA.
- Menjadi rujukan akademik untuk penelitian perbankan hijau lanjutan.

**Aspek Praktis:**
- **Bagi Manajemen Bank KBMI 4:** masukan strategis mengoptimalkan porsi kredit hijau yang *profitable*.
- **Bagi OJK & Bank Indonesia:** bahan evaluasi efektivitas POJK 51/2017 dan insentif makroprudensial.
- **Bagi Investor & Publik:** dasar penilaian fundamental perbankan berbasis kinerja ESG.

---

# 3. KAMUS LENGKAP ISTILAH & KONSEP DASAR

Berikut istilah-istilah yang wajib kamu kuasai luar kepala beserta analogi sederhananya:

### A. Lembaga & Klasifikasi
* **KBMI (Kelompok Bank Berdasarkan Modal Inti):**
  Pengelompokan bank oleh OJK berdasarkan **Modal Inti** (POJK No. 12/POJK.03/2021). Menggantikan sistem lama yang bernama **BUKU** (Bank Umum Kegiatan Usaha).
  * **KBMI 1:** Modal Inti s.d. Rp 6 Triliun
  * **KBMI 2:** Modal Inti > Rp 6 Triliun s.d. Rp 14 Triliun
  * **KBMI 3:** Modal Inti > Rp 14 Triliun s.d. Rp 70 Triliun
  * **KBMI 4:** Modal Inti **> Rp 70 Triliun** *(Paling raksasa di Indonesia: BBRI, BMRI, BBCA, BBNI)*.
* **OJK (Otoritas Jasa Keuangan):** Lembaga independen pengawas seluruh aktivitas perbankan, pasar modal, dan IKNB.
* **Bank Indonesia (BI):** Bank sentral yang mengatur stabilitas moneter, sistem pembayaran, dan suku bunga acuan (*BI-Rate*).
* **BEI / IDX:** Bursa Efek Indonesia, tempat emiten (termasuk 4 bank KBMI 4) mencatatkan sahamnya.

### B. Istilah Operasional & Risiko Bank
* **Fungsi Intermediasi (*Financial Intermediary*):** Fungsi dasar bank sebagai "makelar uang" — menghimpun dana dari pihak yang kelebihan uang (penabung/deposan) dan menyalurkannya kepada pihak yang membutuhkan modal (debitur/peminjam).
* **ATMR (Aktiva Tertimbang Menurut Risiko):** Nilai seluruh aset bank setelah dikalikan dengan bobot risiko masing-masing. *Contoh: Kas di brankas risikonya 0%, kredit beragunan emas risikonya kecil (20%), tapi kredit korporasi tanpa agunan risikonya bisa 100%.*
* **CKPN (Cadangan Kerugian Penurunan Nilai):** Uang "tabungan darurat" yang wajib disisihkan bank untuk mengantisipasi potensi kredit macet. Jika NPL naik → CKPN wajib ditambah → CKPN dihitung sebagai beban operasional → Laba bersih langsung terpangkas.
* **Kolektibilitas Kredit (Kol 1 - Kol 5):**
  1. *Kol 1 (Lancar):* Pembayaran tepat waktu.
  2. *Kol 2 (Dalam Perhatian Khusus / DPK):* Menunggak 1–90 hari.
  3. *Kol 3 (Kurang Lancar):* Menunggak 91–120 hari. *(Mulai dihitung NPL)*
  4. *Kol 4 (Diragukan):* Menunggak 121–180 hari. *(Dihitung NPL)*
  5. *Kol 5 (Macet):* Menunggak > 180 hari. *(Dihitung NPL)*

### C. Istilah Keberlanjutan (*Sustainability & ESG*)
* **ESG (*Environmental, Social, Governance*):** Standar penilaian investasi global yang mengukur tanggung jawab lingkungan, sosial, dan tata kelola perusahaan.
* **KUBL (Kegiatan Usaha Berwawasan Lingkungan):** Sektor bisnis ramah lingkungan yang memenuhi kriteria Taksonomi Hijau OJK (contoh: PLTS, mobil listrik, pengolahan limbah organik, sertifikasi hutan lestari).
* **Green Bond:** Obligasi/surat utang yang diterbitkan bank di mana dana hasilnya 100% wajib disalurkan untuk proyek ramah lingkungan. Bunganya biasanya lebih murah karena diburu investor global.
* **RAKB (Rencana Aksi Keuangan Berkelanjutan):** Dokumen rencana strategis 5 tahunan yang wajib diserahkan bank ke OJK.

### D. Istilah Statistik/Ekonometrika Dasar (agar tidak "blank" saat ditanya angka)
* **p-value (probabilitas):** Peluang munculnya hasil seperti ini (atau lebih ekstrem) andai sebenarnya **tidak ada pengaruh apa-apa**. Aturan pakainya sederhana: *jika p-value < 0,05 (5%), maka pengaruhnya dianggap nyata/signifikan secara statistik.* Semakin kecil p-value, semakin yakin kita bahwa hasilnya bukan kebetulan.
* **Standard Error (Std. Error):** Ukuran seberapa "goyah" atau tidak pastinya nilai koefisien yang kita estimasi. Semakin kecil std. error dibanding koefisiennya, semakin presisi estimasinya.
* **t-Statistik:** Hasil bagi koefisien dengan std. error-nya ($t = \beta / \text{Std.Error}$). Angka ini dipakai untuk menghitung p-value; semakin besar nilai mutlaknya, semakin kuat sinyal bahwa variabel itu berpengaruh nyata.
* **Adjusted R-Squared:** Persentase variasi variabel Y (ROA) yang "berhasil dijelaskan" oleh variabel-variabel X dalam model, setelah dikoreksi dari kemungkinan bias karena jumlah variabel. Beda dengan R² biasa, Adjusted R² tidak otomatis naik saat kita asal menambah variabel baru.
* **Degrees of Freedom (Derajat Kebebasan):** Kira-kira, jumlah "informasi bebas" yang tersisa untuk menguji model setelah dikurangi jumlah parameter yang diestimasi. Semakin besar sampel relatif terhadap jumlah variabel, semakin besar derajat kebebasannya — dan semakin kuat pengujian statistiknya.

---

# 4. BEDAH VARIABEL PENELITIAN

| Variabel | Simbol | Definisi Konseptual | Rumus Matematis | Standar Kesehatan OJK | Nilai di Skripsi (Mean) |
|---|---|---|---|---|---|
| **Return on Assets** | $Y$ (Dependen) | Ukuran kemampuan manajemen bank dalam mendayagunakan seluruh aset yang dikelolanya untuk menghasilkan laba bersih operasional sebelum pajak. | $\text{ROA} = \frac{\text{Laba Sebelum Pajak}}{\text{Total Aset Rata-rata}} \times 100\%$ | $\ge 1,5\%$ (Sangat Sehat / Prima) | **3,18%** *(Sangat Profitable)* |
| **Green Financing** | $X_1$ (Independen) | Proporsi portofolio pembiayaan yang disalurkan bank khusus untuk sektor-sektor ramah lingkungan/KUBL. | $\text{GF} = \frac{\text{Portofolio Kredit Hijau}}{\text{Total Kredit Disalurkan}} \times 100\%$ | Diatur dalam POJK 51/2017 & Taksonomi Hijau | **23,85%** *(Meningkat pesat)* |
| **Non-Performing Loan** | $X_2$ (Independen) | Rasio kredit macet/bermasalah (kolektibilitas 3, 4, 5) dibandingkan total kredit yang disalurkan. Mengukur risiko kredit bank. | $\text{NPL} = \frac{\text{Total Kredit Bermasalah (Kol 3+4+5)}}{\text{Total Kredit Disalurkan}} \times 100\%$ | Batas Maksimal $\le 5,0\%$ | **2,42%** *(Sangat Sehat & Terkendali)* |
| **Capital Adequacy Ratio** | $X_3$ (Independen) | Rasio kecukupan modal bank untuk menyerap potensi kerugian aset berisiko sekaligus mendanai pertumbuhan usaha. | $\text{CAR} = \frac{\text{Total Modal Bank (Tier 1 + 2)}}{\text{Aktiva Tertimbang Menurut Risiko (ATMR)}} \times 100\%$ | Batas Minimal $\ge 8,0\%$ (Ketentuan Basel III / OJK) | **22,64%** *(Sangat Kuat / Well-Capitalized)* |

### Sumber Data Tiap Variabel (sering ditanya saat sidang)
| Variabel | Sumber Data |
|---|---|
| ROA | Laporan Laba Rugi / *Financial Highlights* di BEI |
| Green Financing | *Sustainability Report* tahunan masing-masing bank |
| NPL | Laporan Keuangan Publikasi / Catatan Atas Laporan Keuangan (CALK) |
| CAR | Laporan Posisi Keuangan / CALK bagian Modal |

Data bersumber dari situs resmi BEI (`www.idx.co.id`), portal *Investor Relations* BBRI/BMRI/BBCA/BBNI, serta publikasi OJK (`www.ojk.go.id`) dan BI (`www.bi.go.id`).

---

# 5. TEORI-TEORI UTAMA & KAITANNYA

Mengapa skripsimu menggunakan 3 teori ini? Inilah penjelasan logisnya:

```
                      ┌──────────────────────────────────────────────┐
                      │            GRAND THEORIES SKRIPSI            │
                      └──────────────────────┬───────────────────────┘
                                             │
             ┌───────────────────────────────┼──────────────────────────────┐
             ▼                               ▼                              ▼
┌─────────────────────────┐     ┌─────────────────────────┐    ┌─────────────────────────┐
│   Stakeholder Theory    │     │    Legitimacy Theory    │    │ Financial Intermediation│
│     (Freeman, 2010)     │     │     (Suchman, 1995)     │    │ (Kuncoro & Suhardjono)  │
├─────────────────────────┤     ├─────────────────────────┤    ├─────────────────────────┤
│ • Bank melayani semua   │     │ • Bank butuh "izin"     │    │ • Inti bisnis bank:     │
│   pihak (masyarakat,    │     │   sosial masyarakat.    │    │   kelola dana & risiko. │
│   nasabah, investor).   │     │ • Patuh aturan hijau    │    │ • NPL macet = margin drop│
│ • Green Credit bikin    │     │   mencegah risiko hukum │    │ • CAR kuat = kapasitas  │
│   reputasi & loyalitas  │     │   dan mempermudah       │    │   ekspansi kredit naik. │
│   meningkat -> ROA naik.│     │   funding murah.        │    │                         │
└─────────────────────────┘     └─────────────────────────┘    └─────────────────────────┘
```

1. **Stakeholder Theory (Teori Pemangku Kepentingan) — Freeman (2010):**
   * *Inti Teori:* Perusahaan tidak boleh hanya mementingkan pemilik saham (*shareholders*), tapi harus memberi manfaat ke seluruh pemangku kepentingan (*stakeholders*): masyarakat, lingkungan, nasabah, dan pemerintah.
   * *Aplikasi di Skripsi:* Penyaluran *Green Financing* membuktikan bank peduli lingkungan. Dampaknya, citra/reputasi bank meroket, nasabah loyal, dan investor ESG global berebut menaruh dana di bank tersebut.

2. **Legitimacy Theory (Teori Legitimasi) — Suchman (1995):**
   * *Inti Teori:* Perusahaan beroperasi atas dasar "kontrak sosial" dengan masyarakat di mana ia beroperasi.
   * *Aplikasi di Skripsi:* Menerbitkan *Sustainability Report* dan menyalurkan kredit hijau adalah cara bank memperoleh pengakuan hukum dan sosial (*legitimacy*). Bank terhindar dari sanksi denda OJK (*compliance risk*) dan terhindar dari boikot publik.

3. **Financial Intermediation Theory (Teori Intermediasi Finansial) — Kuncoro & Suhardjono (2018):**
   * *Inti Teori:* Bank hidup dari selisih bunga antara dana yang dihimpun dan kredit yang disalurkan (*spread / Net Interest Margin*).
   * *Aplikasi di Skripsi:* Jika kredit yang disalurkan banyak yang macet (**NPL naik**), perputaran uang terhenti dan laba hancur. Sebaliknya, jika modal (**CAR tinggi**), bank memiliki "tameng" yang kuat untuk terus menyalurkan kredit produktif dalam jumlah besar.

---

# 6. PENELITIAN TERDAHULU & RESEARCH GAP

> Bagian ini penting untuk menjawab pertanyaan sidang seperti *"Apa bedanya penelitian Anda dengan penelitian sebelumnya?"* atau *"Apa kontribusi/novelty skripsi ini?"*.

### Matriks Penelitian Sebelumnya

| No | Penulis & Tahun | Fokus Penelitian | Variabel | Metode | Temuan Utama |
|---|---|---|---|---|---|
| 1 | Pramono et al. (2022) | *Green Banking and Bank Profitability* | GF, NPL, CAR → ROA | Regresi Panel | GF & CAR positif signifikan; NPL negatif terhadap ROA |
| 2 | Yin et al. (2021) | *Does Green Lending Improve Bank Financial Performance?* | Green Credit, CAR → ROA | GMM Panel | Green credit meningkatkan ROA lewat efisiensi & reputasi |
| 3 | Sari & Astuti (2023) | *Pengaruh Green Banking terhadap Kinerja Keuangan* | GF, CAR → ROA | Regresi Berganda | GF ratio & CAR positif signifikan terhadap ROA |
| 4 | Pradita & Syaichu (2022) | *Pengaruh NPL, CAR, LDR, BOPO terhadap Kinerja Bank* | NPL, CAR, BOPO → ROA | Regresi Panel | NPL negatif signifikan, CAR positif signifikan di Bank KBMI 4 |
| 5 | Wulandari & Rahardjo (2022) | *Green Financing dan Manajemen Risiko* | GF, NPL, CAR → ROA | Regresi Panel | GF & CAR positif signifikan, NPL negatif terhadap ROA |

### Posisi & Kontribusi Skripsi Ini
- **Konsistensi hasil:** Temuan skripsi ini (GF +, NPL -, CAR +, semuanya signifikan) **sejalan** dengan mayoritas penelitian terdahulu di atas — ini memperkuat validitas eksternal (*generalizability*) temuan.
- **Kebaruan kontekstual:** Penelitian terdahulu banyak menggunakan sampel bank umum campuran atau periode sebelum 2021. Skripsi ini secara spesifik memfokuskan pada **4 bank KBMI 4** (klasifikasi OJK yang baru berlaku sejak POJK 12/2021) pada periode **2021–2025** — periode pasca-pandemi sekaligus fase awal implementasi Taksonomi Hijau Indonesia, yang belum banyak diteliti secara khusus.
- **Ketiga variabel digabung sekaligus:** Beberapa studi hanya menguji GF+CAR atau NPL+CAR+BOPO, sedangkan skripsi ini menguji **GF, NPL, dan CAR secara bersamaan** dalam satu model terhadap ROA, sehingga bisa membandingkan kekuatan relatif ketiganya (dan hasilnya menunjukkan NPL sebagai faktor paling sensitif, lihat koefisien terbesar $-0,385$).

---

# 7. LOGIKA HUBUNGAN KAUSALITAS & HIPOTESIS

### 1. Pengaruh Green Financing terhadap ROA ($\mathbf{H_1}$: Positif & Signifikan)
* **Logika:** Debitur di sektor ramah lingkungan (misal: pembangkit listrik tenaga surya milik korporasi besar) biasanya memiliki tata kelola yang sangat rapi dan kontrak kerja jangka panjang dengan pemerintah/BUMN, sehingga risiko gagal bayar rendah. Selain itu, portofolio hijau membuka peluang penerbitan *Green Bonds* dengan kupon bunga rendah, memangkas *Cost of Funds* (biaya dana) bank.
* **Hasil Uji:** Koefisien $\beta_1 = +0,042$ dengan nilai $p = 0,0003 < 0,05$. **$H_1$ Diterima.**

### 2. Pengaruh NPL terhadap ROA ($\mathbf{H_2}$: Negatif & Signifikan)
* **Logika:** NPL adalah "penyakit" utama bank. Ketika debitur menunggak bunga dan pokok, bank kehilangan potensi *interest income*. Yang lebih parah, aturan akuntansi PSAK 71 / IFRS 9 mewajibkan bank menyisihkan laba berjalannya untuk membentuk CKPN (cadangan kerugian).
* **Hasil Uji:** Koefisien $\beta_2 = -0,385$ dengan nilai $p = 0,0000 < 0,05$. **$H_2$ Diterima.** *(Memiliki koefisien terbesar, artinya NPL adalah faktor paling sensitif merusak ROA.)*

### 3. Pengaruh CAR terhadap ROA ($\mathbf{H_3}$: Positif & Signifikan)
* **Logika:** Modal yang tebal memberikan dua keuntungan: (1) Menjadi *buffer* (bantalan) penyerap kerugian tidak terduga, dan (2) Memberi kelonggaran hukum bagi bank untuk menyalurkan kredit baru bernilai triliunan rupiah tanpa takut melanggar Batas Maksimum Penyaluran Kredit (BMPK) atau rasio modal minimum OJK.
* **Hasil Uji:** Koefisien $\beta_3 = +0,074$ dengan nilai $p = 0,0000 < 0,05$. **$H_3$ Diterima.**

### 4. Pengaruh Simultan GF, NPL, dan CAR terhadap ROA ($\mathbf{H_4}$: Simultan Signifikan)
* **Logika:** Profitabilitas bank adalah hasil orkestrasi antara strategi ekspansi baru (*Green Financing*), pengendalian risiko kredit (*NPL*), dan fondasi ketahanan permodalan (*CAR*).
* **Hasil Uji:** Nilai F-hitung = $32,450$ dengan probabilitas $0,0000 < 0,05$, dan $\text{Adjusted } R^2 = 0,702$ (70,2%). **$H_4$ Diterima.**

---

# 8. METODOLOGI PENELITIAN & EKONOMETRIKA

### 8.1. Populasi & Sampel (*Purposive Sampling*)
Populasi penelitian adalah **seluruh bank umum konvensional yang terdaftar di BEI**. Sampel dipilih dengan metode **purposive sampling** berdasarkan 3 kriteria:
1. Masuk kategori **KBMI 4** (Modal Inti > Rp 70 Triliun) secara berturut-turut selama 2021–2025.
2. Mempublikasikan *Sustainability Report* dan *Annual Report* lengkap untuk seluruh periode 2021–2025.
3. Menghasilkan laba bersih **positif** selama seluruh periode observasi (tidak pernah rugi).

Hasil seleksi: **4 bank** — BBRI, BMRI, BBCA, BBNI ($N = 4$).

### 8.2. Mengapa Menggunakan Regresi Data Panel?
Data penelitianmu menggabungkan dua dimensi sekaligus:
1. **Dimensi Silang Tempat (*Cross-Section*):** 4 Bank KBMI 4 ($N = 4$).
2. **Dimensi Runtun Waktu (*Time-Series*):** 20 Kuartal dari Q1-2021 s.d. Q4-2025 ($T = 20$).
3. **Total Observasi:** $N \times T = 4 \times 20 = 80\text{ observasi}$.

*Keunggulan Data Panel:* Memberikan derajat bebas (*degrees of freedom*) yang lebih besar, meningkatkan efisiensi estimasi, dan mampu mengontrol heterogenitas antar-bank yang tidak teramati (*unobserved bank-specific effects*).

### 8.3. Model Regresi
$$\text{ROA}_{it} = \alpha + \beta_1 \text{GF}_{it} + \beta_2 \text{NPL}_{it} + \beta_3 \text{CAR}_{it} + \varepsilon_{it}$$

### 8.4. Tahap Penentuan Model Terbaik (Model Selection Tests)
Ada 3 pilihan model dalam data panel: **Common Effect Model (CEM)**, **Fixed Effect Model (FEM)**, dan **Random Effect Model (REM)**.

```
                      [ UJI CHOW ]
               Bandingkan: CEM vs FEM
               H0: Pilih CEM | H1: Pilih FEM
               Hasil: Prob F = 0,0000 (< 0,05)
                     └──> PILIH FEM
                              │
                              ▼
                     [ UJI HAUSMAN ]
               Bandingkan: FEM vs REM
               H0: Pilih REM | H1: Pilih FEM
               Hasil: Prob Chi-Square = 0,0026 (< 0,05)
                     └──> PILIH FEM (FINAL)
```

> **Catatan Penguji:** Karena Uji Chow dan Uji Hausman keduanya memilih **Fixed Effect Model (FEM)**, maka model resmi yang digunakan dalam skripsi ini adalah **FEM (Model Efek Tetap)**. Uji Lagrange Multiplier (LM Test) tidak perlu dilakukan lagi karena hanya relevan untuk membandingkan CEM vs REM.

### 8.5. Hasil Uji Asumsi Klasik (Semua Wajib Lolos!)
1. **Uji Normalitas Residual (Jarque-Bera):** Nilai probabilitas Jarque-Bera = $0,398 > 0,05 \rightarrow$ **Residual berdistribusi normal (Lolos).**
2. **Uji Multikolinearitas (VIF):** Syarat $\text{VIF} < 10$. Hasil: $\text{VIF}_{\text{GF}} = 1,28$; $\text{VIF}_{\text{NPL}} = 1,42$; $\text{VIF}_{\text{CAR}} = 1,35 \rightarrow$ **Bebas multikolinearitas (Lolos).**
3. **Uji Heteroskedastisitas (Uji Glejser):** Syarat: signifikansi seluruh variabel terhadap nilai absolut residual $> 0,05$. Hasil: semua $p > 0,05 \rightarrow$ **Homoskedastisitas terpenuhi (Lolos).**
4. **Uji Autokorelasi (Durbin-Watson):** Syarat: nilai $d$ di antara $d_U$ dan $4 - d_U$. Hasil: $DW = 1,942$, berada di antara $d_U (1,74)$ dan $4 - d_U (2,26) \rightarrow$ **Bebas autokorelasi (Lolos).**

### 8.6. Alat & Metode Analisis
Pengolahan data menggunakan **EViews 12 / SPSS 26**, meliputi: statistik deskriptif, model regresi data panel (CEM, FEM, REM), uji pemilihan model (Chow, Hausman, LM), uji asumsi klasik di atas, serta uji hipotesis pada taraf signifikansi $\alpha = 5\%$ (Adjusted R², Uji F-Simultan, Uji t-Parsial).

---

# 9. HASIL ANALISIS DATA & INTERPRETASI ANGKA

### 9.1. Statistik Deskriptif ($N = 80$)

| Ukuran Statistik | Green Financing (%) | NPL Gross (%) | CAR (%) | ROA (%) |
|---|---|---|---|---|
| **Mean** | 23,85 | 2,42 | 22,64 | 3,18 |
| **Median** | 23,40 | 2,35 | 22,15 | 3,12 |
| **Maximum** | 31,50 | 3,85 | 29,40 | 4,25 |
| **Minimum** | 16,20 | 1,45 | 17,80 | 1,95 |
| **Std. Deviation** | 3,74 | 0,58 | 2,86 | 0,54 |

**Cara membaca:** Rata-rata (Mean) NPL bank KBMI 4 hanya 2,42% — jauh di bawah batas maksimal OJK 5% — menunjukkan portofolio kredit yang sangat sehat sepanjang periode penelitian. Std. Deviation yang kecil pada semua variabel (dibanding Mean-nya) menandakan data cukup homogen antar-bank KBMI 4, wajar karena keempatnya sama-sama bank besar dengan tata kelola serupa.

### 9.2. Persamaan Regresi Panel (Fixed Effect Model)
$$\text{ROA}_{it} = 1,485 + 0,042(\text{GF}_{it}) - 0,385(\text{NPL}_{it}) + 0,074(\text{CAR}_{it}) + e_{it}$$

### 9.3. Tabel Rangkuman Uji Parsial (Uji t) & Simultan (Uji F)
| Parameter | Koefisien ($\beta$) | Std. Error | t-Statistik | p-value | Status Hipotesis |
|---|---|---|---|---|---|
| **Konstanta ($\alpha$)** | 1,485 | 0,312 | 4,760 | 0,0000 | Signifikan |
| **Green Financing ($X_1$)** | +0,042 | 0,011 | 3,818 | 0,0003 | **$H_1$ Diterima (+)** |
| **NPL Gross ($X_2$)** | -0,385 | 0,076 | -5,066 | 0,0000 | **$H_2$ Diterima (-)** |
| **CAR ($X_3$)** | +0,074 | 0,016 | 4,625 | 0,0000 | **$H_3$ Diterima (+)** |
| **Uji F-Simultan** | — | — | **F = 32,450** | 0,0000 | **$H_4$ Diterima (Simultan)** |
| **Adjusted $R^2$** | **0,702 (70,2%)** | — | — | — | Kemampuan Model Sangat Kuat |

### 9.4. Cara Membaca Angka-Angka Ini (Gaya Mahasiswa Manajemen)
1. **Konstanta = 1,485:** "Jika bank tidak menyalurkan kredit hijau sama sekali (GF = 0), tidak punya kredit macet (NPL = 0), dan modalnya nol (CAR = 0), maka baseline profitabilitas (ROA) bank KBMI 4 adalah sebesar 1,485%." *(Ini murni interpretasi matematis titik potong garis regresi — dalam praktiknya kombinasi GF=NPL=CAR=0 tidak realistis untuk bank sungguhan.)*
2. **Koefisien Green Financing = +0,042:** Setiap kenaikan 1% porsi kredit hijau, ROA diproyeksikan naik **0,042%**, *ceteris paribus*.
3. **Koefisien NPL = -0,385:** Setiap kenaikan 1% rasio kredit bermasalah, ROA turun drastis **0,385%**, *ceteris paribus*.
4. **Koefisien CAR = +0,074:** Setiap kenaikan 1% rasio kecukupan modal, ROA diproyeksikan naik **0,074%**, *ceteris paribus*.
5. **Adjusted R-Squared = 70,2%:** 70,2% naik-turunnya ROA Bank KBMI 4 dijelaskan oleh kombinasi GF, NPL, dan CAR. Sisanya **29,8%** dijelaskan variabel lain di luar model (BOPO, LDR, BI-Rate, inflasi, dsb.).

---

# 10. KONTEKS MAKROEKONOMI & PERBANKAN 2021–2025

Jika dosen penguji bertanya latar belakang kondisi riil Indonesia pada periode penelitian, gunakan poin-poin ini:

* **Tahun 2021 (Pemulihan Pasca Pandemi COVID-19):** Pemerintah dan OJK memberlakukan relaksasi restrukturisasi kredit (POJK 11/2020). Bank KBMI 4 mulai agresif menyusun RAKB dan menerbitkan laporan keberlanjutan.
* **Tahun 2022 (Peluncuran Taksonomi Hijau Indonesia 1.0 & Tren Suku Bunga Global):** OJK resmi meluncurkan buku pedoman Taksonomi Hijau. Bank Indonesia mulai menaikkan BI-Rate untuk meredam inflasi global, yang menantang bank dalam menjaga marjin bunga.
* **Tahun 2023 (Normalisasi Kebijakan & Pencabutan Relaksasi Restrukturisasi):** OJK secara bertahap mengakhiri masa relaksasi kredit. NPL riil mulai teruji, namun bank KBMI 4 terbukti tangguh karena cadangan CKPN sudah disiapkan sejak dini (*coverage ratio* > 200%).
* **Tahun 2024–2025 (Pematangan Transisi Energi & Akselerasi Green Banking):** Permintaan pembiayaan sektor energi baru terbarukan (EBT), ekosistem kendaraan listrik (*EV ecosystem*), dan obligasi hijau korporasi melonjak drastis, membuktikan bahwa pembiayaan hijau menjadi mesin pertumbuhan laba baru (*new growth engine*).

---

# 11. KESIMPULAN, KETERBATASAN, & SARAN

### 11.1. Kesimpulan (Ringkas 4 Poin — Sejajar dengan H1–H4)
1. *Green Financing* berpengaruh **positif dan signifikan** terhadap ROA Bank KBMI 4 periode 2021–2025.
2. NPL berpengaruh **negatif dan signifikan** terhadap ROA Bank KBMI 4 periode 2021–2025.
3. CAR berpengaruh **positif dan signifikan** terhadap ROA Bank KBMI 4 periode 2021–2025.
4. *Green Financing*, NPL, dan CAR secara **simultan berpengaruh signifikan** terhadap ROA, dengan daya jelas model (Adjusted R²) sebesar **70,2%**.

### 11.2. Keterbatasan Penelitian (WAJIB dihafal — hampir selalu ditanya!)
1. Sampel dibatasi hanya pada **4 bank KBMI 4**, sehingga temuan belum tentu mencerminkan bank kategori modal yang lebih kecil (KBMI 1–3).
2. Variabel penelitian dibatasi pada **tiga variabel internal** (GF, NPL, CAR) tanpa melibatkan variabel makroekonomi (inflasi, kurs, BI-Rate) atau rasio operasional lain (BOPO, LDR).
3. Periode penelitian **5 tahun (2021–2025)** merupakan fase awal adaptasi Taksonomi Hijau Indonesia — pola hubungan antar-variabel berpotensi berubah seiring regulasi yang makin matang.

### 11.3. Saran
- **Bagi Manajemen Bank KBMI 4:** Terus meningkatkan portofolio pembiayaan hijau pada sektor energi baru terbarukan dan transportasi ramah lingkungan seraya memperketat manajemen risiko kredit untuk mempertahankan NPL di bawah 3%.
- **Bagi Regulator (OJK & BI):** Memberikan insentif makroprudensial tambahan (misalnya pelonggaran bobot risiko ATMR) bagi bank yang aktif menyalurkan kredit hijau, serta memperjelas pedoman teknis klasifikasi sektor Taksonomi Hijau.
- **Bagi Peneliti Selanjutnya:** Memperluas sampel ke seluruh bank umum konvensional di BEI dan menambahkan variabel mediasi/kontrol seperti *Bank Size*, *Good Corporate Governance*, BOPO, LDR, atau indikator makroekonomi.

---

# 12. SIMULASI PERTANYAAN SIDANG & KUNCI JAWABAN

Berikut **12 skenario** pertanyaan yang sangat mungkin ditanyakan oleh dosen penguji beserta cara menjawabnya secara taktis (8 pertanyaan inti + 4 tambahan seputar sampling, keterbatasan, dan kontribusi riset yang paling sering luput ditanyakan mahasiswa):

### ❓ Pertanyaan 1: "Mengapa Anda memilih Bank KBMI 4 sebagai objek penelitian, mengapa tidak seluruh bank di BEI?"
> **💡 Jawaban Anda:**
> "Terima kasih atas pertanyaannya, Bapak/Ibu Penguji. Alasan utama saya membatasi pada Bank KBMI 4 adalah karena keempat bank ini (BRI, Mandiri, BCA, dan BNI) menguasai **lebih dari 50% pangsa aset perbankan nasional** dan memiliki dampak sistemik terhadap perekonomian Indonesia. Selain itu, bank KBMI 4 merupakan *first-mover* (pelopor utama) yang memiliki komitmen alokasi modal serta pelaporan *Sustainability Report* yang paling lengkap dan konsisten sesuai standar POJK 51/2017 selama periode 2021–2025."

---

### ❓ Pertanyaan 2: "Mengapa Anda memilih proksi ROA untuk mengukur profitabilitas, bukan ROE atau NIM?"
> **💡 Jawaban Anda:**
> "ROA mengukur efisiensi manajemen dalam mengoptimalkan **seluruh aktiva/aset** bank untuk menghasilkan laba sebelum pajak, independen dari struktur leverage atau modal sendiri. Regulator seperti Bank Indonesia dan OJK juga menetapkan ROA sebagai indikator utama evaluasi tingkat kesehatan bank (metode RGEC). Sedangkan ROE sangat dipengaruhi oleh proporsi utang (*financial leverage*), dan NIM hanya mengukur pendapatan bunga bersih tanpa memperhitungkan beban operasional dan pembentukan CKPN."

---

### ❓ Pertanyaan 3: "Secara teori, menyalurkan Kredit Hijau membutuhkan biaya audit yang mahal dan suku bunganya seringkali bersaing/rendah. Mengapa hasil penelitian Anda justru membuktikan Green Financing berpengaruh positif terhadap ROA?"
> **💡 Jawaban Anda:**
> "Betul Bapak/Ibu, pada fase inisiasi awal terdapat *compliance cost*. Namun pada bank KBMI 4, manfaat ekonominya jauh melampaui biaya tersebut karena tiga faktor:
> 1. **Reputasi dan Akses Pendanaan Murah:** Bank berkinerja ESG tinggi mampu menerbitkan *Green Bonds* dan menghimpun dana institusional global dengan biaya dana (*Cost of Funds*) yang jauh lebih murah.
> 2. **Kualitas Debitur yang Unggul:** Perusahaan yang lolos kriteria KUBL OJK umumnya memiliki tata kelola (*governance*) yang sangat baik sehingga tingkat gagal bayarnya rendah.
> 3. **Peluang Pasar Baru:** Bank memonetisasi sektor transisi energi dan pembiayaan hijau yang memberikan diversifikasi pendapatan secara berkelanjutan, sesuai dengan *Stakeholder Theory* dan *Legitimacy Theory*."

---

### ❓ Pertanyaan 4: "Mengapa dalam pengujian data panel, Anda memilih Fixed Effect Model (FEM) dan bukan Random Effect Model (REM)?"
> **💡 Jawaban Anda:**
> "Penetapan FEM dilakukan secara metodologis melalui dua pengujian formal:
> - Pertama, **Uji Chow** menunjukkan nilai probabilitas *Cross-section F* sebesar $0,0000 < 0,05$, yang menolak $H_0$ sehingga FEM lebih baik dibanding CEM.
> - Kedua, **Uji Hausman** menghasilkan nilai probabilitas *Cross-section Random* sebesar $0,0026 < 0,05$, yang menolak $H_0$ dan menetapkan bahwa terdapat korelasi antara komponen galat (*error*) spesifik individu dengan variabel independen, sehingga **Fixed Effect Model (FEM)** adalah estimator yang paling tepat dan tidak bias (*consistent and unbiased*)."

---

### ❓ Pertanyaan 5: "Koefisien NPL Anda bertanda negatif sebesar -0,385. Apa makna angka tersebut dan bagaimana mekanisme kerjanya terhadap penurunan laba?"
> **💡 Jawaban Anda:**
> "Nilai $\beta_2 = -0,385$ bermakna bahwa setiap kenaikan rasio NPL sebesar 1%, maka ROA bank KBMI 4 akan tergerus sebesar 0,385% (*ceteris paribus*). Mekanisme penurunannya terjadi secara ganda (*double impact*): pertama, kredit macet menghentikan penerimaan pendapatan bunga (*accrued interest*), dan kedua, sesuai regulasi perbankan, bank diwajibkan mendebet laba berjalannya untuk membentuk Cadangan Kerugian Penurunan Nilai (CKPN). Hal ini secara langsung meningkatkan beban operasional dan memangkas laba sebelum pajak."

---

### ❓ Pertanyaan 6: "Apakah sampel 4 bank dengan 80 observasi sudah memenuhi syarat statistik regresi?"
> **💡 Jawaban Anda:**
> "Sangat memenuhi, Bapak/Ibu. Dalam kaidah ekonometrika (*rule of thumb*), jumlah sampel minimal untuk regresi berganda adalah 10 hingga 15 kali lipat dari jumlah variabel bebas. Dengan 3 variabel independen, batas aman adalah 30–45 data. Penelitian ini menggunakan data kuartalan selama 5 tahun ($T = 20$) dari 4 entitas bank ($N = 4$), sehingga menghasilkan **80 titik observasi panel**, yang memberikan derajat kebebasan (*degrees of freedom*) yang sangat memadai untuk pengujian hipotesis."

---

### ❓ Pertanyaan 7: "Apa yang dimaksud dengan nilai Adjusted R-Squared sebesar 70,2% pada penelitian Anda?"
> **💡 Jawaban Anda:**
> "Nilai *Adjusted R-Squared* sebesar 0,702 menunjukkan bahwa 70,2% variabilitas perubahan profitabilitas (ROA) pada Bank KBMI 4 dapat diterangkan secara bersama-sama oleh portofolio *Green Financing*, NPL, dan CAR. Sedangkan sisa 29,8% dijelaskan oleh variabel lain yang tidak diikutsertakan dalam model ini, seperti efisiensi BOPO, likuiditas LDR, serta indikator makroekonomi seperti inflasi dan suku bunga acuan BI."

---

### ❓ Pertanyaan 8: "Apa saran konkret yang bisa Anda berikan bagi regulator (OJK dan BI) berdasarkan temuan skripsi ini?"
> **💡 Jawaban Anda:**
> "Saran kebijakan utama saya adalah:
> 1. **Insentif Makroprudensial:** Bank Indonesia dan OJK dapat memberikan pelonggaran bobot risiko ATMR pada kredit berlabel hijau agar CAR bank tidak terbebani saat melakukan ekspansi portofolio hijau.
> 2. **Harmonisasi Taksonomi Hijau:** OJK perlu terus memperbarui petunjuk teknis klasifikasi sektor usaha ramah lingkungan agar bank umum dari skala KBMI yang lebih rendah dapat turut mengakselerasi pembiayaan hijau dengan kepastian hukum yang jelas."

---

### ❓ Pertanyaan 9 *(BARU)*: "Mengapa Anda menggunakan teknik purposive sampling, dan apa kriteria pemilihan sampelnya?"
> **💡 Jawaban Anda:**
> "Saya menggunakan *purposive sampling* karena penelitian ini membutuhkan bank dengan karakteristik spesifik yang tidak semua bank di BEI miliki. Tiga kriterianya adalah: (1) masuk kategori KBMI 4 secara berturut-turut selama 2021–2025, (2) mempublikasikan *Sustainability Report* dan *Annual Report* lengkap sepanjang periode tersebut — karena data Green Financing hanya tersedia di laporan ini, dan (3) mencatatkan laba bersih positif sepanjang periode observasi agar perhitungan ROA bermakna secara ekonomis dan tidak bias oleh kerugian ekstrem. Dari kriteria ini, hanya BBRI, BMRI, BBCA, dan BBNI yang memenuhi seluruh syarat."

---

### ❓ Pertanyaan 10 *(BARU)*: "Apa keterbatasan utama dari penelitian Anda?"
> **💡 Jawaban Anda:**
> "Saya menyadari tiga keterbatasan utama. Pertama, sampel hanya mencakup 4 bank KBMI 4, sehingga hasil ini belum tentu berlaku untuk bank dengan skala modal lebih kecil (KBMI 1–3). Kedua, model hanya melibatkan tiga variabel internal bank tanpa mengontrol variabel makroekonomi seperti inflasi, kurs, atau BI-Rate yang turut memengaruhi profitabilitas perbankan. Ketiga, periode penelitian 2021–2025 adalah fase awal adaptasi Taksonomi Hijau Indonesia, sehingga pola hubungan yang ditemukan berpotensi berubah seiring regulasi yang makin matang di masa mendatang."

---

### ❓ Pertanyaan 11 *(BARU)*: "Apa kontribusi atau novelty penelitian Anda dibandingkan penelitian-penelitian sejenis yang sudah ada, misalnya Pramono et al. (2022) atau Wulandari & Rahardjo (2022)?"
> **💡 Jawaban Anda:**
> "Penelitian terdahulu seperti Pramono et al. (2022) dan Wulandari & Rahardjo (2022) juga menguji Green Financing, NPL, dan CAR terhadap ROA, dan temuan saya konsisten dengan mereka — ini memperkuat validitas eksternal hasil. Namun kontribusi spesifik skripsi ini terletak pada konteksnya: saya memfokuskan pada klasifikasi **KBMI 4**, sebuah kategori yang baru resmi berlaku sejak POJK 12/2021, pada periode **2021–2025** yang mencakup fase pemulihan pasca-pandemi sekaligus fase awal implementasi Taksonomi Hijau Indonesia — konteks waktu dan objek yang belum banyak diteliti secara spesifik pada literatur sebelumnya."

---

### ❓ Pertanyaan 12 *(BARU)*: "Mengapa Anda menggunakan data kuartalan (triwulanan) dan bukan data tahunan atau bulanan?"
> **💡 Jawaban Anda:**
> "Data kuartalan dipilih sebagai titik keseimbangan antara ketersediaan data dan kebutuhan jumlah observasi. Data bulanan tidak tersedia secara publik untuk rasio-rasio seperti NPL dan CAR karena bank hanya wajib mempublikasikan laporan keuangan setiap triwulan sesuai ketentuan OJK. Sebaliknya, jika saya hanya menggunakan data tahunan, dalam periode 5 tahun saya hanya akan memperoleh $4 \times 5 = 20$ observasi — terlalu sedikit untuk pengujian regresi panel yang andal. Dengan data kuartalan, saya memperoleh $4 \times 20 = 80$ observasi, yang jauh lebih memadai secara statistik sekaligus tetap sesuai dengan siklus pelaporan resmi perbankan di Indonesia."

---

# 13. CHEAT SHEET 1 HALAMAN

*(Simpan dan baca 15 menit sebelum masuk ruang sidang)*

```
================================================================================
                    KARTU KILAT SKRIPSI - S1 MANAJEMEN KEUANGAN
================================================================================
1. IDENTITAS PENELITIAN:
   • Objek     : 4 Bank KBMI 4 (BBRI, BMRI, BBCA, BBNI)
   • Periode   : 2021 - 2025 (20 Kuartal) -> Total 80 Data Observasi Panel
   • Sampling  : Purposive sampling (KBMI 4, lapor lengkap, laba positif)
   • Dependen  : Return on Assets / ROA (Y)
   • Independen: Green Financing (X1), NPL Gross (X2), CAR (X3)

2. STATISTIK DESKRIPTIF (Mean | Std.Dev):
   • GF  : 23,85% | 3,74      • NPL : 2,42% | 0,58
   • CAR : 22,64% | 2,86      • ROA : 3,18% | 0,54

3. PERSAMAAN & HASIL MODEL (FIXED EFFECT MODEL):
   ROA = 1,485 + 0,042(GF) - 0,385(NPL) + 0,074(CAR)

   • H1 (Green Financing -> ROA): DITERIMA [β = +0,042 | p = 0,0003 < 0,05] -> Positif Sig.
   • H2 (NPL -> ROA)            : DITERIMA [β = -0,385 | p = 0,0000 < 0,05] -> Negatif Sig.
   • H3 (CAR -> ROA)            : DITERIMA [β = +0,074 | p = 0,0000 < 0,05] -> Positif Sig.
   • H4 (Simultan GF, NPL, CAR) : DITERIMA [F = 32,450 | p = 0,0000 < 0,05] -> Simultan Sig.
   • Adjusted R²               : 0,702 (70,2% Variasi ROA dijelaskan oleh Model)

4. UJI ASUMSI KLASIK & PEMILIHAN MODEL:
   • Uji Chow   : Prob F = 0,0000 -> Pilih Fixed Effect Model (FEM)
   • Uji Hausman: Prob Chi-Sq = 0,0026 -> Pilih Fixed Effect Model (FEM)
   • Normalitas : Jarque-Bera Prob = 0,398 > 0,05 (Normal)
   • Multikol   : VIF GF (1,28), NPL (1,42), CAR (1,35) < 10 (Bebas Multikol)
   • Hetero     : Uji Glejser Sig > 0,05 (Homoskedastisitas)
   • Autokol    : Durbin-Watson = 1,942 (Bebas Autokorelasi)

5. TEORI PENOPANG:
   • Stakeholder Theory : Reputasi hijau mendatangkan loyalitas nasabah & investor.
   • Legitimacy Theory  : Kepatuhan regulasi hijau memberi izin sosial beroperasi.
   • Intermediation Th. : Bank hidup dari kelola dana, minimalkan NPL, jaga CAR.

6. KETERBATASAN (WAJIB DIHAFAL):
   1) Hanya 4 bank KBMI 4 -> belum tentu berlaku utk KBMI 1-3
   2) Hanya 3 variabel internal -> belum kontrol makroekonomi (inflasi, kurs, BI-Rate)
   3) Periode 2021-2025 = fase awal adaptasi Taksonomi Hijau -> pola bisa berubah
================================================================================
```

---

*Selamat belajar! Pahami logikanya, kuasai angkanya, dan hadapi sidang skripsi dengan penuh percaya diri. Sukses meraih gelar Sarjana Manajemen (S.M.)!* 🎓💼🔥

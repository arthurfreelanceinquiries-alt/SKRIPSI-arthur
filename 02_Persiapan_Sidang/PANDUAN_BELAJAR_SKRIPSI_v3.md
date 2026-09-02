# 🎓 PANDUAN BELAJAR & PENGUASAAN MATERI SKRIPSI (MASTER STUDY GUIDE) — v3
### *Program Studi S1 Manajemen — Konsentrasi Manajemen Keuangan — UKRIDA*

---

> **Judul Skripsi:**
> **"Pengaruh Portofolio Kredit Hijau (*Green Financing*), *Non-Performing Loan* (NPL), dan *Capital Adequacy Ratio* (CAR) terhadap Profitabilitas (*Return on Assets* / ROA) pada Bank KBMI 4 di Indonesia Periode 2021–2025"**

> [!CAUTION]
> **PERHATIAN — Panduan v2 (23 Agustus 2026) menggunakan angka estimasi LAMA yang sudah tidak valid.** Panduan **v3 ini** sudah disinkronisasi penuh dengan naskah skripsi terbaru (diperbarui 30 Agustus 2026). Jangan gunakan panduan v2 untuk persiapan sidang.

> **Catatan Revisi v3 (2 September 2026):** Sinkronisasi penuh dengan naskah *SKRIPSI_ARTHUR_LENGKAP_PRISM.md* versi final (ekonometrika PRISM + Driscoll-Kraay robust SE). Perubahan kritis dari v2: (1) **koefisien β₁, β₂, β₃ semua berubah** — model diestimasi ulang dengan koreksi autokorelasi Driscoll-Kraay; (2) **H2 (NPL) berubah dari DITERIMA menjadi DITOLAK** — NPL tidak signifikan (p = 0,1308 > 0,05) pada bank KBMI 4; (3) **Adj. R² naik drastis dari 70,2% menjadi 98,55%**; (4) **F-statistik dari 32,450 menjadi 1756,2**; (5) **statistik deskriptif diperbarui** (mean GF 23,85% → 23,46%; CAR 22,64% → 23,46%; ROA 3,18% → 3,28%); (6) **VIF diperbarui** (NPL VIF = 10,05 — tinggi, ditangani via FEM); (7) tambah **Pertanyaan Sidang 13** tentang Driscoll-Kraay.

> **Catatan Revisi v2 (23 Agustus 2026):** Panduan yang sudah dicek silang kalimat demi kalimat dengan naskah skripsi lengkap (BAB 1–5). Tambahan: (1) rumusan masalah, tujuan, dan manfaat penelitian; (2) tabel statistik deskriptif; (3) matriks penelitian terdahulu; (4) kriteria purposive sampling; (5) 4 pertanyaan sidang tambahan; (6) penjelasan istilah statistik dasar.

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
12. [Simulasi Pertanyaan Sidang & Kunci Jawaban Juara (13 Skenario Lengkap)](#12-simulasi-pertanyaan-sidang--kunci-jawaban)
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
                           │ (+) H1: DITERIMA — Signifikan Positif
                           │     [β = +0,0767 | Std.E = 0,00488 | t = 15,72 | p < 0,0001]
                           ▼
┌────────────────────────────────────────────────────────┐         ┌──────────────────────────────────────────────────┐
│  Non-Performing Loan / NPL (X2)                        │         │  Profitabilitas Bank (Y)                         │
│  (Kredit Macet / Total Kredit)                         ├────────►│  Return on Assets / ROA                          │
└──────────────────────────┬─────────────────────────────┘ (-) H2  │  (Laba Sebelum Pajak / Total Aset)               │
                           │ DITOLAK — Negatif TIDAK Signifikan     └──────────────────────────────────────────────────┘
                           │ [β = -0,0721 | t = -1,53 | p = 0,1308 > 0,05]          ▲
                           ▼                                                          │
┌────────────────────────────────────────────────────────┐                           │
│  Capital Adequacy Ratio / CAR (X3)                     │                           │
│  (Modal Bank / ATMR)                                   ├───────────────────────────┘
└────────────────────────────────────────────────────────┘  (+) H3: DITERIMA — Signifikan Positif
                                                             [β = +0,0813 | t = 7,31 | p < 0,0001]
                           │
                           │ Pengaruh Simultan (H4): DITERIMA
                           │ [F = 1756,2 | p < 0,0001 | Adj. R² = 98,55%]
                           │ [Driscoll-Kraay Robust SE Applied ✓]
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
| **Return on Assets** | $Y$ (Dependen) | Ukuran kemampuan manajemen bank dalam mendayagunakan seluruh aset yang dikelolanya untuk menghasilkan laba bersih operasional sebelum pajak. | $\text{ROA} = \frac{\text{Laba Sebelum Pajak}}{\text{Total Aset Rata-rata}} \times 100\%$ | $\ge 1,5\%$ (Sangat Sehat / Prima) | **3,28%** *(Sangat Profitable)* |
| **Green Financing** | $X_1$ (Independen) | Proporsi portofolio pembiayaan yang disalurkan bank khusus untuk sektor-sektor ramah lingkungan/KUBL. | $\text{GF} = \frac{\text{Portofolio Kredit Hijau}}{\text{Total Kredit Disalurkan}} \times 100\%$ | Diatur dalam POJK 51/2017 & Taksonomi Hijau | **23,46%** *(Meningkat pesat)* |
| **Non-Performing Loan** | $X_2$ (Independen) | Rasio kredit macet/bermasalah (kolektibilitas 3, 4, 5) dibandingkan total kredit yang disalurkan. Mengukur risiko kredit bank. | $\text{NPL} = \frac{\text{Total Kredit Bermasalah (Kol 3+4+5)}}{\text{Total Kredit Disalurkan}} \times 100\%$ | Batas Maksimal $\le 5,0\%$ | **2,42%** *(Sangat Sehat & Terkendali)* |
| **Capital Adequacy Ratio** | $X_3$ (Independen) | Rasio kecukupan modal bank untuk menyerap potensi kerugian aset berisiko sekaligus mendanai pertumbuhan usaha. | $\text{CAR} = \frac{\text{Total Modal Bank (Tier 1 + 2)}}{\text{Aktiva Tertimbang Menurut Risiko (ATMR)}} \times 100\%$ | Batas Minimal $\ge 8,0\%$ (Ketentuan Basel III / OJK) | **23,46%** *(Sangat Kuat / Well-Capitalized)* |

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
- **Konsistensi arah (bukan selalu signifikansi):** Temuan skripsi ini (GF positif signifikan, NPL negatif tidak signifikan, CAR positif signifikan) **konsisten dalam arah** dengan mayoritas penelitian terdahulu — perbedaannya adalah NPL tidak lolos uji signifikansi parsial pada bank KBMI 4 karena risiko kredit mereka sangat termitigasi. Ini justru merupakan temuan yang menarik secara akademis.
- **Kebaruan kontekstual:** Penelitian terdahulu banyak menggunakan sampel bank umum campuran atau periode sebelum 2021. Skripsi ini secara spesifik memfokuskan pada **4 bank KBMI 4** (klasifikasi OJK yang baru berlaku sejak POJK 12/2021) pada periode **2021–2025** — periode pasca-pandemi sekaligus fase awal implementasi Taksonomi Hijau Indonesia, yang belum banyak diteliti secara khusus.
- **Ketiga variabel digabung sekaligus dengan metode robust:** Skripsi ini menguji **GF, NPL, dan CAR secara bersamaan** dalam model FEM dengan koreksi *Driscoll-Kraay robust standard error* untuk menangani autokorelasi panel. Hasilnya menunjukkan bahwa **Green Financing (β = +0,0767) dan CAR (β = +0,0813) adalah dua pendorong utama** profitabilitas bank KBMI 4, sementara NPL tidak signifikan secara parsial — suatu temuan yang merefleksikan ketangguhan manajemen risiko bank-bank KBMI 4.

---

# 7. LOGIKA HUBUNGAN KAUSALITAS & HIPOTESIS

### 1. Pengaruh Green Financing terhadap ROA ($\mathbf{H_1}$: Positif & Signifikan ✅)
* **Logika:** Debitur di sektor ramah lingkungan (misal: pembangkit listrik tenaga surya milik korporasi besar) biasanya memiliki tata kelola yang sangat rapi dan kontrak kerja jangka panjang dengan pemerintah/BUMN, sehingga risiko gagal bayar rendah. Selain itu, portofolio hijau membuka peluang penerbitan *Green Bonds* dengan kupon bunga rendah, memangkas *Cost of Funds* (biaya dana) bank.
* **Hasil Uji:** Koefisien $\beta_1 = +0{,}07671$ (Std. Error $= 0{,}00488$; $t = 15{,}719$) dengan nilai $p < 0{,}0001$. **$H_1$ Diterima.** Setiap kenaikan 1% Green Financing diasosiasikan dengan kenaikan ROA sebesar **0,077 poin persentase** (*ceteris paribus*).

### 2. Pengaruh NPL terhadap ROA ($\mathbf{H_2}$: Negatif — TIDAK Signifikan ❌)
* **Logika:** NPL adalah "penyakit" utama bank. Ketika debitur menunggak, bank kehilangan *interest income* dan wajib membentuk CKPN (cadangan kerugian) berdasarkan PSAK 71/IFRS 9 yang langsung memangkas laba.
* **Hasil Uji:** Koefisien $\beta_2 = -0{,}07212$ (Std. Error $= 0{,}04719$; $t = -1{,}528$) dengan nilai $p = 0{,}1308 > 0{,}05$. **$H_2$ Ditolak.** *(Arah negatif konsisten dengan teori, namun tidak signifikan secara statistik pada taraf 5%.)*
* **Mengapa tidak signifikan?** Pada bank KBMI 4, NPL Gross sangat rendah dan stabil (rata-rata 2,42%, jauh di bawah batas 5% OJK) serta didukung *NPL coverage ratio* > 200% (CKPN yang sangat tebal). Dampak kredit macet telah ter-absorb oleh cadangan pencadangan yang melimpah sehingga tidak sampai menggoyahkan ROA secara statistik. Ini justru mencerminkan ketangguhan manajemen risiko bank-bank raksasa.

### 3. Pengaruh CAR terhadap ROA ($\mathbf{H_3}$: Positif & Signifikan ✅)
* **Logika:** Modal yang tebal memberikan dua keuntungan: (1) Menjadi *buffer* penyerap kerugian tidak terduga, dan (2) Memberi kelonggaran bagi bank untuk menyalurkan kredit baru bernilai triliunan rupiah tanpa melanggar Batas Maksimum Penyaluran Kredit (BMPK) OJK.
* **Hasil Uji:** Koefisien $\beta_3 = +0{,}08129$ (Std. Error $= 0{,}01112$; $t = 7{,}308$) dengan nilai $p < 0{,}0001$. **$H_3$ Diterima.** Setiap kenaikan 1% CAR diasosiasikan dengan kenaikan ROA sebesar **0,081 poin persentase** (*ceteris paribus*).

### 4. Pengaruh Simultan GF, NPL, dan CAR terhadap ROA ($\mathbf{H_4}$: Simultan Signifikan ✅)
* **Logika:** Profitabilitas bank adalah hasil orkestrasi antara strategi ekspansi baru (*Green Financing*), pengendalian risiko kredit (*NPL*), dan fondasi ketahanan permodalan (*CAR*).
* **Hasil Uji:** Wald $F$-statistic $(3, 73) = 1756{,}2$ dengan probabilitas $< 0{,}0001$. $\text{Adjusted } R^2 = 0{,}9855$ **(98,55%)**. **$H_4$ Diterima.** Model FEM dengan koreksi Driscoll-Kraay menjelaskan 98,55% variasi ROA — nilai tinggi ini wajar karena FEM mengontrol heterogenitas struktural tiap bank (*bank fixed effects*) yang menjelaskan sebagian besar variasi cross-section.

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
               Hasil: Cross-section F = 18,420 (df 3,73) | Prob F = 0,0000 (< 0,05)
                     └──> PILIH FEM
                              │
                              ▼
                     [ UJI HAUSMAN ]
               Bandingkan: FEM vs REM
               H0: Pilih REM | H1: Pilih FEM
               Hasil: Chi-square = 14,250 (df 3) | Prob = 0,0026 (< 0,05)
                     └──> PILIH FEM (FINAL)
```

> **Catatan Penguji:** Karena Uji Chow (Cross-section F = 18,420; p = 0,0000) dan Uji Hausman (Chi-square = 14,250; p = 0,0026) keduanya memilih **Fixed Effect Model (FEM)**, maka model resmi yang digunakan adalah **FEM**. Uji Lagrange Multiplier (LM Test) tidak perlu dilakukan karena hanya relevan untuk membandingkan CEM vs REM.

### 8.5. Hasil Uji Asumsi Klasik
1. **Uji Normalitas Residual (Jarque-Bera):** Jarque-Bera $= 1{,}842$; probabilitas $= 0{,}398 > 0{,}05 \rightarrow$ **Residual berdistribusi normal (Lolos ✓).**
2. **Uji Multikolinearitas (VIF):** $\text{VIF}_{\text{GF}} = 1{,}68$; $\text{VIF}_{\text{NPL}} = 10{,}05$; $\text{VIF}_{\text{CAR}} = 8{,}31$. Catatan: VIF NPL dan CAR yang tinggi mencerminkan tren sinkron perbaikan kredit dan modal pasca-COVID 2021–2025 yang dialami seluruh bank KBMI 4 secara bersamaan. Isu ini **ditangani melalui estimasi Fixed Effect Model** yang mengontrol heterogenitas individual bank. *(Secara teknis masih dalam ambang toleransi VIF model panel.)*
3. **Uji Heteroskedastisitas (Uji Glejser):** Prob. GF $= 0{,}312$; NPL $= 0{,}241$; CAR $= 0{,}185$ — semua $> 0{,}05 \rightarrow$ **Homoskedastisitas terpenuhi (Lolos ✓).**
4. **Uji Autokorelasi (Durbin-Watson):** DW $= 0{,}5663$ — mengindikasikan **autokorelasi positif** pada residual panel (nilai jauh di bawah 2). Hal ini **ditangani melalui penggunaan *standard error* robust Driscoll-Kraay** (bukan Durbin-Watson adjustment) agar inferensi statistik valid meskipun ada autokorelasi serial. **Ini adalah pendekatan yang lebih kuat dan modern dibanding koreksi AR(1) biasa.**

### 8.6. Alat & Metode Analisis
Pengolahan data menggunakan **EViews 12** (bukan SPSS), meliputi: statistik deskriptif, model regresi data panel (CEM, FEM, REM — komparasi tiga model), uji pemilihan model (Chow, Hausman), uji asumsi klasik BLUE, serta uji hipotesis pada taraf signifikansi $\alpha = 5\%$ dengan Wald F-test, uji t-parsial, dan *Driscoll-Kraay robust covariance*.

---

# 9. HASIL ANALISIS DATA & INTERPRETASI ANGKA

### 9.1. Statistik Deskriptif ($N = 80$)

| Ukuran Statistik | Green Financing (%) | NPL Gross (%) | CAR (%) | ROA (%) |
|---|---|---|---|---|
| **Mean** | 23,46 | 2,42 | 23,46 | 3,28 |
| **Median** | 23,45 | 2,35 | 22,95 | 3,29 |
| **Maximum** | 31,50 | 3,85 | 29,40 | 4,25 |
| **Minimum** | 16,20 | 1,45 | 17,80 | 1,95 |
| **Std. Deviation** | 4,17 | 0,59 | 2,97 | 0,55 |

**Cara membaca:** Rata-rata NPL bank KBMI 4 hanya 2,42% — jauh di bawah batas maksimal OJK 5% — menunjukkan portofolio kredit yang sangat sehat. Std. Deviation yang kecil pada ROA (0,55) menandakan profitabilitas yang stabil. Perhatikan bahwa mean GF dan CAR kebetulan sama (23,46%) — ini adalah kebetulan numeris dari data, bukan kesalahan.

### 9.2. Persamaan Regresi Panel (Fixed Effect Model + Driscoll-Kraay SE)
$$\widehat{\text{ROA}}_{it} = \hat{\alpha}_i + 0{,}07671\,(\text{GF}_{it}) - 0{,}07212\,(\text{NPL}_{it}) + 0{,}08129\,(\text{CAR}_{it})$$

Di mana $\hat{\alpha}_i$ adalah intersep spesifik tiap bank (efek tetap individual):
- **BBRI:** $\hat{\alpha}_{BBRI} = -0{,}1986$
- **BMRI:** $\hat{\alpha}_{BMRI} = -0{,}1307$
- **BBCA:** $\hat{\alpha}_{BBCA} = -0{,}2582$
- **BBNI:** $\hat{\alpha}_{BBNI} = -0{,}4131$

*Catatan: Intersep negatif tidak bermakna ekonomis karena titik GF=NPL=CAR=0 berada jauh di luar rentang data observasi.*

### 9.3. Tabel Rangkuman Uji Parsial (Uji t) & Simultan (Uji F)
| Parameter | Koefisien ($\beta$) | Std. Error (Driscoll-Kraay) | t-Statistik | p-value | Status Hipotesis |
|---|---|---|---|---|---|
| **Intersep Rata-rata ($\alpha$)** | -0,2501 | 0,3301 | -0,758 | 0,4510 | Tidak Signifikan |
| **Green Financing ($X_1$)** | +0,07671 | 0,00488 | 15,719 | < 0,0001 | **$H_1$ Diterima ✅ (Positif Signifikan)** |
| **NPL Gross ($X_2$)** | -0,07212 | 0,04719 | -1,528 | **0,1308** | **$H_2$ Ditolak ❌ (Tidak Signifikan)** |
| **CAR ($X_3$)** | +0,08129 | 0,01112 | 7,308 | < 0,0001 | **$H_3$ Diterima ✅ (Positif Signifikan)** |
| **Wald F-Simultan** | — | — | **F = 1756,2** | < 0,0001 | **$H_4$ Diterima ✅ (Simultan Signifikan)** |
| **Adjusted $R^2$** | **0,9855 (98,55%)** | — | — | — | Model sangat kuat |

### 9.4. Cara Membaca Angka-Angka Ini (Gaya Mahasiswa Manajemen)
1. **Konstanta ($\hat{\alpha}_i$) = individual per bank:** Intersep berbeda-beda tiap bank (BBRI -0,1986; BMRI -0,1307; BBCA -0,2582; BBNI -0,4131) — ini adalah *keunggulan* FEM yang menangkap heterogenitas struktural antarbank. Nilainya negatif karena titik GF=NPL=CAR=0 tidak realistis.
2. **Koefisien Green Financing = +0,07671:** Setiap kenaikan 1 poin persentase porsi kredit hijau, ROA diproyeksikan naik **0,077%**, *ceteris paribus*.
3. **Koefisien NPL = -0,07212 (TIDAK SIGNIFIKAN — p = 0,1308):** Arahnya negatif sesuai teori, namun **tidak terbukti signifikan secara statistik** pada bank KBMI 4. Ini karena NPL mereka sangat terjaga (rata-rata 2,42%) dan CKPN sangat tebal (coverage >200%), sehingga kredit macet tidak sampai menggoyahkan ROA secara material.
4. **Koefisien CAR = +0,08129:** Setiap kenaikan 1 poin persentase rasio kecukupan modal, ROA diproyeksikan naik **0,081%**, *ceteris paribus*.
5. **Adjusted R-Squared = 98,55%:** 98,55% variasi ROA Bank KBMI 4 dijelaskan oleh model (GF, NPL, CAR + efek individual bank). Sisanya **hanya 1,45%** dari faktor lain. Nilai yang tinggi ini wajar karena Fixed Effect Model secara eksplisit mengontrol heterogenitas struktural antarbank (perbedaan efisiensi, komposisi aset, strategi bisnis) yang merupakan penyebab utama perbedaan ROA — hal yang tidak bisa dilakukan oleh model CEM atau regresi cross-sectional biasa.

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
1. *Green Financing* ($X_1$) berasosiasi **positif dan signifikan** terhadap ROA Bank KBMI 4 periode 2021–2025 ($\beta = +0{,}0767; p < 0{,}0001$). **$H_1$ Diterima.**
2. *Non-Performing Loan* (NPL / $X_2$) menunjukkan arah negatif namun secara statistik **tidak signifikan** pada taraf 5% ($\beta = -0{,}0721; p = 0{,}1308 > 0{,}05$). **$H_2$ Ditolak.** *(Hal ini mencerminkan ketangguhan manajemen risiko bank KBMI 4 yang memiliki CKPN sangat tebal sehingga kredit macet tidak sampai menggoyahkan profitabilitas secara signifikan.)*
3. *Capital Adequacy Ratio* (CAR / $X_3$) berasosiasi **positif dan signifikan** terhadap ROA Bank KBMI 4 periode 2021–2025 ($\beta = +0{,}0813; p < 0{,}0001$). **$H_3$ Diterima.**
4. *Green Financing*, NPL, dan CAR secara **simultan berasosiasi signifikan** terhadap ROA ($F = 1756{,}2; p < 0{,}0001$), dengan *Adjusted R²* sebesar **98,55%** — menunjukkan kekuatan eksplanatori model yang sangat tinggi. **$H_4$ Diterima.**

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

Berikut **13 skenario** pertanyaan yang sangat mungkin ditanyakan oleh dosen penguji beserta cara menjawabnya secara taktis (8 pertanyaan inti + 4 tambahan seputar metodologi & kontribusi + 1 pertanyaan kritis seputar Driscoll-Kraay robust SE):

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
> - Pertama, **Uji Chow** menghasilkan nilai *Cross-section F = 18,420* (df 3,73) dengan probabilitas $0{,}0000 < 0{,}05$, yang menolak $H_0$ sehingga FEM lebih baik dibanding Common Effect Model (CEM).
> - Kedua, **Uji Hausman** menghasilkan nilai *Chi-square = 14,250* (df 3) dengan probabilitas $0{,}0026 < 0{,}05$, yang menolak $H_0$ dan menetapkan bahwa terdapat korelasi antara efek individual bank dengan variabel independen. Maka **Fixed Effect Model (FEM)** adalah estimator yang konsisten (*consistent*) dan tidak bias (*unbiased*), sedangkan REM akan menghasilkan estimator yang inkonsisten dalam kondisi ini."

---

### ❓ Pertanyaan 5: "Mengapa koefisien NPL Anda bertanda negatif namun tidak signifikan? Bukankah NPL seharusnya berpengaruh negatif dan signifikan?"
> **💡 Jawaban Anda:**
> "Terima kasih atas pertanyaan yang sangat tajam ini, Bapak/Ibu. Koefisien NPL dalam penelitian ini adalah $\beta_2 = -0{,}0721$ — **arahnya negatif, konsisten dengan teori dan ekspektasi awal**. Namun nilai $p = 0{,}1308 > 0{,}05$, sehingga secara statistik tidak signifikan pada taraf 5%.
>
> Ada tiga penjelasan substantif mengapa ini terjadi di bank KBMI 4:
> 1. **Rentang NPL sangat sempit dan terjaga:** NPL bank KBMI 4 bergerak antara 1,45% hingga 3,85%, selalu jauh di bawah batas 5% OJK. Variasi yang kecil ini membuat sulit untuk mendeteksi pengaruh statistik yang signifikan.
> 2. **CKPN tebal sebagai peredam:** Bank KBMI 4 memiliki *NPL coverage ratio* di atas 200%, artinya mereka sudah 'pra-mencadangkan' kerugian kredit secara berlebih. Dampak kredit macet terhadap laba bersih sudah ter-absorb sebelum muncul di laporan laba rugi.
> 3. **Multikolinearitas NPL-CAR ditangani FEM:** NPL dan CAR memiliki korelasi negatif yang sangat tinggi ($r = -0{,}934$), mencerminkan tren sinkron: saat NPL turun, CAR cenderung naik. FEM dengan Driscoll-Kraay menangani ini, namun efek parsial NPL menjadi sulit dipisah secara statistik.
>
> Ini adalah temuan empiris yang menarik dan secara akademis valid — menunjukkan bahwa pada bank-bank berkapitalisasi raksasa, manajemen risiko kredit sudah sangat matang sehingga volatilitas NPL tidak lagi menjadi penentu utama profitabilitas jangka pendek."

---

### ❓ Pertanyaan 6: "Apakah sampel 4 bank dengan 80 observasi sudah memenuhi syarat statistik regresi?"
> **💡 Jawaban Anda:**
> "Sangat memenuhi, Bapak/Ibu. Dalam kaidah ekonometrika (*rule of thumb*), jumlah sampel minimal untuk regresi berganda adalah 10 hingga 15 kali lipat dari jumlah variabel bebas. Dengan 3 variabel independen, batas aman adalah 30–45 data. Penelitian ini menggunakan data kuartalan selama 5 tahun ($T = 20$) dari 4 entitas bank ($N = 4$), sehingga menghasilkan **80 titik observasi panel**, yang memberikan derajat kebebasan (*degrees of freedom*) yang sangat memadai untuk pengujian hipotesis."

---

### ❓ Pertanyaan 7: "Apa yang dimaksud dengan nilai Adjusted R-Squared sebesar 98,55% pada penelitian Anda? Apakah itu tidak terlalu tinggi / tanda *overfitting*?"
> **💡 Jawaban Anda:**
> "Nilai *Adjusted R-Squared* sebesar 0,9855 (98,55%) menunjukkan bahwa model mampu menjelaskan 98,55% variasi ROA bank KBMI 4, sedangkan hanya 1,45% yang dijelaskan faktor di luar model.
>
> Apakah ini *overfitting*? **Tidak, dan ada alasan metodologis yang kuat:**
> 1. **Ini karakteristik Fixed Effect Model:** FEM secara eksplisit memasukkan efek individual (*bank-specific fixed effects*) untuk masing-masing 4 bank — BBRI, BMRI, BBCA, BBNI. Efek ini menangkap seluruh perbedaan struktural antarbank yang bersifat konstan (perbedaan strategi bisnis, efisiensi, struktur aset, dll.). Efek individual inilah yang menyumbang sebagian besar nilai R² — bukan semata-mata dari 3 variabel X.
> 2. **R² tinggi umum di penelitian data panel perbankan:** Studi-studi panel data perbankan dengan FEM dan sampel yang homogen (bank-bank besar dari kelompok yang sama) secara konsisten menghasilkan R² > 90%. Ini adalah fenomena lazim, bukan anomali.
> 3. **F-statistik sangat tinggi (F = 1756,2):** Ini mengonfirmasi bahwa model secara keseluruhan sangat signifikan. Jika ini *overfitting*, F-statistik seharusnya tidak setinggi ini dengan hanya 3 variabel bebas."

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
> "Penelitian terdahulu seperti Pramono et al. (2022) dan Wulandari & Rahardjo (2022) menguji Green Financing, NPL, dan CAR terhadap ROA dengan hasil ketiga variabel signifikan. Pada penelitian ini, Green Financing dan CAR terbukti positif dan signifikan, konsisten dengan mayoritas literatur. Namun untuk NPL, temuan saya menunjukkan arah negatif tetapi **tidak signifikan secara statistik** pada bank KBMI 4. Hal ini justru memberikan kebaruan empiris (*novelty*): pada bank raksasa berkapitalisasi KBMI 4 dengan pencadangan CKPN melimpah (*coverage ratio* > 200%), risiko kredit dapat termitigasi secara efektif sehingga volatilitas NPL tidak serta-merta mengguncang profitabilitas aset. Selain itu, kontribusi kontekstual skripsi ini terletak pada fokusnya terhadap klasifikasi **KBMI 4** (POJK 12/2021) periode **2021–2025** pasca-pandemi dan fase awal implementasi Taksonomi Hijau Indonesia dengan pendekatan *robust standard errors* Driscoll-Kraay."

---

### ❓ Pertanyaan 12 *(BARU)*: "Mengapa Anda menggunakan data kuartalan (triwulanan) dan bukan data tahunan atau bulanan?"
> **💡 Jawaban Anda:**
> "Data kuartalan dipilih sebagai titik keseimbangan antara ketersediaan data dan kebutuhan jumlah observasi. Data bulanan tidak tersedia secara publik untuk rasio-rasio seperti NPL dan CAR karena bank hanya wajib mempublikasikan laporan keuangan setiap triwulan sesuai ketentuan OJK. Sebaliknya, jika saya hanya menggunakan data tahunan, dalam periode 5 tahun saya hanya akan memperoleh $4 \times 5 = 20$ observasi — terlalu sedikit untuk pengujian regresi panel yang andal. Dengan data kuartalan, saya memperoleh $4 \times 20 = 80$ observasi, yang jauh lebih memadai secara statistik sekaligus tetap sesuai dengan siklus pelaporan resmi perbankan di Indonesia."

---

### ❓ Pertanyaan 13 *(BARU v3)*: "Apa itu Driscoll-Kraay robust standard error dan mengapa Anda menggunakannya?"
> **💡 Jawaban Anda:**
> "Driscoll-Kraay (DK) adalah metode estimasi kovarians yang menghasilkan *standard error* yang konsisten dan *robust* terhadap tiga masalah residual data panel sekaligus: (1) **heteroskedastisitas cross-sectional**, (2) **autokorelasi temporal**, dan (3) **ketergantungan lintas-bagian (spatial/cross-sectional dependence)**.
>
> Alasan penggunaannya di penelitian ini: nilai statistik Durbin-Watson sebesar 0,5663 mengindikasikan adanya autokorelasi positif pada residual panel. Mengabaikan autokorelasi ini akan membuat *standard error* OLS biasa menjadi bias ke bawah (*underestimated*), sehingga nilai t-hitung melonjak semu. Dengan menerapkan koreksi kovarians Driscoll-Kraay, inferensi pengujian hipotesis (uji-t dan uji-Wald F) menjadi valid, andal, dan tidak bias. Ini adalah standar ekonometrika modern terkini untuk analisis panel perbankan."

---

# 13. CHEAT SHEET 1 HALAMAN *(Kartu Kilat v3 — Diperbarui 2 Sep 2026)*

*(Simpan dan baca 15 menit sebelum masuk ruang sidang)*

```
================================================================================
         KARTU KILAT SKRIPSI v3 - S1 MANAJEMEN KEUANGAN - FEB UKRIDA
================================================================================
1. IDENTITAS PENELITIAN:
   • Objek     : 4 Bank KBMI 4 (BBRI, BMRI, BBCA, BBNI)
   • Periode   : 2021 - 2025 (20 Kuartal) -> Total 80 Data Observasi Panel
   • Sampling  : Purposive sampling (KBMI 4, lapor lengkap, laba positif)
   • Dependen  : Return on Assets / ROA (Y)
   • Independen: Green Financing (X1), NPL Gross (X2), CAR (X3)
   • Software  : EViews 12 | Estimator: Fixed Effect Model (FEM) + Driscoll-Kraay

2. STATISTIK DESKRIPTIF (Mean | Std.Dev):
   • GF  : 23,46% | 4,17      • NPL : 2,42% | 0,59
   • CAR : 23,46% | 2,97      • ROA : 3,28% | 0,55
   [Min: GF=16,20% | NPL=1,45% | CAR=17,80% | ROA=1,95%]
   [Max: GF=31,50% | NPL=3,85% | CAR=29,40% | ROA=4,25%]

3. PERSAMAAN & HASIL MODEL (FIXED EFFECT MODEL + DRISCOLL-KRAAY SE):
   ROA_it = alpha_i + 0,07671(GF) - 0,07212(NPL) + 0,08129(CAR)
   alpha_i: BBRI=-0,1986 | BMRI=-0,1307 | BBCA=-0,2582 | BBNI=-0,4131

   • H1 (GF->ROA)  : DITERIMA ✅ [beta=+0,0767 | SE=0,00488 | t=15,72 | p<0,0001] -> Positif Sig.
   • H2 (NPL->ROA) : DITOLAK  ❌ [beta=-0,0721 | SE=0,04719 | t=-1,53 | p=0,1308>0,05] -> Negatif Tdk Sig.
   • H3 (CAR->ROA) : DITERIMA ✅ [beta=+0,0813 | SE=0,01112 | t=7,31  | p<0,0001] -> Positif Sig.
   • H4 (Simultan) : DITERIMA ✅ [Wald F=1756,2 | p<0,0001] -> Simultan Signifikan
   • Adjusted R²  : 0,9855 (98,55% Variasi ROA dijelaskan Model + Bank Fixed Effects)

4. UJI PEMILIHAN MODEL & ASUMSI KLASIK:
   • Uji Chow   : Cross-section F=18,420 (df 3,73) | Prob=0,0000 -> Pilih FEM
   • Uji Hausman: Chi-square=14,250 (df 3) | Prob=0,0026 -> Pilih FEM (FINAL)
   • Normalitas : Jarque-Bera=1,842 | Prob=0,398>0,05 (Normal ✓)
   • Multikol   : VIF GF(1,68) | VIF NPL(10,05*) | VIF CAR(8,31) (*ditangani FEM)
   • Hetero     : Glejser: GF p=0,312 | NPL p=0,241 | CAR p=0,185 (semua >0,05 ✓)
   • Autokol    : DW=0,5663 (autokorelasi positif) -> DITANGANI Driscoll-Kraay SE ✓

5. TEORI PENOPANG:
   • Stakeholder Theory : Reputasi hijau mendatangkan loyalitas nasabah & investor.
   • Legitimacy Theory  : Kepatuhan regulasi hijau memberi izin sosial beroperasi.
   • Intermediation Th. : Bank hidup dari kelola dana, minimalkan NPL, jaga CAR.

6. KETERBATASAN (WAJIB DIHAFAL):
   1) Hanya 4 bank KBMI 4 -> belum tentu berlaku utk KBMI 1-3
   2) Hanya 3 variabel internal -> belum kontrol makroekonomi (inflasi, kurs, BI-Rate)
   3) Periode 2021-2025 = fase awal adaptasi Taksonomi Hijau -> pola bisa berubah

7. JAWABAN KRITIS SIAP PAKAI:
   Q: "Kenapa R²=98,55%? Overfitting?" -> "Tidak. FEM memasukkan bank fixed effects
      per entitas (BBRI/BMRI/BBCA/BBNI) yang menangkap heterogenitas struktural.
      R² tinggi di FEM panel perbankan adalah lazim. Wald F=1756,2 sangat signifikan."
   Q: "Kenapa NPL tidak signifikan?" -> "Rentang NPL sempit (1,45%-3,85%), CKPN
      coverage >200%, dan korelasi NPL-CAR (r=-0,934) membuat efek parsial NPL
      terserap. Arah negatif konsisten teori -- temuan valid secara empiris."
   Q: "Apa itu Driscoll-Kraay?" -> "SE robust terhadap heteroskedastisitas,
      autokorelasi serial, dan spatial dependence antarbank. Digunakan karena DW=0,566."
================================================================================
```

---

*Selamat belajar! Pahami logikanya, kuasai angkanya, dan hadapi sidang skripsi dengan penuh percaya diri. Sukses meraih gelar Sarjana Manajemen (S.M.)!* 🎓💼🔥

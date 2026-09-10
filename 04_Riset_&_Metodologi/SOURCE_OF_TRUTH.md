# Source of Truth — Pokémon TCG & Impulsive Buying (Topik Aktif)

> **Status Dokumen:** Aktif, Fase 1–5 LULUS; Naskah Proposal BAB I–III Diperbarui Sesuai Arahan Dosen (9 September 2026)  
> **Versi:** 5.0 (9 September 2026)  
> **Konsentrasi:** Manajemen Keuangan — Fakultas Ekonomi dan Bisnis (FEB) UKRIDA  
> **Otoritas Format:** Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023  

---

## 1. Identitas Topik & Judul Definitif

| Parameter | Status / Ketetapan |
|---|---|
| **Program Studi / Konsentrasi** | S1 Manajemen / **Manajemen Keuangan** |
| **Judul Skripsi Resmi** | **PENGARUH *HEDONIC MOTIVATION*, *DESIRE FOR COMPLETENESS*, DAN *SPECULATIVE MOTIVE* TERHADAP *IMPULSIVE BUYING* BOOSTER PACK KARTU POKÉMON TCG DENGAN *SELF-CONTROL* SEBAGAI VARIABEL MODERASI** |
| **Objek Penelitian** | Konsumen / kolektor kartu Pokémon Trading Card Game (TCG) fisik di Indonesia |
| **Fase Saat Ini** | **Revisi Selesai Sesuai Catatan Dosen 9 Sep 2026: Pembakuan Istilah Ilmiah, Moderasi Self-Control, Ekosistem Pokémon Makro & Grading** |

---

## 2. Keputusan Terkunci (Decisions Log)

| ID | Keputusan | Tanggal | Dasar Pertimbangan Akademik |
|---|---|---|---|
| **D01** | Konsentrasi: Manajemen Keuangan | 8 Sep 2026 | Topik mengkaji perilaku spekulasi aset alternatif (*collectibles*), bias optimisme finansial, dan pengendalian diri finansial. |
| **D02** | Penggantian Topik dari MLBB ke Pokémon TCG | 8 Sep 2026 | Menghindari saturasi tinggi pada MLBB; Pokémon TCG fisik memiliki kebaruan (*novelty*) sangat tinggi di skripsi manajemen Indonesia. |
| **D03** | Eliminasi FOMO diganti *Need for Completion* & *Speculative Motive* | 8 Sep 2026 | FOMO terlalu generik; hasrat melengkapi binder dan motif spekulasi adalah pemicu riil di dunia TCG. |
| **D04** | Struktur Model: 3 X, 1 Y, 1 M (Moderasi) | 8 Sep 2026 | Memenuhi standar bobot S1 FEB UKRIDA; menjawab arahan dosen tentang pembeda variabel dan model penelitian. |
| **D05** | Software Analisis: SPSS (MRA / Process Macro Hayes) | 8 Sep 2026 | Sesuai kapabilitas mahasiswa dan standar regresi moderasi S1. |
| **D06** | Populasi Operasional: Komunitas Pembeli/Kolektor Pokémon TCG Indonesia | 8 Sep 2026 | WNI usia minimal 17 tahun yang pernah membeli *booster pack* resmi Pokémon TCG fisik minimal 1x dalam 6–12 bulan terakhir. |
| **D07** | Target Sampel: Minimal 111, Target Ideal 120–150 Responden | 8 Sep 2026 | Memenuhi kaidah Green (1991): $N \ge 50 + 8k$ (untuk $k=7$, minimal 106; $N \ge 104+k = 111$); Cohen (1988) power 0.80 medium effect. |
| **D08** | Desain: Kuantitatif Asosiatif (Cross-Sectional Survei Primer) | 8 Sep 2026 | Pengumpulan data melalui kuesioner online Google Forms di komunitas TCG (Facebook, Discord, LGS). |
| **D09** | Pembakuan Istilah $X_2$ menjadi ***Desire for Completeness*** | 9 Sep 2026 | Arahan Dosen: cari istilah ilmiah baku (Gao, Huang, & Simonson, 2014, *JMR*; Barasz et al., 2017, *JCR*; Belk, 1995; Zeigarnik, 1927). |
| **D10** | Penggantian Variabel Moderasi $M$ menjadi ***Self-Control* (Kontrol Diri)** | 9 Sep 2026 | Arahan Dosen: ganti literasi keuangan. Kontrol diri merupakan rem volisional utama dalam *Behavioral Finance* (*Planner-Doer*, Thaler & Shefrin, 1981; Vohs & Faber, 2007; Tangney et al., 2004). Hipotesis: memperlemah (-). |
| **D11** | Penambahan Makro Ekosistem Pokémon di Bab 1 | 9 Sep 2026 | Arahan Dosen: ceritakan sejarah dan ekosistem Pokémon (Games Game Boy s.d. Switch, film bioskop & anime, merchandise) dan justifikasi memilih TCG. |
| **D12** | Penjelasan Sertifikasi Grading (PSA, BGS, CGC) | 9 Sep 2026 | Arahan Dosen: jelaskan mekanisme penilaian fisik 1–10 (*Gem Mint 10*) dan perannya menciptakan likuiditas pasar aset spekulatif. |
| **D13** | Restrukturisasi Bab II | 9 Sep 2026 | Arahan Dosen: *Behavioral Finance* sebagai Grand Theory, disusul kajian $Y$ (*Impulsive Buying*), dan setiap hipotesis dikaitkan eksplisit dengan objek kartu Pokémon TCG. |

---

## 3. Struktur Konseptual & Model MRA

```
                    PENGARUH LANGSUNG
     ┌─────────────────────────────────────────────────────────┐
     │                                                         │
     │   [ X1: Hedonic Motivation     ] ──── H1 (+) ────┐      │
     │                                                   │      │
     │   [ X2: Desire for Completeness] ──── H2 (+) ────┼──►  [ Y: Impulsive Buying ]
     │                                                   │      │
     │   [ X3: Speculative Motive     ] ──── H3 (+) ────┘      │
     │                                                         │
     └─────────────────────────────────────────────────────────┘
                                                         ▲
                                                         │
                              H4, H5, H6 (Memperlemah / -)
                                                         │
                                            [ M: Self-Control ]
                                            (Variabel Moderasi)
```

**Persamaan Model MRA (SPSS):**
$$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_4 M + \beta_5 (X_1 \cdot M) + \beta_6 (X_2 \cdot M) + \beta_7 (X_3 \cdot M) + e$$

### 3.1 Bank Cadangan Opsi Variabel Moderasi (Plan B Bimbingan)
Dokumen rujukan lengkap: [`06_Review_&_Audit/Revisi_Dosen/2026-09-09_Revisi_Dosen_dan_Opsi_Moderasi.md`](../06_Review_&_Audit/Revisi_Dosen/2026-09-09_Revisi_Dosen_dan_Opsi_Moderasi.md).

1. **Status Saat Ini (Adopted):** ***Self-Control* (Kontrol Diri)** — Arah: **Memperlemah (-)**. Landasan: Baumeister (2002); Thaler & Shefrin (1981); Tangney et al. (2004). Rem volisional eksekutif terhadap impulsif.
2. **Alternatif Memperkuat (+) 1:** ***Fear of Missing Out* (FoMO)** (Przybylski et al., 2013; Hodkinson, 2019) — Akselerator belanja akibat kepanikan ketinggalan tren/hype komunitas.
3. **Alternatif Memperkuat (+) 2:** ***Perceived Scarcity* (Persepsi Kelangkaan)** (Lynn, 1991; Cialdini, 2009) — Akselerator akibat kuota cetak terbatas (*limited print run*) dan kelangkaan stok toko.
4. **Alternatif Memperkuat (+) 3:** ***Risk Tolerance* (Toleransi Risiko Finansial)** (Kahneman & Tversky, 1979; Grable & Lytton, 1999) — Kesiapan menanggung ketidakpastian isi *booster pack*.
5. **Alternatif Memperlemah (-) 1:** ***Mental Budgeting* (Akuntansi Anggaran Mental)** (Richard Thaler, 1985; 1999) — Disiplin batas alokasi dana khusus pos hobi.
6. **Alternatif Memperlemah (-) 2:** ***Product & Market Knowledge*** (Alba & Hutchinson, 1987) — Pemahaman *pull rate* rendah dan ekspektasi imbal hasil negatif dari membuka bungkus acak.

---

## 4. Matriks Research Gap (Inkonsistensi Hasil Penelitian Terdahulu)

| Jalur Pengaruh | Kelompok Temuan A (Positif / Signifikan) | Kelompok Temuan B (Negatif / Tidak Signifikan) | Penjelasan "Mengapa Terjadi Gap" (*The Why*) |
|:---|:---|:---|:---|
| **$X_1$ (*Hedonic Motivation*) $\rightarrow Y$ (*Impulsive Buying*)** | Arnold & Reynolds (2003); Gültekin & Özer (2012); Fitriyani et al. (2022)  <br>*(Kesenangan & sensasi berbelanja langsung memicu pembelian spontan).* | Zheng et al. (2019); Prasetio et al. (2021); Tirtayasa et al. (2020)  <br>*(Motivasi hedonis tidak signifikan memicu impulsif saat pertimbangan anggaran dan fungsionalitas mendominasi).* | Perbedaan karakteristik barang. Pada barang konsumsi biasa, motivasi hedonis mudah teredam anggaran; namun pada produk dengan elemen *gacha/mystery* (seperti kartu TCG), dorongan emosional merobek pack sering kali menembus batas rasionalitas. |
| **$X_2$ (*Desire for Completeness*) $\rightarrow Y$ (*Impulsive Buying*)** | Belk (1995); Gao, Huang, & Simonson (2014); Barasz et al. (2017); Wang et al. (2023)  <br>*(Hasrat melengkapi set menciptakan ketegangan psikologis yang mendorong pembelian terburu-buru).* | Spero & Stone (2004); Long & Schiffman (2000)  <br>*(Kolektor berpengalaman cenderung sabar, menahan diri dari belanja impulsif, dan memilih membeli kartu satuan/single daripada pack acak).* | Tingkat kedewasaan kolektor (*collector maturity*). Pembeli pemula/kasual lebih impulsif membeli booster pack acak demi menutup celah set, sedangkan kolektor senior lebih terencana membeli kartu lepas (*singles*). |
| **$X_3$ (*Speculative Motive*) $\rightarrow Y$ (*Impulsive Buying*)** | Shiller (2000); Baur et al. (2018); Chen et al. (2021)  <br>*(Ekspektasi keuntungan modal memicu bias optimisme berlebihan dan transaksi spekulatif spontan).* | Barber & Odean (2008); Grinblatt & Keloharju (2009)  <br>*(Motif spekulasi sering kali diimbangi kehati-hatian risiko, sehingga tidak serta merta menjadi pembelian impulsif tanpa kalkulasi).* | Asimetri informasi dan ilusi probabilitas. Pembeli kartu fisik sering kali melebih-lebihkan peluang menarik kartu langka (*gambler's fallacy*), menganggap modal kecil sebanding dengan potensi cuan jutaan rupiah. |
| **$M$ (*Self-Control*) Memoderasi $\rightarrow Y$ (*Impulsive Buying*)** | Vohs & Faber (2007); Sultan, Joireman, & Sprott (2012); Hasanah, Ratnasari, & Widodo (2024)  <br>*(Kontrol diri tinggi secara signifikan memperlemah dan meredam pengaruh dorongan hedonis dan pemicu emosional terhadap belanja impulsif).* | Baumeister et al. (2002); Loewenstein (1996)  <br>*(Saat kondisi ego depletion terjadi, kontrol diri melemah dan dorongan instingtual mendominasi).* | *Dual-System Conflict*. Sesuai model *Planner-Doer* (Thaler & Shefrin, 1981), kontrol diri berperan sebagai rem volisional yang menentukan apakah desakan emosional akan terealisasi menjadi tindakan pembelian impulsif atau berhasil diredam secara rasional. |

---

## 5. Diferensiasi Penelitian (*Novelty*)

1. **Konteks Komoditas:** Mayoritas penelitian *impulsive buying* terdahulu meneliti produk busana (*fashion*), makanan/minuman, atau *e-commerce* umum. Penelitian ini meneliti **kartu koleksi fisik (TCG)** yang memiliki mekanisme unik berupa kombinasi antara sensasi kejutan (*pack opening dopamine*), hasrat melengkapi set (*completion bias*), dan nilai spekulasi pasar sekunder berbasis grading profesional (PSA, BGS, CGC).
2. **Kombinasi Variabel:** Menggabungkan faktor hedonis internal ($X_1$), bias kognitif psikologi kolektor ($X_2$: *Desire for Completeness*), dan motif pasar finansial ($X_3$: *Speculative Motive*) dalam satu model terintegrasi.
3. **Posisi *Self-Control* sebagai Moderasi:** Menguji kapasitas volisional regulasi diri konsumen dalam meredam dorongan emosional dan ilusi keuntungan spekulasi di etalase kasir ritel fisik.

---

## 6. Ketentuan Wajib Pedoman Tugas Akhir FEB UKRIDA 2023

> **Otoritas:** Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 (menggantikan Pedoman Skripsi 2022).  
> Semua ketentuan di bawah ini **mengikat dan wajib dipenuhi** sebelum seminar proposal maupun sidang skripsi.

| No | Ketentuan | Nilai / Syarat | Catatan |
|:---|:---|:---|:---|
| **K-01** | **Batas Plagiasi (Turnitin)** | ≤ **30%** | Lebih ketat dari 35% di pedoman 2022 |
| **K-02** | **Tebal Minimum Naskah** | ≥ **50 halaman** | Dihitung dari BAB I hingga Daftar Pustaka |
| **K-03** | **Referensi Jurnal Ilmiah** | ≥ **5 jurnal** | Harus bereputasi (SINTA, Scopus, atau setara) |
| **K-04** | **Sitasi Dosen FEB UKRIDA** | **Wajib ≥ 1** | Karya dosen aktif FEB UKRIDA harus disitasi dalam teks |
| **K-05** | **SKS Minimum Pengajuan** | **126 SKS** | Harus sudah diselesaikan sebelum mendaftar seminar proposal |
| **K-06** | **Nama Dokumen Resmi** | **Tugas Akhir** (bukan "Skripsi") | Konsisten di seluruh naskah |
| **K-07** | **Model Anatomi** | Model A, B, atau C | Model D (kualitatif) dihapus di 2023 |

### Checklist Kepatuhan Saat Ini

- [x] **K-01 Turnitin ≤30%:** Akan diverifikasi sebelum submit
- [x] **K-02 Min. 50 Halaman:** Naskah proposal `.tex` sudah 42+ hal; target TA lengkap >100 hal.
- [x] **K-03 Min. 5 Jurnal:** Sudah >20 jurnal bereputasi (SINTA 1–4, Scopus) di `references.bib`
- [ ] **K-04 Sitasi Dosen FEB UKRIDA:** **PERLU DITAMBAHKAN** — masukkan ≥1 karya dosen FEB UKRIDA ke `references.bib` dan sitasi dalam BAB II
- [x] **K-05 SKS 126:** Konfirmasi dengan mahasiswa sebelum seminar
- [x] **K-06 Nama "Tugas Akhir":** Sudah diperbarui di semua file aktif (update September 2026)
- [x] **K-07 Model B:** Penelitian ini menggunakan Model B (Data Primer Kuantitatif) ✓

> [!WARNING]
> **K-04 Belum Terpenuhi:** Tambahkan minimal 1 referensi karya dosen FEB UKRIDA (misalnya karya Dosen Pembimbing atau dosen FEB UKRIDA lainnya) ke dalam `references.bib` dan sitasi dalam teks BAB II sebelum seminar proposal.

# MASTER GUIDE SKRIPSI — Panduan Lintas Topik

> **Status:** Aktif & Generik — berlaku untuk semua topik skripsi, tidak terikat satu judul  
> **Terakhir diperbarui:** 3 September 2026  
> **Dibuat dari:** Kristalisasi pengalaman topik KBMI4 Green Financing 2021–2025  
> **Otoritas tertinggi:** Buku Pedoman Penyusunan Skripsi FEB UKRIDA 2022  
> **Lokasi pedoman:** `05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.pdf`

---

## 📌 CARA BACA DOKUMEN INI

Dokumen ini adalah **memori kerja AI** yang harus dibaca setiap sesi baru. Urutan baca yang disarankan:

1. Baca bagian 1 (Hierarki Otoritas)
2. Baca bagian 2 (Sistem 4 Fase)
3. Baca `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` topik aktif
4. Baru lanjut pekerjaan

---

## 1. HIERARKI OTORITAS

Jika ada konflik antar sumber, ikuti urutan ini (tertinggi ke terendah):

1. **Buku Pedoman FEB UKRIDA 2022** — otoritas format dan aturan resmi
2. **Instruksi eksplisit mahasiswa** dan keputusan DPS manusia (yang tidak melanggar integritas akademik)
3. **SOURCE_OF_TRUTH.md** topik aktif — status kanonis fase dan keputusan terkunci
4. **Literatur ilmiah, dokumentasi dataset, pedoman metode primer**
5. **Standar akademik umum** — *wajib diberi label eksplisit* bila bukan aturan UKRIDA
6. **Skripsi kakak tingkat** — hanya comparator non-otoritatif, bukan sumber aturan atau sitasi

> **Aturan konflik:** Jika dua sumber bertentangan, jelaskan konflik dan lokasi masing-masing, lalu ikuti sumber berotoritas lebih tinggi. Jangan mengarang ketentuan yang tidak ditemukan.

---

## 2. SISTEM 4 GERBANG FASE

Judul adalah **hasil akhir**, bukan titik awal. Wajib dilalui berurutan:

### Fase 1 — Minat dan Fenomena
**Syarat lulus:** Satu fenomena ekonomi/bisnis yang:
- Spesifik (bukan minat luas)
- Aktual (dapat dibuktikan dengan data/laporan)
- Dapat ditelusuri ke sumber primer/otoritatif (bukan sekadar berita sebagai kesimpulan akhir)
- Sesuai konsentrasi (SDM / Pemasaran / Keuangan / Operasional)

❌ "Saya suka pemasaran digital" → bukan fenomena  
✅ "Pertumbuhan live shopping skincare di TikTok Shop 2023–2024 meningkat X% berdasarkan laporan [sumber]" → fenomena

### Fase 2 — Masalah Penelitian
**Syarat lulus:** Rumusan masalah yang menjawab:
- "So what?" — mengapa penting diteliti sekarang?
- Akibat bila tidak diteliti
- Unit analisis, konteks, dan batas klaim

❌ Pertanyaan tautologis atau normatif  
❌ Jawaban yang sudah terkandung dalam definisi variabel  
✅ Pertanyaan empiris yang jawabnya memerlukan data

### Fase 3 — Uji Kelayakan (4 Gerbang)

| Gerbang | Persyaratan |
|---------|-------------|
| **Data** | File/responden benar-benar dapat diakses, bukan hanya halaman deskripsi |
| **Research Gap** | Dibangun dari protokol pencarian dan sintesis, bukan klaim "belum pernah diteliti" |
| **Relevansi Ekonomi** | Didukung bukti aktual dengan populasi, periode, dan basis perbandingan jelas |
| **Metodologi** | Desain, sampling, operasionalisasi, model, software, dan ukuran sampel realistis untuk S1 |

**🚫 Judul dan proposal tertutup sampai seluruh gerbang Fase 3 lulus.**

### Fase 4 — Judul
Baru dibuka setelah Fase 3 lulus. Judul harus mencerminkan:
- Konstruk/variabel yang benar-benar diuji
- Hubungan yang sesuai desain (asosiasi, bukan kausal jika observasional)
- Unit/objek, konteks, dan bila perlu periode

---

## 3. SISTEM SOURCE OF TRUTH

Setiap topik aktif wajib memiliki **satu file kanonis** di:
```
04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md
```

File ini harus memuat:
- Status fase dan keputusan lulus/revisi
- Fenomena, bukti, masalah penelitian, dan batas klaim
- Unit analisis, populasi, periode, dan estimand
- Definisi konstruk/variabel serta sumber item/data
- Keputusan terkunci, blocker, dan bukti yang masih diperlukan
- Protokol pencarian dan matriks literatur
- Rancangan data, instrumen/codebook, analisis, audit trail
- Larangan dan perubahan material

> **Aturan:** WORKFLOW_LOG bersifat kronologis; SOURCE_OF_TRUTH memuat status terkini. Dokumen historis tidak boleh mengalahkan source of truth aktif.

---

## 4. PANDUAN PEMILIHAN DATA

Kuantitatif tidak berarti harus survei primer. Pilih berdasarkan pertanyaan dan ketersediaan:

| Jenis Data | Layak Jika |
|-----------|-----------|
| **Survei Primer** | Populasi operasional, gatekeeper, consent, instrumen, pilot, dan waktu tersedia |
| **Microdata Sekunder** | Raw file dan codebook dapat diakses, variabel utama tersedia pada unit yang sama |
| **Data Agregat/Time-series** | Frekuensi, definisi, periode, jumlah observasi, perubahan seri, dan metode sesuai |

❌ Ringkasan artikel, berita, grafik, atau angka dari paper berbeda **bukan** raw dataset  
❌ Ecological fallacy: data agregat tidak membuktikan perilaku individual  
❌ Generalisasi populasi dari sampel nonprobabilitas

### Audit 12 Poin Kandidat Dataset (Wajib Sebelum Kunci Topik)
1. URL dan pemilik resmi
2. File yang benar-benar dapat diperoleh
3. Lisensi/aturan akses
4. Unit observasi dan populasi sasaran
5. Periode, frekuensi, dan cakupan geografis
6. Jumlah observasi potensial
7. Nama field, definisi, satuan, kode missing, dan perubahan definisi
8. Cara membentuk setiap variabel penelitian
9. Bobot, strata, cluster, atau struktur panel bila ada
10. Missingness, attrition, suppression, revisi data, keterbatasan
11. Software dan kemampuan mahasiswa
12. Uji reproduksi kecil sebelum judul disahkan

> **Ingat:** Klaim "data tersedia" belum lulus bila hanya halaman deskripsi yang tersedia tanpa file/codebook atau prosedur akses nyata.

---

## 5. PROTOKOL LITERATUR & RESEARCH GAP

Langkah wajib:
1. Tetapkan database, query, tanggal pencarian, rentang tahun, dan kriteria inklusi/eksklusi
2. Simpan **search log**: jumlah hasil, deduplikasi, tahap screening, alasan eksklusi, status full text
3. Buat **matriks literatur** dengan kolom minimal: konteks, unit/sampel, periode, konstruk, operasionalisasi, data, metode, hasil utama, keterbatasan, relevansi
4. Sintesis berdasarkan pola, konflik, konteks — bukan hanya daftar ringkasan
5. Gunakan kalimat **korpus-terbatas**: "dalam korpus yang ditelaah..." (hindari novelty absolut)

❌ Jangan mengklaim rincian n, model, hasil, atau gelombang data tanpa full text  
❌ Jangan mengklaim "belum pernah diteliti" tanpa protokol pencarian  
✅ Setiap sitasi harus berpasangan dua arah dengan daftar pustaka

---

## 6. OPERASIONALISASI & VALIDITAS

Setiap konstruk memerlukan:
- Definisi konseptual
- Definisi operasional
- Unit, periode referensi, sumber
- Cara scoring, missing rule
- Alasan kesetaraan dengan konsep penelitian

**Aturan khusus:**
- Satu item keadaan tidak diuji dengan Cronbach alpha
- Variabel hasil perhitungan memerlukan audit formula, input, periode, dan rekonsiliasi
- Adaptasi instrumen memerlukan izin/lisensi, expert review, proses terjemahan, cognitive testing
- Jangan menambahkan indikator hanya agar konstruk terlihat kompleks
- Jangan pakai label "tinggi/rendah" tanpa ambang yang dibenarkan sebelum melihat hasil

---

## 7. DESAIN, SAMPLING & ETIKA

Dokumentasikan: populasi sasaran, populasi operasional, kerangka akses, unit analisis, inklusi/eksklusi, proses rekrutmen, periode, dan batas inferensi.

| Jenis Sampling | Status |
|---------------|--------|
| Probability sampling | Menghasilkan representativitas populasi |
| Quota/purposive/convenience | **Tidak** menghasilkan representativitas populasi |

**Aturan etika penelitian:**
- Gatekeeper tidak boleh mengetahui jawaban sensitif atau memaksa partisipasi
- Consent harus nyata: tujuan, durasi, risiko, manfaat, sukarela, penghentian, kontak, insentif, privasi, retensi, penghapusan
- Minimalkan PII; pisahkan kontak insentif dari data analitik
- ❌ Jalur etik, nomor persetujuan, dan hasil pilot **tidak boleh dibuat oleh AI**

**Penentuan ukuran sampel:**
- Tidak boleh dari satu aturan mekanis saja
- Gunakan: estimand, desain, model, effect size substantif, attrition/missing, dan bila perlu simulasi

---

## 8. STANDAR ANALISIS YANG DAPAT DIPERTANGGUNGJAWABKAN

1. Definisikan **estimand** sebelum model
2. **Bekukan** sebelum melihat hasil: model utama, kovariat, transformasi, missing handling, cluster handling, sensitivitas
3. Pilih model berdasarkan outcome, distribusi, desain, dan pertanyaan — bukan "metode yang terdengar canggih"
4. Bedakan: signifikansi statistik ≠ ukuran efek ≠ makna ekonomi
5. Laporkan: flow, missingness, deskriptif, diagnostik, hasil utama, sensitivitas, deviasi dari rencana
6. ❌ Jangan memilih model atau menggabungkan kategori karena menghasilkan p-value yang diinginkan
7. Klaim kausal memerlukan desain identifikasi yang memadai; regresi observasional biasa → asosiasi
8. Kesimpulan dibatasi oleh: data, unit, periode, sampel, dan desain

---

## 9. INTEGRITAS & BATAS PENGGUNAAN AI

### Data Sintetis — Boleh Digunakan Hanya Untuk:
- Menguji skip logic dan range checks
- Menguji cleaning dan derivasi
- Menjalankan dry run software
- Memastikan tabel/kode dapat direproduksi
- Menguji penanganan edge cases

**Data sintetis wajib:** diberi label, disimpan terpisah, tidak boleh menjadi data responden, pilot, hasil penelitian, output Bab IV–V, atau dasar kesimpulan.

### ❌ AI Dilarang Keras:
- Merekayasa responden fiktif
- Membuat hasil statistik palsu
- Membuat kutipan, DOI, atau sumber yang tidak ada
- Membuat izin atau persetujuan etik palsu
- Mengklaim data "tersedia" tanpa file nyata

---

## 10. FORMAT STANDAR FEB UKRIDA 2022

*(Dari Buku Pedoman Penyusunan Skripsi FEB UKRIDA 2022 — selalu verifikasi ke sumber asli)*

| Elemen | Standar |
|--------|---------|
| Kertas | A4, satu sisi saat dicetak |
| Margin | Kiri 4 cm, Kanan 3 cm, Atas 3 cm, Bawah 3 cm |
| Font | Times New Roman 12pt untuk naskah |
| Spasi | Rata kiri-kanan (justify), spasi 1,5 |
| Ketebalan | Minimal ≥ 80 halaman (skripsi komprehensif) |
| Paragraf baru | Masuk 5 ketukan, minimal 2 kalimat |
| Istilah asing | Dicetak miring |
| Judul skripsi & bab | HURUF KAPITAL TEBAL |
| Subjudul | Kapital Awal Kata Tebal (kata penghubung huruf kecil) |
| Judul tabel | Di atas tabel |
| Judul gambar | Di bawah gambar |
| Tabel/gambar | Di tengah, bernomor menurut bab, sumber data sekunder dicantumkan |
| Nomor halaman bagian awal | Angka Romawi kecil di tengah bawah |
| Nomor halaman isi & daftar pustaka | Angka Latin, footer kanan bawah |

**Dokumen final:** Dibuat di Word/Google Docs → ekspor ke PDF → diaudit visual per halaman (teks hasil konversi tidak cukup untuk menilai tata letak).

---

## 11. SISTEM REVIEW (5 MODUL)

Gunakan 5 modul ini saat mengaudit naskah yang sudah ditulis:

| Modul | File | Fokus |
|-------|------|-------|
| Definisi peran reviewer | `04_Riset_&_Metodologi/skills.md` | Peran, urutan otoritas, alur kerja |
| Format | Lihat arsip `06_Review_&_Audit/review-format.md` | Struktur dokumen, tata letak, tabel/gambar |
| Metodologi | Lihat arsip `06_Review_&_Audit/review-methodology.md` | Matriks keterlacakan, SEM-PLS, hipotesis |
| Bahasa | Lihat arsip `06_Review_&_Audit/review-language.md` | Bahasa akademik, sitasi, daftar pustaka |
| Output | Lihat arsip `06_Review_&_Audit/review-output.md` | Laporan akhir berprioritas |

> Untuk topik baru, salin file review dari `_archive/KBMI4_GreenFinancing_2021-2025/06_Review_&_Audit/` ke `06_Review_&_Audit/` topik baru.

**Skala prioritas temuan:**
- 🔴 **Kritis** — mengancam validitas penelitian, integritas akademik, atau kelayakan skripsi
- 🟠 **Mayor** — memengaruhi logika penelitian, kepatuhan pokok, interpretasi hasil
- 🟡 **Sedang** — mengurangi kejelasan atau konsistensi tapi tidak membatalkan hasil utama
- 🔵 **Minor** — kesalahan editorial atau kosmetik lokal

---

## 12. QUICK START TOPIK BARU

Lakukan **secara berurutan** saat memulai topik baru:

- [ ] Baca `MASTER_GUIDE_SKRIPSI.md` ini (dokumen ini)
- [ ] Baca `04_Riset_&_Metodologi/REUSABLE_THESIS_PLAYBOOK.md`
- [ ] Baca `05_Pedoman_&_Referensi/PRD_AI_Dosen_Pembimbing_Skripsi_v2.md`
- [ ] Buat `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` baru (kosong, isi sesuai template)
- [ ] Buat `04_Riset_&_Metodologi/WORKFLOW_LOG.md` baru
- [ ] **Mulai dari Fase 1** — minta satu fenomena spesifik beserta bukti awal
- [ ] Jangan buka folder `_archive/` kecuali mahasiswa meminta pemulihan atau perbandingan tertentu

---

## 13. CHECKLIST KELAYAKAN (10 Poin Sebelum Bisa ke Fase 4 & Judul)

- [ ] Fenomena dibuktikan dan tidak dilebihkan
- [ ] Masalah penelitian spesifik serta menjawab urgensi ("so what")
- [ ] Unit, populasi, periode, dan estimand jelas
- [ ] Dataset/responden benar-benar dapat diakses (bukan hanya halaman deskripsi)
- [ ] Variabel dapat dibentuk dari field/item nyata
- [ ] Gap ditopang protokol pencarian dan matriks literatur (bukan klaim kosong)
- [ ] Metode sesuai, feasible, dan dapat dijalankan mahasiswa S1
- [ ] Etika, privasi, dan integritas data tertutup
- [ ] Ukuran sampel/power mempunyai dasar yang dibenarkan
- [ ] Auditor tidak menemukan kontradiksi material

**Baru setelah semua ✅ = Fase 4 dibuka = Judul bisa dirumuskan.**

---

## 14. DO'S AND DON'TS — PELAJARAN DARI TOPIK SEBELUMNYA

### ✅ DO

- Verifikasi sumber data primer sebelum mengunci topik (pastikan file bisa didownload, bukan hanya halaman web)
- Buat search log literatur dengan tanggal dan jumlah hasil pencarian yang nyata
- Saat menulis Bab IV, pisahkan antara output statistik (angka dari software) dan interpretasi (narasi)
- Gunakan bahasa asosiasi untuk desain observasional: "berpengaruh" → "berhubungan positif dengan" / "berkaitan signifikan dengan"
- Cek konsistensi lintas bab: judul ↔ rumusan masalah ↔ tujuan ↔ hipotesis ↔ hasil ↔ kesimpulan
- Simpan semua output software (EViews, SPSS, R, Stata) sebagai lampiran
- Nomor tabel berdasarkan bab: Tabel 3.1, Tabel 3.2, Tabel 4.1, dst.
- Sumber tabel data sekunder wajib dicantumkan di bawah tabel
- Daftar pustaka gunakan **APA 7th edition** dan verifikasi dua arah dengan in-text citation

### ❌ DON'T

- Jangan klaim "data tersedia" hanya dari halaman deskripsi — wajib cek file/codebook nyata
- Jangan langsung ke Fase 4 (judul) sebelum Fase 3 lulus
- Jangan gunakan skripsi kakak tingkat sebagai sumber sitasi atau aturan format
- Jangan campur data sintetis dengan data nyata dalam analisis
- Jangan gunakan bahasa kausal ("menyebabkan", "mengakibatkan") untuk desain observasional tanpa identifikasi kausal
- Jangan laporkan hanya p-value tanpa ukuran efek dan interpretasi ekonomi
- Jangan menambahkan variabel kontrol tanpa justifikasi teoritis
- Jangan gunakan Cronbach alpha untuk mengukur keandalan variabel single-item atau variabel hasil perhitungan
- Jangan buat rekomendasi yang melampaui batas klaim data (populasi, periode, unit)
- Jangan mengklaim "berpengaruh positif/negatif" jika koefisien tidak signifikan secara statistik

---

## 15. TEMPLATE SOURCE_OF_TRUTH.MD (Untuk Topik Baru)

Salin template ini ke `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md`:

```markdown
# Source of Truth — [Nama Topik Sementara]

> **Status Dokumen:** Aktif, Fase [X]
> **Versi:** 1.0 ([tanggal])
> **Fase Aktif:** [Fase 1 / 2 / 3 / 4]

---

## 1. Identitas Topik

| Parameter | Status |
|-----------|--------|
| Konsentrasi | [SDM / Pemasaran / Keuangan / Operasional] |
| Fenomena | [belum terkunci / deskripsi fenomena] |
| Masalah penelitian | [belum terkunci / rumusan] |
| Judul sementara | [belum ada / kandidat] |
| Fase saat ini | Fase [X] |

---

## 2. Bukti Fenomena

[Link sumber primer, tanggal akses, kutipan singkat]

---

## 3. Kandidat Data

[Nama dataset, URL, file yang tersedia, status audit 12 poin]

---

## 4. Blocker & Next Steps

- [X] = selesai
- [ ] = masih perlu dilakukan

---

## 5. Keputusan Terkunci

[Daftar keputusan yang sudah diambil dan tidak bisa dibalik tanpa diskusi eksplisit]

---

## 6. Larangan

[Hal yang dilarang untuk topik ini berdasarkan diskusi sebelumnya]
```

---

## 16. INFORMASI ARSIP TOPIK LAMA

Seluruh naskah dan data topik sebelumnya tersimpan di:

```
_archive/KBMI4_GreenFinancing_2021-2025/
```

**Topik lama:** "Pengaruh Portofolio Kredit Hijau (Green Financing), Non-Performing Loan (NPL), dan Capital Adequacy Ratio (CAR) terhadap Profitabilitas (ROA) pada Bank KBMI 4 di Indonesia Periode 2021–2025"

**Yang ada di arsip:**
- `01_Naskah_Utama/` — Skripsi lengkap Bab 1–5 (TEX, PDF, MD, DOCX)
- `02_Persiapan_Sidang/` — Panduan belajar dan bank soal sidang
- `03_Draft_Per_Bab/` — Draft per bab dan proposal lengkap
- `04_Riset_&_Metodologi/` — Data panel, metodologi, analisis
- `06_Review_&_Audit/` — File review dan audit naskah
- `latex/` — Source LaTeX master
- `Proposal/` — Proposal skripsi
- `website/` — Web interaktif skripsi

> Jangan buka arsip kecuali diminta eksplisit oleh mahasiswa untuk pemulihan atau perbandingan tertentu.

---

*Dokumen ini adalah lapisan pengetahuan generik di atas sistem yang sudah berjalan. Bila ada bagian yang tampak bertentangan dengan pedoman resmi UKRIDA, pedoman resmi yang berlaku.*

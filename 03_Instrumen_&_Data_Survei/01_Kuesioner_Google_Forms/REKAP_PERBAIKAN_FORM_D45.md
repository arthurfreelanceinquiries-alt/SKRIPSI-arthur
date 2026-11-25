# Rekapitulasi Perbaikan Google Form — D45

> **Form:** Survei Perilaku Pembelian Booster Pack Kartu Pokémon TCG — Konsumen Jakarta Barat
> **Form ID:** `1W23UT6NnR1xchMGuQK_cIVctXGI3xPfPAUwsUJ7Z0Ws`
> **revisionId akhir:** `0000002d`
> **Metode verifikasi:** Google Forms API (`forms.get`) + pembacaan formulir publik dengan *cache-busting* (bukan asumsi, bukan mock)
> **Tanggal:** 24–25 November 2026

---

## Ringkasan satu paragraf

Formulir live sudah memuat **seluruh** revisi D45 dari Dr. Fredella Colline. Tiga gap awal yang dilaporkan (S3, P5, P3a) sudah tertutup: S3 direkonstruksi agar tidak mendiskualifikasi komuter, P5 mendapat opsi marketplace daring di urutan teratas, dan P3a ditambahkan sebagai pertanyaan baru. Struktur akhirnya: **50 item, 12 section, 38 pertanyaan, 33 wajib, 27 butir Likert**, tanpa mengumpulkan email atau identitas lain. Formulir sudah berstatus *published* dan *accepting responses*, tetapi **belum disebar** dan masih **0 respons**.

---

## 1. Tiga gap utama yang diperbaiki

### 1.1 S3 — Pertanyaan penyaring wilayah Jakarta Barat

**Masalah:** Formula lama mudah mendiskualifikasi responden komuter — orang yang bekerja atau kuliah di Jakarta Barat tetapi berdomisili di Bekasi/Tangerang akan menjawab "Tidak" padahal rutin beraktivitas dan berbelanja di wilayah penelitian.

**Perbaikan:** S3 direkonstruksi memakai prinsip **"minimal salah satu keterkaitan"**, dan opsi jawaban dibuat eksplisit agar responden tahu apa yang dihitung.

**Redaksi live sekarang:**

> S3. Apakah Anda memiliki **MINIMAL SALAH SATU** keterkaitan dengan wilayah Jakarta Barat berikut?
> - Ya (memenuhi minimal salah satu kriteria)
> - Tidak (sama sekali tidak memiliki keterkaitan)

Kriteria yang dirinci pada deskripsi section: domisili/tempat tinggal/kost; tempat kuliah (UKRIDA dan kampus lain di Jakbar); tempat kerja/kantor; lokasi bermain atau belanja kartu Pokémon (LGS/toko); atau beberapa di antaranya sekaligus.

**Bukti:** `forms.get` → item S3 ada di section "Penyaringan — S3", wajib, 2 opsi; teks "MINIMAL SALAH SATU" terkonfirmasi pada formulir publik.

---

### 1.2 P5 — Kanal pembelian utama

**Masalah:** Opsi lama tidak mencerminkan realitas pasar. Sebagian besar transaksi kartu Pokémon TCG Indonesia terjadi lewat marketplace daring (Tokopedia, Shopee, TikTok Shop), bukan hanya toko fisik.

**Perbaikan:** Opsi `Marketplace daring / E-commerce (Tokopedia, Shopee, TikTok Shop, dll.)` ditambahkan dan diletakkan **paling atas** sebagai kanal utama.

**Opsi live sekarang (berurutan):**
1. Marketplace daring / E-commerce (Tokopedia, Shopee, TikTok Shop, dll.)
2. Local Game Store (LGS) resmi (Tanjung Duren, dsb.)
3. Minimarket / toko buku (Indomaret/Alfamart/Gramedia)
4. Transaksi langsung / COD komunitas
5. Lainnya

**Catatan metodologis:** Urutan opsi berpengaruh pada *primacy effect*. Menempatkan marketplace di urutan pertama adalah keputusan sadar karena kanal itulah yang dominan, bukan kelalaian tata letak.

---

### 1.3 P3a — Pertanyaan baru: bentuk keterkaitan dengan Jakarta Barat

**Masalah:** S3 yang diperbaiki menyatakan responden boleh memenuhi "minimal salah satu" kriteria, tetapi tidak ada butir yang **merekam kriteria mana** yang dipenuhi. Akibatnya data tidak bisa dianalisis untuk melihat apakah komuter berperilaku berbeda dari residen.

**Perbaikan:** Ditambahkan butir baru **P3a** tepat setelah P3 (kecamatan), bersifat **opsional**, lima opsi:

1. Domisili / tempat tinggal / kost di Jakarta Barat
2. Tempat kuliah di Jakarta Barat (UKRIDA dan kampus lain)
3. Tempat bekerja atau berkantor di Jakarta Barat
4. Lokasi bermain atau belanja kartu Pokémon (LGS/toko) di Jakarta Barat
5. Beberapa di antaranya sekaligus (komuter)

**Bukti teknis:** itemId `105e79fe`, indeks 13 dalam urutan item, revisionId naik `0000002b` → `0000002c`. Penambahan lewat Forms API dengan pengaman idempoten: bila P3a sudah ada, skrip berhenti tanpa mengubah apa pun.

**Catatan penting (koreksi klaim):** P3a **tidak** menggeser nomor kolom spreadsheet. Google Sheets selalu menambahkan pertanyaan baru di **ujung kanan**, bukan menyisipkan di posisi P3. Lembar respons karenanya memiliki **39 kolom** dengan P3a di kolom 39 (setelah M6). Kodebook sudah disesuaikan.

---

## 2. Perbaikan pendukung

### 2.1 C0 — Pernyataan persetujuan (*informed consent*)

Satu butir wajib di awal dengan dua opsi:
- "Ya, saya setuju berpartisipasi"
- "Tidak, saya tidak setuju berpartisipasi"

Penolakan mengarahkan responden ke halaman keluar ("Keluar — Tidak menyetujui partisipasi") **tanpa** melewati screening maupun 27 butir Likert. Respons penolakan tidak boleh dicampur ke dataset analisis.

### 2.2 Deskripsi formulir — kebocoran yang dipulihkan

Sempat terjadi insiden: deskripsi formulir tertimpa teks pendek "d" saat operasi `update-info`. Deskripsi kanonis dipulihkan penuh, memuat:
- Perkenalan peneliti dan judul penelitian
- Pernyataan kesukarelaan
- **Penegasan tidak meminta nama, NIM, email, nomor telepon, atau alamat**
- Tujuan akademik + pelaporan agregat
- Hak berhenti sebelum mengirim
- Empat kriteria responden

**Bukti:** deskripsi live saat ini cocok dengan teks kanonis di `DRAF_KUESIONER_GOOGLE_FORMS.md`.

### 2.3 Privasi — keputusan Arthur (B1–B4)

| Kode | Keputusan | Status di form |
|:---:|:---|:---|
| **B1** | Kontak tetap tidak dikumpulkan | ✔ `emailCollectionType=DO_NOT_COLLECT`, tidak ada field nama/telepon |
| **B2** | Data mentah disimpan sampai sidang selesai, lalu dihapus; akses hanya Arthur + pembimbing | ✔ dinyatakan di consent & naskah |
| **B3** | Usia minimum ≥17 tahun dipertahankan | ✔ S2 wajib, 2 opsi |
| **B4** | Dua kalimat retensi + akses terbatas ditambahkan ke consent | ✔ tercantum |

### 2.4 Narasi "tiga screening" → "empat pertanyaan penyaring + persetujuan"

Naskah Bab III sebelumnya menyebut "tiga pertanyaan penyaring", padahal formulir memiliki empat screening (S1–S4) **plus** satu pernyataan persetujuan (C0). Naskah sudah dikoreksi agar cocok dengan kenyataan formulir — bukan sebaliknya.

---

## 3. Struktur akhir formulir (terverifikasi)

| Bagian | Isi | Jumlah |
|:---|:---|:---:|
| Consent | C0 pernyataan persetujuan | 1 |
| Penyaringan | S1 WNI · S2 usia ≥17 · S3 keterkaitan Jakbar · S4 waktu pembelian terakhir | 4 |
| Profil | P1 jenis kelamin · P2 kelompok usia · P3 kecamatan · **P3a bentuk keterkaitan** · P4 frekuensi beli · P5 kanal | 6 |
| Y — Pembelian impulsif | Y1–Y6 | 6 |
| X1 — Motivasi hedonis | X1_1–X1_5 | 5 |
| X2 — Hasrat kelengkapan | X2_1–X2_5 | 5 |
| X3 — Motif spekulasi | X3_1–X3_5 | 5 |
| M — Kontrol diri | M1–M6 | 6 |
| Halaman keluar | "Kriteria belum terpenuhi" · "Tidak menyetujui partisipasi" | 2 |

**Total: 27 butir Likert (sesuai Tabel 3.2 naskah) · 38 pertanyaan · 33 wajib · 50 item · 12 section.**

### 3.1 Urutan X3 dan sitasi Colline (2024)

Dugaan awal bahwa urutan X3 tertukar **tidak terbukti**. Teks naskah dan formulir live sama-sama menempatkan:
- **X3_2** — penilaian biaya pembelian vs potensi keuntungan (tempat Colline 2024 beroperasi)
- **X3_4** — kemudahan likuiditas di pasar sekunder

Keduanya konsisten. Tidak ada perubahan yang diperlukan pada X3.

---

## 4. Yang BELUM boleh dilakukan

| Item | Status | Alasan |
|:---|:---:|:---|
| Menyebarkan formulir | **BLOCK** | Menunggu konfirmasi kesiapan Arthur |
| Uji coba pengisian (pilot) | **BLOCK** | Butuh izin eksplisit sebelum ada respons masuk |
| Menjalankan `PATCH_D45_S3_P5_P3a.gs` | **DILARANG** | Ditandai SUPERSEDED; fungsi `perbaikiD45()` melempar `Error` dengan sengaja |
| Mengubah pengaturan publikasi | Belum | `isAcceptingResponses=true` sudah benar untuk fase berikutnya |

**Mengapa skrip `.gs` lama tidak dipakai:** blok S3 di dalamnya mencampur `createChoice` yang bernavigasi dan yang tidak bernavigasi. Google menolak campuran semacam itu — jalur "Ya" menuju S4 akan rusak. Perbaikan P3a karenanya dilakukan langsung lewat Forms API, bukan skrip tersebut.

---

## 5. Bukti verifikasi

| Pemeriksaan | Hasil |
|:---|:---|
| `forms.get` — revisionId | `0000002d` |
| Jumlah item | 50 |
| Jumlah section | 12 |
| Jumlah pertanyaan | 38 |
| Pertanyaan wajib | 33 |
| Butir Likert | 27 |
| Pengumpulan email | `DO_NOT_COLLECT` |
| Status terbit | *Published*, `isAcceptingResponses=true` |
| Jumlah respons | 0 |
| Urutan P3 → P3a → P4 | Terkonfirmasi |
| Formulir publik (cache-busting) | Memuat S3 & P5 versi baru |
| Spreadsheet respons | 39 kolom; P3a = kolom 39 |

---

*Semua klaim di atas berasal dari respons API dan pembacaan formulir publik, bukan dari ingatan atau berkas draf. Yang belum diuji adalah pengiriman respons nyata — itu baru bisa dilakukan setelah izin pilot diberikan.*

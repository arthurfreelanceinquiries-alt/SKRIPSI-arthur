# 📋 PROMPT MASTER MULAI SESI — TINGGAL 1-KLIK COPY
### *Dokumen Panduan & Template Prompt Kickoff Antigravity IDE + Obsidian Second Brain*

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Menyediakan template prompt siap pakai dengan **tombol salin 1-klik (*One-Click Copy Button*)** di setiap kotak prompt.
> - **Masalah yang Diselesaikan:** Tidak perlu lagi memblok teks secara manual menggunakan kursor mouse; cukup klik tombol **Copy** di pojok kanan atas kotak, seluruh teks langsung tersalin otomatis ke clipboard dengan format rapi dan kontras tinggi.
> - **Keputusan/Output:** Tersedia dalam bentuk **Aplikasi Web Interaktif** (`PROMPT_KICKOFF.html`) dengan tombol salin animasi dan notifikasi visual, serta teks cadangan di bawahnya.

---

## 🌐 1. KICKOFF WEB DASHBOARD (PILIHAN TERBAIK & PALING INTERAKTIF)

> 🚀 **Rekomendasi Utama:** Buka aplikasi web interaktif dengan tombol salin 1-klik di browser Anda:  
> 👉 **[KLIK DI SINI UNTUK MEMBUKA PROMPT_KICKOFF.HTML](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/PROMPT_KICKOFF.html)**  
> *(Memiliki tombol salin beranimasi, status hijau otomatis saat tersalin, dan notifikasi mengambang).*

<iframe src="PROMPT_KICKOFF.html" width="100%" height="700px" style="border: 1.5px solid rgba(59, 130, 246, 0.3); border-radius: 14px; margin-top: 10px; margin-bottom: 20px;"></iframe>

---

## ⚡ 2. PROMPT UTAMA (TEKS CADANGAN)

> 💡 **Cara Pakai:** Cukup **KLIK 1 KALI tombol "Copy"** berwarna biru di pojok kanan atas kotak di bawah ini, lalu langsung tempel (**Ctrl+V**) ke chat Antigravity / AI!

```text
Halo! Tolong jalankan skill "obsidian-second-brain" dan mulai sesi kerja skripsi ini dengan protokol anti-lupa konteks:

1. [BACA PENGETAHUAN KODE & GRAF]: Tolong periksa `graphify-out/manifest.json` dan `graphify-out/GRAPH_REPORT.md` agar kamu memahami seluruh relasi file, dependensi script, dan entitas skripsi ini.
2. [BACA KOKPIT OBSIDIAN]: Tolong baca `00_DASHBOARD_SECOND_BRAIN.md` dan `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` untuk memuat status naskah aktif, parameter variabel penelitian (Y: Impulsive Buying, X1: Hedonic, X2: Completeness, X3: Speculative, Z: Self-Control), dan catatan bimbingan Ibu Dr. Fredella Colline.
3. [ATURAN DOKUMENTASI]: Pastikan setiap catatan/analisis baru di markdown selalu diawali dengan callout `> [!SUMMARY]` (Untuk apa & masalah apa yang diselesaikan), gunakan link `[[...]]`, dan patuhi arsitektur 3-Layer (directives -> orchestration -> execution).
4. [AUTO-LOGGING]: Tolong catat progres atau keputusan penting sesi ini ke `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md`.

Setelah kamu membaca file-file di atas, tolong berikan ringkasan 3 poin:
- Status terkini naskah proposal (lengkap & tanpa Bab 3).
- Konteks penelitian yang aktif di ingatanmu.
- Tanyakan apa fokus pekerjaan yang ingin kita selesaikan hari ini!
```

---

## 🎯 2. PROMPT ALTERNATIF (SESUAI KEBUTUHAN KHUSUS)

Jika Anda ingin sesi hari ini berfokus pada pekerjaan spesifik, silakan klik tombol **Copy** pada salah satu opsi berikut:

---

### 🔹 Opsi 2: Sesi Bimbingan Dosen / Memasukkan Catatan Revisi Baru
*Gunakan ini jika Anda baru saja selesai bimbingan dengan Ibu Fredella dan ingin AI membantu merevisi naskah:*

```text
Halo! Jalankan skill "obsidian-second-brain". Saya baru saja mendapat catatan/revisi dari Dosen Pembimbing (Ibu Dr. Fredella Colline).

1. Tolong baca `00_DASHBOARD_SECOND_BRAIN.md` dan file naskah induk `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex`.
2. Saya akan tempelkan catatan bimbingan dosen di chat berikutnya.
3. Tolong buatkan analisis perubahannya, petakan ke bab mana saja yang terdampak, gunakan format `> [!SUMMARY]`, dan catat ke `07_Review_&_Audit/Revisi_Dosen/` serta `LOG_SESI_SECOND_BRAIN.md`.

Apakah kamu siap menerima catatan bimbingannya?
```

---

### 🔹 Opsi 3: Sesi Persiapan Sidang / Latihan Tanya Jawab Soal Sulit
*Gunakan ini jika Anda ingin simulasi tanya jawab mental untuk persiapan seminar proposal:*

```text
Halo! Jalankan skill "obsidian-second-brain". Hari ini saya ingin berlatih persiapan sidang/seminar proposal skripsi Pokémon TCG.

1. Tolong baca `02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.md` dan `02_Persiapan_Sidang/01_Bank_Soal_&_Flashcard/03_PERTANYAAN_SIDANG_SULIT.md`.
2. Bertindaklah sebagai Dosen Penguji Sidang yang kritis namun konstruktif.
3. Berikan saya 1 pertanyaan sidang (mulai dari level dasar hingga jebakan seperti SULIT 11 tentang asal-usul referensi). Tunggu jawaban saya, lalu berikan nilai dan evaluasi cara menjawab yang lebih tajam!

Bisa kita mulai dari pertanyaan pertama?
```

---

### 🔹 Opsi 4: Sesi Cek & Verifikasi Naskah / Kompilasi PDF
*Gunakan ini jika Anda ingin memastikan semua file, grafik, dan PDF bebas dari error:*

```text
Halo! Jalankan skill "obsidian-second-brain". Tolong lakukan audit kesehatan naskah dan build pipeline:

1. Periksa integritas file di `01_Naskah_Utama/` (pastikan logo UKRIDA pentagram vektor terpasang baik di proposal lengkap maupun proposal tanpa Bab 3).
2. Jalankan skrip verifikasi `execution/verify_nobab3_pdf.py` dan `execution/verify_pdf_headers.py`.
3. Laporkan status kompilasi PDF dan pastikan dokumen Word (.docx) tetap sinkron.
```

---

## 🧠 MENGAPA PROMPT INI BIKIN KONTEKS TIDAK HILANG?

Banyak pengguna AI mengeluhkan *"Kok AI-nya lupa ya kemarin kita ngomongin apa?"*. Hal itu terjadi karena sistem AI tidak tahu file mana yang harus dibaca duluan.

Dengan mengirimkan prompt di atas, Anda secara eksplisit **memerintahkan AI untuk membaca "kartu memori" proyek Anda**:
1. **`graphify-out/`**: Memberitahu AI peta graf silsilah kode dan folder skripsi Anda.
2. **`00_DASHBOARD_SECOND_BRAIN.md`**: Memberitahu AI judul, dosen, variabel, dan bab yang sedang dikerjakan.
3. **`SOURCE_OF_TRUTH.md`**: Mencegah AI mengarang rumus, data pasar, atau referensi fiktif.
4. **`LOG_SESI_SECOND_BRAIN.md`**: Mengingatkan AI pada keputusan terakhir yang Anda buat di sesi sebelumnya.

---
*Simpan file ini di bookmark Obsidian Anda. Setiap kali mau mulai kerja, cukup klik tombol Copy di pojok kanan atas kotak, lalu paste ke AI!* 🚀

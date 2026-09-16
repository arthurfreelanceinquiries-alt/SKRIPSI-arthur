# Mandatory Rule: Jaminan Akses Terbuka Tanpa Hambatan Login (No-Login-Wall Policy)

> [!CRITICAL] PERATURAN MUTLAK SUMBER DATA EMPIRIS SKRIPSI
> Seluruh rujukan data empiris, industri, dan portal eksternal yang dicantumkan dalam Skripsi Arthur Reezan **WAJIB DAPAT DIAKSES SECARA LANGSUNG OLEH PUBLIK (DOSEN PEMBIMBING & TIM PENGUJI)**.
> **DILARANG KERAS** menggunakan tautan yang memunculkan hambatan akses (*access barriers*).

---

## 1. Definisi Hambatan Akses Terlarang
Sebuah tautan rujukan dikategorikan **CACAT AKSES** apabila ketika diklik oleh Dosen Pembimbing atau Penguji:
1. **Login Wall / Registrasi Wajib:** Mengharuskan pengguna membuat akun baru atau *sign-in* terlebih dahulu untuk sekadar melihat tabel data atau grafik.
2. **Verifikasi Nomor Telepon / SMS:** Meminta nomor ponsel atau kode OTP untuk mengakses konten (yang rentan gagal pada nomor Indonesia `+62`).
3. **Paywall / Langganan Berbayar:** Mengharuskan pembayaran langganan premium untuk membuka laporan.
4. **Cloudflare / Bot Challenge (HTTP 403 Aggressive):** Terblokir oleh proteksi bot yang menghalangi peramban akademis standar.

---

## 2. Kriteria Sumber Pengganti yang Sah
Jika suatu data pasar (seperti data sertifikasi grading kartu) memiliki nilai urgensi tinggi bagi variabel skripsi namun portal resminya memiliki sistem login tertutup:
1. **Gunakan Basis Data Agregasi Terbuka (Open-Access Market Guide):**  
   Gunakan platform pelacak pasar sekunder global yang menyajikan data setara (*Ungraded vs PSA 10*) namun 100% bebas login untuk publik (contoh utama: **PriceCharting** di `https://www.pricecharting.com/category/pokemon-cards`).
2. **Sertakan Lampiran Bukti Otentik (Defensive Appendix Attachment):**  
   Jika data dari lembaga seperti PSA tetap dirujuk, lampirkan tangkapan layar tabel data primer pada Bagian Lampiran Naskah Skripsi, sehingga dosen tidak pernah dipaksa membuat akun di internet.
3. **Pilihan Sumber Bebas Hambatan (Zero-Barrier Standard):**  
   Prioritaskan sumber resmi korporat terbuka (seperti *The Pokémon Company Figures* di `corporate.pokemon.co.jp/en/aboutus/figures/` dan *Statista Infographics*) yang berstatus *clean HTTP 200* tanpa login.

---

## 3. Protokol Verifikasi Mandatori Sebelum Terbit
Sebelum tautan dicantumkan ke dalam `references.bib`, naskah LaTeX, Word, dan Mendeley, asisten wajib menguji tautan melalui *incognito browser session* / *curl request* untuk memastikan konten terbuka seketika tanpa *redirect* ke halaman pendaftaran.

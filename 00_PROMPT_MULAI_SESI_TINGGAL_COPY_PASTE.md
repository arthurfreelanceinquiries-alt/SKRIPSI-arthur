# 📋 PROMPT MASTER MULAI & TUTUP SESI — TINGGAL 1-KLIK COPY
### *Dokumen Panduan & Template Prompt Kickoff + Closing Antigravity IDE + Obsidian Second Brain*

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Menyediakan sistem prompt dua arah: **Prompt Kickoff (Buka Sesi)** untuk memuat konteks anti-lupa dan **Prompt Closing (Tutup Sesi)** untuk penguncian 10 gerbang kualitas, log otomatis, dan sinkronisasi Git anti-konflik.
> - **Masalah yang Diselesaikan:** Menghilangkan amnesia konteks saat membuka sesi, serta **mencegah tabrakan lokal vs GitHub (merge conflict)** saat mengakhiri sesi. Seluruh perubahan selalu diuji (10/10 PASS), dicatat, di-commit, dan di-push bersih ke GitHub sebelum Anda menutup IDE.
> - **Keputusan/Output:** Tersedia dalam bentuk **Aplikasi Web Interaktif** (`PROMPT_KICKOFF.html`) dengan tombol salin animasi dan notifikasi visual, serta teks cadangan markdown di bawahnya.

---

## 🌐 1. KICKOFF WEB DASHBOARD (PILIHAN TERBAIK & PALING INTERAKTIF)

> 🚀 **Rekomendasi Utama:** Buka aplikasi web interaktif dengan tombol salin 1-klik di browser Anda:  
> 👉 **[KLIK DI SINI UNTUK MEMBUKA PROMPT_KICKOFF.HTML](PROMPT_KICKOFF.html)**  
> *(Memiliki tombol salin beranimasi, status hijau otomatis saat tersalin, dan notifikasi mengambang).*

<iframe src="PROMPT_KICKOFF.html" width="100%" height="700px" style="border: 1.5px solid rgba(59, 130, 246, 0.3); border-radius: 14px; margin-top: 10px; margin-bottom: 20px;"></iframe>

---

## ⚡ 2. PROMPT PEMBUKA SESI (KICKOFF DEFAULT — ANTI-LUPA KONTEKS)

> 💡 **Cara Pakai Saat Mulai Kerja:** Cukup **KLIK 1 KALI tombol "Copy"** berwarna biru di web dashboard (atau salin teks di bawah), lalu langsung tempel (**Ctrl+V**) ke chat Antigravity / AI!

```text
Halo! Tolong jalankan skill "obsidian-second-brain" dan mulai sesi kerja skripsi ini dengan protokol anti-lupa konteks:

1. [BACA PENGETAHUAN KODE & GRAF]: Tolong periksa `graphify-out/manifest.json` dan `graphify-out/GRAPH_REPORT.md` agar kamu memahami seluruh relasi file, dependensi script, dan entitas skripsi ini.
2. [BACA KOKPIT OBSIDIAN]: Tolong baca `00_DASHBOARD_SECOND_BRAIN.md`, `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` (keputusan D01–D30), framework universal `04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md` (+ SOP `directives/universal_thesis_graph_of_agents.md`), dan catatan log terkini `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md` untuk memuat status naskah aktif, parameter variabel penelitian (Y: Impulsive Buying, X1: Hedonic Motivation, X2: Desire for Completeness, X3: Speculative Motive, M: Self-Control sebagai pemoderasi), serta arahan Dosen Pembimbing Ibu Dr. Fredella Colline.
3. [ATURAN KONSEPTUAL & PENULISAN]: Pastikan kepatuhan mutlak terhadap keputusan D30 (tanpa label kaku Grand Theory di Bab 2; Behavioral Finance sebagai kerangka teoretis utama), penataan istilah asing di belakang bahasa Indonesia dengan huruf miring (contoh: kesimetrisan cetak (\emph{centering})), rumus MRA ber-centering mean ($X_i^*, M^*$), dan format callout `> [!SUMMARY]` pada markdown baru.
4. [AUTO-LOGGING]: Tolong catat progres atau keputusan penting sesi ini ke `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md`.

Setelah kamu membaca file-file di atas, tolong berikan ringkasan 3 poin:
- Status terkini naskah proposal (SATU file utama `Proposal_Arthur_PokemonTCG.*` — PDF 48 hlm settled, 54 pustaka mutakhir Q1/SSCI terverifikasi, gate terakhir 10/10 PASS mutlak).
- Konteks penelitian dan fase riset yang aktif di ingatanmu (status pasca-sempro & persiapan penelitian lapangan).
- Tanyakan apa fokus pekerjaan yang ingin kita selesaikan hari ini!
```

---

## 🏁 3. PROMPT PENUTUP SESI (CLOSING & SAFE GIT SYNC — ANTI-TABRAKAN)

> 🛑 **WAJIB DIJALANKAN SEBELUM MENUTUP IDE:** Salin prompt di bawah ini setiap kali Anda selesai bekerja agar AI mengunci naskah, memvalidasi 10 gerbang, mencatat log, dan mengunggahnya bersih ke GitHub. **Mencegah 100% insiden file bertabrakan (*merge conflict*)!**

```text
Halo! Saya ingin MENGAKHIRI SESI KERJA SKRIPSI hari ini. Tolong jalankan protokol "Closing Sesi & Safe Git Sync" secara tuntas:

1. [VERIFIKASI INTEGRITAS NASKAH & PARITAS]:
   - Periksa apakah ada perubahan pada `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex`. Jika ada perubahan, jalankan settled-build C-LOT-3 (xelatex -> bibtex -> 2x xelatex) hingga 48 halaman settled, lalu jalankan `python execution/sync_markdown_from_tex.py` dan rebuild `python execution/build_proposal_word.py`.
   - Jalankan `python execution/run_thesis_graph.py --gate extended` dan pastikan hasil 10/10 PASS mutlak serta 0 tautan sitasi mati (`python execution/verify_all_citation_links.py`).

2. [DOKUMENTASI & SECOND BRAIN]:
   - Periksa apakah ada keputusan konseptual/metodologis atau arahan baru dari dosen (Dr. Fredella Colline / penguji). Jika ada, rekam sebagai baris keputusan kanonis baru (D31, dst.) di `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` lengkap dengan tanggal dan justifikasi ilmiah.
   - Perbarui `04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md` jika terdapat penambahan subsistem atau perubahan arsitektur.
   - Catat seluruh progres, masalah yang diselesaikan, dan keputusan penting sesi ini ke `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md` (awali dengan callout `> [!SUMMARY]`, gunakan `[[wikilinks]]`).
   - Perbarui parameter pada `00_DASHBOARD_SECOND_BRAIN.md` jika ada perubahan status naskah atau referensi.
   - Jalankan pembaruan graf pengetahuan incremental (`python -m graphify` / update).

3. [PRE-FLIGHT GIT SYNC — DETEKSI TABRAKAN DINI]:
   - Jalankan `git fetch origin` untuk memeriksa apakah ada commit baru di remote GitHub yang belum ditarik ke lokal.
   - Jika ada komit remote baru, beri tahu saya dan selesaikan rekonsiliasi/merge secara aman tanpa menimpa kerja lokal.
   - Tampilkan ringkasan status berkas lokal yang berubah (`git status -s`).

4. [CLEAN COMMIT & PUSH KE GITHUB]:
   - Buat commit Git dengan pesan konvensional yang rapi dan deskriptif (format: `feat(...)`, `docs(...)`, atau `fix(...)`).
   - Push commit tersebut ke `origin main`.
   - Verifikasi status akhir: pastikan "Your branch is up to date with 'origin/main', nothing to commit, working tree clean".

5. [KARTU SERAH TERIMA SESI / SESSION HANDOFF CARD]:
   - Sajikan ringkasan penutup:
     a. Rangkuman pekerjaan yang telah tuntas di sesi ini.
     b. Hash commit terakhir di GitHub.
     c. Rekomendasi fokus pekerjaan prioritas yang harus dikerjakan pada sesi berikutnya!
```

---

## 🎯 4. PROMPT ALTERNATIF (SESUAI KEBUTUHAN KHUSUS)

Jika Anda ingin sesi hari ini berfokus pada pekerjaan spesifik, silakan klik tombol **Copy** pada salah satu opsi berikut:

---

### 🔹 Opsi 3: Sesi Bimbingan Dosen / Memasukkan Catatan Revisi Baru
*Gunakan ini jika Anda baru saja selesai bimbingan dengan Ibu Fredella atau dosen penguji sempro dan ingin AI membantu merevisi naskah:*

```text
Halo! Jalankan skill "obsidian-second-brain". Saya baru saja mendapat catatan/arahan revisi dari Dosen Pembimbing (Ibu Dr. Fredella Colline) / Dosen Penguji Sempro.

1. Tolong baca `00_DASHBOARD_SECOND_BRAIN.md`, file naskah induk `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex`, dan berkas revisi terkini di `07_Review_&_Audit/Revisi_Dosen/` (termasuk `2026-09-24_Catatan_Revisi_Seminar_Proposal_Sempro.md`).
2. Saya akan tempelkan catatan bimbingan/revisi di chat berikutnya.
3. Tolong buatkan analisis perubahannya, petakan ke bab mana saja yang terdampak, pastikan tidak melanggar batasan kanonis (D01–D30; model MRA 6H; 54 pustaka bebas halusinasi), simpan catatan ke `07_Review_&_Audit/Revisi_Dosen/` (nama `YYYY-MM-DD_Revisi_[Nama]_[Topik].md`), rekam keputusan barunya sebagai D31 (dan seterusnya) di `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md`, lalu perbarui dashboard dan `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md`.

Apakah kamu siap menerima catatan revisinya?
```

---

### 🔹 Opsi 4: Sesi Persiapan Sidang / Latihan Tanya Jawab Soal Sulit
*Gunakan ini jika Anda ingin simulasi tanya jawab mental untuk pertahanan metodologi kuantitatif MRA, instrumen kuesioner, dan penguasaan teori skripsi:*

```text
Halo! Jalankan skill "obsidian-second-brain". Hari ini saya ingin berlatih simulasi tanya jawab mental dan penguasaan metodologi skripsi Pokémon TCG (persiapan bimbingan kritis / sidang).

1. Tolong baca `02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.md` dan `02_Persiapan_Sidang/01_Bank_Soal_&_Flashcard/03_PERTANYAAN_SIDANG_SULIT.md`.
2. Bertindaklah sebagai Dosen Penguji Sidang yang sangat kritis, teliti terhadap metodologi, dan menjunjung tinggi kaidah FEB UKRIDA 2023.
3. Berikan saya 1 pertanyaan sidang (mulai dari konsep dasar, justifikasi MRA aditif baseline Model 1, alasan eliminasi label Grand Theory, formula Green 1991 N=106-111, hingga asal-usul 54 pustaka). Tunggu jawaban saya, lalu berikan nilai dan evaluasi cara menjawab yang lebih tajam dan meyakinkan penguji!
4. (Opsional, bila saya minta presentasi: rujuk cetak biru 7 slide di `07_Review_&_Audit/Revisi_Dosen/2026-09-22_Arahan_Dosen_Struktur_PPT_Sempro_7_Slide.md`.)

Bisa kita mulai dari pertanyaan pertama?
```

---

### 🔹 Opsi 5: Sesi Cek & Verifikasi Naskah / Kepatuhan UKRIDA 2023 (10/10 PASS)
*Audit 7 langkah: integritas file + logo, settled-build PDF 48 hlm, sinkron angka cetak, 10 gerbang extended parity, hygiene format, self-anneal, dan vonis kelayakan:*

```text
Halo! Jalankan skill "obsidian-second-brain". Tolong lakukan audit kesehatan naskah menyeluruh, kepatuhan FEB UKRIDA 2023, dan verifikasi dokumen multiformat:

[KONTEKS KANONIS — jangan berasumsi lain]: satu-satunya naskah proposal adalah `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.*` (varian NoBab3 dihapus permanen). PDF kanonis = 48 hlm settled (frontmatter romawi i–v: Cover i, TOC ii–iii, LOT iv, LOF v; tubuh arab 1–43: Bab 1=1–10, Bab 2=11–21, Bab 3=22–37, DP=38–43). Enam lembar formal hidup modular di `01_Naskah_Utama/01_Lembar_Persetujuan_Proposal/`.

1. [INTEGRITAS FILE]: Periksa `01_Naskah_Utama/` — pastikan (a) logo pentagram vektor `images/ukrida_pentagram.pdf` dipakai TeX (cover) dan ter-embed di DOCX; (b) tidak ada lockfile basi `~$*.docx`; (c) 6 file modular frontmatter lengkap; (d) tidak ada sisa file `*NoBab3.*`.
2. [SETTLED-BUILD C-LOT-3]: Kompilasi `xelatex` berulang hingga 2 run beruntun jumlah halaman IDENTIK (48 hlm) + 0 LaTeX rerun-warning. Angka sekali-pass dilarang dipakai. Jika total bergeser dari 48, selidiki dulu sebelum lanjut.
3. [SINKRON ANGKA CETAK C-LOT-1]: Samakan angka TOC/LOT/LOF statis DOCX dengan `.toc`/`.lot`/`.lof` PDF (kanonis: LOT hlm 6, 14, 22, 28, 37; LOF hlm 1, 2, 4, 21, 35; TOC BAB 1=1, BAB 2=11, BAB 3=22, DP=38). Bila beda, perbarui `execution/build_proposal_word.py` lalu rebuild DOCX.
4. [ORCHESTRATOR 10 GERBANG EXTENDED]: Jalankan `py execution/run_thesis_graph.py --gate extended` (G1 Mendeley, G2 live-URL, G3 UKRIDA 2023, G4 tipografi pure-black, G5 paritas PDF-vs-Word, G6 outline, G7 buku LibGen, X1 forensik format typo, X3 header PDF massal, X4 layout section Word) + `py execution/verify_all_citation_links.py` (syarat 0 tautan MATI). Seluruh gerbang wajib 10/10 PASS mutlak.
5. [HYGIENE BAHASA & FORMAT]: DOCX wajib 0 sisa backslash LaTeX, 0 singkatan `n.s.`, judul BAB dua baris (shift+enter), rujukan tabel/gambar bernomor eksplisit, dan istilah asing berada di belakang bahasa Indonesia dalam kurung miring (\emph{italics}).
6. [SELF-ANNEAL]: Jika ada gerbang FAIL, perbaiki secara surgical di skrip/dokumen pemiliknya, ulangi uji dari gerbang yang gagal, dan abadikan pelajarannya ke SOP di `directives/`.
7. [LAPORAN]: Sajikan tabel 10 gerbang (PASS/FAIL + bukti), status sinkron DOCX, dan vonis akhir LAYAK KE PEMBIMBING atau BUILD BROKEN. Catat sesi ke `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md` (awali `> [!SUMMARY]`, gunakan `[[wikilinks]]`).
```

---

### 🔹 Opsi 6: Sesi Audit Ilmiah Naskah (Pra-Bimbingan / Pra-Sidang dengan Paper-Audit)
*Gunakan ini jika Anda ingin melakukan peer review ilmiah berstandar tinggi menggunakan skill paper-audit (Tier-3 Gated):*

```text
Halo! Jalankan skill "obsidian-second-brain" dan lakukan audit ilmiah naskah menggunakan skill "paper-audit" (Tier-3 Gated — hanya pada 5 trigger F9: Pra-Bimbingan, Pra-Sidang, Major Rewrite, Verifikasi Resolusi, On-demand):

1. Tolong baca SOP audit di `directives/run_paper_audit.md`, pedoman di `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` (D01–D30), dan laporan audit sebelumnya di `07_Review_&_Audit/Paper_Audits/` (terbaru: `review-2026-09-29-011500.md` temuan F026–F031 telah RESOLVED; jangan false alarm pada item yang sudah lulus).
2. Sebutkan trigger audit sesi ini secara eksplisit.
3. Lakukan audit ilmiah komprehensif (metodologi MRA, formula matematika, klaim fenomena industri, dan 54 sitasi Q1/SSCI terverifikasi) terhadap naskah proposal `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf` (atau `.tex`).
4. Jalankan "challenger pass" untuk menyaring temuan agar tidak terjadi false alarm terhadap standar lokal FEB UKRIDA 2023 dan kesepakatan pembimbing.
5. Terbitkan laporan audit resmi dengan format Fxxx baru ke folder `07_Review_&_Audit/Paper_Audits/` dan catat ringkasannya ke `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md`.

Apakah kamu siap memulai audit naskah ini?
```

---

### 🔹 Opsi 7: Diagnostik Fatal Error Naskah DOCX & Auto-Repair Generator
*Gunakan ini jika Anda menemukan kesalahan fatal pada naskah Word (kebocoran sintaks LaTeX mentah pada tabel/paragraf, border tabel liar pada lembar pengesahan, atau asimetri spasi tanda tangan):*

```text
Halo! Jalankan skill "obsidian-second-brain". Tolong lakukan audit diagnostik tipografi, deteksi kebocoran kode LaTeX mentah, dan auto-repair naskah Microsoft Word (.docx):

1. [DIAGNOSTIK FATAL ERROR]: Jalankan audit ketat `python execution/verify_docx_typography.py` pada file UTAMA `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx`. Periksa apakah ada:
   - Kebocoran sintaks mentah LaTeX (`\begin{longtable}`, `\toprule`, `\rightarrow`, `\begingroup`, sisa `\` yatim, `\ref`/`\url` lolos, dll.) di paragraf/tabel naskah.
   - Border grid tabel liar pada lembar formal modular (`01_Naskah_Utama/01_Lembar_Persetujuan_Proposal/`).
   - Asimetri baseline tanda tangan Dosen Pembimbing vs Kaprodi.
   - Font non-hitam atau themeColor pada heading/run dokumen.
2. [AUTO-REPAIR JIKA ADA ERROR]: Jika ditemukan kegagalan/error fatal pada poin 1:
   - Bersihkan dan format ulang file UTAMA memakai `execution/build_proposal_word.py` (varian NoBab3 sudah dihapus — jangan membuatnya lagi).
   - Pastikan Tabel 1.1 (Matriks Research Gap) dirender sebagai tabel Word APA 7 murni, bukan teks TeX mentah.
   - Kunci tabel identitas & tanda tangan formal menjadi 100% borderless dengan struktur 3-baris presisi.
   - Pastikan seluruh 54 entri Daftar Pustaka memiliki bookmark dan 180+ in-text citations terhubung aktif.
3. [VERIFIKASI ULANG]: Jalankan kembali `python execution/verify_docx_typography.py` dan `python execution/run_thesis_graph.py --gate extended` hingga 10/10 PASS (0 fatal error).
4. Laporkan ringkasan hasil audit sebelum vs sesudah perbaikan!
```

---

## 🧠 MENGAPA SISTEM DUA ARAH (KICKOFF & CLOSING) INI MENJAMIN ZERO-DESYNC & ZERO-CONFLICT?

Banyak pengembang dan peneliti mengalami *"Kok Git saya nabrak?"* atau *"Kok AI-nya lupa ya kemarin kita bahas apa?"*. Hal itu terjadi karena siklus kerja yang terbuka tanpa penguncian.

Dengan memadukan **Prompt Kickoff (Pembuka)** dan **Prompt Closing (Penutup)**:
1. **Saat Membuka Sesi:** AI dipaksa membaca silsilah graf (`graphify-out/`), status naskah 48 hlm (`00_DASHBOARD_SECOND_BRAIN.md`), dan aturan D01–D30 (`SOURCE_OF_TRUTH.md`).
2. **Saat Menutup Sesi:** AI dipaksa memverifikasi 10 gerbang extended, menyinkronkan XeLaTeX/Word/MD, mencatat log sesi, mendeteksi perubahan remote dengan `git fetch`, dan melakukan push bersih ke GitHub.
3. **Hasil:** Repositori Anda **selalu dalam status clean working tree dan up-to-date di GitHub**, siap dibuka di mana saja tanpa risiko tabrakan data!

---
*Simpan file ini di bookmark Obsidian Anda. Buka sesi dengan Opsi 1, dan selalu tutup sesi dengan Opsi 2!* 🚀

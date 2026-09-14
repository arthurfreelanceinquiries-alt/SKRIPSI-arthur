# 📜 LOG SESI SECOND BRAIN — RIWAYAT RISET & PENGEMBANGAN SKRIPSI

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Buku harian riset (*research lab book*) otomatis yang mencatat setiap kemajuan, pemecahan masalah, keputusan metodologis, dan arahan bimbingan per sesi kerja.
> - **Masalah yang Diselesaikan:** Menghilangkan amnesia progres; mendokumentasikan alasan di balik setiap perubahan naskah atau penambahan fitur agar selalu siap dipertanggungjawabkan saat sidang.
> - **Keputusan/Output:** Diperbarui secara otomatis oleh asisten di setiap akhir sesi kerja.

---

## 📅 Sesi 14 September 2026 (Sesi 9 - Pukul 19:10 WIB): Audit Teknis Prism AI, PRD Resolusi, & Rencana Implementasi

* **Fokus Pekerjaan:**
  - Menjalankan skill `obsidian-second-brain` dan membedah laporan *Technical and Editorial Review* Prism AI (1.227 baris evaluasi proposal).
  - Melakukan analisis kritis terhadap 11 temuan teknis: memilah temuan yang wajib direvisi (model aditif baseline MRA, terminologi mean-centering, pasal KUHPerdata, inkonsistensi sitasi, butir kuesioner) vs temuan false alarm / over-engineering (asset gambar lengkap, references.bib lengkap, cluster-robust overkill).
  - Menyusun dokumen PRD lengkap di [[04_Riset_&_Metodologi/PRD_RESOLUSI_REVIEW_TEKNIS_PRISM_AI.md]] dan catatan review resmi di [[07_Review_&_Audit/Revisi_Dosen/2026-09-14_Review_Teknis_Prism_AI_dan_Matriks_Resolusi.md]].
  - Mengunci keputusan baru **D20** di [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]].
  - Menyusun rancangan eksekusi terstruktur pada dokumen `implementation_plan.md`.
* **Masalah yang Diselesaikan:**
  - Menemukan dan merancang perbaikan atas kelemahan mendasar model perbandingan MRA (Persamaan 3.1 & 3.2) di mana Model 1 sebelumnya belum menyertakan pemoderasi $M$, sehingga $\Delta R^2$ mencampuradukkan efek langsung $M$ dengan interaksi moderasi.
  - Mengeliminasi kekeliruan sitasi hukum Pasal 330 KUHPerdata untuk batas usia 17 tahun, mengalihkan ke UU No. 24/2013 tentang Administrasi Kependudukan (KTP) dan diskresi finansial.
  - Memperbaiki kontradiksi sitasi celah empiris Prasetio (2021) di Bab 1 dan typo "dimediasi" di Bab 2.
  - Menyelaraskan butir kuesioner Tabel 3.2 ($X_1$ role shopping, $X_3$ likuiditas riil & eliminasi istilah cuan, $M$ kapasitas regulasi diri umum).
* **Keputusan / Output Teknis:**
  - Dokumen PRD Baru: [[04_Riset_&_Metodologi/PRD_RESOLUSI_REVIEW_TEKNIS_PRISM_AI.md]].
  - Catatan Audit Baru: [[07_Review_&_Audit/Revisi_Dosen/2026-09-14_Review_Teknis_Prism_AI_dan_Matriks_Resolusi.md]].
  - Source of Truth Diperbarui: Klausul **D20** resmi ditambahkan pada [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]].
  - Implementation Plan Siap Eksekusi: menunggu konfirmasi pengguna untuk eksekusi modifikasi berkas LaTeX, draf markdown, dan skrip Word OMML.

---

## 📅 Sesi 14 September 2026 (Sesi 8): Inisialisasi Sesi Kerja & Sinkronisasi Ekosistem Second Brain

* **Fokus Pekerjaan:**
  - Inisialisasi sesi kerja skripsi dengan protokol resmi `obsidian-second-brain` dan anti-lupa konteks.
  - Sinkronisasi graf pengetahuan (`graphify-out/GRAPH_REPORT.md` & `graphify-out/manifest.json`).
  - Pemuatan status naskah aktif, parameter variabel ($Y$, $X_1$, $X_2$, $X_3$, $Z$), serta arahan bimbingan Dr. Fredella Colline dari `[[00_DASHBOARD_SECOND_BRAIN.md]]` dan `[[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]]`.
* **Masalah yang Diselesaikan:**
  - Memastikan seluruh parameter riset terkunci (D01–D19), aturan penulisan Pedoman TA FEB UKRIDA 2023, struktur 3-Layer, dan kualitas tipografi naskah Word & LaTeX termuat sempurna di memori kerja sebelum mengeksekusi tugas baru.
* **Keputusan / Output Teknis:**
  - Protokol dokumentasi baku ditegakkan: Callout `> [!SUMMARY]`, tautan bidirectional `[[...]]`, dan verifikasi deterministik.
  - Konfirmasi status naskah (lengkap 50 halaman dan tanpa Bab 3 33 halaman dalam format PDF dan Word OMML) siap dipakai.
  - Menunggu fokus pekerjaan spesifik dari pengguna untuk sesi hari ini.

---

## 📅 Sesi 14 September 2026 (Sesi 7): Integrasi Arsitektur 3-Layer & Pipeline Hybrid (Pandoc + Script) untuk Native Word Equation OMML

* **Fokus Pekerjaan:**
  - Mengimplementasikan arsitektur 3-Layer (Directive, Orchestration, Execution) pada pipeline generator Microsoft Word (`execution/build_proposal_word.py`).
  - Mengintegrasikan **Pandoc 3.11** (diinstal via Windows Package Manager / winget) sebagai sub-engine matematika untuk mengekstraksi notasi LaTeX menjadi objek rumus asli Microsoft Word (**OpenXML `<m:oMathPara>` / Cambria Math**).
  - Menghilangkan kompromi konversi lama di mana rumus regresi MRA di Bab 3 diturunkan derajatnya (*downgraded*) menjadi teks datar biasa tanpa subskrip/superskrip matematika.
  - Memperbarui naskah [[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]] dan [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]].
* **Masalah yang Diselesaikan:**
  - **Kelemahan Pandoc Murni:** Pandoc murni tidak mampu memenuhi tata kelola baku FEB UKRIDA 2023 (margin 4-3-3-3 cm, pemisahan nomor Romawi bawah vs Arab kanan atas, titik-titik daftar isi di 14.0 cm, tabel APA 7th edition, dan mode NoBab3).
  - **Kelemahan Python-docx Murni:** python-docx tidak memiliki parser LaTeX math built-in sehingga rumus matematika sebelumnya diubah menjadi teks datar polos (menghapus tanda subskrip `_` dan superskrip `^`).
  - **Solusi Sinergis (Hybrid 2-Stage):** Pandoc mengekstraksi rumus matematika LaTeX menjadi pohon elemen `<m:oMathPara>`, kemudian `build_proposal_word.py` menyematkannya ke dalam dokumen berstandar UKRIDA FEB 2023.
* **Keputusan / Output Teknis:**
  - Dokumen PRD Baru: [[04_Riset_&_Metodologi/PRD_HYBRID_PANDOC_SCRIPT_GENERATOR.md]].
  - Pembaruan Directive: [[directives/generate_thesis_word_document.md]].
  - Pembangun Naskah Hybrid: [[execution/build_proposal_word.py]] (dengan `latex_to_omml_pandoc`).
  - Naskah Word Tergenerasi & Tervalidasi:
    1. [[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]] (Varian review steril tanpa Bab 3, tanpa lembar pengesahan, pure black #000000, 36 halaman reflow).
    2. [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]] (Varian proposal lengkap dengan 6 objek persamaan Word OMML native di Bab 3).
  - Verifikasi:
    - `verify_docx_typography.py`: PASS 100%.
    - `verify_pdf_docx_parity.py`: PASS 100%.
    - Word COM Headless Export (`convert_docx.ps1`): Berhasil mengekspor kedua dokumen tanpa galat atau popup peringatan.

---

## 📅 Sesi 14 September 2026 (Sesi 6): Institusionalisasi Pedoman Wajib PRD & Penuntasan Masalah Dot Leaders Daftar Isi di Google Docs / Word

* **Fokus Pekerjaan:**
  - Menjadikan [[04_Riset_&_Metodologi/PRD_SINKRONISASI_DOCX_DAN_AUDIT_FILE.md]] dan [[04_Riset_&_Metodologi/PRD_REVISI_DOCX_KUALITAS_LATEX.md]] sebagai aturan permanen wajib (*inviolable directives*) di seluruh ekosistem asisten AI (`.agents/rules/`, `GEMINI.md`, `CLAUDE.md`, `AGENTS.md`, dan `00_DASHBOARD_SECOND_BRAIN.md`).
  - Investigasi tuntas dan penyelesaian akar penyebab hilangnya titik-titik (*dot leaders*) serta nomor halaman yang menempel pada judul saat dokumen Word dibuka di **Google Docs**, Word Online, dan penampil mobile/web.
  - Pemutakhiran skrip pembangun Word [[execution/build_proposal_word.py]] dan suite verifikasi [[execution/verify_docx_typography.py]].
* **Masalah yang Diselesaikan:**
  - **Akar Masalah Titik Hilang di Google Docs:** Properti `right_indent = Cm(0.8)` pada paragraf TOC/LOT/LOF menarik batas kanan paragraf menjadi 13.2 cm, sementara tab stop dipasang pada 14.0 cm (di luar batas). Google Docs menganggap tab stop di luar batas margin sebagai *invalid* dan membuangnya (*discard*), sehingga tab kembali ke jarak default 0.5 inci polos tanpa garis titik-titik.
  - **Solusi Mutlak:** Mengeliminasi `right_indent = Cm(0.8)` (menjadi `Cm(0)`), memisahkan run teks judul, run mandiri `<w:r><w:tab/></w:r>`, dan run mandiri nomor halaman `<w:r><w:t>{page}</w:t></w:r>` persis seperti struktur naskah skripsi terdahulu Arthur yang telah disetujui FEB UKRIDA (`Skripsi_Arthur_FINAL.docx`).
  - **Institusionalisasi Aturan Permanen:** Dibuat aturan `.agents/rules/mandatory_thesis_sync_and_quality.md` yang mewajibkan zero desync, zero theme color (pure black `#000000`), dan audit otomatis sebelum penyelesaian tugas.
* **Keputusan / Output Teknis:**
  - Berkas Aturan Permanen: [[.agents/rules/mandatory_thesis_sync_and_quality.md]].
  - Berkas Naskah Word Terkini & Tervalidasi: [[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]] & [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]].
  - Hasil Audit Paritas & Tipografi: 100% PASS pada seluruh pengujian.

---

## 📅 Sesi 14 September 2026 (Sesi 5): Penyelarasan Tipografi DOCX Tingkat Lanjut (Pure Black #000000 & Garis Titik-Titik Daftar Isi)

* **Fokus Pekerjaan:**
  - Penyelarasan visual tingkat lanjut pada berkas Microsoft Word (`Proposal_Arthur_NoBab3.docx` dan `Proposal_Arthur_PokemonTCG.docx`) agar memiliki kualitas tipografi setara master PDF/LaTeX.
  - Investigasi dan eliminasi akar penyebab warna font biru pada heading (DAFTAR GAMBAR, BAB 1 PENDAHULUAN, 1.1 Latar Belakang).
  - Investigasi dan perbaikan garis titik-titik (*dot leaders*) pada Daftar Isi, Daftar Tabel, dan Daftar Gambar yang sebelumnya tidak muncul pada penampil dokumen seperti Google Docs dan Word Online.
  - Perbaikan unescaping notasi mata uang `US$` dan spasi LaTeX agar tidak memunculkan karakter escape `US\`.
* **Masalah yang Diselesaikan:**
  - **Akar Penyebab Warna Biru:** Terjadi karena OpenXML `styles.xml` mewarisi tema bawaan Word (`themeColor="accent1"`), dan tag run `<w:r>` di dalam heading tidak memuat deklarasi warna eksplisit. Solusi: Menerapkan penghapusan atribut tema dokumen dan menyuntikkan `<w:color w:val="000000"/>` eksplisit pada tingkat run, diikuti rekursif document-wide pure black pass.
  - **Akar Penyebab Garis Titik Hilang:** Terjadi akibat penggunaan style paragraf ad-hoc tanpa registrasi resmi style `TOC 1`, `TOC 2`, `TOC 3` di `styles.xml`, serta perhitungan posisi tab stop yang keliru mengurangi indentasi kiri (13.2 cm & 12.6 cm alih-alih 14.0 cm). Solusi: Mengonfigurasi tab stop ber-leader titik (`w:leader="dot"`) pada posisi tepat `14.0 cm` (`7938 dxa`) untuk seluruh tingkatan TOC, serta mendaftarkan style `TOC 1`, `TOC 2`, `TOC 3` secara baku.
  - **Verifikasi Visual Ekspor:** Melakukan ekspor DOCX ke PDF via Word COM headless dan mengekstraksi blok teks serta render gambar via PyMuPDF. Terbukti 100% span teks ber-RGB `(0, 0, 0)` dan garis titik-titik tampak sangat presisi dan rapi.
* **Keputusan / Output Teknis:**
  - PRD Tipografi: `[[04_Riset_&_Metodologi/PRD_REVISI_DOCX_KUALITAS_LATEX.md]]`.
  - Laporan Paritas Diperbarui: `[[04_Riset_&_Metodologi/LAPORAN_KOMPARASI_PDF_VS_DOCX.md]]`.
  - Skrip Builder: `[[execution/build_proposal_word.py]]` (dilengkapi pure black & dot leaders generator).
  - Skrip Verifikasi: `[[execution/verify_docx_typography.py]]` (audit 100% lulus untuk 36 entri NoBab3 dan 59 entri versi lengkap).
  - Dokumen Word Siap Pakai: `[[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]]` dan `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]]`.

---

## 📅 Sesi 14 September 2026 (Sesi 4): Sinkronisasi Penuh DOCX vs Master PDF & Audit Repositori

* **Fokus Pekerjaan:**
  - Sinkronisasi dokumen Microsoft Word (`Proposal_Arthur_NoBab3.docx` dan `Proposal_Arthur_PokemonTCG.docx`) dengan master PDF terbaru (`Proposal_Arthur_NoBab3.pdf` 33 halaman dan `Proposal_Arthur_PokemonTCG.pdf` 50 halaman).
  - Perbaikan bug relatif pada skrip `execution/sync_markdown_from_tex.py` dan regenerasi naskah `PROPOSAL_SKRIPSI_POKEMON_TCG.md`.
  - Refaktorisasi modular generator Word `execution/build_proposal_word.py` (ekstraksi lembar pengesahan, penomoran romawi `ii`, restrukturisasi TOC/LOT/LOF).
  - Audit paritas menyeluruh menggunakan script otomasi Layer 3 (`verify_pdf_docx_parity.py` dan `verify_docx_typography.py`).
* **Masalah yang Diselesaikan:**
  - **Inkonsistensi Lembar Formal:** Menghilangkan lembar Pernyataan Keaslian, Persetujuan, dan Pengesahan pada varian `NoBab3.docx` agar sesuai 100% dengan PDF mode bimbingan dosen.
  - **Inkonsistensi Penomoran Halaman:** Memastikan frontmatter `NoBab3.docx` langsung diawali KATA PENGANTAR dengan nomor romawi `ii`.
  - **Prioritas Dosen Pembimbing:** Memperbarui 7 butir ucapan terima kasih pada Kata Pengantar dengan mendahulukan Dosen Pembimbing Ibu Dr. Fredella Colline di urutan nomor 1.
  - **Daftar Isi Bersih:** Menghapus sub-bab usang (1.2.1, 1.2.2, 1.5, 1.6), menempatkan batasan masalah di 3.1.1 Bab 3, dan memperbaiki nomor Daftar Pustaka agar tidak keliru menunjuk hal. 49.
  - **Uji Paritas Otomatis:** Kedua dokumen (.docx) berhasil dibangun bersih dan lulus 100% uji tipografi serta uji paritas PDF vs DOCX.
* **Keputusan / Output Teknis:**
  - PRD Sinkronisasi: `[[04_Riset_&_Metodologi/PRD_SINKRONISASI_DOCX_DAN_AUDIT_FILE.md]]`.
  - Laporan Paritas: `[[04_Riset_&_Metodologi/LAPORAN_KOMPARASI_PDF_VS_DOCX.md]]`.
  - Skrip Builder Word: `[[execution/build_proposal_word.py]]`.
  - Skrip Audit Paritas: `[[execution/verify_pdf_docx_parity.py]]`.
  - Naskah Word Terkini: `[[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]]` & `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]]`.


* **Fokus Pekerjaan:**
  - Inisialisasi sesi kerja skripsi dengan protokol resmi `obsidian-second-brain`.
  - Sinkronisasi graf pengetahuan (`graphify-out/GRAPH_REPORT.md` - 1.024 nodes, 1.007 edges, 75 komunitas).
  - Pemuatan status naskah aktif, parameter variabel ($Y$, $X_1$, $X_2$, $X_3$, $Z$), serta catatan bimbingan Dr. Fredella Colline dari `[[00_DASHBOARD_SECOND_BRAIN.md]]` dan `[[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]]`.
* **Masalah yang Diselesaikan:**
  - Memastikan seluruh keputusan terkunci (D01–D19), aturan penulisan Pedoman TA UKRIDA 2023, serta pemisahan naskah (lengkap 46 hlm vs tanpa Bab 3 33 hlm) tertanam utuh sebelum pengerjaan dimulai.
* **Keputusan / Output Teknis:**
  - Status naskah proposal terkonfirmasi konsisten.
  - Sesi kerja siap menerima instruksi pengerjaan fokus hari ini.

---

## 📅 Sesi 14 September 2026 (Sesi 2): Pengaktifan Obsidian Second Brain & Integrasi Graphify

* **Fokus Pekerjaan:**
  - Konfigurasi skill dan rules resmi `obsidian-second-brain` untuk Antigravity.
  - Pembuatan master dashboard MOC (`00_DASHBOARD_SECOND_BRAIN.md`).
  - Penegasan protokol pre-flight Graphify dan pencatatan purpose-driven otomatis.
* **Masalah yang Diselesaikan:**
  - Mengintegrasikan Obsidian agar menjadi Otak Kedua yang proaktif: membaca struktur pengetahuan Graphify sebelum sesi dimulai, menyaring intisari dengan callout `> [!SUMMARY]`, dan mencatat riwayat pemecahan masalah ke file log secara otomatis.
* **Keputusan / Output Teknis:**
  - File Skill: `[[.agents/skills/obsidian-second-brain/SKILL.md]]` dan global config.
  - File Rules: `[[.agents/rules/obsidian_second_brain.md]]`.
  - Master Dashboard: `[[00_DASHBOARD_SECOND_BRAIN.md]]`.
  - Master Kickoff Prompt: `[[00_PROMPT_MULAI_SESI_TINGGAL_COPY_PASTE.md]]`.
  - Web App Kickoff (1-Klik Copy): `[[PROMPT_KICKOFF.html]]`.
  - Log Sesi: `[[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]]`.

---

## 📅 Sesi 14 September 2026 (Sesi 1): Penyusunan Kunci Jawaban Asal-Usul Referensi

* **Fokus Pekerjaan:**
  - Formulasi jawaban ilmiah saat dosen menanyakan asal-usul referensi teori dan jurnal yang sangat banyak (era 1974 s/d 2025).
  - Integrasi jawaban ke dalam materi persiapan sidang.
* **Masalah yang Diselesaikan:**
  - Mengatasi kecemasan mahasiswa saat ditanya *"Dapat semua referensi ini dari mana?"* dengan menyusun argumen 3 pilar: 10 jurnal empiris open-access, buku teks babon monograf, dan instrumen skala baku (cross-referencing).
  - Menyediakan taktik *"Citation Chaining / Snowballing Method"* dan legalitas akses melalui E-Resources Perpusnas RI.
* **Keputusan / Output Teknis:**
  - Menambahkan **Pertanyaan 17** pada `[[02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.md]]`.
  - Menambahkan **SULIT 11** pada `[[02_Persiapan_Sidang/01_Bank_Soal_&_Flashcard/03_PERTANYAAN_SIDANG_SULIT.md]]`.
  - Mengompilasi ulang PDF panduan belajar: `[[02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.pdf]]` (46.4 KB).

---

## 📅 Sesi 13–14 September 2026: Reorganisasi Repositori, Logo Vektor UKRIDA, & Naskah Tanpa Bab 3

* **Fokus Pekerjaan:**
  - Penataan ulang folder repositori `SKRIPSI-arthur` dari urutan 01 s/d 07 tanpa duplikasi nomor.
  - Pemasangan logo pentagram resmi UKRIDA di halaman cover naskah proposal.
  - Pembuatan varian proposal tanpa Bab 3 dan tanpa 3 lembar pengesahan formal.
* **Masalah yang Diselesaikan:**
  - Mengeliminasi inkonsistensi nomor folder (`05_` ganda) dan folder split gambar (`figures/` & `images/`).
  - Menghilangkan tampilan logo UKRIDA buram/pecah dengan mengonversi SVG resmi universitas menjadi format vektor PDF murni (`ukrida_pentagram.pdf`).
  - Menghasilkan PDF proposal 33 halaman yang mengalir rapi dari Cover langsung ke Kata Pengantar (halaman ii) tanpa Bab 3.
* **Keputusan / Output Teknis:**
  - Naskah Induk: `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex]]` & `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf]]`.
  - Naskah Varian: `[[01_Naskah_Utama/Proposal_Arthur_NoBab3.tex]]` & `[[01_Naskah_Utama/Proposal_Arthur_NoBab3.pdf]]`.
  - Aset Vektor Logo: `[[01_Naskah_Utama/images/ukrida_pentagram.pdf]]`.
  - Skrip Otomasi: `[[execution/build_proposal_nobab3_pdf.py]]` dan `[[execution/verify_nobab3_pdf.py]]`.
  - Pengarsipan Scratch: 38 file diff lama diarsipkan ke `[[scratch/_legacy_diffs/]]`.
  - Dokumentasi: Catatan Walkthrough Sesi Kerja IDE.

---

## 📅 Sesi 14 September 2026 (Sesi 2): Standardisasi Heading & Injeksi Komponen Daftar Isi Otomatis Word/Docs

> [!SUMMARY]
> Mengatasi masalah garis titik-titik (*dot leaders*) Daftar Isi yang hilang saat dokumen Word diimpor ke Google Docs, serta menstandarisasi gaya `Heading 1`, `Heading 2`, dan `Heading 3` dari Bab 1 hingga Daftar Pustaka agar terdeteksi 100% otomatis oleh fitur *Table of Contents* Google Docs dan MS Word.

* **Fokus Pekerjaan:**
  - Diagnostik kendala hilangnya titik-titik Daftar Isi di Google Docs pada file `Proposal_Arthur_PokemonTCG.docx` dan `Proposal_Arthur_NoBab3.docx`.
  - Menstandarisasi hierarki Heading (Bab, Sub-bab, Anak Sub-bab, dan Daftar Pustaka) dengan gaya resmi Word (`Heading 1`, `Heading 2`, `Heading 3`).
  - Mengintegrasikan komponen resmi *Native Word Table of Contents* (`w:sdt` / `TablesOfContents.Add`) melalui otomatisasi Word COM dan OpenXML.
  - Memproteksi judul tabel (*Tabel 2.1*, *3.1*, dst.) dan judul gambar (*Gambar 1.1*, dst.) agar tidak membawa gaya Heading yang bisa mengotori Daftar Isi.
  - Memisahkan judul halaman "DAFTAR ISI" dari gaya `Heading 1` agar tidak terjadi duplikasi rekursif di dalam Daftar Isi.
* **Masalah yang Diselesaikan:**
  - **Akar Masalah Hilangnya Titik-Titik:** Generator Word sebelumnya menyusun Daftar Isi sebagai paragraf teks biasa dengan karakter tab (`\t`). Microsoft Word mendukung atribut XML `w:leader="dot"` pada tab, namun Google Docs mengabaikannya dan merender spasi kosong putih lebar.
  - **Solusi Komponen Otomatis:** Google Docs hanya menampilkan garis titik-titik jika dokumen menggunakan komponen resmi *Table of Contents*. Dengan menginjeksi komponen native Word TOC, Google Docs secara otomatis mengonversinya menjadi widget Daftar Isi interaktif lengkap dengan garis titik-titik dan tombol *Update*.
  - **Struktur Heading Rapi:** Semua Bab 1–3 dan DAFTAR PUSTAKA berstatus `Heading 1` (outline level 0), seluruh sub-bab `1.1`–`3.7` berstatus `Heading 2` (outline level 1), dan seluruh anak sub-bab `1.4.1`–`3.5.6` berstatus `Heading 3` (outline level 2).
* **Keputusan / Output Teknis:**
  - Generator Diperbarui: `[[execution/build_proposal_word.py]]` mengintegrasikan `inject_native_word_toc()`, `add_daftar_isi_heading()`, dan proteksi judul tabel/gambar.
    - Validasi Tipografi: `[[execution/verify_docx_typography.py]]` lulus audit 100% pada kedua varian dokumen.
    - Validasi Outline: `[[execution/verify_word_outline.py]]` lulus audit 100% (12 Level 0, 16 Level 1, 28 Level 2) pada `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]]`.
    - Dokumen Output Bersih: `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]]` dan `[[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]]`.

---

## 📅 Sesi 14 September 2026 (Sesi 3): Resolusi Review Teknis & Editorial Prism AI (Audit Metodologis, MRA Baseline, & Penyelarasan Multi-Format)

> [!SUMMARY]
> Merespons dan menyelesaikan 11 temuan telaah teknis (*peer review*) dari Prism AI terhadap naskah proposal skripsi Arthur, menyusun dokumen arsitektur PRD Resolusi Teknis, memperbaiki model ekonometrika MRA menjadi Model Aditif Baseline (mengisolasi $\Delta R^2$), mengoreksi terminologi *mean-centering*, memperbarui dasar hukum usia 17 tahun ke UU Adminduk, menyelaraskan butir kuesioner Tabel 3.2, serta memastikan *zero desync* di seluruh format (XeLaTeX PDF, Word DOCX, dan Markdown draf).

* **Fokus Pekerjaan:**
  - Audit dan klasifikasi triage 11 temuan Prism AI ke dalam tiga kelompok: Wajib Direvisi (koreksi fatal), Penyempurnaan Konten (rigoritas psikometri/ekonometrika), dan Non-Revisi (*false alarm* aset hilang & *over-engineering* analisis kluster/IRB medis).
  - Rekonstruksi spesifikasi Model 1 menjadi Model Aditif Baseline yang menyertakan efek utama pemoderasi ($M^*$), sehingga Model 2 MRA Penuh murni mengisolasi peningkatan daya penjelas 3 istilah interaksi moderasi ($\Delta R^2$) melalui statistik $F_{\text{change}}$ ($df_1 = 3, df_2 = N - 8$).
  - Koreksi terminologi statistik: mengganti "standarisasi skor rata-rata" menjadi "pemusatan rata-rata (*mean-centering*)", serta mengklarifikasi fungsinya dalam mereduksi multikolinearitas non-esensial antara prediktor dengan produk interaksinya tanpa mengubah nilai $R^2$ maupun koefisien interaksi.
  - Koreksi dasar hukum kriteria inklusi usia 17 tahun: mengeliminasi Pasal 330 KUHPerdata (yang sebenarnya mengatur usia 21 tahun), beralih ke UU No. 24 Tahun 2013 tentang Administrasi Kependudukan (KTP sebagai bukti kedewasaan sipil/administratif), diskresi keuangan mandiri, dan kapasitas memberikan *informed consent*.
  - Penyempurnaan instrumen kuesioner Tabel 3.2:
    - $X_1$ butir X1.4: diselaraskan dengan dimensi *Role Shopping* Arnold & Reynolds (2003) (berbelanja untuk dihadiahkan/dimainkan bersama teman atau keluarga).
    - $X_3$ butir X3.1–X3.5: mengeliminasi istilah percakapan non-formal "cuan" menjadi istilah akademik "apresiasi modal / potensi laba finansial", serta butir X3.2 mengukur persepsi kemudahan mencairkan kartu menjadi uang tunai di pasar sekunder (likuiditas riil).
    - $M$ butir M1–M6: dirumuskan sebagai kapasitas volisional regulasi diri umum (Tangney BSCS 2004) dan kepatuhan anggaran, guna menjamin validitas diskriminan terhadap perilaku belanja kasir $Y$.
  - Rekonsiliasi sitasi gap Bab 1: menghapus kontradiksi internal `prasetio2021hedonic` dari kelompok tidak signifikan di Bab 1 (diganti Zheng et al. 2019 dan Tirtayasa et al. 2020), dan mempertahankan Prasetio (2021) di kelompok pengaruh positif di Bab 2.
  - Perbaikan tipografi & editorial: koreksi typo "dimediasi" menjadi "dimoderasi" pada H5, koreksi persentase lonjakan produksi menjadi "sebesar 125%", perbaikan legenda Gambar 2.1, dan penyempurnaan label diagram alur Gambar 3.1.
* **Masalah yang Diselesaikan:**
  - Menyelamatkan validitas metodologi ekonometrika dari kesalahan fatal percampuran efek langsung $M$ dengan efek interaksi moderasi pada uji $F_{\text{change}}$ dan $\Delta R^2$.
  - Mencegah mahasiswa terpojok dalam seminar proposal akibat kesalahan kutipan fakta hukum perdata (KUHPerdata Pasal 330) dan kontradiksi sitasi gap antar-bab.
  - Mengamankan validitas konstruk instrumen penelitian sebelum disebarkan ke responden survei lapangan.
* **Keputusan / Output Teknis:**
  - Dokumen PRD Arsitektur: `[[04_Riset_&_Metodologi/PRD_RESOLUSI_REVIEW_TEKNIS_PRISM_AI.md]]`.
  - Catatan Riwayat Audit: `[[07_Review_&_Audit/Revisi_Dosen/2026-09-14_Review_Teknis_Prism_AI_dan_Matriks_Resolusi.md]]`.
  - Keputusan Terkunci: D20 ditambahkan ke `[[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]]`.
  - Master XeLaTeX Terkompilasi Bebas Galat:
    - `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.pdf]]` (54 halaman — melampaui batas minimal 50 halaman K-02 UKRIDA 2023).
    - `[[01_Naskah_Utama/Proposal_Arthur_NoBab3.pdf]]` (35 halaman — naskah bersih untuk bimbingan dosen).
  - Generator Word & Output DOCX Bersih:
    - `[[execution/build_proposal_word.py]]` diperbarui (OMML equations, clean text regex, Abstrak & Abstract updated).
    - `[[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx]]` dan `[[01_Naskah_Utama/Proposal_Arthur_NoBab3.docx]]`.
  - Seluruh Skrip Verifikasi Lulus 100%:
    - `[[execution/verify_docx_typography.py]]`: PASS 100% (Pure Black, 0 stray asterisks/dollars/LaTeX commands, valid dot leaders & 12pt abstracts).
    - `[[execution/verify_word_outline.py]]`: PASS 100% (56 heading terverifikasi).
    - `[[execution/verify_pdf_docx_parity.py]]`: PASS 100% (Paritas sempurna NoBab3 dan Full Proposal).
    - `[[execution/verify_format_and_typos.py]]`: PASS 100% (Margin 4-4-3-3, APA 7th tables, 0 typo/leakage).

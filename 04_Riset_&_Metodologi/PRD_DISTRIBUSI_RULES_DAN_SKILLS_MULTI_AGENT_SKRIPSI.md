# 📜 PRD & Matriks Distribusi Rules, Directives, dan Skills ke Tim Multi-Agent Skripsi

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Mendokumentasikan secara permanen distribusi 11 *inviolable rules*, 18 directives SOP, dan 6 *specialized skills* ke dalam konfigurasi sistem (`SOUL.md` & `skills/thesis/`) seluruh agen tim skripsi Pokémon TCG Arthur Reezan.
> - **Masalah yang Diselesaikan:** Mencegah amnesia antar-agen dan memastikan setiap agen spesialis bekerja tanpa melakukan kesalahan (*zero regression*, *zero AI-markers*, kepatuhan mutlak UKRIDA 2023, integritas MRA 2-tahap).
> - **Keputusan/Output:** Seluruh 6 profil agen Hermes (`@skripsi-orchestrator`, `@auditor-skripsi`, `@literatur`, `@metodologi`, `@penulis`, `@statistik`) telah diperbarui `SOUL.md`-nya dan dipasangi paket *thesis skills* lengkap di `D:/AI/hermes/profiles/<agent>/skills/thesis/`.

---

## 1. Arsitektur 3 Lapis Sistem Multi-Agent (AGENTS.md)

1. **Layer 1: Directive (Apa yang Harus Dikerjakan):**
   - 18 SOP di direktori `directives/*.md` mengatur alur kerja baku, mulai dari unduhan PDF, audit kesetaraan naskah, verifikasi LibGen, hingga sinkronisasi Mendeley.
2. **Layer 2: Orchestration (Pengambilan Keputusan & Perutean Cerdas):**
   - Dijalankan oleh `@skripsi-orchestrator` untuk mendelegasikan tugas ke agen spesialis, menyintesis hasil, dan menangani kendala teknis.
3. **Layer 3: Execution (Eksekusi Deterministik):**
   - Skrip Python di direktori `execution/*.py` yang mengeksekusi perhitungan, validasi paritas, parsing BibTeX, kompilasi XeLaTeX, dan generator Word.

---

## 2. Matriks Penugasan Rules & Directives Per Agen

| Agen Spesialis | Peran Utama | Rules Mandatori (.agents/rules/) | Directives Kunci (directives/) | Skills Terpasang (skills/thesis/) |
|:---|:---|:---|:---|:---|
| **@auditor-skripsi** | Quality Gatekeeper & Auditor Independen | - `mandatory_thesis_sync_and_quality.md`<br>- `mandatory_citation_typography_and_gap_rules.md`<br>- `mandatory_gdocs_and_docx_citation_linking.md`<br>- `mandatory_no_ai_markers.md`<br>- `mandatory_no_raw_latex_in_docx.md`<br>- `mandatory_humanized_academic_tone.md`<br>- `mandatory_zero_unsupported_claims.md`<br>- `mandatory_verifiable_theories_and_books.md`<br>- `no_login_wall_empirical_sources.md` | - `run_paper_audit.md`<br>- `verify_ukrida_2023_guidelines.md`<br>- `audit_pdf_vs_docx_fidelity.md`<br>- `verify_mendeley_integrity.md` | - `paper-audit`<br>- `humanizer-id`<br>- `gdocs-citation-linker`<br>- `task-breakdown` |
| **@literatur** | Riset Pustaka & Verifikasi Fisik PDF | - `mandatory_verifiable_theories_and_books.md`<br>- `no_login_wall_empirical_sources.md`<br>- `mandatory_citation_typography_and_gap_rules.md`<br>- Rasio 80/20 & 14 Seminal Terkunci | - `download_journal_references.md`<br>- `empirical_source_verification.md`<br>- `verify_book_sources_libgen.md`<br>- `verify_mendeley_integrity.md` | - `paper-audit`<br>- `task-breakdown` |
| **@metodologi** | Desain Penelitian & Instrumen Bab III | - `mandatory_zero_unsupported_claims.md`<br>- Parameter Kanonis `SOURCE_OF_TRUTH.md` (Populasi Jakarta Barat, $N \ge 111$, 60 item) | - `verify_ukrida_2023_guidelines.md`<br>- `run_paper_audit.md` | - `paper-audit`<br>- `task-breakdown` |
| **@penulis** | Penulisan Naskah Ilmiah Bab I–V | - `mandatory_humanized_academic_tone.md`<br>- `mandatory_no_ai_markers.md`<br>- `mandatory_no_raw_latex_in_docx.md`<br>- `mandatory_citation_typography_and_gap_rules.md`<br>- `mandatory_gdocs_and_docx_citation_linking.md`<br>- `mandatory_zero_unsupported_claims.md` | - `generate_thesis_word_document.md`<br>- `verify_ukrida_2023_guidelines.md` | - `humanizer-id`<br>- `gdocs-citation-linker`<br>- `paper-audit` |
| **@statistik** | Analisis Statistik MRA 2-Tahap | - Model 2-Tahap Aiken & West (1991)<br>- Wajib Mean-Centering ($X_i^*, M^*$)<br>- Arah Moderasi Pelemahan (Dampening, H4–H6 negatif)<br>- Standar Tabel APA 7th (Zero raw LaTeX) | - Evaluasi Asumsi Klasik (VIF < 5)<br>- Simple Slopes ($\pm 1 \text{ SD}$) | - `paper-audit`<br>- `task-breakdown` |
| **@skripsi-orchestrator** | Pemimpin Orkestrasi & Sinkronisasi | - Seluruh 11 Rules Mandatori<br>- Obsidian Second Brain Protocol<br>- Extended 11 Quality Gates (11/11 PASS) | - `universal_thesis_graph_of_agents.md`<br>- Seluruh 18 Directives | - Seluruh 6 Skills Lengkap |

---

## 3. Rincian Penegakan Aturan (Negative Constraints & Quality Gates)

1. **Paritas 6-Arah Tanpa Desinkronisasi:**
   - LaTeX TeX = Word DOCX = Markdown MD = BibTeX = Mendeley RIS = PDF (58 Halaman).
2. **Tipografi Hitam Murni (*Pure Black #000000*):**
   - Tidak ada warna tema Word (`w:themeColor`). Seluruh judul dan teks tabel wajib RGB `000000`.
3. **Format Sitasi In-Text APA 7th:**
   - Hanya nama belakang (*surname only*), haram gelar akademik.
   - 2 penulis: `&` dalam kurung, `dan` dalam kalimat.
   - 3+ penulis: Penulis pertama + `et al.` sejak pemunculan pertama.
4. **Zero AI Telltale Markers:**
   - Dilarang membiarkan karakter markdown mentah (`$`, `*`, `#`, ```) atau emoji tercetak dalam PDF/DOCX resmi.
5. **Zero Unsupported Claims:**
   - Setiap angka dan data harus didukung bukti tabel/dokumen riil (misal: PriceCharting, Statista, laporan resmi BPS/Pokémon Company). Dilarang membuat asumsi demografi tanpa sensus.

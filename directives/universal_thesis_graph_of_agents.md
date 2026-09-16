# Directive: Universal Thesis Graph of Agents — SOP Eksekusi

> [!SUMMARY] Tujuan & Ruang Lingkup Directive Ini
> - **Tujuan:** SOP baku menjalankan framework [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] sebagai graph 11 agen (A0–A11) dengan gerbang observable.
> - **Masalah yang Dicegah:** Eksekusi melompat fase, audit per-edit yang boros token, desync LaTeX↔Word, silent-drop Mendeley, ghost citation, dan klaim lolos tanpa verifikasi.
> - **Otoritas:** [[04_Riset_&_Metodologi/REUSABLE_THESIS_PLAYBOOK.md]] · [[05_Pedoman_&_Referensi/PRD_AI_Dosen_Pembimbing_Skripsi_v2.md]] · [[.agents/rules/3_layer_architecture.md]].

---

## 1. Prasyarat (Pre-flight, A11)

1. Baca `graphify-out/manifest.json` atau `graphify-out/GRAPH_REPORT.md`.
2. Baca [[00_DASHBOARD_SECOND_BRAIN.md]] + Source of Truth aktif.
3. Nyatakan kesiapan kontekstual (fase + keputusan terkunci D-nn).
4. Jangan mulai kerja tanpa pre-flight. Sesi tanpa pre-flight dianggap tidak terjadi (C-LOG-1).

## 2. Fase Eksekusi (urutan wajib)

| Fase | Agen | Perintah / Skill | Gerbang DONE (gagal = berhenti) |
|---|---|---|---|
| F1 Framing | A1 | Isi `TEMPLATE_SOURCE_OF_TRUTH_UNIVERSAL.md` → bekukan unit/populasi/periode/estimand/eksklusi/selesai-jika | Checklist Layak 10 poin playbook ✅ |
| F2 Canon | A2 | `py execution/verify_book_sources.py` + uji incognito/curl tiap URL | `NOT_FOUND=0`, 0 login-wall |
| F3 Evidence | A3 | `py execution/verify_pdf_headers.py` → `py execution/generate_journal_catalog.py` → `py execution/verify_live_urls.py` → `py execution/verify_all_citation_links.py` (0 DEAD; WALLED dicatat; DEAD = perbaiki via Crossref/PDF primer atau GANTI sumber + selaraskan klaim, C-LINK-1) | `%PDF` semua; katalog lengkap; live-check PASS |
| F4 Construct | A4 | `py execution/analyze_completeness_construct.py` (atau padanannya per topik) | Tiap konstruk → teori + skala baku |
| F5 Method | A5 | Tulis Bab 3, freeze Model 1/2 + N + etik | Estimand + model frozen verbatim |
| F6 Stats | A6 | Olah data (SPSS/R) + laporkan ΔR², effect size | p-value tidak pernah tanpa effect size |
| F7 Build | A7 | `py execution/build_proposal_word.py [--no-chapter3]` + `py execution/build_proposal_nobab3_pdf.py` + `py execution/sync_markdown_from_tex.py`. Wajib: angka TOC/LOT/LOF = angka cetak PDF (C-LOT-1); `\caption{...}` mentah dilarang lolos; entri LOT/LOF terhyperlink 100% (laporan builder `N caption, M entri` harus imbang) | File ter-build tanpa error XML |
| F8 Parity | A8 | `py execution/run_thesis_graph.py --gate parity` (G1–G7) + `verify_all_citation_links.py` (0 DEAD). Mendeley cloud: `--push` + `--prune --dry` + `--sync-links`, lalu verifikasi baca-balik (N dokumen = N RIS). Token mati → `--refresh` | 7/7 PASS, 1 FAIL = BUILD BROKEN |
| F9 Audit | A9 | `directives/run_paper_audit.md` **hanya** pada 5 trigger (Pra-Bimbingan, Pra-Sempro, Major Rewrite, Verifikasi Resolusi, On-demand) | Critical=0, Major selesai/terjustifikasi |
| F10 Defense | A10 | `py execution/build_interactive_presentation.py` + `py execution/build_study_guide_pdf.py` | Panduan sinkron SoT; PDF <5MB |
| F11 Log | A11 | Append [[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]] + update dashboard | Timestamp + keputusan + file tersentuh |

Paralelisasi aman: F2+F3 boleh paralel setelah F1 DONE. Varian Full/NoBab3 di F7 boleh paralel. Sisanya sekuensial.

## 3. Gerbang Parity A8 (detail perintah)

```powershell
py execution/run_thesis_graph.py --gate parity
# setara manual:
py execution/verify_mendeley_integrity.py   # G1
py execution/verify_live_urls.py            # G2
py execution/verify_all_citation_links.py   # G2b (0 DEAD, C-LINK-1)
py execution/verify_ukrida_compliance.py    # G3
py execution/verify_docx_typography.py      # G4
py execution/verify_pdf_docx_parity.py      # G5
py execution/verify_word_outline.py         # G6
py execution/verify_book_sources.py         # G7
```

Aturan: jalankan berurutan; berhenti di FAIL pertama; perbaiki secara surgical di agen pemilik; ulangi dari gerbang yang gagal (self-anneal: fix script → test → update directive ini).

## 4. Kebijakan Audit Tier (anti-boros)

- **T1 Continuous** (<2s, 0 token): G3+G4+G5+G6 tiap edit harian.
- **T2 Heuristic** pra-kompilasi: `paper-audit/scripts/proofing_scan.py` + BibTeX.
- **T3 Gated** deep audit: hanya 5 trigger F9. Dilarang audit per-edit kecil.

## 5. Karpathy Hygiene (A0, tiap handoff)

Sebelum serah-terima antar agen, jawab 8 checklist ini (dari §6 framework):

1. GOAL-link tertulis? 2. Asumsi + alternatif tertulis? 3. Acceptance observable? 4. Verified vs Proposed dipisah?
5. Falsifier diisi? 6. Tidak ada skipped-check diklaim pass? 7. Opsi paling sederhana dipilih? 8. Perubahan surgical (file lain utuh)?

Satu jawaban TIDAK = kembalikan ke agen pengirim.

## 6. Edge Cases

- **Pedoman kampus ≠ UKRIDA:** ganti angka di `verify_ukrida_compliance.py` + PRD audit pedoman; graph tidak berubah.
- **Metode ≠ MRA:** ganti hanya F5/F6 (model frozen + uji); F8/F9 tetap sama.
- **Golden truth bukan LaTeX:** tetapkan 1 golden truth (`.tex`/`.docx`/`.md`); A7+A8 mengikutinya; jangan dua kebenaran.
- **Buku lokal tak ada di LibGen:** scan resmi Perpusnas + catat di ledger sebagai `observation`; jika teori esensial hilang → ganti setara (lihat C-BOOK-1).
- **URL login-wall tapi data krusial:** ganti agregator terbuka + lampirkan screenshot di lampiran (lihat `no_login_wall_empirical_sources`).

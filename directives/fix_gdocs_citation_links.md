> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** SOP baku memperbaiki sitasi-klik yang putus setelah DOCX di-convert ke Google Docs web.
> - **Masalah yang Diselesaikan:** Konverter Google membuang `<w:hyperlink w:anchor>` + bookmark Word sehingga `(Penulis, Tahun)` jadi teks mati di Docs.
> - **Keputusan/Output:** Dua lapis — (1) DOCX visible-bookmark `Ref_*`/`Cap_*`, (2) relink native via [[execution/fix_gdocs_citation_links.gs]].

# Directive: Perbaikan Sitasi-Klik di Google Docs Web

> **Otoritas:** [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] (`C-CITE-2`) · [[04_Riset_&_Metodologi/IMPLEMENTATION_PLAN_LOT_LOF_MENDELEY.md]] §6 · `execution/build_proposal_word.py` (`link_citations_to_dp`).

## 1. Akar Masalah (terverifikasi)

1. DOCX memakai hyperlink internal OOXML `<w:hyperlink w:anchor="Ref_kunci">` ke `<w:bookmarkStart w:name="Ref_kunci">` di tiap entri [[DAFTAR PUSTAKA]]. Di Word desktop: 241 tautan (full) / 202 (NoBab3), Ctrl+klik 100% jalan.
2. Bookmark lama berawalan underscore (`_Ref_*`, `_Cap_*`) = *hidden bookmark* menurut spec Word. Importer Google Docs memprioritaskan bookmark visible dan sering membuang hidden + anchor-nya. Hasil: sitasi putus di Docs web.
3. Ini limitasi konverter Google (kasus serupa: Paperpile refs terhapus saat edit via Docs web), bukan kesalahan isi naskah.

## 2. Perbaikan Lapis-1 (DOCX, sudah diterapkan)

- `execution/build_proposal_word.py`: `_Ref_<kunci>` → `Ref_<kunci>`, `_Cap_<T>_<n>_<m>` → `Cap_<T>_<n>_<m>` (visible, tetap `<40` char, mulai huruf).
- Rebuild: `py execution/build_proposal_word.py` + `--no-chapter3` → DP bookmark 55 entri, sitasi 241/202 tautan.
- Verifikasi: `py execution/run_thesis_graph.py --gate parity` wajib 7/7 PASS. Word: Ctrl+klik sitasi → lompat ke DP.

## 3. Perbaikan Lapis-2 (Google Docs, wajib setelah Convert)

Gunakan [[execution/fix_gdocs_citation_links.gs]] (Apps Script, syntax-checked via `node --check`):

1. Upload DOCX ke Drive → Open with Google Docs (Convert).
2. Di Docs hasil konversi: Extensions → Apps Script → hapus Code.gs → paste isi `.gs` → Save.
3. Run → `relinkCitationsToDP` → Authorize → Run lagi.
4. Kembali ke Docs: klik biasa sitasi `(Statista, 2024)` → lompat ke DP.
5. (Opsional) Run `verifyCitationLinks` untuk laporan total/ber-link/tak ber-link.
6. Script idempoten (membersihkan bookmark lama dulu); DP multi-penulis (`dan`/`and`/`&`) + `et al.` + korporat (`Statista`, `The Pokémon Company`) ditangani via pencocokan surname+tahun.

## 4. Batasan Jujur

- Field plugin Mendeley Cite tetap tidak bisa dibuat manual andal; rantai resmi = paragraf → DP (Docs bookmark) → URL biru di entri DP → sumber/Mendeley.
- Jika Google mengubah importer di masa depan, Lapis-1 saja mungkin cukup; sampai saat itu Lapis-2 adalah garansi.
- Jangan menambah karakter `[🔗]` di sitasi — melanggar format UKRIDA.

## 5. Verifikasi Selesai

- [ ] DOCX: `verify_docx_typography.py` + `verify_pdf_docx_parity.py` PASS.
- [ ] Word desktop: Ctrl+klik 3 sitasi acak → DP benar.
- [ ] Google Docs (setelah script): klik biasa 3 sitasi acak → DP benar; `verifyCitationLinks` menunjukkan 0 tak ber-link (atau hanya sitasi tak terparse yang dilaporkan jujur).

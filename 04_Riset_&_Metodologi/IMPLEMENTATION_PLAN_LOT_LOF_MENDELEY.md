> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Rencana implementasi tereksekusi untuk 3 kendala user 16 Sep 2026 malam: (1) Daftar Tabel/Gambar di Word, (2) linkage Mendeley–Daftar Pustaka–sitasi paragraf, (3) push cloud belum lengkap.
> - **Masalah yang Diselesaikan:** Angka LOT/LOF basi, entri tak berpotensi-titik & tak bisa diklik, caption longtable bocor mentah, baris highlight Gao/Sultan fiktif, cloud hanya 3/55 dokumen.
> - **Keputusan/Output:** Semua diperbaiki + terverifikasi (11/11 gerbang, 0 link mati, cloud 55/55); aturan diabadikan di [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] (`C-MEND-2`, `C-LOT-1`) dan [[directives/universal_thesis_graph_of_agents.md]] (F7/F8).

# IMPLEMENTATION PLAN — LOT/LOF Hyperlink + Mendeley Linkage (eksekusi 16 Sep 2026)

## 1. Masalah 1 — Daftar Tabel/Gambar Word

| Gejala (bukti) | Akar masalah | Perbaikan (file:baris) |
|---|---|---|
| Angka halaman basi era 55 hlm (mis. Tabel 2.1→15, Gambar 2.1→20) padahal PDF 62 hlm | `lot_items`/`lof_items`/`toc_items` hardcoded tak pernah disinkron pasca-Sesi 16 | `execution/build_proposal_word.py`: angka = angka cetak PDF (LOT: T1.1→13,14,15; T2.1→22; T3.1→30; T3.2→36; T3.3→44; LOF: 2,3,5,29,43; TOC statis Bab 1–3 + sub-bab + DP diselaraskan; label 2.1.3 → *Collection-Goal Tipping Point Effect*) |
| Titik-titik tak tampil di Word (screenshot user) | Stop paragraf ganda konflik (`clear@7938` + `right@7937`) menutupi style | Helper `_clear_latent_tab_stops` + `_add_dot_tab_7938` (satu stop 7938-dot); style kustom TOC11/21/31 sudah benar (right-dot-7938) sehingga hasil akhir = satu stop efektif |
| Entri tak bisa diklik | Paragraf statis tanpa hyperlink/bookmark | `link_lot_lof_entries(doc)`: bookmark tiap caption tubuh + bungkus entri dalam `<w:hyperlink>` internal (tetap hitam #000000, tanpa garis bawah). Hasil: full 10 caption/12 entri, NoBab3 6/8 — 100% |
| `\caption{Matriks...}` mentah terlihat di badan DOCX | Cabang `\caption{...}` longtable tak ditangani builder | Cabang baru: petakan judul caption → nomor via `lot_items`, render caption tubuh baku (gagal petakan = fallback judul polos, tak pernah dibuang diam-diam) |
| G4 FAIL pasca-perbaikan ("missing tab stop") | Verifier hanya baca stop paragraf; Word menormalisasi stop identik-style | `execution/verify_docx_typography.py`: fallback baca stop dari definisi style (`_style_tab_stops`) — gerbang selaras kebenaran render Word |

Struktur frontmatter (Daftar Isi → Daftar Tabel → Daftar Gambar, masing-masing halaman sendiri) DIPERTAHANKAN — sesuai Pedoman UKRIDA; yang diperbaiki adalah isi, angka, titik, dan klikabilitasnya.

## 2. Masalah 2 — Linkage Mendeley ↔ Daftar Pustaka ↔ Sitasi Paragraf

Mekanisme tiga-arah (aturan baru `C-MEND-2`):
1. **Kunci**: `\cite{kunci}` tex = key BibTeX = `ID` RIS = judul dokumen cloud (cocok string) — diverifikasi G1 + perbandingan API.
2. **Link**: `UR` RIS (53/55) → `websites` dokumen cloud via `--sync-links`; DOI → `identifiers`.
3. **Bukti sidang**: `directives/highlight_mendeley_citations.md` — baris Gao & Sultan ditulis ulang ke metadata ground truth (judul/jurnal/hlm/DOI asli) + status PDF jujur (belum diarsipkan → unduh via DOI, jangan karang nomor halaman).
4. Token kedaluwarsa (401) → `--refresh` (perintah baru di konektor), bukan `--auth` ulang.

## 3. Masalah 3 — Push Cloud Belum Lengkap

Fakta: akun cloud tinggal 3/55 dokumen (perpustakaan lama terhapus di sisi user/Mendeley). Tindakan: `--push` membuat 52 dokumen (0 gagal) → `--prune` tidak diperlukan (tak ada basi) → verifikasi baca-balik API: **55 dokumen, 53 ber-websites, 0 judul hilang**. Perintah `--prune` (baru, dengan `--dry`) tersedia untuk pembersihan pasca-ganti sumber.

## 4. Verifikasi Penutup (bukti, bukan klaim)

- `run_thesis_graph.py --gate extended`: **11/11 PASS** (G1–G7 + X1–X4).
- `verify_all_citation_links.py`: 32 hidup / 21 walled / **0 MATI**.
- Probe XML: entri LOT/LOF = `<w:hyperlink w:anchor>` + 1 stop efektif right-dot-7938; 0 bocoran `\caption`.
- Cloud API: 55/55 judul cocok RIS; 53 websites.

## 5. Rollback (jika regresi di sesi berikut)

- Builder: `git revert` blok `_clear/_add/link_lot_lof` + cabang `\caption` + list angka (satu commit terpisah disarankan).
- Verifier G4: hapus fallback `_style_tab_stops` bila Word truth berubah.
- Cloud: `--prune --dry` sebelum hapus massal; token di `token.json` (gitignored) dapat diregenerasi via `--auth`.

## 6. Sitasi Tubuh Bisa Diklik → Daftar Pustaka (aturan `C-CITE-2` & `C-CITE-3`)

| Gejala (bukti) | Akar masalah | Perbaikan 3 Lapis |
|---|---|---|
| Sitasi `(Statista, 2024)` teks mati, diklik diam di Word | Generator hanya menulis teks; field plugin Mendeley tak bisa dibuat manual andal | **Layer 1 (DOCX):** `link_citations_to_dp`: bookmark visible `Ref_<kunci>` per entri DP (urutan `.bbl`; tak sama = mati total, tanpa awalan `_Ref_`) + hyperlink internal OOXML tiap kemunculan (tetap hitam, tanpa garis bawah). Pola dari `.aux` natbib: paren, naratif, bare multi-kata, + segmen multi-sitasi (termasuk penulis tunggal) |
| Sitasi putus saat di-convert ke Google Docs Web | Konverter Google Drive membuang `<w:hyperlink w:anchor>` dan bookmark Word | **Layer 3 (Google Docs):** Jalankan Apps Script `execution/fix_gdocs_citation_links.gs` (`relinkCitationsToDP`) via menu Extensions > Apps Script. Membuat bookmark Docs native (`#bookmark=<id>`) per entri DP dan menautkan sitasi in-text. Navigasi cukup klik biasa (single click). |
| `et al..` titik ganda di DOCX | `clean_academic_text` menambah titik di atas titik yg ada | Konsumsi titik opsional (`et al\.?`); pola toleran (`et al\.+`) |
| `Pok{\'e}mon` mentah di DOCX | Jalur baca-TeX langsung lolos dari normalisasi aksen | Normalisasi aksen di `clean_academic_text` (é/ü/ö/è) |
| `(; Hayes, 2018)` — teks HILANG (insiden serius, tertangkap sebelum kirim) | Offset `p.text` vs run langsung bergeser oleh teks hyperlink bersarang | Peta offset jujur (`_para_map`, unit atomik) + split pada node + snapshot/restore + verifikasi `p.text` per paragraf. Pelajaran: JANGAN rebuild run dari offset buta; JANGAN bungkam exception tanpa invariant check |
| Navigasi berbeda antar platform | Perilaku native software pengolah kata | Di Word Desktop = **Ctrl+klik**; di Google Docs Web (setelah script) = **klik biasa** (single click) |

Verifikasi:
1. **Layer 1 & 2 (DOCX):** Full 55/55 kunci terhubung (NoBab3 51 + 4 khusus-Bab-3 sah tak terhubung); 0 `(;`; 0 kunci mentah; 0 anchor yatim; teks paragraf identik pre/post (invariant check); 11/11 gerbang tetap PASS.
2. **Layer 3 (Google Docs):** `relinkCitationsToDP()` sukses memetakan DP dan sitasi tubuh; `verifyCitationLinks()` membuktikan 0 sitasi tak ber-link; klik biasa pada sitasi langsung melompat ke DAFTAR PUSTAKA.


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

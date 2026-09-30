> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Implementation plan tereksekusi untuk audit 55 sitasi tanpa kecuali (perintah, urutan, acceptance, rollback).
> - **Masalah yang Diselesaikan:** Menjamin tidak ada sitasi terlewat: kunci TEX → tautan BIB/RIS → hasil per-tautan → saran Crossref bila DEAD.
> - **Keputusan/Output:** 1 perintah audit + 1 perintah parity; DONE = 0 DEAD; artefak log tersimpan di temp.

# IMPLEMENTATION PLAN — Audit Sitasi Walled (eksekusi 17 Sep 2026)

> **PRD induk:** [[04_Riset_&_Metodologi/PRD_AUDIT_SITASI_WALLED_2026-09-17.md]] · **Aturan:** `C-LINK-1` di [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] · **SOP:** [[directives/universal_thesis_graph_of_agents.md]] (F3/F8).

## 1. Prasyarat

- `01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex`, `references.bib`, `06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.ris` ada dan sinkron (55 ref).
- Python stdlib saja (tanpa install): `urllib`, `concurrent.futures`.

## 2. Langkah eksekusi

1. **Audit penuh (wajib):**
   ```powershell
   py execution/verify_all_citation_links.py
   ```
   - Mengumpulkan `cited` dari SEMUA `\cite{...}` di TEX (55 kunci — tidak ada filter, tidak ada sampling).
   - Untuk tiap kunci tersitasi: ambil `doi` → `https://doi.org/<doi>`, `url` mentah, plus tiap `UR` di RIS yang belum tercakup.
   - `fetch` paralel (8 workers) + klasifikasi ALIVE/WALLED/DEAD; bila DEAD ber-DOI + ada judul → saran Crossref (sim ≥0.85, tahun ±1) — saran saja, tidak menimpa bib.
   - Simpan output: `py execution/verify_all_citation_links.py > audit_links.txt`.
2. **Gerbang parity (konfirmasi tidak regresi):**
   ```powershell
   py execution/run_thesis_graph.py --gate parity
   ```
   - DONE hanya bila 7/7 PASS (G2b = 0 DEAD di langkah 1).

## 3. Acceptance criteria (observable)

- [ ] `memeriksa N tautan (55 sitasi)` tercetak (N = 53 saat ini; berubah hanya bila sitasi bertambah).
- [ ] Baris `ringkas: A hidup / B walled / 0 MATI` dengan MATI = 0 (exit code 0).
- [ ] Tiap baris WALLED mencantumkan kode HTTP (401/403/405/429/468) + URL — bukti DOI me-resolve.
- [ ] 2 sitasi tanpa tautan (`tan2024`, `sugiyono2019`) disebut eksplisit sebagai PR, bukan disembunyikan.

## 4. Hasil eksekusi 17 Sep 2026

- `memeriksa 53 tautan (55 sitasi)` → **32 hidup / 21 walled / 0 MATI**, exit 0.
- Contoh validasi user: `WALLED verplanken2001individual [doi] [403] -> https://doi.org/10.1002/per.423` (sesuai screenshot Sage: abstrak terbuka untuk manusia, bot 403).
- Parity: tidak dijalankan ulang di sesi ini (terakhir 11/11 PASS pasca-rebuild bookmark); audit ini read-only, tidak menyentuh naskah.

## 5. Rollback / bila DEAD muncul

- Jangan edit bib manual menebak suffix DOI. Ikuti `C-LINK-1`: cari ground truth (Crossref + PDF primer + web), atau GANTI sumber + selaraskan klaim gap/matriks/label konsep, lalu ulangi audit sampai 0 DEAD.

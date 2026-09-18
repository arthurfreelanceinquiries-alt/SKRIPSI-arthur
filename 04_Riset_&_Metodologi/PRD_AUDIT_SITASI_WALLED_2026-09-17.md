> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** PRD plan audit klikabilitas SELURUH sitasi naskah (0 terlewat) untuk menjawab pertanyaan user: berapa sitasi yang terhalang paywall/anti-bot.
> - **Masalah yang Diselesaikan:** Membedakan tegas WALLED (DOI sah tapi penerbit pasang dinding, mis. Sage `verplanken2001` di screenshot user) vs DEAD (DOI mati wajib diganti) per aturan [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] (`C-LINK-1`).
> - **Keputusan/Output:** 55 sitasi diaudit → 53 tautan diperiksa → 32 hidup / 21 walled / 0 MATI → PASS; 2 sitasi tanpa tautan sah tetap PR terbuka.

# PRD — Audit Walled vs Dead Seluruh Sitasi (17 Sep 2026)

> **Otoritas:** [[directives/universal_thesis_graph_of_agents.md]] (F3, F8-G2b) · `C-LINK-1` · Skrip [[execution/verify_all_citation_links.py]] · Naskah [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex]] + [[01_Naskah_Utama/references.bib]] + [[06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.ris]]

## 1. Scope (tanpa kecuali)

- Sumber sitasi: SELURUH kunci `\cite{...}` di `.tex` → **55 sitasi**.
- Sumber tautan: `doi`+`url` tiap entri tersitasi di `.bib` + `UR` di RIS → **53 tautan** diperiksa.
- Selisih 2 = sitasi tanpa tautan sah (dikenal, bukan terlewat): `tan2024ketidakpastian` (DOI katalog mati, portal OJS tak terjangkau) dan `sugiyono2019metode` (hanya pindaian lokal). Keduanya dilaporkan jujur, tidak dikarang.

## 2. Metodologi (C-LINK-1)

- `fetch` stdlib + threads (8 workers), UA browser, timeout 20s + 2 retry untuk error jaringan (HTTP respons tidak di-retry).
- Klasifikasi: ALIVE (200/301/302/303/307/308) / WALLED (401/403/405/429/468 = DOI terdaftar & me-resolve, tapi anti-bot/paywall penerbit) / DEAD (404/410/5xx/timeout/DNS = wajib perbaiki via Crossref/PDF primer atau GANTI sumber + selaraskan klaim).
- Contoh user (screenshot): `verplanken2001individual` DOI `10.1002/per.423` → HTTP 403 di Sage = **WALLED** (halaman abstrak terbuka di browser manusia seperti screenshot, tapi bot ditolak). Bukan DOI mati.

## 3. Hasil (17 Sep 2026, exit 0)

**Ringkasan: 32 hidup / 21 terhalang-bot / 0 MATI.**

WALLED (21, DOI sah — bukan FAIL):
`babin1994work`, `barasz2017pseudo`, `barber2008all`, `baumeister2002yield`, `colline2024biases` (468 wall penerbit pasca-302), `gao2014completing`, `green1991subjects`, `hirschman1982hedonic`, `katauke2023financial`, `long2000consuming`, `pricecharting2024` (403 Cloudflare katalog terbuka), `rook1987buying`, `rook1995normative`, `simon1955behavioral`, `spero2004approach`, `stern1962significance`, `tangney2004high`, `thaler1981economic`, `thaler1985mental`, `verplanken2001individual` (contoh user), `vohs2007spent`.

ALIVE (32): termasuk `statista2024pokemon`, `pokemoncompany2024`, `gong2024unveiling`, `sultan2012building`, `tirtayasa2020effect`, `zheng2019impact`, 8 DOI Crossref exact + Open Library.

## 4. Keputusan

- WALLED ≠ cacat naskah: sitasinya sah (Crossref terdaftar, judul/jurnal/vol cocok), hanya butuh browser manusia / akses kampus untuk full-text. Tidak ada penggantian sumber.
- 0 DEAD → gerbang G2b PASS. PR terbuka tinggal 2 sitasi tanpa tautan (`tan2024`, `sugiyono2019`).

## 5. Addendum pasca-audit (temuan entri campuran `barasz2017pseudo`)

- Saat menyusun [[04_Riset_&_Metodologi/BUKTI_AKSES_SITASI_WALLED.md]], pengecekan judul-vs-DOI menemukan entri campuran: penulis+judul Barasz et al. (2017) terpasang pada jurnal/vol/hlm/DOI milik paper lain (Rozenkrants et al., JCR 44(4):759–777, `10.1093/jcr/ucx067`) — kelas kesalahan yang sama dengan kasus Gao/Sultan (sesi 16 Sep).
- Ground truth (Crossref, 17 Sep): Barasz, John, Keenan & Norton (2017), *Pseudo-set framing*, *Journal of Experimental Psychology: General*, 146(10):1460–1477, DOI `10.1037/xge0000337`.
- Ditulis ulang di: `references.bib`, DP [[01_Naskah_Utama/PROPOSAL_SKRIPSI_POKEMON_TCG.md]] (entri 8), [[03_Draft_Per_Bab/DAFTAR_PUSTAKA_TENTATIF.md]], [[03_Draft_Per_Bab/BAB_II_TINJAUAN_PUSTAKA.md]] (sekaligus meluruskan *Journal of Marketing Research* → *Journal of Marketing* untuk Gao di kalimat yang sama). Narasi Bab 1–3 tidak menyebut nama jurnal untuk Barasz sehingga tidak ada klaim teks yang perlu diselaraskan.
- Diregenerate: PDF (62 hlm, `.bbl` baru), DOCX (241 sitasi-klik), RIS/Bib Mendeley (55 ref).
- Audit ulang: **33 hidup / 20 walled / 0 MATI** (DOI baru ALIVE).
- Pelajaran sistemik: `verify_all_citation_links.py` hanya memeriksa status HTTP, bukan kecocokan judul — DOI salah-tapi-resolve lolos. Diusulkan penguatan C-LINK-1: cek judul-vs-Crossref berkala untuk seluruh DOI.

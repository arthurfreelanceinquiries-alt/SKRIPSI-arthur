> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Daftar bukti akses per sitasi WALLED (opsi A) agar tiap sitasi paywall tetap bisa dibuktikan ke dosen/penguji tanpa menghapusnya.
> - **Masalah yang Diselesaikan:** DOI bisa dibuka tapi full-text terkunci (contoh [[verplanken2001individual]] di Sage) sehingga mahasiswa takut sitasi dianggap fiktif.
> - **Keputusan/Output:** 20/20 DOI terkonfirmasi Crossref eksak (judul+jurnal+tahun); tiap entri punya ≥2 jalur bukti independen; status: PERTAHANKAN semua, 0 diganti; 1 entri campuran (`barasz2017pseudo`) ditulis ulang ke ground truth.

# Bukti Akses Sitasi Walled — 20 Entri + 1 Diperbaiki (17 Sep 2026)

> **Audit induk:** [[04_Riset_&_Metodologi/PRD_AUDIT_SITASI_WALLED_2026-09-17.md]] (32 hidup / 21 walled / 0 MATI) · **Aturan:** `C-LINK-1` di [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] · **Metode verifikasi:** `https://api.crossref.org/works/<DOI>` (17 Sep 2026, 20/20 cocok eksak) + `verify_all_citation_links.py` (HTTP resolve).

## Cara membaca tiap entri

- **Bukti-1 DOI resolve:** kode HTTP saat Fetcher bot mengakses `https://doi.org/<DOI>` (403/468 = terdaftar & me-resolve, hanya menolak bot — DOI fiktif akan 404 seperti kasus Gao lama).
- **Bukti-2 Crossref:** metadata terdaftar (judul + jurnal + tahun cocok dengan [[01_Naskah_Utama/references.bib]]).
- **Bukti-3 akses manusia:** apa yang terbuka di browser (abstrak/halaman artikel) + jalur full-text (Perpusnas, akses kampus, repositori OA, sitasi sekunder open).
- **Peran:** lokasi di naskah (dihitung dari [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex]]).

## Kelompok 1 — Fondasional Y (skala & definisi Impulsive Buying)

| Kunci | Peran | Bukti |
|---|---|---|
| `stern1962significance` (JM 1962, Sage 10.1177) | Klasifikasi 4 tipe impulse; Temuan B gap (4x) | DOI resolve 403; Crossref: *The Significance of Impulse Buying Today*, JM 1962 ✓; abstrak terbuka di Sage; disitasi ulang di [[amos2014meta]] (open meta-analisis) + [[beatty1998impulse]] (ALIVE) |
| `rook1987buying` (JCR 1987) | Definisi Y (4x) | DOI resolve 403; Crossref: *The Buying Impulse*, JCR 1987 ✓; disitasi ulang di hampir semua paper Y open (Amos 2014, Pranggabayu 2022) |
| `rook1995normative` (JCR 1995) | Skala normatif pembanding (2x) | DOI resolve 403; Crossref: *Normative Influences on Impulsive Buying Behavior*, JCR 1995 ✓; pasangan selalu dikutip bersama Rook 1987 |
| `verplanken2001individual` (EJP 2001, contoh user) | **Skala Y IBTS** (3x: Bab 1, 2, 3) | DOI resolve 403; Crossref: *Individual differences in impulse buying tendency*, EJP 2001 ✓; **abstrak lengkap terbuka** di journals.sagepub.com (sesuai screenshot user: 20-item, kognitif+afektif, Big Five) — isi skala didokumentasikan dari abstrak + sitasi sekunder open |

## Kelompok 2 — Fondasional X1 (hedonis)

| Kunci | Peran | Bukti |
|---|---|---|
| `hirschman1982hedonic` (JM 1982, Sage 10.1177) | Konsumsi pengalaman; Temuan B (4x) | DOI resolve 403; Crossref: *Hedonic Consumption*, JM 1982 ✓; disitasi ulang di [[arnold2003hedonic]] (ALIVE) |
| `babin1994work` (JCR 1994) | Nilai hedonis/utiliter (3x) | DOI resolve 403; Crossref: *Work and/or Fun*, JCR 1994 ✓; konstruknya dipakai ulang di paper open X1 |

## Kelompok 3 — Inti X2 (irreplaceable)

| Kunci | Peran | Bukti |
|---|---|---|
| `gao2014completing` (JM 2014) | *Collection-goal tipping point* (10x) | DOI resolve 403; Crossref: *The Influence of Initial Possession Level...*, JM 2014 ✓ (pernah diperbaiki dari DOI fiktif → ground truth, sesi 16 Sep); didukung [[belk1995collecting]] (buku, PDF lokal) |
| `barasz2017pseudo` (JEP:G 2017 — DIPERBAIKI 17 Sep, sebelumnya salah tertulis JCR/ucx067) | *Pseudo-Set Framing* (10x) | DOI resolve **ALIVE**; Crossref ground truth: Barasz, John, Keenan & Norton (2017), *Pseudo-set framing*, JEP:G 146(10):1460–1477, DOI `10.1037/xge0000337` ✓; entri bib/MD/draf diselaraskan; audit pasca-perbaikan 33 hidup / 20 walled / 0 MATI |
| `long2000consuming` (Emerald) | Temuan B gap X2 (2x) | DOI resolve 403; Crossref: *Consumption values and relationships*, JCM 2000 ✓ (satu digit pernah dibetulkan) |
| `spero2004approach` (Emerald) | Temuan B gap X2 (2x) | DOI resolve 403; Crossref: *Agents of change...*, QMR 2004 ✓ |

## Kelompok 4 — Inti Z + finansial (irreplaceable)

| Kunci | Peran | Bukti |
|---|---|---|
| `baumeister2002yield` (JCR 2002) | *Self-Regulation Theory* (7x) | DOI resolve 403; Crossref: *Yielding to Temptation...*, JCR 2002 ✓ (17 Sep) |
| `tangney2004high` (J. Personality 2004, Wiley) | **Skala BSCS** (8x) | DOI resolve 403; Crossref: *High Self-Control Predicts...*, 2004 ✓ (17 Sep); konstruk dipakai ulang di [[sultan2012building]] (ALIVE) + [[apidana2022peran]] (open) |
| `vohs2007spent` (JCR 2007) | *Ego depletion* (6x) | DOI resolve 403; Crossref: *Spent Resources...*, JCR 2007 ✓ (17 Sep) |
| `thaler1981economic` (JPE 1981) | *Planner-Doer* (5x) | DOI resolve 403; Crossref: *An Economic Theory of Self-Control*, JPE 1981 ✓ |
| `thaler1985mental` (Mktg Sci 1985) | *Mental Accounting* (1x) | DOI resolve 403; Crossref: *Mental Accounting and Consumer Choice*, 1985 ✓ |
| `barber2008all` (RFS, Oxford) | Temuan B X3 (4x) | DOI resolve 403; Crossref: *All That Glitters...*, RFS 2007/2008 ✓ |
| `simon1955behavioral` (QJE 1955) | *Bounded rationality* (1x) | DOI resolve 403; Crossref: *A Behavioral Model of Rational Choice*, QJE 1955 ✓ |

## Kelompok 5 — Metodologi & empiris (terbuka untuk manusia)

| Kunci | Peran | Bukti |
|---|---|---|
| `green1991subjects` (Taylor) | Formula sampel N (3x) | DOI resolve 403; Crossref: *How Many Subjects...*, MBR 1991 ✓; rumus `N ≥ 50+8k` dikutip ulang di [[hair2019multivariate]] + [[ghozali2018aplikasi]] (PDF lokal) |
| `katauke2023financial` (MDPI Sustainability) | Empiris Tabel 2.1 (6x) | DOI resolve 403 (anti-bot saja); artikel **fully open** di mdpi.com — buka di browser + simpan PDF |
| `colline2024biases` (OJS AFS) | Sitasi dosen K-04 wajib (11x) | 468 = wall penerbit pasca-redirect, bukan DOI mati (Crossref eksak, sesi 16 Sep); halaman artikel OJS terbuka di browser |
| `pricecharting2024` (katalog web) | Gambar 1.3 + data (3x) | 403 Cloudflare untuk bot; **katalog terbuka** di browser: `pricecharting.com/console/pokemon-shining-fates` — screenshot + tanggal akses sebagai bukti |

## Jalur bukti umum (berlaku semua entri)

1. **DOI resolve non-404** (bukti terdaftar) — log audit 17 Sep.
2. **Crossref eksak** (judul+jurnal+tahun) — cek 17 Sep, 20/20 cocok.
3. **Abstrak terbuka** di halaman penerbit (Sage/Oxford/Wiley menampilkan judul+abstrak gratis; paywall hanya untuk PDF full-text).
4. **Sitasi sekunder open** — paper ALIVE (Amos 2014, Beatty 1998, Arnold 2003, Sultan 2012, paper SINTA) mengutip dan merangkum temuan yang sama.
5. **Akses institusional** — Perpusnas RI / E-Resources kampus untuk full-text bila penguji meminta (taktik *Citation Chaining*, SULIT 11 di [[02_Persiapan_Sidang/01_Bank_Soal_&_Flashcard/03_PERTANYAAN_SIDANG_SULIT.md]]).

## Keputusan akhir

**PERTAHANKAN 20 sitasi walled (0 diganti) + 1 entri campuran ditulis ulang ke ground truth (`barasz2017pseudo` → JEP:G 146(10):1460–1477, DOI `10.1037/xge0000337`, kini ALIVE).** Audit pasca-perbaikan: 33 hidup / 20 walled / 0 MATI. Tindak lanjut fisik sebelum sidang: (1) simpan PDF `katauke2023` dari MDPI; (2) screenshot PriceCharting + halaman OJS Colline bertanggal; (3) siapkan jawaban lisan SULIT 11 untuk fondasional klasik.

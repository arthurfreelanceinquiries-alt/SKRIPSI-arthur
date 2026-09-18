# Directive: Ledger Bukti Halaman & PDF Lokal (D26 — 3 Tier)

> [!SUMMARY] Tujuan & Ruang Lingkup Directive Ini
> - **Tujuan:** Setiap klaim empiris penting dapat ditunjuk halaman PDF-nya saat sidang; setiap karya tersitasi punya bukti lokal.
> - **Masalah yang Dicegah:** Sitasi tanpa bukti buka-cepat, klaim "menurut jurnal X" yang tak terlacak, ghost edisi kedua.
> - **Otoritas:** [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]] D26 · Arsitektur 3-Layer (directives -> orchestration -> execution).

---

## 1. Tiga Tier (urutan wajib)

| Tier | Cakupan | Syarat | Bukti |
|---|---|---|---|
| **Wajib** (pre-sempro) | 10 jurnal empiris inti + seluruh klaim matriks gap (Subjek 1–7) & hipotesis (H1–H6) | PDF lokal + 1 baris ledger per klaim: `klaim → file → hlm. PDF → kutipan kunci ≤25 kata` | `EVIDENCE_LEDGER_HALAMAN.md` + `verify_evidence_ledger.py` PASS |
| **Pelengkap** | Teori/skala tersitasi (Rook, Verplanken, Arnold, Gao, Sultan, dst.) | PDF lokal di `02_Jurnal_Teori_&_Metodologi/` (kehadiran saja, tanpa halaman); bila paywall dan tak terjangkau mesin, status jujur `AKSES-TERVERIFIKASI` (landing penerbit HTTP 200 + metadata Crossref ✓ + jalur akses institusi/Perpusnas) | `verify_pdf_headers.py` PASS (atau status akses tercatat di ledger) |
| **Web** | 3 data industri (Statista, Pokémon Co., PriceCharting) | Snapshot HTML + tanggal akses + live-check 200 (tak bisa PDF) | `snapshots/` + `verify_live_urls.py` PASS |

## 2. Aturan pencatatan halaman

1. Nomor halaman = **halaman PDF** (angka tercetak bila sama; jika beda, tulis `hlm. PDF pX (tercetak pY)`).
2. Catat **hash ukuran + tanggal unduh** tiap PDF (paginasi antar-edisi berbeda; ledger terikat ke file spesifik).
3. Kelas klaim mengikuti Evidence Ledger: `fact / observation / inference / assumption` — halaman wajib untuk `fact` & `inference`.
4. Klaim yang PDF-nya Tier Pelengkap (belum diarsip) ditulis eksplisit `PDF: tier-pelengkap (belum diarsip)` — bukan klaim pass.
5. Halaman TIDAK masuk sitasi in-text (parafrasa APA tak wajib halaman) → nol desync naskah.

## 3. Eksekusi (Layer 3)

```powershell
py execution/verify_evidence_ledger.py   # Tier Wajib: PDF ada + baris ledger + hlm. dalam rentang
py execution/verify_pdf_headers.py       # Tier Pelengkap: %PDF + ukuran wajar
py execution/verify_live_urls.py         # Tier Web: HTTP 200 + tanggal akses
```

Gagal satu = BUILD BROKEN untuk paket kirim sempro (perbaiki file/ledger-nya, bukan klaimnya).

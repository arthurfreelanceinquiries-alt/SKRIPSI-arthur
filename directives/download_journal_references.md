# Directive: SOP Download dan Katalogisasi Referensi Jurnal Skripsi

## Tujuan
Mengunduh naskah lengkap (full-text) artikel jurnal dan konferensi yang menjadi rujukan dalam proposal/skripsi, memverifikasi integritas file PDF, dan menyusun katalog metadata terstruktur untuk memudahkan verifikasi dosen pembimbing, penguji, dan penulisan Bab 2 & Bab 3.

## Struktur Penyimpanan
Semua file referensi disimpan dalam direktori:
- `05_Referensi_Jurnal_PDF/01_Empiris_Utama_2021-2025/` (10 Jurnal Empiris Inti Tabel 2.1 & Subbab 2.4)
- `05_Referensi_Jurnal_PDF/02_Jurnal_Teori_&_Metodologi/` (Landasan Teori Seminal & Skala Pengukuran)
- `05_Referensi_Jurnal_PDF/KATALOG_REFERENSI_JURNAL.md` (Katalog Metadata Lengkap)

## Aturan Penamaan File
Format baku: `[Tahun]_[NamaPenulisUtama]_[KataKunciJudul]_[NamaJurnalSingkat].pdf`  
Contoh:
- `2024_Gong_et_al_Unveiling_Enigma_Blind_Box_Heliyon_Q1.pdf`
- `2024_Colline_Biases_Indonesian_Stock_Investor_AFS.pdf`

## Prosedur Eksekusi (Layer 3)
1. **Verifikasi Binary Header PDF:**
   Setiap file PDF yang diunduh wajib lolos verifikasi binary header `%PDF-`. Jika file berukuran sangat kecil (< 20 KB) atau berisi string `<!DOCTYPE html>` (halaman interstitial/Cloudflare/SafeLine), file dianggap tidak valid dan harus ditolak/diunduh ulang.
   - Script: `execution/verify_pdf_headers.py`
2. **Kompilasi Katalog Terstruktur:**
   Ekstrak metadata (Penulis, Tahun, Judul, Jurnal, Volume/Issue/Halaman, DOI, Status Indeksasi, Peran Variabel dalam Skripsi) dan buat file `KATALOG_REFERENSI_JURNAL.md`.
   - Script: `execution/generate_journal_catalog.py`

## Edge Cases & Solusi
- **Server WAF (SafeLine/Cloudflare):** Buka melalui sesi browser otentik atau gunakan mirror institusi (UPM, Harvard DASH, Garuda, OneSearch).
- **Client-Side PoW Challenge (PMC):** Ekstrak melalui Chrome CDP session atau Google Scholar mirror.
- **Paywalled Classics:** Gunakan preprint author di repositori universitas resmi (DASH Harvard, ResearchGate direct, open access repositories).

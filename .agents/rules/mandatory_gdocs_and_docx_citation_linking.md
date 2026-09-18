# 📜 Mandatory Rule: Penegakan Tautan Sitasi Lintas Platform (Word DOCX & Google Docs)

> **Otoritas:** Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 · Standard APA 7th Edition · [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] (`C-CITE-2` & `C-CITE-3`)  
> **Status:** Wajib dan Mengikat (*Mandatory Rule*) — Berlaku untuk setiap penambahan sitasi baru, bab baru, maupun regenerasi naskah Word & Google Docs.

---

## 1. Prinsip Utama: Sitasi Bukan Teks Mati (*Zero Dead Citation*)

1. **Seluruh Sitasi In-Text Wajib Terhubung:**
   - Setiap kemunculan sitasi in-text baik parentetikal `(Nama, Tahun)` maupun naratif `Nama (Tahun)` di dalam tubuh naskah **DILARANG KERAS** dibiarkan sebagai teks pasif/mati.
   - Sitasi harus berfungsi sebagai tautan interaktif yang langsung mengantarkan pembaca/penguji ke entri bibliografi lengkap di **DAFTAR PUSTAKA**.
2. **Kepatuhan Tiga Lapis (3-Layer Architecture):**
   - **Layer 1 (Word DOCX):** Menggunakan bookmark visible OOXML `Ref_<kunci>` (panjang `< 40` karakter, diawali huruf, tanpa awalan underscore `_Ref_`). Tautan internal memakai `<w:hyperlink w:anchor="Ref_<kunci>">`.
   - **Layer 2 (Verifikasi Invariant Parity):** Generator naskah wajib membuktikan 0 anchor yatim (*zero orphaned anchors*), 100% entri DAFTAR PUSTAKA ter-bookmark, dan tidak ada distorsi teks paragraf (`p.text` pre/post identik).
   - **Layer 3 (Google Docs Web Native):** Karena konverter Google Drive kerap melucuti hyperlink internal Word saat proses konversi, setiap naskah yang dibuka di Google Docs **WAJIB** menjalankan relinker Apps Script [`execution/fix_gdocs_citation_links.gs`](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/execution/fix_gdocs_citation_links.gs) untuk mengaktifkan native bookmark `#bookmark=<id>`.

---

## 2. Standar Tipografi Tautan Sitasi (Anti-Visual Pollution)

1. **Warna dan Garis Bawah di DOCX Tubuh:**
   - Hyperlink sitasi di dalam paragraf tubuh tesis **HARUS TETAP HITAM (*Pure Black*)** dan **TANPA GARIS BAWAH (*No Underline*)**.
   - **DILARANG** mengubah teks sitasi menjadi biru bergaris bawah di dalam paragraf tubuh karena merusak estetika naskah resmi akademik UKRIDA.
2. **Larangan Simbol Buatan:**
   - **DILARANG KERAS** menambahkan emoji atau simbol tautan seperti `[🔗]` atau `(link)` di samping nama penulis. Sitasi harus terlihat bersih dan murni sesuai kaidah APA 7th.
3. **URL Luar Hanya di DAFTAR PUSTAKA:**
   - Tautan berwarna biru bergaris bawah **HANYA** diperbolehkan pada entri DOI / URL resmi di bagian **DAFTAR PUSTAKA** (mengantarkan pembaca ke sumber primer online).

---

## 3. Aturan Nama Kunci & Bookmark

1. **Format Kunci Ref:**
   - Bookmark entri DAFTAR PUSTAKA wajib dinamai `Ref_<CitationKey>` (contoh: `Ref_Barasz2017`, `Ref_Statista2024`, `Ref_Colline2024`).
   - Panjang nama bookmark maksimal 39 karakter (batas aman Word OOXML).
   - Dilarang karakter spasi atau karakter ilegal XML di dalam nama bookmark.
2. **Aturan Bookmark Caption (LOT & LOF):**
   - Bookmark tabel: `Cap_T_<bab>_<nomor>` (contoh: `Cap_T_1_1`).
   - Bookmark gambar: `Cap_G_<bab>_<nomor>` (contoh: `Cap_G_1_2`).

---

## 4. Protokol Konversi & Eksekusi di Google Docs

Setiap kali naskah diekspor ke Google Docs untuk dibaca atau dibagikan ke dosen pembimbing:
1. Pengguna/Asisten wajib membuka menu **Extensions > Apps Script** di Google Docs terkait.
2. Menyalin kode dari [`execution/fix_gdocs_citation_links.gs`](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/execution/fix_gdocs_citation_links.gs).
3. Menjalankan fungsi `relinkCitationsToDP`.
4. Memastikan laporan eksekusi menghasilkan:
   - `DP ter-bookmark` = total entri pustaka.
   - `Dilewati (tak cocok)` = 0 (semua sitasi terpetakan).
5. Pada Google Docs Web, navigasi sitasi berfungsi dengan **klik biasa** (single click), mempermudah dosen mereview referensi secara instan tanpa perlu menahan tombol Ctrl.

---

## 5. Rujukan & Skill Terkait
- **Skill Operasional:** `gdocs-citation-linker` ([`SKILL.md`](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/.agents/skills/gdocs-citation-linker/SKILL.md))
- **Skrip Eksekusi:** [`execution/fix_gdocs_citation_links.gs`](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/execution/fix_gdocs_citation_links.gs)
- **Directive Terkait:** [`directives/fix_gdocs_citation_links.md`](file:///d:/Perkuliahan/Skripsi/SKRIPSI-arthur/directives/fix_gdocs_citation_links.md)

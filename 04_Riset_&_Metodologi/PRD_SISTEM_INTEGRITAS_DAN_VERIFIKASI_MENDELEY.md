# PRD: Sistem Penjaminan Integritas, Validasi Tag, dan Paritas 1:1 Mendeley Reference Manager

> [!SUMMARY] Tujuan & Solusi Dokumen Ini
> - **Untuk Apa:** Menjadi dokumen spesifikasi produk (*Product Requirements Document*) dan arsitektur pengamanan baku agar seluruh pustaka referensi skripsi Arthur Reezan yang diimpor ke Mendeley Reference Manager selalu 100% lengkap, akurat, dan identik (*zero-discrepancy*) dengan naskah skripsi (LaTeX, Word, dan Markdown).
> - **Masalah yang Diselesaikan:** Menghilangkan risiko fatal *Silent Drop* pada Mendeley (di mana tag RIS yang tidak dikenali seperti `TY  - ELEC` dilewati/dihapus secara diam-diam tanpa peringatan kesalahan), mencegah desinkronisasi jumlah referensi (misal 52 vs 56), mengeliminasi kekeliruan pencocokan kunci BibTeX (*heuristic key mismatch*), serta menjamin keutuhan karakter khusus (diakritik seperti `é` pada Pokémon dan penulisan penulis korporat).
> - **Keputusan/Output:** Cetak biru arsitektur 3-Layer, standarisasi tag RIS Mendeley-whitelist, pembentukan test suite pra-terbang (*pre-flight verification script* `verify_mendeley_integrity.py`), dan SOP bimbingan anti-cacat.

---

## 1. Latar Belakang & Analisis Kejadian (*Post-Mortem Insiden 16 Sep 2026*)

### 1.1 Kronologi Kejadian
Pada sesi revisi bimbingan dosen (Ibu Dr. Fredella Colline), mahasiswa diminta memasukkan seluruh sumber referensi ke dalam manajer referensi Mendeley serta melengkapi 4 data rujukan industri resmi Pokémon (The Pokémon Company 2024, Statista 2024, ICv2 & TCGplayer 2024, dan PSA 2024).

Ketika file `.ris` pertama kali diimpor oleh Arthur ke aplikasi Mendeley Reference Manager, muncul notifikasi sukses:
> *"1 file uploaded, 52 references generated"*

Meskipun nampak sukses, Arthur dengan sangat jeli menyadari adanya kejanggalan: naskah skripsi memiliki **56 referensi**, namun Mendeley hanya memuat **52 referensi** (terdapat 4 referensi yang hilang).

### 1.2 Akar Masalah Teknis (*Root Causes*)
1. **Perilaku *Silent Drop* pada Parser Mendeley:**
   Mendeley Reference Manager menggunakan parser RIS yang sangat ketat terhadap tag jenis dokumen (`TY`). Tag standar seperti `TY  - ELEC` (Electronic Citation / Webpage yang umum di EndNote/Zotero) **tidak didukung oleh Mendeley**. Saat menemukan tag tersebut, parser Mendeley tidak memunculkan dialog error atau peringatan, melainkan **mengabaikan dan membuang entri tersebut secara diam-diam**.
   $$\text{Total Terbaca: } 40 \text{ JOUR} + 11 \text{ BOOK} + 1 \text{ CONF} = 52 \text{ Referensi (4 Data Pokémon Dibuang)}$$
2. **Kelemahan Pencocokan Heuristik Kunci Sitasi (*Fuzzy Key Resolution*):**
   Skrip generator awal menggunakan pencocokan substring nama belakang dan tahun (`author_lead[:4] in k.lower()`). Pada penulis seminal dengan publikasi ganda di tahun yang sama (seperti Leilei Gao tahun 2014), skrip secara keliru memilih entri `gao2014set` alih-alih `gao2014completing` (*The "Completing the Set" Effect* di *Journal of Marketing Research*).
3. **Disparitas Sitasi In-Text Antar Format:**
   Pada naskah LaTeX `Proposal_Arthur_PokemonTCG.tex`, sitasi Keynes (1936) tertulis sebagai teks mentah tanpa sintaks `\citet{keynes1936general}`, sehingga kunci sitasi yang diekstrak parser TeX hanya berjumlah 55 kunci, berbeda dengan naskah Word dan Markdown yang memuat 56 entri.
4. **Absensi Verifikasi Otomatis Sebelum Rilis (*Pre-Flight Gap*):**
   Sistem sebelumnya telah memiliki audit tipografi Word dan kepatuhan Pedoman FEB UKRIDA 2023, namun belum memiliki pengujian otomatis khusus untuk menguji paritas 1:1 file ekspor Mendeley terhadap naskah.

### 1.3 Dampak Bahaya Jika Tidak Terdeteksi
Jika mahasiswa tidak jeli, 4 data rujukan industri yang secara eksplisit diminta oleh Dosen Pembimbing tidak akan masuk ke Mendeley. Ketika dosen meminta bukti kepustakaan di Mendeley atau memeriksa sitasi melalui Mendeley Cite di Word, data tersebut akan hilang, berpotensi menggagalkan kelulusan administrasi seminar proposal dan merusak kredibilitas akademik.

---

## 2. Tujuan & Sasaran Mutlak (*System Goals*)

1. **Jaminan Paritas 6-Arah 100% Identik (*Zero-Discrepancy Rule*):**
   $$\text{Count}(\text{TeX}) = \text{Count}(\text{Markdown}) = \text{Count}(\text{Word}) = \text{Count}(\text{RIS}) = \text{Count}(\text{Bib}) = \text{Count}(\text{Mendeley}) = 56$$
2. **Kepatuhan Whitelist Tag RIS Mendeley 100%:**
   Mengharamkan tag `ELEC`, `WEB`, `MISC`, atau tag tidak dikenal lainnya. Seluruh entri wajib menggunakan subset resmi Mendeley:
   - `TY  - JOUR` (Artikel Jurnal Ilmiah)
   - `TY  - BOOK` (Buku Teks / Monograf)
   - `TY  - RPRT` (Laporan Resmi Korporat / Industri / Whitepaper)
   - `TY  - CONF` (Prosiding Konferensi Ilmiah)
   - `TY  - THES` (Tesis / Disertasi)
   - `TY  - GEN` (Generik / Dokumen Lain)
3. **Resolusi Kunci Deterministik (Bebas Heuristik):**
   Pencocokan kunci sitasi wajib bersifat deterministik berbasis kamus kanonikal (*canonical registry*) tanpa tebakan regex.
4. **Integritas Karakter Khusus & Penulis Korporat:**
   Menjamin encoding UTF-8 murni tanpa karakter pengganti (`\ufffd`), mempertahankan huruf beraksen (seperti `é` pada Pokémon, `ö` pada Gültekin & Özer), serta memformat penulis korporat (`The Pokémon Company`, `ICv2`, `PSA`) agar tidak dibalik secara keliru menjadi nama orang oleh Mendeley.
5. **Pintu Gerbang Otomatis (*Automated Pre-Flight Gatekeeper*):**
   Membangun suite audit otomatis `execution/verify_mendeley_integrity.py` yang dijalankan setiap kali ada perubahan referensi dan terintegrasi dalam suite verifikasi naskah.

---

## 3. Desain Arsitektur 3-Layer

```
┌─────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: DIRECTIVES                                                     │
│ - directives/verify_mendeley_integrity.md                               │
│   (SOP baku integritas Mendeley, whitelist tag, aturan metadata wajib)  │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ LAYER 2: ORCHESTRATION                                                  │
│ - 04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md [Keputusan D21]              │
│ - 06_Referensi_Jurnal_PDF/PANDUAN_IMPORT_MENDELEY_1_MENIT.md            │
│ - execution/generate_mendeley_library.py (Generator Deterministik)      │
│   * Sinkronisasi TeX, Markdown, Word, BibTeX, dan RIS                   │
│   * Whitelist mapping otomatis & sanitasi tag ilegal                    │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ LAYER 3: EXECUTION & AUTOMATED TESTING                                  │
│ - execution/verify_mendeley_integrity.py                                │
│   * Test 1: 6-Way Count Parity (56 == 56 == 56 == 56)                   │
│   * Test 2: Whitelist Tag Compliance (0 illegal tags)                   │
│   * Test 3: Citation Key Set Equality (Set Diff == Empty)               │
│   * Test 4: Mandatory Metadata Field Completeness                       │
│   * Test 5: UTF-8 & Diacritic Integrity (Zero byte corruption)          │
│   * Test 6: Word Document Bibliography Audit                            │
│ - Integrasi ke execution/verify_ukrida_compliance.py                    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Spesifikasi Persyaratan Fungsional (*Functional Requirements*)

### 4.1 Modul Pemetaan Tipe Dokumen (Tag Whitelist Enforcement)
Setiap entri dari `references.bib` wajib dikonversi mengikuti tabel ketat berikut:

| Tipe BibTeX Asal | Tag RIS Target | Label Dokumen di Mendeley | Keterangan Standarisasi |
|:---|:---:|:---|:---|
| `@article` | `TY  - JOUR` | *Journal Article* | Wajib memuat `JO`, `VL`, `IS`, `SP`, `EP`. |
| `@book` | `TY  - BOOK` | *Book* | Wajib memuat `PB`, `CY` (Publisher & City). |
| `@inproceedings`, `@conference` | `TY  - CONF` | *Conference Proceedings* | Wajib memuat `BT` (Book/Proceedings Title). |
| `@report`, `@techreport`, `@misc` | `TY  - RPRT` | *Report* | **Penyelamat data industri**: Menggantikan `ELEC` agar dikenali 100% oleh Mendeley. |
| `@phdthesis`, `@mastersthesis` | `TY  - THES` | *Thesis* | Memuat universitas pada `PB`. |
| Dokumen Lainnya | `TY  - GEN` | *Generic* | Fallback resmi yang didukung Mendeley. |
| **DILARANG KERAS** | `TY  - ELEC`, `TY  - WEB` | *Unsupported* | **DIBLOKIR TOTAL** oleh validator pra-rilis. |

### 4.2 Standarisasi Metadata Minimal (*Required Fields*)
Setiap entri di dalam file `.ris` wajib memiliki:
1. `TY` : Tipe dokumen valid (whitelist).
2. `TI` : Judul lengkap tanpa kurung kurawal BibTeX `{...}`.
3. `AU` : Penulis (satu baris per penulis). Penulis korporat tanpa tanda koma terbalik.
4. `PY` / `Y1` : Tahun publikasi (4 digit numerik).
5. `PB` / `JO` : Nama penerbit (untuk buku/laporan) atau nama jurnal ilmiah.
6. `ID` : Kunci sitasi unik (*cite key*) yang identik dengan BibTeX dan LaTeX.
7. `ER` : Penutup entri (*End of Record*) dengan format `ER  - \n`.

### 4.3 Sinkronisasi Naskah LaTeX `Proposal_Arthur_PokemonTCG.tex`
- Baris sitasi Keynes pada teks naskah wajib diubah dari teks polos `Keynes (1936)` menjadi sitasi formal `\citet{keynes1936general}`.
- Memastikan tepat 56 kunci sitasi unik diekstrak secara otomatis dari naskah TeX.
- Mengoreksi mapping `gao2014completing` agar selaras antara LaTeX, Markdown, Word, dan Mendeley.

---

## 5. Rencana Pengujian & Kriteria Keberhasilan (*Acceptance Criteria*)

Suite audit otomatis `verify_mendeley_integrity.py` harus memberikan hasil **PASS 100%** untuk 6 pengujian berikut:

1. **Test 1 (Paritas Jumlah Entri):**
   - TeX Cites = 56
   - Markdown DAFTAR PUSTAKA = 56
   - Word DAFTAR PUSTAKA = 56
   - `Mendeley_Library_Arthur_PokemonTCG.ris` = 56 entri `ER  -`
   - `Mendeley_Library_Arthur_PokemonTCG.bib` = 56 entri `@...`
2. **Test 2 (Audit Tag Whitelist):**
   - 0 entri mengandung `TY  - ELEC`, `TY  - WEB`, atau tag di luar whitelist.
3. **Test 3 (Kesetaraan Kunci Sitasi):**
   - `set(TeX_Keys) == set(RIS_Keys) == set(Bib_Keys)`
   - Himpunan selisih (*set difference*) harus kosong $\emptyset$.
4. **Test 4 (Kelengkapan Metadata):**
   - 100% entri memiliki Title, Author, Year, Venue/Publisher, dan ID.
5. **Test 5 (Integritas Karakter & Diakritik UTF-8):**
   - File tersimpan dalam UTF-8 tanpa BOM.
   - Tidak ada karakter korup `\ufffd`.
   - String `Pokémon` dan `Gültekin` terbaca secara sempurna.
6. **Test 6 (Audit Dokumen Word):**
   - Seluruh 56 referensi tercetak rapi di Word, tersusun abjad A–Z, tanpa nomor urut, dengan hanging indent 1.25 cm.

---

## 6. Integrasi Operasional Bimbingan (SOP Mahasiswa)

Setiap kali mahasiswa melakukan perubahan pada daftar pustaka atau menambah referensi baru:
1. Jalankan `python execution/generate_mendeley_library.py`.
2. Jalankan `python execution/verify_mendeley_integrity.py` (wajib status **ALL TESTS PASSED**).
3. Buka Mendeley Reference Manager $\rightarrow$ `Ctrl + A` $\rightarrow$ `Delete` $\rightarrow$ `Add new` $\rightarrow$ `Import library (.ris)`.
4. Pastikan notifikasi Mendeley selalu menampilkan angka yang sama dengan naskah:
   > **"1 file uploaded, [N] references generated"** (di mana $N = \text{jumlah pustaka skripsi}$).

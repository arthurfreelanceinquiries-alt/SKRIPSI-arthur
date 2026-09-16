# Directive: Verifikasi Integritas, Validasi Tag, dan Paritas 1:1 Mendeley Reference Manager

> [!SUMMARY] Tujuan & Ruang Lingkup Directive Ini
> - **Tujuan:** Menetapkan Standard Operating Procedure (SOP) baku pengujian integritas, validasi tag RIS, dan penjaminan paritas jumlah referensi 1:1 (*zero-discrepancy*) antara naskah skripsi (LaTeX, Word, Markdown) dengan berkas ekspor Mendeley (`.ris` dan `.bib`).
> - **Masalah yang Dicegah:** Mengeliminasi bahaya *Silent Drop* pada Mendeley (di mana dokumen dengan tag yang tidak didukung seperti `TY  - ELEC` dibuang secara diam-diam tanpa peringatan), desinkronisasi jumlah sitasi (misal naskah 56 tapi Mendeley 52), serta korupsi karakter khusus/penulis korporat.
> - **Otoritas:** Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 Subbab 3.7 & Standar Kompatibilitas Mendeley Reference Manager (v2.100+).

---

## 1. Aturan Paritas Mutlak 1:1 (*The Zero-Discrepancy Rule*)

Setiap kali naskah atau kepustakaan diperbarui, jumlah referensi pada seluruh lapisan dokumen wajib bernilai identik:
$$\text{Count}(\text{TeX Cites}) = \text{Count}(\text{Markdown DP}) = \text{Count}(\text{Word DP}) = \text{Count}(\text{RIS Records}) = \text{Count}(\text{BibTeX Entries}) = 56$$

Jika salah satu media memiliki selisih angka (walaupun hanya selisih 1 referensi), status build dinyatakan **GAGAL (BUILD BROKEN)** dan dilarang diserahkan ke Dosen Pembimbing.

---

## 2. Tabel Whitelist Resmi Tag RIS Mendeley Reference Manager

Mendeley Reference Manager menggunakan parser yang sangat sensitif. Hanya tag-tag berikut yang diizinkan:

| BibTeX Entry Type | RIS Tag | Label Dokumen Mendeley | Keterangan & Bidang Wajib |
|:---|:---:|:---|:---|
| `@article` | `TY  - JOUR` | *Journal Article* | Wajib memuat `TI`, `AU`, `PY`, `JO`/`JF`, `VL`, `IS`, `SP`, `EP`. |
| `@book` | `TY  - BOOK` | *Book* | Wajib memuat `TI`, `AU`, `PY`, `PB`, `CY` (Kota Penerbit). |
| `@inproceedings`, `@conference` | `TY  - CONF` | *Conference Proceedings* | Wajib memuat `TI`, `AU`, `PY`, `BT` (Book Title), `PB`. |
| `@report`, `@techreport`, `@misc` | `TY  - RPRT` | *Report* | **Wajib untuk data industri/whitepaper**: Statista, The Pokémon Company, ICv2, PSA. |
| `@phdthesis`, `@mastersthesis` | `TY  - THES` | *Thesis* | Wajib memuat universitas pada `PB`. |
| Jenis lainnya | `TY  - GEN` | *Generic* | Fallback resmi jika tidak cocok dengan kategori di atas. |

### ⛔ Tag yang Diharamkan Secara Mutlak (*Strictly Prohibited*)
* `TY  - ELEC` (Electronic / Web Citation) $\rightarrow$ **DILARANG!** Mendeley akan membuang record secara diam-diam.
* `TY  - WEB` $\rightarrow$ **DILARANG!**
* `TY  - MISC` $\rightarrow$ **DILARANG!**

---

## 3. Spesifikasi Metadata Minimal per Entri RIS

Setiap blok referensi di dalam file `.ris` wajib ditutup dengan `ER  - ` dan memuat bidang-bidang berikut tanpa exception:
1. `TY  - [TAG]` : Tag valid sesuai whitelist di atas.
2. `TI  - [Judul]` : Judul lengkap artikel/buku/laporan tanpa kurung kurawal BibTeX `{...}`.
3. `AU  - [Penulis]` : Satu baris `AU  - ` untuk setiap nama pengarang. Nama organisasi/korporat (misal `The Pokémon Company`) ditulis apa adanya tanpa pembalikan koma.
4. `PY  - [Tahun]` & `Y1  - [Tahun]` : Tahun 4 digit numerik.
5. `PB  - [Penerbit]` atau `JO  - [Nama Jurnal]` : Instansi penerbit atau jurnal ilmiah penampung.
6. `ID  - [CiteKey]` : Kunci sitasi unik yang identik dengan BibTeX dan LaTeX.
7. `UR  - [URL]` : Wajib memuat tautan web aktif berprotokol `https://` untuk seluruh entri laporan industri (`RPRT`), sehingga tombol *"Open URL"* pada Mendeley Reference Manager aktif. Di dokumen Word, URL wajib dirender sebagai elemen OpenXML `<w:hyperlink>` yang dapat diklik langsung oleh dosen.

---

## 4. Standar Encoding & Karakter Khusus

1. **Format Encoding:** File `.ris` dan `.bib` wajib disimpan dalam format **UTF-8 (tanpa BOM)**.
2. **Karakter Pengganti:** Dilarang keras memuat karakter pengganti Unicode `\ufffd` (tanda tanya hitam ``).
3. **Diakritik:** Huruf vokal beraksen wajib tampil bersih dan terbaca (misal: `Pokémon`, `Gültekin`, `Özer`).
4. **Tanda Sambung:** Rentang halaman dan angka wajib menggunakan en-dash (`–`) atau tanda hubung standar (`-`), bukan em-dash rusak.

---

## 5. Prosedur Eksekusi & Pengujian Mahasiswa

Sebelum melakukan bimbingan atau mengumpulkan naskah:
1. **Regenerasi Library:**
   ```powershell
   py execution/generate_mendeley_library.py
   ```
2. **Uji Integritas Pra-Terbang (*Pre-Flight Audit*):**
   ```powershell
   py execution/verify_mendeley_integrity.py
   ```
   *Pastikan seluruh 6 pengujian berstatus [PASS].*
3. **Impor ke Aplikasi Mendeley Reference Manager:**
   - Hapus pustaka lama (`Ctrl + A` $\rightarrow$ `Delete`).
   - Klik `+ Add new` $\rightarrow$ `Import library` $\rightarrow$ `RIS (*.ris)`.
   - Pilih `06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.ris`.
   - **Verifikasi Visual:** Pastikan notifikasi hijau pojok kanan bawah berbunyi tepat:
     > **"1 file uploaded, 56 references generated"**

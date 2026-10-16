# BERITA ACARA AUDIT FISIK FINAL — 14 PDF Pengganti 80/20 Skripsi Pokemon TCG Arthur

## File Status
- Nama berkas audit: BERITA_ACARA_AUDIT_FISIK_14_PDF_PENGGANTI_2026-10-16.md
- Tanggal diaudit: 16 Oktober 2026 (21.15-21.30 WIB)
- Auditor: @auditor-skripsi (Thesis Auditor, Hermes Agent)
- Sumber perintah: @skripsi-orchestrator (2 sub-agent downloader deleg_74d2825d sa-0 dan sa-1 SUDAH SELESAI)
- Folder target: D:/Perkuliahan/Skripsi/SKRIPSI-arthur/06_Referensi_Jurnal_PDF/
- File rujukan sitasi: 01_Naskah_Utama/references.bib (86 entri, commit 87fc80c) + Proposal_Arthur_PokemonTCG.tex
- Metode: verifikasi fisik independen dengan pypdf (header %PDF, hitung halaman, ekstrak teks hlm 1-2, cek section Referensi di 3 hlm akhir, cocokkan judul + penulis + tahun + jurnal vs BibTeX)
- Chapters included: Audit referensi (BAB II / Tinjauan Pustaka + Daftar Pustaka), bukan audit BAB I-V
- Overall status: NEEDS REVISION (10 LULUS, 4 GAGAL — belum layak maju ke Dr. Fredella Colline sebelum 4 DOI gagal diganti/dikoreksi)

## Ringkasan Eksekutif
- Total DOI target: 14 (dari commit 87fc80c references.bib)
- LULUS FISIK FULL-TEXT: 10 dokumen (71,4%)
- GAGAL / DITOLAK: 4 dokumen (28,6%)
- Prinsip audit: klaim metadata DITOLAK, hanya file fisik yang dihitung. File HTML/bot-wall/corrupt DITOLAK mutlak.
- Koreksi auditor atas klaim orchestrator: entri rafael2023ego DINYATAKAN GAGAL (file yang ada di disk adalah artikel ReMark BJM DOI 10.5585/remark.v22i2.21818, BUKAN artikel JCB DOI 10.1002/cb.2148 yang disitasi di BibTeX).

## Hasil Per DOI (Path, Halaman, Ukuran, Verdict)

| No | Bib Key / DOI | Path File Fisik | Hlm | Ukuran | Verdict | Alasan |
|----|---------------|-----------------|-----|--------|---------|--------|
| 1 | giarlotta2024simon / 10.1007/s10203-024-00436-2 | 02_Jurnal_Teori_&_Metodologi/2024_Giarlotta_Petralia_Simon_Bounded_Rationality_DEF.pdf | 20 | 383,3 KB | LULUS | Full-text utuh. Teks hlm 1 memuat judul Simons bounded rationality + Giarlotta + Petralia + Decisions in Economics and Finance (2024) 47:327-346 + DOI cocok. Ada section References. |
| 2 | beikverdi2024post / 10.1002/cb.2287 | TIDAK ADA (tidak disimpan — tepat, file HTML bot-wall 5,7 KB sebelumnya sudah dibuang) | 0 | 0 KB | GAGAL | Berkas PDF fisik TIDAK DITEMUKAN. Penyebab: Wiley 403 + Theseus Anubis 403. Tidak ada preprint terbuka. BUTUH ALTERNATIF. |
| 3 | aquino2024expecting / 10.1177/15270025241245638 | 01_Empiris_Utama_2021-2025/2024_Aquino_Gershenson_Nostalgia_Baseball_Card_Prices_JSE.pdf | 33 | 467,7 KB | LULUS | Full-text utuh. Teks hlm 1: Expecting the Expected? + Aquino + Gershenson + Abstract trading cards pricing anomaly. Sumber Gershenson Archive (legal author-copy). Section References tidak terdeteksi di 3 hlm akhir oleh parser (kemungkinan format footnote) — tidak menggugurkan karena isi 33 hlm utuh. |
| 4 | huo2023exploring / 10.1177/21582440231172678 | 01_Empiris_Utama_2021-2025/2023_Huo_Wang_Sadiq_Pang_Impulse_LiveStreaming_SOR_SAGEOpen.pdf | 15 | 339,5 KB | LULUS | Full-text utuh. Teks hlm 1: SAGE Open April-June 2023 + DOI 10.1177/21582440231172678 + Huo/Wang/Sadiq/Pang + SOR Model. Sumber LNU Repo (legal). File corrupt 171 KB versi lama SUDAH DIGANTI dengan versi valid. |
| 5 | gachter2022individual / 10.1007/s11238-021-09839-8 | 02_Jurnal_Teori_&_Metodologi/2022_Gachter_Johnson_Herrmann_Individual_Loss_Aversion_TD.pdf | 26 | 857,1 KB | LULUS | Full-text utuh. Teks hlm 1: Individual-level loss aversion + Gachter/Johnson/Herrmann + DOI Springer. Ada section References. |
| 6 | baumeister2024selfcontrol / 10.1016/j.copsyc.2024.101882 | 02_Jurnal_Teori_&_Metodologi/2024_Baumeister_Andre_Southwick_Tice_Self_Control_Ego_Depletion_COPSYC.pdf | 7 | 269,5 KB | LULUS | Full-text utuh. Teks hlm 1: Self-control and limited willpower + Baumeister/Andre/Southwick/Tice + Review COPSYC. Sumber Southwick Archive (author-copy legal). Panjang 7 hlm wajar untuk artikel review COPSYC 101882. |
| 7 | widyastuti2024power / 10.21070/ijler.v19i2.1104 | 01_Empiris_Utama_2021-2025/2024_Widyastuti_Hariasih_Hedonic_Impulse_Buying_IJLER.pdf | 12 | 1200,7 KB | LULUS BERSYARAT (fisik LULUS, sitasi CATATAN) | Fisik: full-text utuh 12 hlm, header %PDF valid, bukan XML. File corrupt 64 KB versi lama SUDAH DIGANTI dengan arsip UMSIDA 1200 KB. CATATAN SITASI: redaksi judul di hlm 1 PDF (The Role of Hedonic Shopping Motivation, Price Discount and Shopping Lifestyle to...) BERBEDA redaksi dengan judul BibTeX (The Power of Hedonic Motivation and Discounts Through Releasing Impulse Buying in Indonesia). Wajib verifikasi manual DOI vs OJS sebelum sempro. |
| 8 | skwara2023effects / 10.1002/cb.2193 | 02_Jurnal_Teori_&_Metodologi/2023_Skwara_Mental_Accounting_JCB.pdf | 18 | 1514,3 KB | LULUS | Full-text utuh. Teks hlm 1: Skwara Florian + Effects of mental accounting + JCB Vol 22 pp 1265-1281 + DOI 10.1002/cb.2193 + hdl.handle.net/10419/288081 (EconStor postprint legal, Provided in Cooperation with Wiley). File HTML bot-wall 5,7 KB versi awal SUDAH DIGANTI. |
| 9 | zhao2025effect / 10.1111/ajsp.12663 | TIDAK ADA (tidak disimpan) | 0 | 0 KB | GAGAL | Berkas PDF fisik TIDAK DITEMUKAN. Penyebab: Wiley closed, tidak ada preprint terbuka. BUTUH ALTERNATIF. |
| 10 | rafael2023ego / 10.1002/cb.2148 | 02_Jurnal_Teori_&_Metodologi/2023_Rafael_Lopes_Ego_Depletion_ReMark_BJM_ALTERNATIF_BUKAN_JCB_Wiley.pdf (49 hlm, 1193,6 KB) | 49 (dokumen lain) | 1193,6 KB | GAGAL (MISMATCH SITASI) | File fisik yang ada BUKAN naskah yang disitasi. Teks hlm 1: THE INTELLECTUAL FRAMEWORK OF EGO DEPLETION + Rafael (ESPM) + Braz Jour Mark ReMark + DOI 10.5585/remark.v22i2.21818. Yang disitasi di BibTeX: Ego Depletion in Consumer Behavior (JCB, DOI 10.1002/cb.2148). Judul + jurnal + DOI TIDAK COCOK. Dilarang sitasi silang. BUTUH ALTERNATIF atau ganti BibTeX ke entri ReMark bila memang mau pakai naskah ini. |
| 11 | alfina2023fomo / 10.1080/23311975.2023.2250033 | 01_Empiris_Utama_2021-2025/2023_Alfina_Hartini_Mardhiyah_FOMO_Cogent.pdf | 23 | 2051,3 KB | LULUS | Full-text utuh. Teks hlm 1: Alfina/Hartini/Mardhiyah + FOMO related consumer behaviour + Cogent Business & Management Vol 10 + DOI 10.1080/23311975.2023.2250033 + hdl.handle.net/10419/294597 (EconStor postprint legal, Provided in Cooperation with Taylor & Francis). |
| 12 | mariyana2023influence / 10.24123/jmb.v22i2.691 | 01_Empiris_Utama_2021-2025/2023_Mariyana_Djawoto_Suhermin_Hedonic_Shopping_Motivation_MABIS.pdf | 15 | 319,9 KB | LULUS | Full-text utuh. Teks hlm 1: Mariyana/Djawoto/Suhermin + Jurnal Manajemen dan Bisnis Vol 22 No 2 + DOI 10.24123/jmb.v22i2.691. Ada section References. |
| 13 | prihatiningrum2021effect / 10.2991/aebmr.k.211117.015 | 01_Empiris_Utama_2021-2025/2021_Prihatiningrum_Said_Self_Control_Impulse_Buying_Atlantis.pdf | 7 | 507,6 KB | LULUS | Full-text utuh. Teks hlm 1: Prihatiningrum/Said (ULM Banjarmasin) + judul cocok + Atlantis Press AEBMR. Ada section References. |
| 14 | anoop2025online / 10.1002/cb.2418 | TIDAK ADA (tidak disimpan) | 0 | 0 KB | GAGAL | Berkas PDF fisik TIDAK DITEMUKAN. Penyebab: Wiley closed 2025, tidak ada preprint terbuka. BUTUH ALTERNATIF. |

## Critical Issues (Must Fix Sebelum Submission ke Dr. Fredella Colline)
- [ ] GAGAL-1 beikverdi2024post (10.1002/cb.2287): tidak ada PDF fisik. Aksi: (a) cari author-manuscript di Theseus/LUT repository manual, atau (b) GANTI referensi dengan artikel OA lain yang setara (post-purchase impulse / regret), update references.bib + sitasi di TeX + MD. Jangan sitasi tanpa file fisik.
- [ ] GAGAL-2 zhao2025effect (10.1111/ajsp.12663): tidak ada PDF fisik (Wiley closed). Aksi: ganti dengan artikel self-control → impulsive consumption yang OA, atau hapus dari 14 pengganti dan hitung ulang rasio 80/20.
- [ ] GAGAL-3 rafael2023ego (10.1002/cb.2148): file di disk adalah artikel LAIN (ReMark BJM). Aksi: PILIH SATU — (a) tetap pakai JCB 2023 → wajib dapatkan file JCB yang benar, atau (b) pakai file ReMark yang ada → ubah entri BibTeX ke Rafael 2023 ReMark (DOI 10.5585/remark.v22i2.21818, judul THE INTELLECTUAL FRAMEWORK OF EGO DEPLETION) + ubah semua sitasi di TeX/MD + rename file tanpa label ALTERNATIF. Dilarang 상태 campuran.
- [ ] GAGAL-4 anoop2025online (10.1002/cb.2418): tidak ada PDF fisik (Wiley closed 2025). Aksi: ganti dengan systematic review impulse buying yang OA (mis. Amos et al. 2014 atau artikel MDPI/SAGE OA), update BibTeX + sitasi.
- [ ] CATATAN SITASI widyastuti2024power: verifikasi manual judul OJS vs BibTeX. Aksi: buka DOI 10.21070/ijler.v19i2.1104, samakan judul BibTeX persis dengan judul artikel resmi, kompilasi ulang .bbl.

## Minor Issues (Should Fix)
- [ ] Aquino (33 hlm) & Huo (15 hlm) & Widyastuti (12 hlm): parser tidak menemukan kata references di 3 hlm akhir (kemungkinan ejaan Daftar Pustaka / format endnote). Tidak menggugurkan, tapi mohon cek visual 1 menit per file sebelum sempro.
- [ ] Nama file Beikverdi lama (HTML 5,7 KB) dan Widyastuti XML lama sudah tidak ada di disk (bagus — sudah dibersihkan sub-agent). Pastikan tidak ada sisa file *Beikverdi_Thesis* 5,9 KB ikut terlampir ke Mendeley.
- [ ] Untuk file EconStor (Skwara, Alfina): simpan URL hdl.handle.net di catatan Mendeley sebagai bukti legalitas postprint bila penguji bertanya.

## Kekuatan yang Dicatat
- [ ] 10/14 full-text terverifikasi independen via teks ekstraksi (bukan klaim ukuran saja): Giarlotta 20 hlm, Gachter 26 hlm, Baumeister 7 hlm, Skwara 18 hlm, Aquino 33 hlm, Huo 15 hlm, Widyastuti 12 hlm, Alfina 23 hlm, Mariyana 15 hlm, Prihatiningrum 7 hlm.
- [ ] 2 file corrupt/HTML versi awal (Huo 171 KB, Widyastuti 64 KB XML, Beikverdi 5,7 KB) sudah diganti/dibuang dengan benar — disiplin quality gate sub-agent bagus.
- [ ] Jalur legal-OA terdokumentasi jelas: Springer Hybrid OA (Giarlotta, Gachter), EconStor postprint (Skwara, Alfina), institutional archive (Aquino-Gershenson, Huo-LNU, Baumeister-Southwick, Widyastuti-UMSIDA), OJS/Atlantis OA (Mariyana, Prihatiningrum).
- [ ] Struktur folder 01_Empiris vs 02_Teori konsisten dan nama file informatif.

## Statistik Pendukung 80/20 (per 16 Okt 2026)
- references.bib: 86 entri total, 46 terbit >= 2021 (53,5%), 40 terbit < 2021 (46,5%).
- Artinya target 80% mutakhir BELUM TERCAPAI dengan komposisi sekarang. 10 PDF LULUS dari 14 pengganti membantu, tetapi 4 GAGAL harus diganti dengan referensi mutakhir ber-PDF fisik agar rasio naik. Saya tidak yakin ambang 80/20 yang dimaksud Kaprodi adalah 80% dari total sitasi atau 80% dari sitasi inti — konsultasikan ke advisor.

## Rekomendasi Auditor
- Siap untuk review Dr. Fredella Colline? BELUM. Status NEEDS REVISION.
- Estimasi waktu ke siklus revisi berikutnya: 2-4 hari (tergantung kecepatan dapat 4 PDF alternatif OA + update BibTeX/TeX + kompilasi ulang).
- Langkah berikutnya yang disarankan: (1) @skripsi-orchestrator spawn pencarian 4 alternatif OA, (2) @literatur usulkan kandidat pengganti yang relevan konstruk (post-purchase impulse, self-control-moderated consumption, ego depletion JCB-alternatif, online impulse review), (3) saya audit ulang 4 file baru sebelum BibTeX difinalkan.

## Lampiran Teknis
- Script eksekusi: D:/AI/hermes/profiles/auditor-skripsi/cache/scratch/audit_execution.py (pypdf, header check, ekstraksi teks)
- Data mentah JSON: 07_Review_&_Audit/Paper_Audits/audit_fisik_14_doi_2026-10-16.json (14 record, termasuk first_page_text_sample 600 karakter per file LULUS)
- Log terminal penuh tersimpan di cache auditor (termasuk peringatan fontTools yang tidak memengaruhi hitung halaman).

*Disusun independen oleh @auditor-skripsi. I'm unsure about ambang resmi 80/20 Kaprodi — consult your advisor.*

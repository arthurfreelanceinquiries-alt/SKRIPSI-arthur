# Register Input dan Bukti Manusia — Fase 3

> Versi kerja: 0.1, 10 Agustus 2026  
> Status: daftar blocker kanonis; kolom bukti hanya boleh diisi dari informasi nyata pengguna, DPS, reviewer, unit etik, gatekeeper, atau pilot  
> Larangan: rencana, placeholder, data sintetis, dan keluaran AI tidak boleh dicatat sebagai bukti pelaksanaan.

## 1. Fungsi Dokumen

Dokumen ini memisahkan pekerjaan yang dapat disiapkan agen dari keputusan dan bukti yang wajib berasal dari manusia atau pelaksanaan lapangan. Fase 3 tidak lulus hanya karena instrumen, analisis, atau pilot telah direncanakan. Setiap bukti baru harus direkonsiliasi ke SOURCE_OF_TRUTH.md, DECISION_LOG.md, METHODOLOGY_BLUEPRINT.md, INSTRUMENT_DRAFT.md, DATA_DICTIONARY.md, ANALYSIS_SPEC.md, dan WORKFLOW_LOG.md.

## 2. Urutan Penguncian

| Prioritas | Input/bukti wajib | Bentuk bukti yang dapat diterima | Dampak bila belum ada | Status |
|---|---|---|---|---|
| A1 | Batas geografis operasional | Daftar kota/kabupaten atau wilayah yang benar-benar akan dicakup | Populasi, site, dan inferensi belum dapat dibekukan | TERBUKA |
| A2 | Site/gatekeeper nyata | Nama organisasi/komunitas/kanal, pihak yang dapat dihubungi, hubungan mahasiswa dengan pihak itu, dan konfirmasi akses | Recruitment frame, quota, dan feasibility data belum nyata | TERBUKA |
| A3 | Proses rekrutmen | Cara undangan disebar, siapa yang mengundang, unit rekrutmen, serta larangan gatekeeper melihat jawaban | Risiko selection, coercion, dan ketergantungan cluster belum dapat dinilai | TERBUKA |
| A4 | Pemetaan cluster | Mapping site/channel/recruitment chain ke cluster_id tanpa PII | Standard error yang sesuai belum dapat ditentukan | TERBUKA |
| A5 | Batas inferensi | Persetujuan bahwa hasil hanya berlaku pada eligible completers yang berhasil direkrut melalui site penelitian, bukan seluruh Jabodetabek | Klaim populasi berisiko berlebihan | TERBUKA |
| B1 | Bulan fieldwork | Satu bulan kalender buka–tutup survei yang realistis | M-3, M-2, dan M-1 tidak dapat dinamai | TERBUKA |
| B2 | Musiman periode | Catatan apakah periode memuat Ramadan, Idulfitri/THR, bonus, tahun ajaran, atau peristiwa relevan lain berdasarkan kalender nyata | Interpretasi tiga bulan berisiko lepas konteks | TERBUKA |
| C1 | Software dan akses | Nama software, versi, lisensi/akses, serta perangkat yang tersedia | Pipeline statistik belum terbukti feasible | TERBUKA |
| C2 | Kemampuan analisis | Pernyataan jujur kemampuan mahasiswa dan bukti dry run Gamma-log, OLS log-ratio, adjusted predictions, diagnostic, serta output reproduktif | Metode kandidat belum layak dijanjikan | TERBUKA |
| D1 | Jalur etik UKRIDA | Prosedur/unit yang berwenang, dokumen wajib, dan keputusan apakah persetujuan formal diperlukan | Rekrutmen responden belum boleh dimulai | TERBUKA |
| D2 | Consent final | Identitas peneliti/contact person nyata, tujuan, durasi, risiko, manfaat, sukarela, penghentian, insentif, retensi, dan penghapusan | Instrumen belum siap lapangan | TERBUKA |
| D3 | Privasi dan deduplikasi | Mekanisme token, pemisahan kontak insentif, akses data, lokasi simpan, retensi, penghapusan, serta uji false match/non-match | Data sensitif belum aman | TERBUKA |
| E1 | Expert reviewer | Nama, kompetensi, afiliasi, konflik kepentingan, tanggal, versi instrumen, komentar, dan response-to-review log | Validitas isi belum dibuktikan | TERBUKA |
| E2 | Cognitive interview | Peserta nyata dengan consent, profil relevan, versi, probe, issue-resolution log, dan retest | Proses respons X/Y belum dibuktikan | TERBUKA |
| F1 | Keputusan klasifikasi | Keputusan expert tentang reksa dana pasar uang, utang informal/lain, penalti aktual, jadwal tidak bulanan, dan pembulatan nominal | Codebook belum final | TERBUKA |
| F2 | Form elektronik | Platform, versi, skip logic, roster, recap, missing/refusal, range checks, dan version hash | Data tidak dapat dikumpulkan konsisten | TERBUKA |
| F3 | Dry run sintetis | Hasil aktual terhadap T01–T30, defect log, revisi, dan retest; tetap dilabeli bukan data penelitian | Logic gate belum lulus | TERBUKA |
| G1 | Field pilot aktual | Flow, waktu, drop-off, refusal, kelengkapan, sumber angka, distribusi X/Y, flags, cluster, dan issue log | Gerbang Data tetap REVISI | TERBUKA |
| G2 | Smallest effect substantif | Keputusan DPS/mahasiswa sebelum melihat hasil utama, disertai arti ekonominya | Power tidak mempunyai target ilmiah | TERBUKA |
| G3 | Power dan ukuran sampel | Parameter pilot, skenario, kode/output simulasi, target screened–eligible–complete, dan keputusan final | Ukuran sampel tidak boleh dikarang | TERBUKA |
| G4 | Freeze sebelum survei utama | Instrumen, periode, codebook, cleaning, estimand, model, sensitivitas, cluster, missing, dan version hash | Survei utama belum boleh dimulai | TERBUKA |

## 3. Paket Input Pertama: Akses Lapangan

Isi bagian ini dengan fakta yang dapat diverifikasi:

- Wilayah operasional yang benar-benar dapat dijangkau:
- Nama site/komunitas/organisasi/kanal:
- Nama atau jabatan gatekeeper yang dapat dihubungi:
- Hubungan/akses mahasiswa ke gatekeeper:
- Bukti akses yang tersedia:
- Perkiraan cara undangan disebar:
- Siapa yang dapat melihat daftar calon peserta:
- Apakah gatekeeper dapat dicegah melihat jawaban:
- Apakah pengguna menerima inferensi nonprobabilitas yang terbatas pada R=1:

Jangan mengisi “Jabodetabek” sebagai akses bila belum ada sedikitnya satu site nyata. Jangan memakai teman dekat sebagai bukti representativitas. Akses rekrutmen dan klaim populasi adalah dua hal berbeda.

## 4. Paket Input Kedua: Periode dan Perangkat

- Bulan fieldwork:
- M-3:
- M-2:
- M-1:
- Konteks musiman yang terverifikasi:
- Software:
- Versi/lisensi:
- Perangkat:
- Kemampuan yang sudah dikuasai:
- Bagian pipeline yang perlu dipelajari:

## 5. Paket Input Ketiga: Etik dan Reviewer

- Jalur etik/unit UKRIDA:
- Contact person peneliti:
- Kebijakan insentif:
- Lokasi penyimpanan:
- Pihak yang mempunyai akses:
- Lama retensi dan cara penghapusan:
- Mekanisme deduplikasi:
- Calon expert reviewer dan kompetensinya:
- Rencana cognitive interview yang sudah disetujui manusia:

## 6. Aturan Pembaruan Status

Status hanya berubah dari TERBUKA setelah bukti diserahkan dan diperiksa. “Sudah ada,” “nanti dicari,” atau nama yang dibuat AI bukan bukti. Setiap perubahan mencatat tanggal, sumber, keputusan, konsekuensi metodologis, file terdampak, dan siapa yang menyetujui. Kelulusan setiap gerbang tetap memerlukan keputusan substantif DPS dan audit kepatuhan.


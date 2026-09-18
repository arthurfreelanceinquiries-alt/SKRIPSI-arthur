# PRD: Humanisasi Naskah Proposal — Menuju Uji Kemiripan AI ≤ 20%

> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** PRD + rencana + implementation plan humanisasi naskah proposal (skill `humanizer-id`, kedalaman default **seimbang**) agar tulisan terbaca sebagai karya akademik mahasiswa S1 yang autentik dan siap menghadapi uji kemiripan AI kampus (ambang ≤ 20%).
> - **Masalah yang Diselesaikan:** Naskah 65 halaman disusun dengan bantuan AI intensif sehingga berisiko tinggi mengandung pola generik (pembuka pengisi, ritme seragam, abstraksi menumpuk); belum ada baseline, glosarium, dan alur verifikasi makna untuk perbaikan yang aman.
> - **Keputusan/Output:** Diagnosis berbasis bukti (skor baseline audit 18 Sep 2026), kontrak fidelity, glosarium istilah, rencana 5 fase, implementation plan langkah-demi-langkah dengan gerbang verifikasi, dan kriteria selesai berbasis proses — **tanpa janji lolos detektor** (lihat §2).

---

## 1. Konteks & Ruang Lingkup

- **Dokumen sumber (wajib dibaca sebelum eksekusi):** [[01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex]] (master LaTeX, 65 hlm), [[03_Draft_Per_Bab/BAB_I_PENDAHULUAN.md]], [[03_Draft_Per_Bab/BAB_II_TINJAUAN_PUSTAKA.md]], [[03_Draft_Per_Bab/BAB_III_METODE_PENELITIAN.md]], [[04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md]], [[00_DASHBOARD_SECOND_BRAIN.md]].
- **In-scope:** prosa Bab I–III (+ abstrak/ringkasan bila ada di master TeX). Urutan eksekusi: Bab III → Bab II → Bab I (Bab III paling prosedural/mudah dibakukan; Bab I paling naratif, dikerjakan terakhir saat suara sudah stabil).
- **Out-of-scope (dilarang diubah):** `references.bib`, angka/satuan, sitasi/kunci `\cite{}`, URL/DOI, label/ref, persamaan MRA, caption tabel/gambar, pernyataan penggunaan AI bila diwajibkan kampus.
- **Aturan sinkronisasi workspace (inviolable):** setiap perubahan prosa pada master TeX wajib diikuti `sync_markdown_from_tex.py` + `build_proposal_word.py` + `verify_docx_typography.py` + `verify_pdf_docx_parity.py` (keduanya PASS) sesuai [[04_Riset_&_Metodologi/PRD_SINKRONISASI_DOCX_DAN_AUDIT_FILE.md]].

## 2. Batas Jujur yang Mengikat (dari skill humanizer-id)

1. **Tidak ada janji lolos detektor atau skor keaslian.** Detektor AI bersifat probabilistik, tidak stabil antar-versi, dan tidak membuktikan kepengarangan. Target "≤ 20%" diperlakukan sebagai **ambang risiko kampus**, bukan hasil yang dapat dijamin dari sisi penyuntingan.
2. **Tidak ada manipulasi curang:** dilarang memasukkan salah ketik buatan, tata bahasa rusak, pengalaman/emosi rekaan, kutipan palsu, atau pengakuan penggunaan AI yang dihapus bila memang diwajibkan/dicantumkan.
3. **Naskah pengguna tidak dikirim ke layanan humanizer/detektor eksternal** untuk penilaian gaya. Verifikasi dilakukan lokal (skrip audit + baca manual).
4. **Makna dibekukan** (lihat §4). Perubahan nol adalah hasil valid bila teks sudah baik — tidak ada kuota jumlah kalimat yang harus diganti.
5. Klaim kepatuhan EYD/kampus hanya sejauh yang benar-benar diperiksa; bila pedoman kampus tidak tersedia, dipakai ragam akademik umum dan dinyatakan eksplisit.

## 3. Baseline Bukti Awal (18 Sep 2026, `audit_text.py scan`, skrip bawaan skill)

| Berkas | Total temuan | Rincian | Interpretasi awal |
|---|---|---|---|
| BAB I | 18 | H07: 12, H06: 4, H10: 2 | H07 mayoritas struktur sah (judul/caption tebal di Markdown, bukan penekanan isi); H06/H10 antrean baca manual |
| BAB II | 32 | H07: 30, H06: 1, H10: 1 | Sama — dominasi H07 struktural; fokus manusia pada H10 + alur "selain itu" antar-ringkasan studi |
| BAB III | 31 | H07: 27, H06: 2, H10: 1, **H02: 1** | Satu temuan H02 (sumber kabur, baris ~prosedur) wajib ditelusuri — kandidat perbaikan nyata pertama |

> Catatan metodologis: `scan` hanya menandai **pemicu leksikal untuk dibaca manusia**, bukan skor AI dan bukan diagnosis. Tidak ada ambang kelulusan persentase. Diagnosis memakai taksonomi H01–H20 pada §5 dan selalu diputuskan oleh pembacaan konteks, bukan oleh jumlah temuan.

## 4. Kontrak Fidelity (isi yang dibekukan per Bab, diverifikasi via `compare` + baca manual)

| Unsur | Contoh di naskah ini | Aturan |
|---|---|---|
| Angka & satuan | US$ 100,0 M; 64,8 M kartu; n & kriteria (WNI ≥ 17 th, ≥ 1×/12 bln); β, p, α, skor PSA 1–10 | Nilai, tanda, denominator, periode, pasangan model–nilai tidak berubah |
| Klaim & kepastian | "H3 ditolak (p = 0,597)"; "PLS-SEM bukan MRA"; status rencana-vs-hasil Bab III | Negasi, hedging ("dapat/belum/mungkin"), kausalitas dipertahankan |
| Sitasi | 54 kunci bib; posisi dukungan klaim (mis. Lienardy-H4 genuine, Apidana/Artadita-H3 gagal-moderasi) | Tidak menggeser dukungan sitasi antar-kalimat saat menggabung kalimat |
| Istilah | Glosarium §6 — satu konsep satu istilah | Dilarang sinonim bergilir (validasi/pengujian/evaluasi tidak dipertukarkan) |
| Format | `\cite{}`, `\ref{}`, `\label{}`, matematika, tabel, caption | Suntik prosa saja; perintah LaTeX utuh |
| Suara | Sudut pandang penulis yang ada | Tidak menambah emosi/kenangan/analogi pribadi |

## 5. Diagnosis: Taksonomi H01–H20 yang Diprioritaskan untuk Naskah Ini

Berdasarkan genre proposal kuantitatif + baseline §3, prioritas baca manual (bukan daftar kata terlarang):

1. **H04 pembuka pengisi** ("di era modern/digital...") — mulai dari masalah yang tersedia.
2. **H14 penjelasan berulang** — definisi Y/X1/X2/X3/Z yang diulang di Bab I, II, dan III dipadatkan dengan rujukan silang, tanpa menghapus definisi operasional.
3. **H11 penghubung otomatis** — uji setiap "oleh karena itu/sehingga"; pertahankan hanya hubungan kausal yang didukung.
4. **H10 abstraksi menumpuk** — "optimalisasi/komprehensif/berkelanjutan" diganti verba + objek konkret yang sudah ada di bahan.
5. **H13 ritme seragam & H12 daftar dipaksakan** — pecah/gabung kalimat karena beban informasi; buang butir daftar yang mengulang.
6. **H15 terjemahan kaku & H16 sinonim konsep** — selaraskan dengan glosarium §6.
7. **H02 sumber kabur** — temuan Bab III + sapuan "para ahli/penelitian menunjukkan" tanpa sitasi jelas.
8. **H18 kepastian statistik** — "signifikan" hanya untuk hasil uji; beda numerik deskriptif tidak disebut signifikan; "tidak berbeda signifikan" ≠ "setara".
9. **H08 keseimbangan palsu & H09 penutup generik** — akhir subbab berhenti pada simpulan/batas/tindakan yang didukung.
10. **H05 artefak chatbot** — sapuan frasa meta ("berikut revisinya...") bila tertinggal di badan naskah.

## 6. Glosarium Istilah (konsisten di seluruh naskah; Inggris dipertahankan bila istilah bidang)

*Impulsive Buying*, *Hedonic Motivation*, *Desire for Completeness*, *Speculative Motive*, *Self-Control* (moderator), *booster pack/blind pack*, *gacha*, *pseudo-set framing*, *completing the set*, *hedonic browsing*, *Brief Self-Control Scale (BSCS)*, *Moderated Regression Analysis (MRA)*, *mean-centering*, *grading* PSA, *secondary market*, *mint/Gem Mint*. Padanan Indonesia dipakai bila lazim (mis. "pembelian impulsif" berdampingan dengan istilah Inggris pada kemunculan pertama per bab), lalu konsisten.

## 7. Rencana Kerja (Plan) — 5 Fase

- **Fase 0 — Persiapan & gerbang masuk (0,5 sesi).** Kunci scope (§1), kedalaman seimbang, dan jawaban 3 keputusan §10. Bekukan baseline §3 sebagai pembanding. *Gerbang:* SoT + 3 berkas draf terbaca; tidak ada perubahan naskah sebelum gerbang ini.
- **Fase 1 — Audit per bab, mode audit saja (3 sesi: III → II → I).** Untuk tiap bab: jalankan `scan`, baca temuan dalam konteks, catat temuan format `lokasi | ID | potongan | dampak | tindakan | batas bukti`; bedakan kesalahan makna/bukti vs pilihan gaya vs butuh verifikasi. Tidak menyunting berkas naskah pada fase ini. *Gerbang:* daftar temuan per bab disetujui user; ambiguitas makna ditandai sebagai pertanyaan, bukan ditebak.
- **Fase 2 — Tulis ulang seimbang per bab (3 sesi).** Terapkan §5 sesuai prioritas; nyatakan pokok lebih awal; variasikan panjang kalimat mengikuti isi; pertahankan kontrak §4 + glosarium §6 + EYD Edisi V. Kerjakan di **revisi terpisah** (salinan berkas `.humanized.md` per bab) agar sumber utuh sampai disetujui. *Gerbang per bab:* `compare` pratinjau menunjukkan 0 diff tak-disengaja pada token angka/sitasi/ref; baca-akhir sebagai pembaca sasaran (penguji) lolos.
- **Fase 3 — Porting ke master + paritas workspace (1–2 sesi).** Pindahkan prosa yang disetujui ke master TeX (prosa saja), lalu rantai wajib: `xelatex+bibtex` → `sync_markdown_from_tex.py` → `build_proposal_word.py` → `verify_docx_typography.py` + `verify_pdf_docx_parity.py` + `verify_intext_citations.py` + `verify_italic_typography.py` (semua PASS) → regen artefak sidang bila berubah. *Gerbang:* gate parity 7/7 konsep (tidak ada FAIL di luar pengecualian NoBab3 yang sudah diputuskan).
- **Fase 4 — Serah terima & log (0,5 sesi).** Tabel sebelum/sesudah untuk perubahan substantif, catatan sisa (klaim yang ditahan karena ambiguitas), pembaruan [[04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md]] + dashboard, dan panduan uji mandiri kampus oleh user (§9). *Gerbang:* user membaca-akhir dan menyatakan terima per bab.

Peran pemeriksaan (dilakukan bertahap oleh satu agen, dinyatakan sebagai pemeriksaan bertahap): (a) editor bahasa/ragam, (b) pemeriksa makna/bukti (menjaga §4), (c) peninjau pembaca (simulasi penguji). Ketidaksepakatan antar-peran diselesaikan dengan prinsip: makna/bukti mengalahkan gaya.

## 8. Implementation Plan (langkah eksekusi konkret)

```
F0.1  Baca SoT + 3 draf + master TeX (konteks tetangga per bab).
F0.2  Jalankan scan baseline per bab (sudah ada §3) → arsipkan JSON temuan di .tmp/humanize/.
F0.3  Dapatkan keputusan §10 dari user. Tanpa ini, berhenti (no-guess rule).

F1.x  (per bab B ∈ {III, II, I}):
  1. scan B → temuan.json
  2. Baca tiap temuan dalam konteks ±5 baris; klasifikasikan (makna/gaya/verifikasi).
  3. Tulis AUDIT_B.md (lokasi|ID|potongan|dampak|tindakan|batas bukti).
  4. Minta persetujuan user atas AUDIT_B.md + jawab pertanyaan ambiguitas.

F2.x  (per bab yang disetujui):
  1. Salin B → B.humanized.md; sunting di salinan saja.
  2. Terapkan prioritas §5 sesuai AUDIT_B.md; jaga §4 + §6 + EYD V.
  3. compare B vs B.humanized.md → selidiki tiap diff angka/sitasi/ref/kode.
  4. Baca-akhir sebagai penguji; serahkan diff + tabel sebelum/sesudah substantif.
  5. User terima/tolak per bagian (tidak ada auto-porting).

F3.1  Porting bagian yang diterima ke master TeX (hanya prosa).
F3.2  xelatex → bibtex → xelatex ×2 (65 hlm target tetap).
F3.3  sync_markdown_from_tex.py → build_proposal_word.py.
F3.4  Verifier: docx_typography, pdf_docx_parity, intext_citations,
      italic_typography, mendeley_integrity, live_urls (toleransi: FAIL NoBab3
      sesuai Opsi-1; bot-blocked 403 ≠ FAIL isi).
F3.5  Regen artefak sidang (PANDUAN .pdf + presentasi) bila prosa berubah.
F3.6  verify_evidence_ledger.py tetap PASS (halaman yang dirujuk tak bergeser makna).

F4.1  Tabel perubahan substantif + daftar klaim ditahan (bila ada).
F4.2  Update LOG_SESI_SECOND_BRAIN.md + dashboard + Graphify (bila relevan).
F4.3  Serahkan panduan uji mandiri kampus (§9) + rekomendasi kebijakan AI (§9).
```

Perintah kunci (PowerShell, dari root repo):

```powershell
py "C:\Users\arthu\.agents\skills\humanizer-id\humanizer-id\scripts\audit_text.py" scan "03_Draft_Per_Bab\BAB_III_METODE_PENELITIAN.md"
py "C:\Users\arthu\.agents\skills\humanizer-id\humanizer-id\scripts\audit_text.py" compare "03_Draft_Per_Bab\BAB_III_METODE_PENELITIAN.md" ".tmp\humanize\BAB_III_METODE_PENELITIAN.humanized.md"
py execution/sync_markdown_from_tex.py
py execution/build_proposal_word.py
py execution/verify_docx_typography.py
py execution/verify_pdf_docx_parity.py
```

## 9. Kriteria Selesai & Cara Menguji ≤ 20% Secara Jujur

**Kriteria selesai (berbasis proses, dapat diverifikasi):**

- [ ] 100% temuan audit Fase 1 berstatus ditangani/ditahan-beralasan (nol temuan menggantung).
- [ ] `compare` per bab: 0 perbedaan tak-disengaja pada angka, kunci sitasi, ref, URL/DOI, perintah LaTeX.
- [ ] Seluruh verifier Fase 3 PASS (dengan toleransi yang dinyatakan).
- [ ] Baca-akhir per bab oleh user: "lebih mudah dimengerti, makna dan suara utuh".
- [ ] Log sesi + dashboard diperbarui; tabel sebelum/sesudah tersedia untuk pembimbing bila ditanya asal-usul revisi.

**Tentang pengujian ≤ 20% (wajib dibaca):** pengujian dilakukan **mandiri oleh user di sistem resmi kampus** (mis. Turnitin/sistem sejenis bila itulah yang dipakai UKRIDA) terhadap dokumen final, karena (a) skor detektor tidak stabil dan tidak dapat direplikasi dari luar, (b) naskah tidak dikirim ke layanan eksternal oleh agen. Bila skor melebihi ambang: jangan meminta "putaran parafrasa buta" — kirimkan **bagian yang ditandai sistem + konteksnya**, lalu perbaikan dilakukan terarah mengikuti §5 dengan kontrak §4 tetap berlaku. Pengalaman menunjukkan bagian yang paling sering ditandai adalah latar belakang generik dan ringkasan berderet di tinjauan pustaka — keduanya sudah menjadi prioritas Fase 2.

## 10. Keputusan yang Sudah Dikunci (18 Sep 2026)

1. **Scope: penuh bertahap** — audit + tulis ulang Bab I–III berurutan, mulai Bab III → II → I.
2. **Kedalaman: seimbang** — rapikan frasa dan alur lokal; struktur bab tetap.
3. **Kebijakan kampus (hasil cek Pedoman 2023 oleh agen):**
   - [[05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md]] (butir 4.1) mewajibkan **bukti cek Turnitin, plagiarisme maks. 30%** — di atas itu tidak boleh ikut sidang. **Tidak ada pasal eksplisit tentang detektor AI** di dokumen 2023; ambang "AI ≤ 20%" diperlakukan sebagai ketentuan praktik/pembimbing, bukan pasal pedoman.
   - **Lampiran 4 (Pernyataan Orisinalitas)** mewajibkan pernyataan "dibuat dan diselesaikan sendiri... bukan duplikasi... bukan karya terjemahan", dengan sanksi pembatalan. Konsekuensinya: (a) setiap hasil suntingan **wajib dibaca-akhir dan dipahami user** sebelum porting (gerbang Fase 2/Fase 4 bukan formalitas — user harus bisa mempertahankan tiap kalimat di sidang); (b) tidak ada pernyataan AI terpisah yang perlu ditambahkan/dihapus menurut pedoman 2023 — bila pembimbing meminta pernyataan penggunaan AI, tempelkan teksnya dan PRD ini disesuaikan.

## 11. Adendum Revisi Dosen — Akuntabilitas Atribusi Klaim Jurnal (18 Sep 2026)

Arahan dosen (chat 16 Sep 2026: *"...di sitasi di highlight aja di mendeley biar pas ditanya di buka langsung keliatan"*): tiap kalimat "penulis menyatakan/membuktikan X (Sitasi)" harus dapat dibuka ke halaman + kalimat sumbernya saat sidang. Berlaku untuk SEMUA jurnal, dengan prioritas tertinggi **jurnal dosen pembimbing sendiri** ([[2024_Colline_Biases_Indonesian_Stock_Investor_AFS.pdf]]) — salah atribusi di sana risikonya maksimal.

- Aturan: klaim atribusi diperiksa dalam audit tiap bab (kolom B di berkas AUDIT_*); verdict hanya 4: TERDUKUNG (halaman + kutipan tercatat) / SEBAGIAN / PERLU DILURUSKAN / BUTUH KEPUTUSAN. Klaim ke PDF tak-lokal = setingkat-judul (flag jujur, warisan D26 §B ledger).
- Hasil berjalan: Colline terverifikasi ulang penuh (herding/loss aversion/disposition effect + motif capital gain, PDF p1/p5–p6; n=5, usia 34–69); temuan F-CARRY-1 (frasa "investor muda" di TeX L698 bertentangan dengan sampel 34–69) mengantre di audit Bab II.

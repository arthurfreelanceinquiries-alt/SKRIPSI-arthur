> [!SUMMARY] Tujuan & Solusi Catatan Ini
> - **Untuk Apa:** Template kosong Source of Truth + Evidence Ledger untuk memulai topik skripsi BARU apapun dengan framework Graph of Agents.
> - **Masalah yang Diselesaikan:** Setiap topik baru selama ini mulai dari nol tanpa parameter beku, sehingga riset melebar dan sitasi tidak terlacak.
> - **Keputusan/Output:** Duplikat file ini → isi blok [ISI] → jadikan kanon. Jangan ubah struktur heading agar diverifikasi mesin.

# TEMPLATE SOURCE OF TRUTH UNIVERSAL (Topik Baru)

> **Cara pakai:** salin file ini menjadi `SOURCE_OF_TRUTH_[TOPIK].md`, isi semua `[ISI]`, bekukan sebelum kumpul bukti (§1.2 framework). Rujuk: [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]] · [[04_Riset_&_Metodologi/REUSABLE_THESIS_PLAYBOOK.md]] · [[directives/universal_thesis_graph_of_agents.md]].

---

## 1. Identitas & Interpretasi Beku (wajib sebelum evidence)

| Parameter | Isian |
|---|---|
| Program Studi / Konsentrasi | [ISI] |
| Judul (terkunci SETELAH Fase 1–3) | [ISI] |
| Unit yang diteliti | [ISI: siapa/apa, contoh: konsumen WNI ≥17th] |
| Populasi + kriteria inklusi | [ISI] |
| Periode / versi / batas tanggal | [ISI] |
| Estimand (apa yang diestimasi) | [ISI: β / ΔR² / odds / tema ...] |
| Metode + software | [ISI: MRA-SPSS / SEM-PLS / kualitatif ...] |
| Target sampel + dasar power | [ISI: N≥..., Green 50+8k / Cohen ...] |
| Eksklusi (apa yang TIDAK diklaim) | [ISI] |
| Selesai-jika (completion criteria) | [ISI] |
| Pedoman format kampus | [ISI: nama pedoman + margin/font/spasi/sitasi] |
| Syarat minimal kampus | [ISI: ≥... hlm, ≥... ref, ≥... jurnal] |
| Golden truth naskah | [ISI: 1 file master, mis. Proposal.tex] |

## 2. Decisions Log (kunci tiap keputusan, jangan hapus baris lama)

| ID | Keputusan | Tanggal | Dasar |
|---|---|---|---|
| D01 | [ISI] | [ISI] | [ISI] |
| D02 | [ISI] | [ISI] | [ISI] |

## 3. Model / Kerangka (frozen verbatim)

```text
[ISI: diagram X→Y + moderasi/mediasi, atau kerangka kualitatif]
```

Persamaan / proposisi beku:

```text
[ISI: Model 1: ... ; Model 2: ... (tandai mean-centered dengan *)]
```

## 4. Kanon Sumber (T1–T3 + blacklist T4)

| Level | Sumber | Deep-link kanonis | Status cek |
|---|---|---|---|
| T1 | [ISI] | https://[ISI] | HTTP [ISI], tgl [ISI] |
| T2 | [ISI] | https://[ISI] | HTTP [ISI], tgl [ISI] |
| T3 | [ISI] | https://[ISI] | HTTP [ISI], tgl [ISI] |
| T4-BANNED | [ISI: blog/forum/direktori yang ditolak] | — | DITOLAK karena [ISI] |

## 5. Evidence Ledger (satu baris per klaim — tambah baris sesuai kebutuhan)

| # | Klaim di naskah | Kelas (fact/observation/inference/assumption/unknown) | Sumber + tgl akses | Cek (live/PDF hash/screenshot/status link ALIVE-WALLED-DEAD) | Falsifier (bukti yang menggugurkan; DOI mati = sumber DIGANTI) |
|---|---|---|---|---|---|
| E01 | [ISI] | [ISI] | [ISI] | [ISI] | [ISI] |
| E02 | [ISI] | [ISI] | [ISI] | [ISI] | [ISI] |

Aturan: `inference` tanpa falsifier = turunkan menjadi `assumption`, dilarang masuk Bab 1 sebagai fakta (C-LEDGER-1).

## 6. Scope & Target Filter (tulis batasnya eksplisit)

- **Scope (generalisasi):** [ISI: sejauh apa bukti boleh digeneralisasi + apa yang tidak]
- **Target (kecocokan objek):** [ISI: apakah sampel/versi/workload sama dengan objek + kontradiksi yang diawetkan]

## 7. Acceptance Tiap Agen (observable, angka bukan "rapi")

| Agen | DONE berarti |
|---|---|
| A1 | [ISI] |
| A2 | NOT_FOUND=0, 0 login-wall |
| A3 | semua PDF %PDF; katalog lengkap; `verify_all_citation_links` 0 DEAD (C-LINK-1) |
| A4 | tiap konstruk → teori + skala baku |
| A5 | estimand + model frozen + etik |
| A6 | [ISI: ΔR²/effect size/...] |
| A7 | build tanpa error XML |
| A8 | `run_thesis_graph.py --gate parity` 7/7 PASS |
| A9 | Critical=0 |
| A10 | panduan sinkron SoT; PDF <5MB |
| A11 | log + dashboard terupdate |

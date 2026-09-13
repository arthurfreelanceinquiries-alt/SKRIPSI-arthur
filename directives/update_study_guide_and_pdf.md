# Directive: Update Panduan Belajar & Generate PDF

## Tujuan
SOP resmi untuk memperbarui `PANDUAN_BELAJAR_PROPOSAL.md` sesuai perkembangan naskah terbaru, lalu mengonversinya ke format PDF yang rapi dan mudah dibaca.

## Kriteria Konten Yang Perlu Diperbarui
Sebelum generate PDF, periksa apakah ada hal baru berikut yang belum masuk ke panduan:
1. Revisi rumusan masalah, tujuan, atau hipotesis terbaru (cek vs `SOURCE_OF_TRUTH.md`)
2. Update dosen pembimbing atau detail administrasi
3. Catatan bimbingan baru yang belum dicatat di panduan
4. Hasil audit komparasi PDF vs DOCX yang relevan untuk dipelajari

## Standar Format PDF Output
- **Nama output:** `02_Persiapan_Sidang/PANDUAN_BELAJAR_PROPOSAL.pdf`
- **Engine:** Pandoc (prioritas utama) atau WeasyPrint (fallback)
- **Layout:** A4, margin 2.5 cm semua sisi
- **Font:** Bebas, mengikuti default pandoc/HTML render
- **Bahasa:** Bahasa Indonesia

## Kriteria Keberhasilan
- PDF berhasil dibuat dan dapat dibuka
- Semua section (1–11) terbaca rapi di PDF
- Tidak ada karakter aneh / encoding error
- File ukuran wajar (< 5 MB)

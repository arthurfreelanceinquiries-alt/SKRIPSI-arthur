# Pelestarian makna dan berkas

## Kontrak isi

Sebelum revisi yang cukup panjang, simpan peta ringkas isi yang tidak boleh berubah:

| Unsur | Apa yang dilindungi |
|---|---|
| Angka | Nilai, tanda, satuan, denominator, kelompok, kondisi, periode, interval, dan pasangan model/nilai. |
| Klaim | Siapa melakukan apa, pada objek/populasi apa, kapan, dan dengan syarat apa. |
| Kepastian | Negasi, kemungkinan, rencana, observasi, interpretasi, hipotesis, dan bukti kausal. |
| Sitasi | Nama/nomor/kunci, posisi dukungan terhadap klaim, cakupan satu vs beberapa kalimat. |
| Istilah | Makna operasional; glosarium tidak boleh menyamakan konsep yang berbeda. |
| Format | Kutipan langsung, persamaan, kode, identifier, URL/DOI, label/ref, tabel, dan caption. |
| Suara | Pendapat atau pengalaman yang diberikan penulis, kesopanan, sikap terhadap pembaca. |

Jangan mengisi sumber yang kosong. Jangan memakai kutipan dari satu artikel untuk menopang generalisasi baru setelah kalimat digabung. “Sumber tersedia” bukan berarti isi sumber telah dibaca. Jika verifikasi fakta diminta, lakukan dalam bagian kerja yang jelas dan laporkan koreksinya.

Contoh jebakan: `A = 0,81 dan B = 0,78` menjadi `B = 0,81 dan A = 0,78` lolos pencocokan angka tetapi mengubah hasil. `Tidak berbeda signifikan` menjadi `setara` juga mengubah kesimpulan. Verifikasi semantik tetap wajib meski pemeriksaan token bersih.

## Bahan yang kurang jelas

- Jika bisa memperbaiki kalimat tanpa menyelesaikan ambiguitas, lakukan dan beri catatan singkat di luar revisi.
- Jika inti kalimat ambigu, jangan menebak interpretasi. Pertahankan bagian itu dan tandai pertanyaan spesifik. Lanjutkan bagian lain yang aman.
- Jika pengguna meminta teks final saja, jangan menjejalkan komentar ke paragraf final. Jika ketidakpastian membuat revisi aman mustahil, ajukan satu pertanyaan terarah sebelum mengubah bagian tersebut.
- Koreksi ejaan berbeda dari koreksi hasil ilmiah. Jangan diam-diam mengganti angka atau kesimpulan yang dianggap salah.
- Bila konteks cukup untuk mengenali kesalahan substantif, berikan usulan koreksi yang diberi label jelas di luar suntingan gaya. Usulan tersebut dapat disiapkan tanpa meminta izin baru hanya untuk menunjukkan alternatif yang dapat ditinjau. Jangan menimpa berkas atau menyatakan koreksi sudah disetujui jika ruang lingkupnya hanya gaya. Jika bukti belum cukup, jelaskan bagian yang perlu diverifikasi alih-alih membuat rumusan pengganti.
- Jangan mengunci rujukan ambigu seperti “tahap tersebut” menjadi tahap tertentu hanya untuk membuat kalimat konkret. Gunakan konteks yang benar-benar memastikan acuannya; jika belum, pertahankan atau catat ambiguitas di luar revisi.

## Berkas dan dokumen panjang

Untuk .docx, .pdf, atau format presentasi, gunakan dukungan format host bila tersedia. Skill ini tidak menyediakan parser seluruh format. Ekstraksi teks dari PDF tidak menjamin tabel, urutan baca, dan catatan kaki benar. Periksa tampilan bila bentuknya berpengaruh.

Pada LaTeX, ubah prosa dengan tetap menjaga `\cite{}`, `\ref{}`, `\label{}`, matematika, dan perintah. Jangan mengganti seluruh dokumen dengan teks hasil ekstraksi. Pada Markdown, pertahankan frontmatter, code fence, tautan, dan elemen struktural yang dibutuhkan. Untuk dokumen panjang, buat glosarium bersama dan periksa konsistensi lintas bagian setelah penyuntingan lokal.

Gunakan revisi terpisah jika penimpaan sumber tidak diminta atau belum jelas. Jika perubahan langsung telah diminta, lakukan sesuai lingkup tanpa meminta izin ulang. Jangan mengirim dokumen pengguna ke layanan humanizer/detektor eksternal hanya untuk menilai gaya.

## Bantuan audit teks

`scripts/audit_text.py` menggunakan Python 3 standard library; input adalah teks UTF-8 (.txt, .md, atau .tex). Tidak mengedit input dan tidak memakai jaringan.

```text
python scripts/audit_text.py scan draft.md
python scripts/audit_text.py compare original.tex revised.tex
```

`scan` memberi lokasi pemicu leksikal dan penekanan yang perlu dibaca. Ia melewati code fence dan beberapa blok verbatim tetapi **bukan parser bahasa atau LaTeX lengkap**. Kutipan, istilah statistik yang tepat, dan kode inline mungkin terdeteksi; periksa konteks. Tidak ada ambang skor kelulusan atau persentase AI.

`compare` membandingkan jumlah kemunculan token angka, sitasi LaTeX tertentu, rujukan silang, tautan, dan kode inline. Perbedaan adalah antrean pemeriksaan. Pengulangan yang sengaja dipadatkan dan perubahan format angka yang disetujui dapat memunculkan temuan yang sah. Tanggal/angka dalam prosa, sitasi author-year, perubahan satuan, dan matematika kompleks tidak seluruhnya dikenali. **Token sama tetap tidak menjamin hubungan, negasi, atau makna sama.**

Kode keluar 0 berarti proses selesai, bukan revisi lolos secara semantik. Kode 2 berarti argumen/input gagal. Keluaran JSON dapat disimpan oleh pemanggil untuk laporan jika diperlukan. Pemeriksaan manual lebih penting daripada mengurangi jumlah temuan.

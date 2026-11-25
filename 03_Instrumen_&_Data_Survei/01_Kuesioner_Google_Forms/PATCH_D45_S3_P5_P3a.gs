/**
 * PATCH_D45_S3_P5_P3a.gs  —  ***SUPERSEDED — JANGAN DIJALANKAN***
 * ---------------------------------------------------------------------------
 * STATUS PER 24 NOVEMBER 2026:
 *   Patch D45 sudah DITERAPKAN dan DIVERIFIKASI pada form live lewat Google
 *   Forms API (revisionId 0000002b -> 0000002c), dari akun pemilik:
 *     - S3 sudah memakai redaksi "MINIMAL SALAH SATU" + label opsi eksplisit
 *     - P5 sudah menempatkan "Marketplace daring" di urutan pertama
 *     - P3a sudah ditambahkan (itemId 105e79fe), opsional, berada di kolom
 *       terakhir spreadsheet respons (kolom 39), bukan di samping P3.
 *
 *   Menjalankan perbaikiD45() SEKARANG akan MENIMPA S3 yang sudah benar dan
 *   berisiko MENGHAPUS navigasi opsi "Ya" ke section S4, sehingga rantai
 *   C0 -> S1 -> S2 -> S3 -> S4 rusak. Karena itu file ini disimpan sebagai
 *   catatan sejarah saja.
 *
 *   Verifikasi terkini: python .../d45-patch/patch_p3a.py (mode dry-run).
 *
 * Riwayat fungsi (tidak dijalankan lagi): dryRunD45 / perbaikiD45 / verifikasiD45.
 *
 * CARA PAKAI SEMULA (arsip):
 *   1. Buka https://script.google.com  -> New project
 *   2. Tempel seluruh isi file ini
 *   3. Isi FORM_ID di bawah
 *   4. Jalankan dryRunD45()  -> hanya membaca & mencatat, TIDAK mengubah apa pun
 *   5. Periksa log. Bila sesuai, jalankan perbaikiD45()
 *   6. Jalankan verifikasiD45() untuk konfirmasi hasil
 *
 * CATATAN PENTING (arsip):
 *   - Jangan jalankan perbaikiD45() dua kali; P3a akan terduplikasi.
 *     Skrip sudah menjaga hal ini (deteksi P3a yang sudah ada).
 *   - Menambah P3a TIDAK menggeser nomor kolom di tengah spreadsheet.
 *     Google Sheets menambahkan pertanyaan baru di ujung kanan lembar, jadi
 *     P3a muncul sebagai kolom terakhir. Ekspor ulang CSV / perbarui template
 *     tabulasi setelah patch (lihat KODEBOOK_DAN_TEMPLATE_TABULASI.md).
 *   - Catatan X3 lama pada file ini ("masih parafrase dan belum selaras
 *     Tabel 3.2") TIDAK TERBUKTI dan sudah dicabut: X3_1-X3_5 telah searah
 *     dan seurutan dengan indikator Tabel 3.2. Tidak ada perubahan X3.
 * ---------------------------------------------------------------------------
 */

// ==== KONFIGURASI =================================================================

// ID form. Diambil dari URL edit:
// https://docs.google.com/forms/d/<FORM_ID>/edit
var FORM_ID = '1W23UT6NnR1xchMGuQK_cIVctXGI3xPfPAUwsUJ7Z0Ws';

var JUDUL_S3       = 'S3.';
var JUDUL_P5       = 'P5.';
var JUDUL_P3       = 'P3.';
var JUDUL_P3A      = 'P3a.';
var JUDUL_DISKUAL  = 'Kriteria partisipasi belum terpenuhi';

var TEKS_S3_BARU =
  'S3. Apakah Anda memiliki MINIMAL SALAH SATU keterkaitan dengan wilayah ' +
  'Jakarta Barat? (Contoh: tinggal/kost di Jakbar, ATAU kuliah/kerja di ' +
  'Jakbar seperti UKRIDA/Untar/kantor Jakbar, ATAU pernah/rutin berbelanja ' +
  'atau bermain kartu Pokemon di toko/mall/LGS Jakarta Barat)';

var OPSI_S3_YA   = 'Ya (memenuhi minimal salah satu kriteria di atas)';
var OPSI_S3_TIDAK = 'Tidak (sama sekali tidak tinggal, tidak bekerja/kuliah, ' +
                    'dan tidak bertransaksi di Jakarta Barat)';

var OPSI_P5_BARU = [
  'Marketplace daring / E-commerce (Tokopedia, Shopee, Blibli, TikTok Shop, dll.)',
  'Toko Hobi Lokal / LGS resmi (Tanjung Duren / Central Park / Mall Taman Anggrek / Puri Indah, dll.)',
  'Minimarket / Ritel modern (Indomaret / Alfamart / Gramedia / Toys Kingdom)',
  'Transaksi langsung / COD komunitas sesama pemain',
  'Lainnya'
];

var TEKS_P3A =
  'P3a. Bentuk keterkaitan utama Anda dengan wilayah Jakarta Barat';

var OPSI_P3A = [
  'Domisili / tempat tinggal / kost di Jakarta Barat',
  'Tempat kuliah di Jakarta Barat (UKRIDA, Untar, Trisakti, Binus, dll.)',
  'Tempat bekerja atau berkantor di Jakarta Barat',
  'Lokasi bermain atau belanja kartu Pokemon (LGS / Mall Jakarta Barat)',
  'Beberapa di antaranya sekaligus (komuter lintas wilayah)'
];

// ==== UTILITAS ====================================================================

function bukaForm_() {
  return FormApp.openById(FORM_ID);
}

function cariBerdasarkanAwalan_(items, awalan) {
  for (var i = 0; i < items.length; i++) {
    var t = items[i].getTitle() || '';
    if (t.indexOf(awalan) === 0) {
      return items[i];
    }
  }
  return null;
}

function cariSectionDiskualifikasi_(items) {
  for (var i = 0; i < items.length; i++) {
    if (items[i].getType() === FormApp.ItemType.PAGE_BREAK) {
      var t = items[i].getTitle() || '';
      if (t.indexOf(JUDUL_DISKUAL) !== -1) {
        return items[i].asPageBreakItem();
      }
    }
  }
  return null;
}

// ==== DRY RUN (AMAN: HANYA MEMBACA) ==============================================

function dryRunD45() {
  var form = bukaForm_();
  var items = form.getItems();

  Logger.log('=== DRY RUN D45 — tidak ada perubahan ===');
  Logger.log('Judul form : ' + form.getTitle());
  Logger.log('Jumlah item: ' + items.length);

  var s3 = cariBerdasarkanAwalan_(items, JUDUL_S3);
  var p5 = cariBerdasarkanAwalan_(items, JUDUL_P5);
  var p3 = cariBerdasarkanAwalan_(items, JUDUL_P3);
  var p3a = cariBerdasarkanAwalan_(items, JUDUL_P3A);
  var diskual = cariSectionDiskualifikasi_(items);

  Logger.log('--- Prasyarat ---');
  Logger.log('S3 ditemukan          : ' + (s3 !== null));
  Logger.log('P5 ditemukan          : ' + (p5 !== null));
  Logger.log('P3 ditemukan          : ' + (p3 !== null));
  Logger.log('P3a sudah ada?        : ' + (p3a !== null) + ' (bila true, P3a tidak dibuat ulang)');
  Logger.log('Section diskualifikasi: ' + (diskual !== null));

  if (s3) { Logger.log('S3 sekarang: ' + s3.getTitle()); }
  if (p5) {
    Logger.log('P5 sekarang: ' + p5.asMultipleChoiceItem().getChoices().map(function (c) {
      return c.getValue();
    }).join(' | '));
  }

  if (!s3 || !p5 || !p3 || !diskual) {
    Logger.log('!! PRASYARAT GAGAL — ada butir yang tidak ditemukan. Jangan jalankan perbaikiD45().');
    return;
  }
  Logger.log('--- Prasyarat LENGKAP. Siap menjalankan perbaikiD45(). ---');
}

// ==== PATCH UTAMA ================================================================

function perbaikiD45() {
  throw new Error(
    'SKRIP INI SUDAH SUPERSEDED (24 Nov 2026). Patch D45 telah diterapkan dan ' +
    'diverifikasi pada form live (revisionId 0000002c). Menjalankan fungsi ini ' +
    'akan menimpa S3 yang sudah benar dan berisiko menghapus navigasi "Ya" ke S4. ' +
    'Gunakan patch_p3a.py untuk dry-run verifikasi, bukan skrip arsip ini.'
  );

  /* --- kode arsip di bawah tidak pernah dieksekusi --- */
  var form = bukaForm_();
  var items = form.getItems();

  var s3 = cariBerdasarkanAwalan_(items, JUDUL_S3);
  var p5 = cariBerdasarkanAwalan_(items, JUDUL_P5);
  var p3 = cariBerdasarkanAwalan_(items, JUDUL_P3);
  var p3aExisting = cariBerdasarkanAwalan_(items, JUDUL_P3A);
  var diskual = cariSectionDiskualifikasi_(items);

  if (!s3 || !p5 || !p3 || !diskual) {
    throw new Error('Prasyarat tidak lengkap: S3/P5/P3/section diskualifikasi tidak ditemukan. Dibatalkan.');
  }

  // ---------- 1. S3: redaksi inklusif + label opsi eksplisit ----------
  // ARSIP: blok ini menggabungkan choice tanpa navigasi dan dengan navigasi.
  // Google Forms menolak campuran itu; opsi "Ya" harus tetap menunjuk ke S4.
  var mcS3 = s3.asMultipleChoiceItem();
  var s4 = cariBerdasarkanAwalan_(items, 'S4.');
  if (!s4 || s4.getType() !== FormApp.ItemType.PAGE_BREAK) {
    throw new Error('Section S4 tidak ditemukan; navigasi "Ya" tidak dapat dipertahankan.');
  }
  mcS3.setTitle(TEKS_S3_BARU);
  mcS3.setChoices([
    mcS3.createChoice(OPSI_S3_YA, s4.asPageBreakItem()),  // lanjut ke section S4
    mcS3.createChoice(OPSI_S3_TIDAK, diskual)             // lompat ke section diskualifikasi
  ]);
  Logger.log('OK  S3 diperbarui (routing diskualifikasi dipertahankan).');

  // ---------- 2. P5: marketplace ke urutan pertama ----------
  var mcP5 = p5.asMultipleChoiceItem();
  mcP5.setChoiceValues(OPSI_P5_BARU);
  Logger.log('OK  P5 diperbarui — Marketplace daring kini opsi pertama.');

  // ---------- 3. P3a: tambah setelah P3 ----------
  if (p3aExisting !== null) {
    Logger.log('SKIP P3a sudah ada: ' + p3aExisting.getTitle());
  } else {
    var baru = form.addMultipleChoiceItem();
    baru.setTitle(TEKS_P3A);
    baru.setChoiceValues(OPSI_P3A);
    baru.setRequired(false);

    // Pindahkan tepat setelah P3
    var itemsKini = form.getItems();
    var idxP3 = -1;
    for (var i = 0; i < itemsKini.length; i++) {
      if ((itemsKini[i].getTitle() || '').indexOf(JUDUL_P3) === 0 &&
          (itemsKini[i].getTitle() || '').indexOf(JUDUL_P3A) !== 0) {
        idxP3 = i;
        break;
      }
    }
    if (idxP3 === -1) {
      throw new Error('P3 tidak ditemukan saat memindahkan P3a.');
    }
    form.moveItem(baru, idxP3 + 1);
    Logger.log('OK  P3a ditambahkan pada posisi ' + (idxP3 + 1) + ' (setelah P3).');
  }

  Logger.log('=== SELESAI. Jalankan verifikasiD45() ===');
}

// ==== VERIFIKASI =================================================================

function verifikasiD45() {
  var form = bukaForm_();
  var items = form.getItems();

  Logger.log('=== VERIFIKASI D45 ===');

  var s3 = cariBerdasarkanAwalan_(items, JUDUL_S3);
  Logger.log('S3: ' + (s3 ? s3.getTitle() : 'TIDAK ADA'));
  if (s3) {
    Logger.log('  opsi: ' + s3.asMultipleChoiceItem().getChoices().map(function (c) {
      return c.getValue();
    }).join(' || '));
  }

  var p5 = cariBerdasarkanAwalan_(items, JUDUL_P5);
  if (p5) {
    var vals = p5.asMultipleChoiceItem().getChoices().map(function (c) { return c.getValue(); });
    Logger.log('P5 opsi pertama: ' + vals[0]);
    Logger.log('P5 marketplace di urutan pertama? ' + (vals[0].indexOf('Marketplace') === 0));
  }

  var p3a = cariBerdasarkanAwalan_(items, JUDUL_P3A);
  Logger.log('P3a: ' + (p3a ? p3a.getTitle() : 'TIDAK ADA'));

  // Pastikan P3a tepat setelah P3
  var urutan = items.map(function (it) { return (it.getTitle() || '').split('.')[0]; });
  Logger.log('Urutan kode butir: ' + urutan.join(', '));

  var wajib = items.filter(function (it) {
    return (it.getType() === FormApp.ItemType.MULTIPLE_CHOICE ||
            it.getType() === FormApp.ItemType.SCALE);
  }).length;
  Logger.log('Jumlah butir pilihan-ganda + skala: ' + wajib + ' (harus 37 + 1 P3a = 38 bila P3a baru dibuat)');
}

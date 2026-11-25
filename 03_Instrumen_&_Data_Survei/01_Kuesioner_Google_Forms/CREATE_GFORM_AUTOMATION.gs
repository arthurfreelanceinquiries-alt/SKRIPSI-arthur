/**
 * ==============================================================================
 * PERBAIKAN & PEMBANGUN GOOGLE FORMS — KUESIONER SKRIPSI ARTHUR REEZAN
 * Revisi Kanonis D45 (arahan Dr. Fredella Colline, 17 November 2026)
 * ==============================================================================
 * Judul Penelitian:
 * "Pengaruh Hedonic Motivation, Desire for Completeness, dan Speculative Motive
 *  terhadap Impulsive Buying Booster Pack Kartu Pokemon TCG dengan Self-Control
 *  sebagai Variabel Moderasi (Studi pada Konsumen di Jakarta Barat)"
 *
 * CARA PAKAI (1 menit, tanpa OAuth / tanpa API eksternal):
 *   1. Buka https://script.google.com -> New project
 *   2. Hapus isi editor, tempel SELURUH file ini, lalu Save
 *   3. Pilih fungsi: perbaikiKuesionerRevisiD45 -> Run -> izinkan akses saat diminta
 *   4. Buka menu Execution log untuk melihat ringkasan perubahan
 *   5. Opsional: jalankan verifikasiKuesioner() untuk memeriksa hasil akhir
 *
 * Fungsi ini IDEMPOTEN: boleh dijalankan berulang tanpa merusak formulir.
 * ==============================================================================
 */

// ID form Arthur (dari URL edit). Ganti bila formulir diganti.
var FORM_ID = "1W23UT6NnR1xchMGuQK_cIVctXGI3xPfPAUwsUJ7Z0Ws";

// ---- Spesifikasi revisi D45 ----
var S3_TITLE = "S3. Apakah Anda memiliki MINIMAL SALAH SATU keterkaitan dengan wilayah Jakarta Barat berikut? (Contoh: tinggal/kost di Jakbar, ATAU kuliah/bekerja di Jakbar seperti kampus UKRIDA/Untar/kantor Jakbar, ATAU pernah atau rutin berbelanja/bermain kartu Pokemon di toko/mall/LGS wilayah Jakbar)";
var S3_YA = "Ya (memenuhi minimal salah satu kriteria di atas)";
var S3_TIDAK = "Tidak (sama sekali tidak memiliki keterkaitan dengan Jakarta Barat)";

var P5_TITLE = "P5. Kanal/tempat pembelian utama yang paling sering Anda gunakan";
var P5_OPTS = [
  "Marketplace daring / E-commerce (Tokopedia, Shopee, TikTok Shop, Blibli, dll.)",
  "Local Game Store (LGS) resmi (Tanjung Duren/Central Park/Mall Taman Anggrek/Puri Indah)",
  "Minimarket / toko buku (Indomaret/Alfamart/Gramedia/Toys Kingdom)",
  "Transaksi langsung / COD komunitas",
  "Lainnya"
];

var PAGE_DISKUALIFIKASI = "Penutup";   // penanda judul halaman diskualifikasi
var PAGE_S4 = "Penyaringan — S4";       // penanda judul halaman S4


// ==============================================================================
// UTILITAS
// ==============================================================================

function bukaForm_() {
  var active = null;
  try { active = FormApp.getActiveForm(); } catch (e) { active = null; }
  return active ? active : FormApp.openById(FORM_ID);
}

function cariHalaman_(form, penanda) {
  var items = form.getItems(FormApp.ItemType.PAGE_BREAK);
  for (var i = 0; i < items.length; i++) {
    if (items[i].getTitle().indexOf(penanda) !== -1) return items[i].asPageBreakItem();
  }
  return null;
}

function cariButir_(form, awalanKode) {
  var items = form.getItems();
  for (var i = 0; i < items.length; i++) {
    var t = items[i].getTitle();
    if (t && t.indexOf(awalanKode + ".") === 0) return items[i];
  }
  return null;
}


// ==============================================================================
// FUNGSI UTAMA — PERBAIKAN IN-PLACE REVISI D45 (S3 + P5)
// ==============================================================================

function perbaikiKuesionerRevisiD45() {
  var form = bukaForm_();
  var halamanDiskualifikasi = cariHalaman_(form, PAGE_DISKUALIFIKASI);
  var halamanS4 = cariHalaman_(form, PAGE_S4);

  if (!halamanS4) {
    Logger.log("GAGAL: halaman '" + PAGE_S4 + "' tidak ditemukan. Periksa judul section.");
    return;
  }
  if (!halamanDiskualifikasi) {
    Logger.log("GAGAL: halaman diskualifikasi tidak ditemukan. Periksa judul section.");
    return;
  }

  // ---------- 1. S3: formula inklusif anti-kebingungan komuter ----------
  var butirS3 = cariButir_(form, "S3");
  if (butirS3 && butirS3.getType() === FormApp.ItemType.MULTIPLE_CHOICE) {
    var mcS3 = butirS3.asMultipleChoiceItem();
    mcS3.setTitle(S3_TITLE);
    mcS3.setHelpText("Cukup SATU keterkaitan terpenuhi. Lokasi tinggal, kuliah/kerja, dan tempat bermain boleh berbeda wilayah - selama salah satunya di Jakarta Barat, Anda lolos.");
    mcS3.setChoices([
      mcS3.createChoice(S3_YA, halamanS4),
      mcS3.createChoice(S3_TIDAK, halamanDiskualifikasi)
    ]);
    Logger.log("OK  S3  : judul + opsi + logika cabang diperbarui.");
  } else {
    Logger.log("SKIP S3 : butir tidak ditemukan atau bukan pilihan ganda.");
  }

  // ---------- 2. P5: kanal marketplace daring ----------
  var butirP5 = cariButir_(form, "P5");
  if (butirP5 && butirP5.getType() === FormApp.ItemType.MULTIPLE_CHOICE) {
    var mcP5 = butirP5.asMultipleChoiceItem();
    mcP5.setTitle(P5_TITLE);
    mcP5.setHelpText("Pilih kanal yang PALING SERING Anda gunakan, bukan yang pernah dicoba sekali.");
    mcP5.setChoiceValues(P5_OPTS);
    Logger.log("OK  P5  : " + P5_OPTS.length + " opsi kanal diperbarui (marketplace di urutan pertama).");
  } else {
    Logger.log("SKIP P5 : butir tidak ditemukan atau bukan pilihan ganda.");
  }

  // ---------- RINGKASAN ----------
  Logger.log("=== RINGKASAN PERBAIKAN D45 ===");
  Logger.log("ID Form     : " + form.getId());
  Logger.log("Link Edit   : " + form.getEditUrl());
  Logger.log("Link Publik : " + form.getPublishedUrl());
  Logger.log("Catatan     : jalankan verifikasiKuesioner() untuk memeriksa hasil akhir.");
}


// ==============================================================================
// FUNGSI VERIFIKASI — MEMBACA KONDISI TERKINI FORM
// ==============================================================================

function verifikasiKuesioner() {
  var form = bukaForm_();
  var items = form.getItems();

  Logger.log("=== VERIFIKASI STRUKTUR FORM ===");
  Logger.log("Judul   : " + form.getTitle());
  Logger.log("Jumlah butir: " + items.length);

  // Cek S3
  var s3 = cariButir_(form, "S3");
  if (s3 && s3.getType() === FormApp.ItemType.MULTIPLE_CHOICE) {
    var mc3 = s3.asMultipleChoiceItem();
    Logger.log("--- S3 ---");
    Logger.log("Judul : " + mc3.getTitle());
    var ch3 = mc3.getChoices();
    for (var a = 0; a < ch3.length; a++) {
      Logger.log("  Opsi : " + ch3[a].getValue() + "  -> " + ch3[a].getPageNavigationType());
    }
  }

  // Cek P5
  var p5 = cariButir_(form, "P5");
  if (p5 && p5.getType() === FormApp.ItemType.MULTIPLE_CHOICE) {
    Logger.log("--- P5 ---");
    Logger.log("Judul : " + p5.getTitle());
    var ch5 = p5.asMultipleChoiceItem().getChoices();
    for (var b = 0; b < ch5.length; b++) {
      Logger.log("  Opsi " + (b + 1) + ": " + ch5[b].getValue());
    }
  }

  // Cek urutan kode butir Likert (harus Y1..M6 berurutan, sejalan Tabel 3.2)
  Logger.log("--- URUTAN BUTIR LIKERT (WAJIB Y1..M6) ---");
  var skala = form.getItems(FormApp.ItemType.SCALE);
  var urutan = [];
  for (var c = 0; c < skala.length; c++) {
    urutan.push(skala[c].getTitle().split(".")[0]);
  }
  Logger.log(urutan.join(", "));

  var diharapkan = ["Y1","Y2","Y3","Y4","Y5","Y6","X1_1","X1_2","X1_3","X1_4","X1_5",
                    "X2_1","X2_2","X2_3","X2_4","X2_5","X3_1","X3_2","X3_3","X3_4","X3_5",
                    "M1","M2","M3","M4","M5","M6"];
  var sesuai = (urutan.join(",") === diharapkan.join(","));
  Logger.log("Kesesuaian urutan kode: " + (sesuai ? "SESUAI (27 butir)" : "TIDAK SESUAI - periksa!"));
}


// ==============================================================================
// FUNGSI CADANGAN — MEMBANGUN FORM BARU DARI NOL (bila form lama perlu diganti)
// ==============================================================================

function buatKuesionerSkripsiBaru() {
  var form = FormApp.create("Survei Perilaku Pembelian Booster Pack Kartu Pokemon TCG — Konsumen Jakarta Barat");
  form.setDescription(
    "Perkenalkan, saya Arthur Reezan (S1 Manajemen, FEB UKRIDA). Formulir ini adalah instrumen Tugas Akhir " +
    "mengenai perilaku pembelian booster pack kartu Pokemon TCG pada konsumen di Jakarta Barat.\n\n" +
    "Partisipasi bersifat SUKARELA dan ANONIM. Kami TIDAK meminta nama, NIM, email, nomor HP, atau alamat rumah. " +
    "Jawaban hanya dipakai untuk keperluan akademik dan dilaporkan secara agregat. Estimasi pengisian 5-7 menit.\n\n" +
    "Kriteria partisipan: (1) WNI; (2) usia minimal 17 tahun; (3) memiliki MINIMAL SALAH SATU keterkaitan dengan " +
    "Jakarta Barat (tinggal/kost, kuliah/kerja di Jakbar, ATAU berbelanja/bermain kartu di toko/mall/LGS Jakbar); " +
    "(4) pernah membeli booster pack fisik resmi minimal 1x dalam 12 bulan terakhir."
  );
  form.setProgressBar(true);
  form.setCollectEmail(false);
  form.setIsQuiz(false);
  form.setAllowResponseEdits(false);
  form.setConfirmationMessage("Terima kasih atas partisipasi Anda! Jawaban Anda telah tersimpan.");

  // Halaman diskualifikasi (dibuat lebih dahulu agar bisa dipakai sebagai target navigasi)
  var pageDiskualifikasi = form.addPageBreakItem()
    .setTitle("Penutup — Kriteria partisipasi belum terpenuhi")
    .setHelpText("Terima kasih atas kesediaan Anda. Survei ini dikhususkan bagi responden WNI, berusia minimal 17 tahun, " +
      "memiliki keterkaitan dengan Jakarta Barat, dan pernah membeli booster pack dalam 12 bulan terakhir.")
    .setGoToPage(FormApp.PageNavigationType.SUBMIT);

  // ---------- Section 1: Screening ----------
  var itemS1 = form.addMultipleChoiceItem()
    .setTitle("S1. Apakah Anda Warga Negara Indonesia (WNI)?").setRequired(true);
  var itemS2 = form.addMultipleChoiceItem()
    .setTitle("S2. Apakah usia Anda sudah mencapai 17 tahun atau lebih?").setRequired(true);
  var itemS3 = form.addMultipleChoiceItem()
    .setTitle(S3_TITLE)
    .setHelpText("Cukup SATU keterkaitan terpenuhi. Lokasi tinggal, kuliah/kerja, dan tempat bermain boleh berbeda wilayah - selama salah satunya di Jakarta Barat, Anda lolos.")
    .setRequired(true);
  var itemS4 = form.addMultipleChoiceItem()
    .setTitle("S4. Kapan TERAKHIR kali Anda membeli booster pack fisik resmi Pokemon TCG berbahasa Indonesia?")
    .setRequired(true);

  // ---------- Section 2: Profil ----------
  var pageProfil = form.addPageBreakItem().setTitle("Profil responden");

  form.addMultipleChoiceItem().setTitle("P1. Jenis kelamin").setRequired(false)
    .setChoiceValues(["Laki-laki", "Perempuan"]);
  form.addMultipleChoiceItem().setTitle("P2. Kelompok usia").setRequired(false)
    .setChoiceValues(["17–20 tahun", "21–25 tahun", "26–30 tahun", "Lebih dari 30 tahun"]);

  form.addMultipleChoiceItem().setTitle("P3. Kecamatan aktivitas utama di Jakarta Barat")
    .setHelpText("Tanjung Duren termasuk Kecamatan Grogol Petamburan.").setRequired(false)
    .setChoiceValues(["Cengkareng","Grogol Petamburan","Kalideres","Kebon Jeruk","Kembangan","Palmerah","Taman Sari","Tambora"]);

  form.addMultipleChoiceItem().setTitle("P4. Frekuensi pembelian booster pack dalam 6 bulan terakhir")
    .setHelpText("Jika pembelian terakhir Anda lebih dari 6 bulan lalu, pilih 0 kali.").setRequired(true)
    .setChoiceValues(["0 kali","1 kali","2–3 kali","4–6 kali","Lebih dari 6 kali"]);

  var itemP5 = form.addMultipleChoiceItem()
    .setTitle(P5_TITLE)
    .setHelpText("Pilih kanal yang PALING SERING Anda gunakan, bukan yang pernah dicoba sekali.")
    .setRequired(false)
    .setChoiceValues(P5_OPTS);

  // Helper skala Likert
  function tambahLikert(kode, teks) {
    form.addScaleItem().setTitle(kode + ". " + teks)
      .setBounds(1, 5).setLabels("Sangat Tidak Setuju", "Sangat Setuju").setRequired(true);
  }
  var PETUNJUK = "Berilah penilaian sesuai pengalaman Anda. 1 = Sangat Tidak Setuju; 2 = Tidak Setuju; 3 = Netral; " +
                 "4 = Setuju; 5 = Sangat Setuju. Tidak ada jawaban benar atau salah.";

  // ---------- Y: Impulsive Buying (urutan persis Tabel 3.2) ----------
  form.addPageBreakItem().setTitle("Pengalaman pembelian").setHelpText(PETUNJUK);
  tambahLikert("Y1", "Saya membeli booster pack Pokemon TCG tanpa merencanakan pembelian tersebut sebelumnya.");
  tambahLikert("Y2", "Saya tidak mempertimbangkan dampak keuangan saat membeli booster pack Pokemon TCG.");
  tambahLikert("Y3", "Saya membeli booster pack Pokemon TCG lebih banyak daripada yang semula saya niatkan.");
  tambahLikert("Y4", "Saya terdorong membeli booster pack Pokemon TCG secara spontan saat melihatnya di etalase toko.");
  tambahLikert("Y5", "Saya merasa gembira dan antusias ketika memutuskan membeli booster pack Pokemon TCG secara mendadak.");
  tambahLikert("Y6", "Saya sulit menahan keinginan membeli booster pack Pokemon TCG saat seri baru dirilis.");

  // ---------- X1: Hedonic Motivation ----------
  form.addPageBreakItem().setTitle("Pengalaman dan kesenangan berbelanja").setHelpText(PETUNJUK);
  tambahLikert("X1_1", "Saya merasa senang dan penasaran saat membuka kemasan booster pack Pokemon TCG.");
  tambahLikert("X1_2", "Membeli booster pack Pokemon TCG menjadi cara saya menghibur diri dan meredakan stres.");
  tambahLikert("X1_3", "Saya menikmati interaksi dan kebersamaan dengan teman sehobi saat berbelanja booster pack Pokemon TCG.");
  tambahLikert("X1_4", "Saya senang membeli booster pack Pokemon TCG untuk dihadiahkan atau dinikmati bersama orang lain.");
  tambahLikert("X1_5", "Saya antusias mengikuti tren rilis seri dan pembaruan desain kartu Pokemon TCG.");

  // ---------- X2: Desire for Completeness ----------
  form.addPageBreakItem().setTitle("Kelengkapan koleksi").setHelpText(PETUNJUK);
  tambahLikert("X2_1", "Saya merasa tidak nyaman melihat bagian yang masih kosong dalam satu seri koleksi kartu Pokemon TCG.");
  tambahLikert("X2_2", "Saya merasa tidak tenang saat mengetahui masih ada kartu yang belum saya miliki dalam satu seri koleksi Pokemon TCG.");
  tambahLikert("X2_3", "Saya terdorong untuk terus menambah kartu demi melengkapi satu seri koleksi Pokemon TCG.");
  tambahLikert("X2_4", "Saya merasa puas ketika berhasil melengkapi satu set kartu Pokemon TCG.");
  tambahLikert("X2_5", "Semakin sedikit kartu yang belum saya miliki dalam satu seri, semakin kuat dorongan saya untuk berbelanja demi melengkapinya.");

  // ---------- X3: Speculative Motive (urutan persis Tabel 3.2) ----------
  form.addPageBreakItem().setTitle("Pertimbangan nilai kartu").setHelpText(PETUNJUK);
  tambahLikert("X3_1", "Saya membeli booster pack Pokemon TCG dengan harapan memperoleh kartu langka yang bernilai jual tinggi di masa depan.");
  tambahLikert("X3_2", "Saya menilai biaya membeli booster pack Pokemon TCG sebanding dengan potensi keuntungan dari kartu yang diperoleh di masa depan.");
  tambahLikert("X3_3", "Saya memandang kartu Pokemon TCG sebagai aset alternatif yang nilainya dapat meningkat di masa depan.");
  tambahLikert("X3_4", "Saya menilai kartu Pokemon TCG mudah dan cepat dijual kembali di pasar sekunder.");
  tambahLikert("X3_5", "Saya tertarik pada kartu Pokemon TCG bersertifikasi resmi (grading) karena berpotensi memiliki harga jual kembali yang lebih tinggi.");

  // ---------- M: Self-Control ----------
  form.addPageBreakItem().setTitle("Pengendalian diri saat berbelanja").setHelpText(PETUNJUK);
  tambahLikert("M1", "Saya mampu menolak godaan berbelanja di luar anggaran yang sudah saya rencanakan.");
  tambahLikert("M2", "Saya terbiasa mempertimbangkan konsekuensi keuangan sebelum bertransaksi.");
  tambahLikert("M3", "Saya mampu menahan dorongan untuk membeli secara spontan saat melihat barang yang menarik.");
  tambahLikert("M4", "Saya mampu menunda kesenangan berbelanja saat ini demi tujuan jangka panjang.");
  tambahLikert("M5", "Saya mampu menahan diri agar tidak mudah terpengaruh oleh suasana di toko saat berbelanja.");
  tambahLikert("M6", "Saya konsisten mematuhi batas anggaran pengeluaran yang telah saya tetapkan.");

  // ---------- Logika cabang screening ----------
  itemS1.setChoices([
    itemS1.createChoice("Ya", FormApp.PageNavigationType.CONTINUE),
    itemS1.createChoice("Tidak", pageDiskualifikasi)
  ]);
  itemS2.setChoices([
    itemS2.createChoice("Ya, 17 tahun atau lebih", FormApp.PageNavigationType.CONTINUE),
    itemS2.createChoice("Tidak, di bawah 17 tahun", pageDiskualifikasi)
  ]);
  itemS3.setChoices([
    itemS3.createChoice(S3_YA, FormApp.PageNavigationType.CONTINUE),
    itemS3.createChoice(S3_TIDAK, pageDiskualifikasi)
  ]);
  itemS4.setChoices([
    itemS4.createChoice("Dalam 6 bulan terakhir", pageProfil),
    itemS4.createChoice("Lebih dari 6 bulan sampai dengan 12 bulan terakhir", pageProfil),
    itemS4.createChoice("Lebih dari 12 bulan lalu atau belum pernah", pageDiskualifikasi)
  ]);

  Logger.log("=== FORM BARU BERHASIL DIBUAT ===");
  Logger.log("ID Form     : " + form.getId());
  Logger.log("Link Edit   : " + form.getEditUrl());
  Logger.log("Link Publik : " + form.getPublishedUrl());
}

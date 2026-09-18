/**
 * fix_gdocs_citation_links.gs
 * Layer 3 — Google Docs native relink (pendamping C-CITE-2 DOCX).
 *
 * MASALAH:
 * - DOCX memakai <w:hyperlink w:anchor="Ref_xxx"> ke bookmark Daftar Pustaka.
 *   Di Word (Ctrl+klik) 100% jalan (241 tautan full / 202 NoBab3).
 * - Saat upload + Convert ke Google Docs, konverter Google SERING membuang
 *   hyperlink internal + bookmark Word (limitasi importer, bukan bug naskah).
 *   Akibat: sitasi (Statista, 2024) jadi teks mati di Docs web.
 *   Bookmark hidden (_Ref_xxx) paling sering dibuang; visible (Ref_xxx)
 *   lebih awet tapi tetap tidak dijamin 100% oleh Google.
 *
 * SOLUSI:
 * - Jalankan fungsi relinkCitationsToDP() SEKALI di dalam Google Docs
 *   (Extensions > Apps Script) SETELAH konversi. Script membuat bookmark
 *   Docs-native di tiap entri DAFTAR PUSTAKA lalu menautkan tiap sitasi
 *   tubuh ke bookmark tersebut via '#bookmark=<id>' (klik biasa, tanpa Ctrl).
 * - Idempoten: aman dijalankan ulang (bookmark lama dibersihkan dulu).
 *
 * CARA PAKAI (2 menit):
 * 1. Upload Proposal_Arthur_PokemonTCG.docx ke Drive > Open with Google Docs.
 * 2. Di Docs hasil konversi: Extensions > Apps Script > hapus Code.gs >
 *    paste seluruh file ini > Save > Run > relinkCitationsToDP > Authorize.
 * 3. Kembali ke Docs, klik sitasi (Statista, 2024) -> lompat ke DP.
 * 4. (Opsional) Run verifyCitationLinks() untuk laporan jumlah tautan.
 */

function clearThesisBookmarks() {
  var doc = DocumentApp.getActiveDocument();
  var marks = doc.getBookmarks();
  var removed = 0;
  for (var i = 0; i < marks.length; i++) {
    try { marks[i].remove(); removed++; } catch (e) { /* abaikan */ }
  }
  return removed;
}

function parseDpEntry(text) {
  // kembalikan {surnames:[], year:"", raw:""} atau null
  if (!text) return null;
  var t = text.replace(/\s+/g, ' ').trim();
  if (t.length < 20) return null;
  var m = t.match(/^(.+?)\(\s*((?:19|20)\d{2}[a-z]?)\s*\)/);
  if (!m) return null;
  var authorPart = m[1].trim();
  var year = m[2].substring(0, 4);
  var surnames = [];
  // et al. -> ambil token pertama
  var etal = authorPart.match(/^([A-ZÀ-Ž][\w\-']+)/);
  if (/et al/i.test(authorPart)) {
    if (etal) surnames.push(etal[1]);
    return { surnames: surnames, year: year, raw: authorPart };
  }
  // pecah penulis ganda: dan/and/&/;/,
  var chunks = authorPart.split(/\s+(?:dan|and|&)\s+|;/i);
  for (var i = 0; i < chunks.length; i++) {
    var c = chunks[i].trim();
    if (!c) continue;
    // surname = sebelum koma pertama ("Aiken, L. S." -> "Aiken")
    var s = c.split(',')[0].trim();
    // korporat multi-kata tanpa koma ("Statista", "The Pokémon Company")
    if (s.indexOf(' ') > -1 && chunks.length === 1) {
      // simpan kata pertama + frasa penuh untuk pencocokan longgar
      var first = s.split(' ')[0].replace(/^The$/i, '');
      if (first) surnames.push(first);
      // simpan juga kata kunci kedua bila berarti (Pokemon, Company)
      var words = s.split(' ');
      for (var w = 0; w < words.length; w++) {
        var ww = words[w].replace(/[^A-Za-zÀ-ž]/g, '');
        if (ww.length > 3 && ww.toLowerCase() !== 'the') surnames.push(ww);
      }
    } else {
      s = s.split(' ')[0].replace(/[^A-Za-zÀ-ž\-']/g, '');
      if (s) surnames.push(s);
    }
  }
  // deduplikasi
  var seen = {};
  var out = [];
  for (var j = 0; j < surnames.length; j++) {
    var k = surnames[j].toLowerCase();
    if (k && !seen[k]) { seen[k] = 1; out.push(surnames[j]); }
  }
  if (!out.length) return null;
  return { surnames: out, year: year, raw: authorPart };
}

function relinkCitationsToDP() {
  var doc = DocumentApp.getActiveDocument();
  var body = doc.getBody();
  var paras = body.getParagraphs();

  // 1. Temukan DAFTAR PUSTAKA
  var dpIdx = -1;
  for (var i = 0; i < paras.length; i++) {
    if (paras[i].getText().trim() === 'DAFTAR PUSTAKA') { dpIdx = i; break; }
  }
  if (dpIdx < 0) {
    DocumentApp.getUi().alert('GAGAL: heading DAFTAR PUSTAKA tidak ditemukan.');
    return;
  }

  // 2. Bersihkan bookmark lama (idempoten) + petakan DP
  clearThesisBookmarks();
  var dpMap = []; // [{surnames, year, bookmarkId, para}]
  for (var d = dpIdx + 1; d < paras.length; d++) {
    var txt = paras[d].getText();
    if (!txt || txt.trim().length < 20) continue;
    var info = parseDpEntry(txt);
    if (!info) continue;
    try {
      var pos = doc.newPosition(paras[d], 0);
      var bm = doc.addBookmark(pos);
      dpMap.push({ surnames: info.surnames, year: info.year, bookmarkId: bm.getId(), raw: info.raw });
    } catch (e) { /* lewati entri gagal */ }
  }
  if (!dpMap.length) {
    DocumentApp.getUi().alert('GAGAL: 0 entri DP terparse. Periksa format DP.');
    return;
  }

  // 3. Tautkan sitasi sebelum DP
  var parenRx = /\([^()]{2,160}?,\s*(?:19|20)\d{2}[a-z]?\s*\)/g;
  var narrRx = /([A-ZÀ-Ž][\w\-']+(?:\s+(?:dan|and|&)\s+[A-ZÀ-Ž][\w\-']+)?(?:\s+et al\.?)?)\s*\(\s*((?:19|20)\d{2})[a-z]?\s*\)/g;
  var nLinked = 0, nSkip = 0;

  function bestMatch(spanText) {
    var yr = (spanText.match(/((?:19|20)\d{2})/) || [])[1];
    if (!yr) return null;
    var low = spanText.toLowerCase();
    var best = null, bestScore = 0;
    for (var k = 0; k < dpMap.length; k++) {
      if (dpMap[k].year !== yr) continue;
      var score = 0;
      for (var s = 0; s < dpMap[k].surnames.length; s++) {
        if (low.indexOf(dpMap[k].surnames[s].toLowerCase()) > -1) score++;
      }
      if (score > bestScore) { bestScore = score; best = dpMap[k]; }
    }
    return bestScore > 0 ? best : null;
  }

  for (var p = 0; p < dpIdx; p++) {
    var para = paras[p];
    var style = null;
    try { style = para.getHeading(); } catch (e) {}
    if (style === DocumentApp.ParagraphHeading.HEADING1 ||
        style === DocumentApp.ParagraphHeading.HEADING2 ||
        style === DocumentApp.ParagraphHeading.HEADING3) continue;
    var text = para.getText();
    if (!text || text.length < 10) continue;
    var spans = [];
    var m;
    parenRx.lastIndex = 0;
    while ((m = parenRx.exec(text)) !== null) spans.push({ s: m.index, e: m.index + m[0].length, txt: m[0] });
    narrRx.lastIndex = 0;
    while ((m = narrRx.exec(text)) !== null) {
      var full = m[0];
      var st = m.index, en = m.index + full.length;
      var overlap = false;
      for (var q = 0; q < spans.length; q++) {
        if (!(en <= spans[q].s || st >= spans[q].e)) { overlap = true; break; }
      }
      if (!overlap) spans.push({ s: st, e: en, txt: full });
    }
    if (!spans.length) continue;
    spans.sort(function(a, b) { return b.s - a.s; }); // kanan dulu
    var edit = para.editAsText();
    for (var z = 0; z < spans.length; z++) {
      var hit = bestMatch(spans[z].txt);
      if (!hit) { nSkip++; continue; }
      try {
        edit.setLinkUrl(spans[z].s, spans[z].e - 1, '#bookmark=' + hit.bookmarkId);
        nLinked++;
      } catch (e) { nSkip++; }
    }
  }

  DocumentApp.getUi().alert(
    'Selesai.\nDP ter-bookmark: ' + dpMap.length +
    '\nSitasi tertaut: ' + nLinked +
    '\nDilewati (tak cocok): ' + nSkip +
    '\n\nKlik sitasi (klik biasa) untuk lompat ke Daftar Pustaka.');
  Logger.log('DP=' + dpMap.length + ' linked=' + nLinked + ' skipped=' + nSkip);
}

function verifyCitationLinks() {
  var doc = DocumentApp.getActiveDocument();
  var body = doc.getBody();
  var paras = body.getParagraphs();
  var dpIdx = -1, i;
  for (i = 0; i < paras.length; i++) {
    if (paras[i].getText().trim() === 'DAFTAR PUSTAKA') { dpIdx = i; break; }
  }
  var linked = 0, total = 0;
  var rx = /\([^()]{2,160}?,\s*(?:19|20)\d{2}[a-z]?\s*\)/g;
  for (i = 0; i < (dpIdx > -1 ? dpIdx : paras.length); i++) {
    var et = paras[i].editAsText();
    var tx = paras[i].getText();
    var m;
    rx.lastIndex = 0;
    while ((m = rx.exec(tx)) !== null) {
      total++;
      try {
        var mid = Math.floor((m.index + m.index + m[0].length - 1) / 2);
        if (et.getLinkUrl(mid)) linked++;
      } catch (e) {}
    }
  }
  DocumentApp.getUi().alert('Sitasi paren total: ' + total + '\nBer-link: ' + linked + '\nTak ber-link: ' + (total - linked));
}

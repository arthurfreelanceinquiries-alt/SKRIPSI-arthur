"""Fix LibreOffice Ctrl+Click untuk Daftar Isi -> DAFTAR PUSTAKA dkk.

Akar masalah (Proposal_Arthur_PokemonTCG.docx):
1. Entri DAFTAR ISI adalah teks statis tanpa <w:hyperlink> / field TOC,
   sehingga Ctrl+Klik tidak ke mana-mana. Sedangkan entri DAFTAR TABEL /
   DAFTAR GAMBAR sudah dibungkus hyperlink Cap_* -> bisa diklik.
2. <w:bookmarkStart> disisipkan via paragraph._p.insert(0) sehingga berada
   SEBELUM <w:pPr>. Urutan ini melanggar skema OOXML (pPr wajib anak pertama
   <w:p>). Word toleran, LibreOffice ketat dan dapat mengabaikan bookmark.
3. Heading (BAB, DAFTAR PUSTAKA, DAFTAR TABEL/GAMBAR) tidak punya bookmark,
   sehingga TOC statis tidak punya target taut.

Perbaikan:
- Pindahkan setiap bookmarkStart yang sebelum pPr ke sesudah pPr.
- Tambahkan bookmark TOC_* pada setiap Heading 1/2/3 target.
- Bungkus entri Daftar Isi statis dalam <w:hyperlink anchor=TOC_*>,
  teks 100% identik, format hitam tetap.
- Idempoten: aman dijalankan ulang.
"""
import re
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = Path(r"D:\Perkuliahan\Skripsi\SKRIPSI-arthur\01_Naskah_Utama")

def _slug(text: str) -> str:
    s = re.sub(r'\W+', '_', text.strip(), flags=re.UNICODE)
    s = re.sub(r'_+', '_', s).strip('_')
    return s[:60] if s else 'SEC'

def fix_bookmark_order(doc):
    """Pindahkan bookmarkStart sebelum pPr ke sesudah pPr. Return jumlah diperbaiki."""
    fixed = 0
    for p in doc.paragraphs:
        p_el = p._p
        pPr = p_el.find(qn('w:pPr'))
        if pPr is None:
            continue
        # kumpulkan bookmarkStart yang posisinya sebelum pPr
        children = list(p_el)
        ppr_idx = children.index(pPr)
        misplaced = [c for c in children[:ppr_idx] if c.tag == qn('w:bookmarkStart')]
        for bs in misplaced:
            p_el.remove(bs)
            # sisipkan tepat sesudah pPr (dan sesudah bookmarkStart lain yg sudah benar)
            pPr = p_el.find(qn('w:pPr'))
            idx = list(p_el).index(pPr) + 1
            # lewati bookmarkStart lain agar urutan ID tetap
            while idx < len(list(p_el)) and list(p_el)[idx].tag == qn('w:bookmarkStart'):
                idx += 1
            p_el.insert(idx, bs)
            fixed += 1
    # tabel juga bisa mengandung bookmark? (umumnya tidak, tapi amankan)
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    p_el = p._p
                    pPr = p_el.find(qn('w:pPr'))
                    if pPr is None:
                        continue
                    children = list(p_el)
                    ppr_idx = children.index(pPr)
                    for bs in [c for c in children[:ppr_idx] if c.tag == qn('w:bookmarkStart')]:
                        p_el.remove(bs)
                        pPr = p_el.find(qn('w:pPr'))
                        idx = list(p_el).index(pPr) + 1
                        while idx < len(list(p_el)) and list(p_el)[idx].tag == qn('w:bookmarkStart'):
                            idx += 1
                        p_el.insert(idx, bs)
                        fixed += 1
    return fixed

def collect_existing_ids(doc):
    ids = set()
    for p in list(doc.paragraphs):
        for el in p._p.iter():
            if el.tag in (qn('w:bookmarkStart'), qn('w:bookmarkEnd')):
                ids.add(el.get(qn('w:id')))
    return ids

def ensure_heading_bookmarks(doc):
    """Tambahkan bookmark TOC_* pada Heading 1/2/3 yang belum punya. Return mapping judul->bookmark."""
    # kumpulkan nama bookmark existing
    existing_names = set()
    for p in doc.paragraphs:
        for el in p._p.iter():
            if el.tag == qn('w:bookmarkStart'):
                existing_names.add(el.get(qn('w:name')))
    # ID baru mulai dari max+1
    max_id = 0
    for p in doc.paragraphs:
        for el in p._p.iter():
            if el.tag in (qn('w:bookmarkStart'), qn('w:bookmarkEnd')):
                try:
                    max_id = max(max_id, int(el.get(qn('w:id'))))
                except (TypeError, ValueError):
                    pass
    next_id = max(max_id + 1, 5000)
    mapping = {}  # normalized title -> bookmark name
    for p in doc.paragraphs:
        try:
            st = p.style.name
        except Exception:
            st = ''
        if not st.startswith('Heading'):
            continue
        title = p.text.strip()
        if not title:
            continue
        # sudah punya bookmark langsung? pakai itu
        own = [el.get(qn('w:name')) for el in p._p.iter() if el.tag == qn('w:bookmarkStart')]
        if own:
            mapping[title] = own[0]
            mapping[title.upper()] = own[0]
            mapping[re.sub(r'\s+', ' ', title).strip()] = own[0]
            continue
        slug = _slug(title.upper())
        name = f"TOC_{slug}"
        # pastikan unik
        suffix = 1
        base = name
        while name in existing_names:
            suffix += 1
            name = f"{base}_{suffix}"
        existing_names.add(name)
        bs = OxmlElement('w:bookmarkStart')
        bs.set(qn('w:id'), str(next_id))
        bs.set(qn('w:name'), name)
        be = OxmlElement('w:bookmarkEnd')
        be.set(qn('w:id'), str(next_id))
        next_id += 1
        # sisipkan sesudah pPr (posisi valid OOXML)
        pPr = p._p.find(qn('w:pPr'))
        if pPr is not None:
            idx = list(p._p).index(pPr) + 1
            p._p.insert(idx, bs)
        else:
            p._p.insert(0, bs)
        p._p.append(be)
        mapping[title] = name
        mapping[title.upper()] = name
    return mapping

def _norm_title(s: str) -> str:
    """Normalisasi untuk pencocokan TOC->heading: sub/superskrip, spasi, case."""
    sub_map = str.maketrans({
        '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5',
        '₆': '6', '₇': '7', '₈': '8', '₉': '9', '₀': '0',
        '¹': '1', '²': '2', '³': '3', 'ᵢ': 'i',
        '−': '-', '–': '-', '—': '-',
    })
    s = s.translate(sub_map)
    s = re.sub(r'\s+', ' ', s.strip()).upper()
    # samakan varian R2 / R²
    s = s.replace('R²', 'R2')
    return s

def find_heading_for_toc(toc_title, heading_map):
    """Cocokkan judul TOC ke heading aktual (normalisasi unicode)."""
    # heading_map: judul asli -> bookmark; bangun indeks normalisasi sekali
    norm_index = {_norm_title(k): v for k, v in heading_map.items()}
    return norm_index.get(_norm_title(toc_title))

def link_static_toc(doc, heading_map):
    """Bungkus entri Daftar Isi statis (style TOC*, tanpa hyperlink/field) dalam hyperlink."""
    # Batasi hanya paragraf di antara heading DAFTAR ISI dan DAFTAR TABEL
    paras = list(doc.paragraphs)
    isi_idx = None
    tabel_idx = None
    for i, p in enumerate(paras):
        t = p.text.strip()
        try:
            st = p.style.name
        except Exception:
            st = ''
        if t == 'DAFTAR ISI' and not st.startswith(('TOC', 'Heading')):
            isi_idx = i
        if t == 'DAFTAR TABEL' and isi_idx is not None and tabel_idx is None:
            # heading DAFTAR TABEL (Heading1), bukan entri TOC
            if st.startswith('Heading'):
                tabel_idx = i
                break
    if isi_idx is None:
        print('[WARN] Heading DAFTAR ISI tidak ditemukan, lewati TOC linking.')
        return 0
    if tabel_idx is None:
        tabel_idx = len(paras)
    linked = 0
    skipped_no_target = []
    for p in paras[isi_idx + 1:tabel_idx]:
        try:
            st = p.style.name
        except Exception:
            st = ''
        if not st.lower().startswith('toc'):
            continue
        if '<w:hyperlink' in p._p.xml or 'w:fldChar' in p._p.xml:
            continue
        before = p.text
        if not before.strip():
            continue
        # Pisahkan judul vs nomor halaman (tab terakhir)
        # p.text memakai '\t' untuk tab
        if '\t' in before:
            title_part = before.rsplit('\t', 1)[0].strip()
        else:
            title_part = before.strip()
        target = find_heading_for_toc(title_part, heading_map)
        if target is None:
            skipped_no_target.append(title_part)
            continue
        # Bungkus semua <w:r> langsung dalam hyperlink (pertahankan urutan + tab)
        runs = [r for r in list(p._p) if r.tag == qn('w:r')]
        if not runs:
            continue
        h = OxmlElement('w:hyperlink')
        h.set(qn('w:anchor'), target)
        h.set(qn('w:history'), '1')
        idx0 = list(p._p).index(runs[0])
        for r in runs:
            h.append(r)  # memindahkan (bukan copy) -> teks tetap
        p._p.insert(idx0, h)
        # Invarian: teks tidak berubah
        assert p.text == before, f'Teks berubah: {before!r} -> {p.text!r}'
        linked += 1
    if skipped_no_target:
        print(f'[WARN] {len(skipped_no_target)} entri TOC tanpa target heading (dibiarkan statis):')
        for t in skipped_no_target[:10]:
            print(f'   - {t!r}')
    return linked

def verify_no_orphans(doc):
    anchors = set()
    names = set()
    for p in list(doc.paragraphs):
        for el in p._p.iter():
            if el.tag == qn('w:hyperlink') and el.get(qn('w:anchor')):
                anchors.add(el.get(qn('w:anchor')))
            if el.tag == qn('w:bookmarkStart'):
                names.add(el.get(qn('w:name')))
    # tabel
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for el in p._p.iter():
                        if el.tag == qn('w:hyperlink') and el.get(qn('w:anchor')):
                            anchors.add(el.get(qn('w:anchor')))
                        if el.tag == qn('w:bookmarkStart'):
                            names.add(el.get(qn('w:name')))
    orphans = [a for a in anchors if a not in names]
    return anchors, names, orphans

def process(path: Path, out_suffix='_FIXED_LIBRE'):
    print(f'[*] Memproses {path.name} ...')
    doc = Document(str(path))
    # snapshot teks
    before_texts = [p.text for p in doc.paragraphs]
    n_fix = fix_bookmark_order(doc)
    print(f'    bookmarkStart dipindah ke sesudah pPr: {n_fix}')
    hmap = ensure_heading_bookmarks(doc)
    print(f'    heading ter-bookmark: {len(set(hmap.values()))}')
    n_link = link_static_toc(doc, hmap)
    print(f'    entri Daftar Isi terhubung: {n_link}')
    after_texts = [p.text for p in doc.paragraphs]
    assert before_texts == after_texts, 'TEKS BERUBAH! Batalkan.'
    print('    teks paragraf identik 100% (pre/post snapshot).')
    anchors, names, orphans = verify_no_orphans(doc)
    print(f'    hyperlink anchor unik: {len(anchors)}, bookmark unik: {len(names)}, orphan: {len(orphans)}')
    if orphans:
        print(f'    [FAIL] orphan anchors: {orphans[:10]}')
        raise SystemExit(1)
    out = path.with_name(path.stem + out_suffix + path.suffix)
    doc.save(str(out))
    print(f'    [OK] tersimpan: {out}')
    return out

if __name__ == '__main__':
    import sys
    targets = sys.argv[1:] or [str(BASE / 'Proposal_Arthur_PokemonTCG.docx')]
    for t in targets:
        process(Path(t))

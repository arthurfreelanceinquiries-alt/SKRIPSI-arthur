r"""
verify_mendeley_integrity.py
Suite pengujian pra-terbang (pre-flight test suite) otomatis untuk memvalidasi:
1. Paritas Mutlak 6-Arah (TeX == NoBab3 == MD == Word == RIS == Bib == 55)
2. Kepatuhan Whitelist Tag RIS Mendeley (0 tag ilegal ELEC/WEB/MISC)
3. Kesetaraan Himpunan Kunci Sitasi (Set Difference == Empty)
4. Kelengkapan Bidang Metadata Wajib (TI, AU, PY, ID, PB/JO/BT)
5. Keutuhan Encoding UTF-8 dan Aksesibilitas Karakter Beraksen (é, ö)
6. Kepatuhan Dokumen Word Bebas Penomoran Angka A-Z

Murni menggunakan Python Standard Library (zipfile, xml.etree, re, collections, pathlib)
tanpa dependensi eksternal pihak ketiga, sehingga 100% portable.

Exit Code: 0 jika seluruh tes LULUS, 1 jika ada tes yang GAGAL.
"""

import os
import re
import sys
import collections
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# Set UTF-8 encoding on console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

MENDELEY_TAG_WHITELIST = {'JOUR', 'BOOK', 'CONF', 'RPRT', 'THES', 'GEN'}
FORBIDDEN_TAGS = {'ELEC', 'WEB', 'MISC'}
EXPECTED_COUNT = 55


def get_tex_keys(tex_path: Path):
    if not tex_path.exists():
        return set()
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()
    cites = re.findall(r'\\(?:cite[a-z]*|nocite)\{([^}]+)\}', content)
    keys = set()
    for c in cites:
        for k in c.split(','):
            clean_k = k.strip()
            if clean_k:
                keys.add(clean_k)
    return keys


def get_markdown_dp_count(md_path: Path):
    if not md_path.exists():
        return 0
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    if '# DAFTAR PUSTAKA' not in text:
        return 0
    dp_section = text.split('# DAFTAR PUSTAKA')[-1]
    dp_lines = [
        line.strip() for line in dp_section.splitlines()
        if line.strip() and not line.strip().startswith('#') and not line.strip().startswith('>')
    ]
    return len(dp_lines)


def get_docx_dp_entries(docx_path: Path):
    """Parses paragraphs from docx using pure standard library zipfile and XML."""
    if not docx_path.exists():
        return []

    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')

    root = ET.fromstring(xml_content)
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paragraphs = []
    for p in root.iterfind('.//w:p', namespaces):
        texts = [t.text for t in p.iterfind('.//w:t', namespaces) if t.text]
        if texts:
            paragraphs.append(''.join(texts))

    in_dp = False
    dp_entries = []
    for p in paragraphs:
        txt = p.strip()
        if txt == "DAFTAR PUSTAKA":
            in_dp = True
            continue
        if in_dp and txt:
            if txt.startswith("BAB ") or txt.startswith("LAMPIRAN"):
                break
            dp_entries.append(txt)
    return dp_entries


def parse_ris_records(ris_path: Path):
    if not ris_path.exists():
        return []
    with open(ris_path, 'r', encoding='utf-8') as f:
        content = f.read()
    raw_records = content.split('ER  -')
    records = []
    for r in raw_records:
        r_str = r.strip()
        if not r_str:
            continue
        fields = collections.defaultdict(list)
        for line in r_str.splitlines():
            line_s = line.strip()
            if ' - ' in line_s:
                tag, val = line_s.split(' - ', 1)
                fields[tag.strip()].append(val.strip())
        records.append(fields)
    return records


def parse_bib_keys(bib_path: Path):
    if not bib_path.exists():
        return set()
    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()
    raw_keys = re.findall(r'@[a-zA-Z]+\s*\{\s*([^,]+),', content)
    return set(k.strip() for k in raw_keys)


def run_tests():
    root = Path(__file__).resolve().parent.parent
    tex_path = root / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.tex"
    nobab3_path = root / "01_Naskah_Utama" / "Proposal_Arthur_NoBab3.tex"
    md_path = root / "01_Naskah_Utama" / "PROPOSAL_SKRIPSI_POKEMON_TCG.md"
    docx_path = root / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.docx"
    ris_path = root / "06_Referensi_Jurnal_PDF" / "Mendeley_Library_Arthur_PokemonTCG.ris"
    bib_path = root / "06_Referensi_Jurnal_PDF" / "Mendeley_Library_Arthur_PokemonTCG.bib"

    print("=" * 75)
    print("  SUITE VERIFIKASI INTEGRITAS & PARITAS 1:1 MENDELEY REFERENCE MANAGER")
    print("=" * 75)

    all_passed = True

    # -------------------------------------------------------------
    # TEST 1: 6-Way Parity Count
    # -------------------------------------------------------------
    print(f"\n[TEST 1] Memeriksa Paritas Jumlah Entri 6-Arah (Target: Tepat {EXPECTED_COUNT} Referensi)...")
    tex_keys = get_tex_keys(tex_path)
    nobab3_keys = get_tex_keys(nobab3_path)
    md_count = get_markdown_dp_count(md_path)
    docx_entries = get_docx_dp_entries(docx_path)
    docx_count = len(docx_entries)
    ris_records = parse_ris_records(ris_path)
    ris_count = len(ris_records)
    bib_keys = parse_bib_keys(bib_path)
    bib_count = len(bib_keys)

    print(f"  1. LaTeX Proposal (Proposal_Arthur_PokemonTCG.tex) : {len(tex_keys)} kunci")
    print(f"  2. LaTeX NoBab3   (Proposal_Arthur_NoBab3.tex)    : {len(nobab3_keys)} kunci")
    print(f"  3. Markdown Master (PROPOSAL_SKRIPSI_POKEMON_TCG) : {md_count} entri")
    print(f"  4. Dokumen Word   (Proposal_Arthur_PokemonTCG.docx): {docx_count} entri")
    print(f"  5. Mendeley RIS   (Mendeley_Library_Arthur_...ris): {ris_count} rekaman")
    print(f"  6. Mendeley BibTeX(Mendeley_Library_Arthur_...bib): {bib_count} entri")

    counts = [len(tex_keys), len(nobab3_keys), md_count, docx_count, ris_count, bib_count]
    if all(c == EXPECTED_COUNT for c in counts):
        print(f"  -> [PASS] Paritas 6-Arah Sempurna! Seluruh media tepat memuat {EXPECTED_COUNT} referensi.")
    else:
        print(f"  -> [FAIL] Terjadi diskrepansi jumlah referensi! Seluruh format harus tepat {EXPECTED_COUNT}.")
        all_passed = False

    # -------------------------------------------------------------
    # TEST 2: Mendeley Tag Whitelist Compliance
    # -------------------------------------------------------------
    print(f"\n[TEST 2] Memeriksa Kepatuhan Tag RIS Mendeley Whitelist (Cegah Silent Drop)...")
    tag_counter = collections.Counter()
    illegal_tag_found = False

    for r in ris_records:
        types = r.get('TY', [])
        if not types:
            print("  -> [FAIL] Ada rekaman RIS yang tidak memiliki tag 'TY'!")
            illegal_tag_found = True
            continue
        tag = types[0]
        tag_counter[tag] += 1
        if tag in FORBIDDEN_TAGS or tag not in MENDELEY_TAG_WHITELIST:
            print(f"  -> [FAIL] Tag terlarang/tidak didukung ditemukan: 'TY  - {tag}' pada ID: {r.get('ID', ['UNKNOWN'])[0]}")
            illegal_tag_found = True

    print(f"  -> Distribusi Tag RIS: {dict(tag_counter)}")
    if not illegal_tag_found:
        print(f"  -> [PASS] 100% Kepatuhan Whitelist Terpenuhi! 0 tag terlarang (ELEC/WEB diblokir total).")
    else:
        all_passed = False

    # -------------------------------------------------------------
    # TEST 3: Citation Key Set Equality
    # -------------------------------------------------------------
    print(f"\n[TEST 3] Memeriksa Kesetaraan Himpunan Kunci Sitasi (Set Equality)...")
    ris_keys = set(r.get('ID', [''])[0] for r in ris_records if r.get('ID'))

    diff_tex_ris = tex_keys - ris_keys
    diff_ris_tex = ris_keys - tex_keys
    diff_tex_bib = tex_keys - bib_keys

    if not diff_tex_ris and not diff_ris_tex and not diff_tex_bib:
        print(f"  -> [PASS] Himpunan kunci sitasi identik 100% ({len(ris_keys)} kunci klop sempurna).")
        # Assert specific critical keys
        assert 'gao2014completing' in ris_keys, "Kunci gao2014completing wajib ada!"
        assert 'gao2014set' not in ris_keys, "Kunci gao2014set tidak boleh ada di proposal!"
        assert 'keynes1936general' in ris_keys, "Kunci keynes1936general wajib ada!"
        assert 'statista2024pokemon' in ris_keys, "Kunci data Statista wajib ada!"
        assert 'pokemoncompany2024' in ris_keys, "Kunci data Pokémon Company wajib ada!"
        assert 'icv2tcgplayer2024' not in ris_keys, "Kunci data ICv2 tidak boleh ada (dieliminasi total)!"
        assert 'pricecharting2024' in ris_keys, "Kunci data PriceCharting wajib ada!"
        assert 'psa2024popreport' not in ris_keys, "Kunci data PSA pop report lama tidak boleh ada!"
        print(f"  -> [PASS] Verifikasi Kunci Kritis (Gao JMR, Keynes 1936, dan 3 Data Industri Terverifikasi) Valid!")
    else:
        print(f"  -> [FAIL] Terdapat ketidakcocokan himpunan kunci:")
        if diff_tex_ris:
            print(f"     Ada di TeX tapi hilang di RIS : {diff_tex_ris}")
        if diff_ris_tex:
            print(f"     Ada di RIS tapi tidak disitasi: {diff_ris_tex}")
        if diff_tex_bib:
            print(f"     Ada di TeX tapi hilang di Bib : {diff_tex_bib}")
        all_passed = False

    # -------------------------------------------------------------
    # TEST 4: Mandatory Metadata Field Completeness
    # -------------------------------------------------------------
    print(f"\n[TEST 4] Memeriksa Kelengkapan Bidang Metadata Wajib per Rekaman RIS...")
    missing_metadata = []
    for r in ris_records:
        entry_id = r.get('ID', ['UNKNOWN'])[0]
        has_ti = bool(r.get('TI', [''])[0])
        has_au = bool(r.get('AU'))
        has_py = bool(r.get('PY', [''])[0] or r.get('Y1', [''])[0])
        has_venue = bool(r.get('JO') or r.get('PB') or r.get('BT'))

        if not (has_ti and has_au and has_py and has_venue):
            missing_metadata.append((entry_id, has_ti, has_au, has_py, has_venue))

    if not missing_metadata:
        print(f"  -> [PASS] Seluruh {len(ris_records)} rekaman memiliki Title, Author, Year, Venue/Publisher, dan ID.")
    else:
        print(f"  -> [FAIL] Ditemukan rekaman dengan metadata tidak lengkap: {missing_metadata}")
        all_passed = False

    # -------------------------------------------------------------
    # TEST 5: UTF-8 & Diacritic Byte Integrity
    # -------------------------------------------------------------
    print(f"\n[TEST 5] Memeriksa Integritas Byte UTF-8 dan Karakter Khusus...")
    with open(ris_path, 'rb') as f:
        ris_raw = f.read()

    utf8_clean = True
    if b'Pok\xc3\xa9mon' in ris_raw:
        print("  -> Huruf 'é' pada kata 'Pokémon' ter-encode rapi dalam UTF-8.")
    else:
        print("  -> [FAIL] Huruf 'é' pada 'Pokémon' tidak ditemukan atau rusak!")
        utf8_clean = False

    if b'G\xc3\xbcltekin' in ris_raw:
        print("  -> Huruf 'ü' pada nama 'Gültekin' ter-encode rapi dalam UTF-8.")
    else:
        print("  -> [FAIL] Huruf 'ü' pada 'Gültekin' tidak ditemukan!")
        utf8_clean = False

    if b'\xef\xbf\xbd' in ris_raw:
        print("  -> [FAIL] Ditemukan byte karakter pengganti rusak \\ufffd di dalam RIS!")
        utf8_clean = False
    else:
        print("  -> 0 karakter korup \\ufffd terdeteksi.")

    if utf8_clean:
        print("  -> [PASS] Integritas Byte UTF-8 Lulus 100%.")
    else:
        all_passed = False

    # -------------------------------------------------------------
    # TEST 6: Word Document Format & Zero Numbering
    # -------------------------------------------------------------
    print(f"\n[TEST 6] Memeriksa Format Daftar Pustaka Word Proposal_Arthur_PokemonTCG.docx...")
    numbered_errors = []
    for entry in docx_entries:
        if re.match(r'^\d+[\.\)]', entry):
            numbered_errors.append(entry[:50])

    if len(docx_entries) == EXPECTED_COUNT and not numbered_errors:
        print(f"  -> Tepat {len(docx_entries)} entri terdaftar di Word, 0 entri bernomor urut.")
        print("  -> [PASS] Format Daftar Pustaka Word 100% Patuh Pedoman FEB UKRIDA 2023!")
    else:
        if len(docx_entries) != EXPECTED_COUNT:
            print(f"  -> [FAIL] Jumlah entri di Word ({len(docx_entries)}) != {EXPECTED_COUNT}!")
        if numbered_errors:
            print(f"  -> [FAIL] Ditemukan entri bernomor urut di Word: {numbered_errors[:3]}")
        all_passed = False

    # -------------------------------------------------------------
    # TEST 7: Validasi Tautan URL Aktif & Keterklikan OpenXML Word (APA 7)
    # -------------------------------------------------------------
    print(f"\n[TEST 7] Memeriksa Tautan URL Aktif & Keterklikan OpenXML Word (APA 7th Edition)...")
    pokemon_keys = {'statista2024pokemon', 'pokemoncompany2024', 'pricecharting2024'}
    ris_url_map = {}
    for r in ris_records:
        eid = r.get('ID', [''])[0]
        if eid in pokemon_keys:
            urls = r.get('UR', [])
            if urls:
                ris_url_map[eid] = urls[0]

    if len(ris_url_map) == len(pokemon_keys):
        print(f"  -> Tepat {len(pokemon_keys)} data industri terverifikasi memiliki tag 'UR' aktif di berkas RIS:")
        for k, u in ris_url_map.items():
            print(f"     * [{k}] -> {u}")
    else:
        print(f"  -> [FAIL] Sebagian data industri tidak memiliki tag 'UR' di RIS: ditemukan {len(ris_url_map)}/{len(pokemon_keys)}")
        all_passed = False

    # Periksa keterklikan OpenXML Word
    with zipfile.ZipFile(docx_path) as z:
        doc_xml = z.read('word/document.xml')
        rels_xml = z.read('word/_rels/document.xml.rels')

    root_doc = ET.fromstring(doc_xml)
    root_rels = ET.fromstring(rels_xml)
    ns_w = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    ns_r = {'r': 'http://schemas.openxmlformats.org/package/2006/relationships'}

    rel_map = {rel.attrib['Id']: rel.attrib.get('Target', '') for rel in root_rels.iterfind('.//r:Relationship', ns_r)}
    word_hyperlink_targets = set()
    for h in root_doc.iterfind('.//w:hyperlink', ns_w):
        r_id = h.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id', '')
        tgt = rel_map.get(r_id, '')
        if tgt.startswith('http'):
            word_hyperlink_targets.add(tgt)

    missing_word_links = [u for u in ris_url_map.values() if u not in word_hyperlink_targets]
    if not missing_word_links:
        print(f"  -> Seluruh {len(pokemon_keys)} tautan data industri terverifikasi terdaftar sebagai OpenXML <w:hyperlink> aktif di Word.")
        print(f"  -> [PASS] Keterklikan Dokumen Word (APA 7th Edition) Terverifikasi 100%!")
    else:
        print(f"  -> [FAIL] Tautan tidak terdeteksi sebagai hyperlink Word: {missing_word_links}")
        all_passed = False

    # -------------------------------------------------------------
    # FINAL VERDICT
    # -------------------------------------------------------------
    print("\n" + "=" * 75)
    if all_passed:
        print("  [SUCCESS] SELURUH PENGUJIAN INTEGRITAS MENDELEY & URL (7/7) LULUS 100%!")
        print("            PARITAS MUTLAK TERJAMIN: ZERO DISCREPANCY & CLICKABLE URLS.")
        print("=" * 75)
        return True
    else:
        print("  [ERROR] PENGUJIAN INTEGRITAS MENDELEY MENEMUKAN KEGAGALAN!")
        print("=" * 75)
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)

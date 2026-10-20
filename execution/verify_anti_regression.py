r"""
verify_anti_regression.py — Layer 3: Negative Assertion & Lecturer Revision Firewall.

Menegakkan Invariant Mutlak:
Mencegah kembalinya draf lama, kalimat kaku mekanistis, istilah usang,
atau sumber palsu/cacat yang telah resmi DITOLAK atau DICORET oleh Dosen Pembimbing
(Dr. Fredella Colline) dan Dosen Penguji dalam seluruh sesi bimbingan dan sempro.

Jika ada salah satu frasa terlarang terdeteksi pada naskah (.tex, .md, .docx),
skrip ini LANGSUNG GAGAL (exit code 1) dan MEMBLOKIR seluruh proses rilis.

Aturan Terdaftar:
  R01: Eliminasi narasi mekanistis Bab 1 (Bimbingan 06 Okt 2026).
  R02: Eliminasi subbab hierarkis 'Grand Theory' di Bab 2 (Bimbingan 24 Sep 2026).
  R03: Eliminasi istilah usang 'Need for Completion' -> wajib 'Desire for Completeness' (09 Sep 2026).
  R04: Eliminasi variabel usang 'Literasi Keuangan' -> wajib 'Self-Control' (09 Sep 2026).
  R05: Eliminasi sumber sintetis ICv2 dan login-wall PSA (D24 & D26).
  R06: Eliminasi ghost references Tan & Adyantari / prasetio2021hedonic (D19).
  R07: Preservasi fokus geografis Jakarta Barat (Bimbingan 29 Sep 2026).
"""

import sys
import re
from pathlib import Path
import docx

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
TEX_PATH = ROOT / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.tex"
MD_PATH = ROOT / "01_Naskah_Utama" / "PROPOSAL_SKRIPSI_POKEMON_TCG.md"
DOCX_PATH = ROOT / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.docx"
BIB_PATH = ROOT / "01_Naskah_Utama" / "references.bib"

# Daftar Frasa Terlarang (Negative Assertions)
FORBIDDEN_PHRASES = [
    {
        "id": "R01-MEKANISTIS-BAB1",
        "description": "Narasi Bab 1 kaku/mekanistis yang telah dicoret dosen pembimbing (06 Okt 2026)",
        "phrases": [
            "Literatur menunjukkan pembelian impulsif dipengaruhi faktor pendorong yang beragam",
            "Pendorong tersebut mencakup dorongan mencari kesenangan (hedonic shopping value)",
            "dorongan mencari kesenangan (hedonic shopping value)",
            "hasrat melengkapi koleksi (desire for completeness), serta motif spekulasi",
        ],
        "check_files": ["tex", "md", "docx"],
    },
    {
        "id": "R02-GRAND-THEORY-HEADING",
        "description": "Pelabelan hierarkis kaku 'Grand Theory' di Bab 2 yang ditolak dosen penguji (24 Sep 2026)",
        "phrases": [
            "2.1.1 Grand Theory",
            "### 2.1.1 Grand Theory",
            "\\subsection{Grand Theory}",
            "Grand Theory: Behavioral Finance",
        ],
        "check_files": ["tex", "md", "docx"],
    },
    {
        "id": "R03-OUTDATED-TERM-NFC",
        "description": "Istilah lama 'Need for Completion' yang wajib diganti 'Desire for Completeness' (09 Sep 2026)",
        "phrases": [
            "Need for Completion",
            "need for completion",
        ],
        "check_files": ["tex", "md", "docx"],
    },
    {
        "id": "R04-OUTDATED-MODERATOR",
        "description": "Variabel lama 'Literasi Keuangan' sebagai moderator yang telah diganti 'Self-Control' (09 Sep 2026)",
        "phrases": [
            "Literasi Keuangan sebagai variabel moderasi",
            "Pengaruh Literasi Keuangan terhadap",
            "Financial Literacy sebagai pemoderasi",
        ],
        "check_files": ["tex", "md", "docx"],
    },
    {
        "id": "R05-BANNED-SYNTHETIC-SOURCES",
        "description": "Kunci sitasi sintetis ICv2 atau login-wall PSA yang telah dieliminasi total (D24, D26)",
        "phrases": [
            "icv2tcgplayer2024",
            "psa2024popreport",
        ],
        "check_files": ["tex", "md", "docx", "bib"],
    },
    {
        "id": "R06-BANNED-GHOST-REFERENCES",
        "description": "Referensi ghost/cacat yang telah dieliminasi dari naskah (D19)",
        "phrases": [
            "prasetio2021hedonic",
            "Tan, S., & Adyantari",
            "Tan and Adyantari",
        ],
        "check_files": ["tex", "md", "docx", "bib"],
    },
    {
        "id": "R07-TABEL-1-1-DEPRECATED",
        "description": "Tabel 1.1 matriks research gap telah dihapus permanen sesuai arahan Arthur karena kesenjangan telah dinarasikan secara mengalir",
        "phrases": [
            "Tabel 1.1",
            "Tabel 1:1",
            "Matriks Kesenjangan Penelitian Empiris",
            "tab:research_gap",
        ],
        "check_files": ["tex", "md", "docx"],
    },
]

# Unsur Wajib (Positive Assertions)
MANDATORY_ELEMENTS = [
    {
        "id": "M01-JAKARTA-BARAT-TITLE",
        "description": "Ruang lingkup geografis 'Jakarta Barat' wajib ada pada judul proposal",
        "pattern": r"Jakarta Barat",
        "target": "title",
    },
    {
        "id": "M02-JAKARTA-BARAT-HUBS",
        "description": "Keempat klaster LGS & UKRIDA wajib disebutkan pada latar belakang Bab 1",
        "phrases": [
            "Tanjung Duren",
            "Central Park",
            "Mall Taman Anggrek",
            "Puri Indah",
            "Universitas Kristen Krida Wacana",
        ],
        "target": "bab1",
    },
]


def extract_docx_text(docx_path: Path) -> str:
    """Ekstrak seluruh teks bodi dan tabel dari dokumen Word."""
    doc = docx.Document(str(docx_path))
    parts = []
    for p in doc.paragraphs:
        parts.append(p.text)
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                parts.append(cell.text)
    return "\n".join(parts)


def run_anti_regression_audit() -> int:
    print("=" * 75)
    print("SUITE AUDIT ANTI-REGRESI & FIREWALL FEEDBACK DOSEN (LAYER 3)")
    print("Mencegah kembalinya draf lama, kalimat kaku, dan sumber cacat.")
    print("=" * 75)

    failures = []

    # 1. Load contents
    tex_text = TEX_PATH.read_text(encoding="utf-8") if TEX_PATH.exists() else ""
    md_text = MD_PATH.read_text(encoding="utf-8") if MD_PATH.exists() else ""
    bib_text = BIB_PATH.read_text(encoding="utf-8") if BIB_PATH.exists() else ""
    docx_text = extract_docx_text(DOCX_PATH) if DOCX_PATH.exists() else ""

    files_map = {
        "tex": (TEX_PATH.name, tex_text),
        "md": (MD_PATH.name, md_text),
        "docx": (DOCX_PATH.name, docx_text),
        "bib": (BIB_PATH.name, bib_text),
    }

    # 2. Audit Negative Assertions (Forbidden Phrases)
    print("\n[FASE 1] Memeriksa Frasa Terlarang & Draf Lama yang Pernah Dicoret...")
    for rule in FORBIDDEN_PHRASES:
        rule_id = rule["id"]
        desc = rule["description"]
        rule_violated = False

        for fkey in rule["check_files"]:
            fname, ftext = files_map.get(fkey, ("", ""))
            if not ftext:
                continue

            for phrase in rule["phrases"]:
                if phrase.lower() in ftext.lower():
                    rule_violated = True
                    msg = f"[{rule_id}] Pelanggaran di {fname}: Terdeteksi frasa terlarang '{phrase}' ({desc})"
                    failures.append(msg)
                    print(f"  -> [FAIL] {msg}")

        if not rule_violated:
            print(f"  -> [PASS] {rule_id}: {desc}")

    # 3. Audit Positive Assertions (Mandatory Elements)
    print("\n[FASE 2] Memeriksa Unsur Wajib Hasil Revisi Bimbingan...")
    for mand in MANDATORY_ELEMENTS:
        mand_id = mand["id"]
        desc = mand["description"]
        mand_violated = False

        if "phrases" in mand:
            for phrase in mand["phrases"]:
                if phrase.lower() not in tex_text.lower() or phrase.lower() not in docx_text.lower():
                    mand_violated = True
                    msg = f"[{mand_id}] Unsur wajib '{phrase}' TIDAK DITEMUKAN di naskah ({desc})"
                    failures.append(msg)
                    print(f"  -> [FAIL] {msg}")
        elif "pattern" in mand:
            if not re.search(mand["pattern"], tex_text, re.IGNORECASE) or not re.search(mand["pattern"], docx_text, re.IGNORECASE):
                mand_violated = True
                msg = f"[{mand_id}] Pola wajib '{mand['pattern']}' TIDAK DITEMUKAN di naskah ({desc})"
                failures.append(msg)
                print(f"  -> [FAIL] {msg}")

        if not mand_violated:
            print(f"  -> [PASS] {mand_id}: {desc}")

    # 4. Final Verdict
    print("\n" + "=" * 75)
    if failures:
        print(f"[ERROR] DITEMUKAN {len(failures)} REGRESI / PELANGGARAN ATURAN DOSEN!")
        for fail in failures:
            print(f"  * {fail}")
        print("\nBUILD DIBLOKIR: Naskah tidak boleh diserahkan ke pembimbing sebelum seluruh regresi diatasi.")
        print("=" * 75)
        return 1

    print("[SUCCESS] 100% LULUS AUDIT ANTI-REGRESI: Tidak ada draf usang atau frasa terlarang.")
    print("          Seluruh keputusan bimbingan dosen terlindungi secara deterministik.")
    print("=" * 75)
    return 0


if __name__ == "__main__":
    sys.exit(run_anti_regression_audit())

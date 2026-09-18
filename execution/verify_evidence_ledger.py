r"""
verify_evidence_ledger.py — Layer 3: menegakkan D26 Tier Wajib + Web.

Memeriksa, berbasis EVIDENCE_LEDGER_HALAMAN.md (Section A):
1. Setiap berkas PDF ledger ada, biner valid (%PDF), dan jumlah halaman
   aktual >= halaman maksimum yang disitasi (anti salah-nomor halaman).
2. Setiap klaim Lxx memiliki halaman (format "PDF pN") — bukan janji kosong.
3. Tier Web: 3 snapshot industri ada dan Statista/Pokémon Co berisi judul
   halaman yang benar (PriceCharting boleh terhalang-bot/403 + live-check).

Stdlib + PyMuPDF bila tersedia (fallback: cek header biner saja).
Exit 0 = PASS; 1 = FAIL (BUILD BROKEN untuk paket sempro).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "04_Riset_&_Metodologi" / "EVIDENCE_LEDGER_HALAMAN.md"
JURNAL = ROOT / "06_Referensi_Jurnal_PDF"
SNAP = JURNAL / "snapshots"

try:
    import fitz  # PyMuPDF (opsional)
except ImportError:
    fitz = None


def pdf_pages(path: Path):
    with open(path, "rb") as f:
        head = f.read(5)
    if head != b"%PDF-":
        return 0
    if fitz is None:
        return -1
    try:
        return fitz.open(str(path)).page_count
    except Exception:
        return 0


def main():
    fails = []
    text = LEDGER.read_text(encoding="utf-8")
    sec_a = text.split("## A.")[1].split("## B.")[0]
    rows = [l for l in sec_a.splitlines() if l.startswith("| L")]
    print(f"[*] Baris klaim ledger: {len(rows)}")
    if len(rows) < 15:
        fails.append(f"baris klaim {len(rows)} < 15 (ledger tak lengkap)")

    by_file = {}
    for r in rows:
        m = re.search(r"`((?:01_Empiris|02_Jurnal)[^`]+)`\s*\((\d+)pp\)", r)
        if not m:
            fails.append(f"baris tanpa berkas terparse: {r[:60]}")
            continue
        rel, declared = m.group(1), int(m.group(2))
        pages = sorted({int(x) for x in re.findall(r"PDF p(\d+)", r)})
        if not pages:
            fails.append(f"baris tanpa halaman: {r[:60]}")
            continue
        by_file.setdefault(rel, {"declared": declared, "cited": set()})
        by_file[rel]["cited"].update(pages)

    for rel, info in sorted(by_file.items()):
        p = JURNAL / rel
        if not p.exists():
            fails.append(f"HILANG: {rel}")
            continue
        n = pdf_pages(p)
        if n == 0:
            fails.append(f"BUKAN-PDF: {rel}")
        elif n == -1:
            print(f"  [WARN] {rel}: fitz tak ada, cek biner saja")
        else:
            need = max(info["cited"])
            flag = "OK " if (n == info["declared"] and n >= need) else "FAIL"
            print(f"  [{flag}] {Path(rel).name}: {n}pp (ledger {info['declared']}pp, maks sitasi p{need})")
            if n != info["declared"] or n < need:
                fails.append(f"HALAMAN: {rel} aktual {n}pp vs ledger {info['declared']}pp/sitasi p{need}")

    snaps = {
        "statista_24277_": "Statista",
        "pokemon_co_figures_": "Pok",
        "pricecharting_shining_fates_": "Just a moment",
    }
    for prefix, needle in snaps.items():
        hits = sorted(SNAP.glob(prefix + "*"))
        if not hits:
            fails.append(f"SNAPSHOT HILANG: {prefix}*")
            continue
        body = hits[-1].read_text(encoding="utf-8", errors="replace")
        ok = (needle in body) or ("pricecharting" in prefix and len(body) > 1000)
        print(f"  [{'OK ' if ok else 'FAIL'}] snapshot {hits[-1].name} ({len(body)//1024} KB)")
        if not ok:
            fails.append(f"SNAPSHOT isi salah: {hits[-1].name}")

    print("=" * 70)
    if fails:
        print(f"[FAIL] {len(fails)} temuan:")
        for f in fails:
            print("  -", f)
        return 1
    print("[PASS] Ledger halaman + snapshot Tier Web konsisten 100%.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

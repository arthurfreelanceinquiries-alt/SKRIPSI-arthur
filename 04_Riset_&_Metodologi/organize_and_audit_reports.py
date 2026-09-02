import os
import re
import shutil
import zipfile
import logging
from pathlib import Path

# Silence pypdf logging
logging.getLogger("pypdf").setLevel(logging.ERROR)
import pypdf

BASE_DIR = Path(r"z:\Skripsi\04_Riset_&_Metodologi")
DROPZONE_DIR = BASE_DIR / "00_DROPZONE_LAPORAN"
REPORTS_DIR = BASE_DIR / "Laporan_Keuangan_Resmi"
INVENTORY_FILE = REPORTS_DIR / "STATUS_INVENTARIS_LAPORAN.md"

BANKS = ["BBRI", "BMRI", "BBCA", "BBNI"]
YEARS = [2021, 2022, 2023, 2024, 2025]
QUARTERS = ["Q1", "Q2", "Q3", "Q4"]

BANK_KEYWORDS = {
    "BBRI": ["BANK RAKYAT INDONESIA", "BBRI", "BRI", "PT BANK RAKYAT INDONESIA"],
    "BMRI": ["BANK MANDIRI", "BMRI", "MANDIRI", "PT BANK MANDIRI"],
    "BBCA": ["BANK CENTRAL ASIA", "BBCA", "BCA", "PT BANK CENTRAL ASIA"],
    "BBNI": ["BANK NEGARA INDONESIA", "BBNI", "BNI", "PT BANK NEGARA INDONESIA"]
}

def extract_pdf_snippet(pdf_path: Path):
    try:
        reader = pypdf.PdfReader(str(pdf_path), strict=False)
        text = ""
        for p in reader.pages[:4]:
            t = p.extract_text() or ""
            text += t + " "
        return " ".join(text.split()).upper()
    except Exception as e:
        return ""

def identify_bank(filename: str, snippet: str):
    combined = f"{filename.upper()} {snippet}"
    for bank, kws in BANK_KEYWORDS.items():
        for kw in kws:
            if kw in combined:
                return bank
    return None

def identify_year(filename: str, snippet: str):
    # Search in filename first
    for y in reversed(YEARS):
        if str(y) in filename:
            return y
            
    # Search in text snippet
    for y in reversed(YEARS):
        if str(y) in snippet:
            return y
            
    # Check YY format like 1221, 1222, 1223, 1224, 1225
    m = re.search(r'12(2[1-5])', filename)
    if m:
        return 2000 + int(m.group(1))
        
    return None

def identify_type_and_period(filename: str, snippet: str):
    combined = f"{filename.upper()} {snippet}"
    
    # Check Sustainability Report
    sr_keywords = ["SUSTAINABILITY REPORT", "LAPORAN KEBERLANJUTAN", "SUSTAINABILITY", "KEBERLANJUTAN"]
    for kw in sr_keywords:
        if kw in combined:
            return "SR", None
            
    # Quarters
    if any(k in combined for k in ["Q1", "TW1", "TW 1", "TRIWULAN 1", "TRIWULAN I", "31 MARET", "31 MAR", "MARCH 31", "3103"]):
        return "LK", "Q1"
    if any(k in combined for k in ["Q2", "TW2", "TW 2", "TRIWULAN 2", "TRIWULAN II", "SEMESTER 1", "SEMESTER I", "30 JUNI", "30 JUN", "JUNE 30", "3006"]):
        return "LK", "Q2"
    if any(k in combined for k in ["Q3", "TW3", "TW 3", "TRIWULAN 3", "TRIWULAN III", "30 SEPTEMBER", "30 SEP", "SEPTEMBER 30", "3009"]):
        return "LK", "Q3"
    if any(k in combined for k in ["Q4", "TW4", "TW 4", "TRIWULAN 4", "TRIWULAN IV", "31 DESEMBER", "31 DES", "DECEMBER 31", "31 DEC", "AUDITED", "TAHUNAN", "ANNUAL", "1221", "1222", "1223", "1224", "1225", "FY-", "FY2"]):
        return "LK", "Q4"
        
    return "LK", "Q4" # default audited / annual

def organize_all():
    print(f"[*] Starting triage and organization on {DROPZONE_DIR}...")
    
    # Unzip any zip files in dropzone
    for zf in list(DROPZONE_DIR.glob("*.zip")):
        print(f"[+] Extracting zip: {zf.name}")
        try:
            with zipfile.ZipFile(zf, 'r') as zip_ref:
                extract_path = DROPZONE_DIR / zf.stem
                zip_ref.extractall(extract_path)
            zf.unlink() # remove zip after extract
        except Exception as e:
            print(f"[!] Error extracting {zf.name}: {e}")
            
    # Gather all PDF files in dropzone recursively
    all_pdfs = [p for p in DROPZONE_DIR.rglob("*.pdf") if p.is_file()]
    print(f"[i] Found {len(all_pdfs)} PDF files to process.")
    
    moved_count = 0
    unresolved = []
    
    for pdf in all_pdfs:
        fname = pdf.name
        snippet = extract_pdf_snippet(pdf)
        
        bank = identify_bank(fname, snippet)
        year = identify_year(fname, snippet)
        rep_type, qtr = identify_type_and_period(fname, snippet)
        
        if bank and year:
            if rep_type == "SR":
                target_folder = REPORTS_DIR / bank / "Sustainability_Report"
                target_folder.mkdir(parents=True, exist_ok=True)
                target_name = f"{bank}_{year}_Sustainability_Report.pdf"
            else:
                q = qtr or "Q4"
                target_folder = REPORTS_DIR / bank / "Laporan_Keuangan_Kuartalan"
                target_folder.mkdir(parents=True, exist_ok=True)
                target_name = f"{bank}_{year}_{q}_Laporan_Keuangan.pdf"
                
            dest = target_folder / target_name
            # If target exists and current is duplicate (has (2), (3) etc), we can safely replace or remove
            if dest.exists() and pdf != dest:
                # overwrite with latest or clean up
                pdf.unlink()
                print(f"[~] Cleaned duplicate for: {target_name} ({fname})")
            else:
                shutil.move(str(pdf), str(dest))
                print(f"[+] Placed: {fname} -> {dest.relative_to(BASE_DIR)}")
                moved_count += 1
        else:
            unresolved.append(fname)
            print(f"[!] Unable to classify: {fname} (Bank: {bank}, Year: {year})")
            
    # Clean up empty folders inside dropzone
    for sub in list(DROPZONE_DIR.iterdir()):
        if sub.is_dir():
            try:
                # Remove if empty or only empty dirs
                shutil.rmtree(sub)
                print(f"[~] Cleaned empty folder: {sub.name}")
            except Exception:
                pass
                
    print(f"\n[OK] Processing complete. Placed: {moved_count}, Unresolved: {len(unresolved)}")
    generate_inventory()

def generate_inventory():
    print(f"[*] Updating inventory: {INVENTORY_FILE}")
    
    status_matrix = {}
    sr_matrix = {}
    
    total_lk_target = len(BANKS) * len(YEARS) * len(QUARTERS) # 80
    total_sr_target = len(BANKS) * len(YEARS) # 20
    total_target = total_lk_target + total_sr_target # 100
    
    collected_lk = 0
    collected_sr = 0
    
    for bank in BANKS:
        status_matrix[bank] = {}
        sr_matrix[bank] = {}
        for y in YEARS:
            # Check SR
            sr_folder = REPORTS_DIR / bank / "Sustainability_Report"
            sr_pattern = f"{bank}_{y}_Sustainability_Report.*"
            sr_found = list(sr_folder.glob(sr_pattern)) if sr_folder.exists() else []
            if sr_found:
                sr_matrix[bank][y] = f"✅ `{sr_found[0].name}`"
                collected_sr += 1
            else:
                sr_matrix[bank][y] = "❌ *Missing*"
                
            for q in QUARTERS:
                lk_folder = REPORTS_DIR / bank / "Laporan_Keuangan_Kuartalan"
                lk_pattern = f"{bank}_{y}_{q}_Laporan_Keuangan.*"
                lk_found = list(lk_folder.glob(lk_pattern)) if lk_folder.exists() else []
                if lk_found:
                    status_matrix[bank][f"{y}-{q}"] = f"✅ `{lk_found[0].name}`"
                    collected_lk += 1
                else:
                    status_matrix[bank][f"{y}-{q}"] = "❌ *Missing*"

    total_collected = collected_lk + collected_sr
    pct = (total_collected / total_target) * 100
    
    md = []
    md.append("# 📊 Status Inventaris Laporan Keuangan & Keberlanjutan KBMI 4 (2021–2025)")
    md.append(f"\n**Ringkasan Progres Pengumpulan:**")
    md.append(f"- **Total Terkumpul:** **{total_collected} / {total_target} Berkas** ({pct:.1f}%)")
    md.append(f"- **Laporan Keuangan Kuartalan (LK):** **{collected_lk} / {total_lk_target} Berkas** ({collected_lk/total_lk_target*100:.1f}%)")
    md.append(f"- **Sustainability Reports (SR):** **{collected_sr} / {total_sr_target} Berkas** ({collected_sr/total_sr_target*100:.1f}%)")
    md.append("\n> **Petunjuk:** Taruh semua file unduhan baru di folder [`00_DROPZONE_LAPORAN/`](../00_DROPZONE_LAPORAN/). Sistem akan otomatis merapikan, menstandarisasi nama file, dan memperbarui tabel checklist di bawah ini.\n")
    
    md.append("---")
    md.append("## 1. Matriks Laporan Keuangan Kuartalan (80 Observasi)")
    md.append("\n| Bank | Tahun | Q1 (Mar) | Q2 (Jun) | Q3 (Sep) | Q4 (Des / Audited) |")
    md.append("| :--- | :---: | :---: | :---: | :---: | :---: |")
    
    for bank in BANKS:
        for y in YEARS:
            q1 = status_matrix[bank][f"{y}-Q1"]
            q2 = status_matrix[bank][f"{y}-Q2"]
            q3 = status_matrix[bank][f"{y}-Q3"]
            q4 = status_matrix[bank][f"{y}-Q4"]
            md.append(f"| **{bank}** | {y} | {q1} | {q2} | {q3} | {q4} |")
            
    md.append("\n---")
    md.append("## 2. Matriks Sustainability Report Tahunan (20 Laporan)")
    md.append("\n| Bank | 2021 | 2022 | 2023 | 2024 | 2025 |")
    md.append("| :--- | :---: | :---: | :---: | :---: | :---: |")
    
    for bank in BANKS:
        row = f"| **{bank}** |"
        for y in YEARS:
            row += f" {sr_matrix[bank][y]} |"
        md.append(row)
        
    dropzone_files = [f.name for f in DROPZONE_DIR.iterdir() if f.is_file() and f.name != "PETUNJUK_DROPZONE.md"]
    if dropzone_files:
        md.append("\n---")
        md.append("## ⚠️ Berkas di Dropzone yang Belum Teridentifikasi")
        for df in dropzone_files:
            md.append(f"- `{df}`")

    with open(INVENTORY_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
        
    print(f"[OK] Inventory updated successfully at {INVENTORY_FILE}")

if __name__ == "__main__":
    organize_all()

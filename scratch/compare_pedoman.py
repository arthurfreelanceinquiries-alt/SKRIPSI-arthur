import difflib
import re
import sys

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t2022 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t2023 = f.read()

def clean_text(text):
    # Normalize some ocr/markdown artifacts
    lines = [line.strip() for line in text.splitlines()]
    return lines

lines22 = clean_text(t2022)
lines23 = clean_text(t2023)

with open("scratch/comparison_report.txt", "w", encoding="utf-8") as out:
    out.write(f"2022 Total characters: {len(t2022)}, lines: {len(lines22)}\n")
    out.write(f"2023 Total characters: {len(t2023)}, lines: {len(lines23)}\n\n")

    # Check Bab titles
    out.write("=== BAB TITLES in 2022 ===\n")
    for l in lines22:
        if re.match(r'^(#+\s*)?\*?\*?BAB\s+[0-9IVXLCDM]+', l, re.IGNORECASE):
            out.write(l + "\n")
            
    out.write("\n=== BAB TITLES in 2023 ===\n")
    for l in lines23:
        if re.match(r'^(#+\s*)?\*?\*?BAB\s+[0-9IVXLCDM]+', l, re.IGNORECASE):
            out.write(l + "\n")

    # Check SK Dekan
    out.write("\n=== SK DEKAN ===\n")
    for l in lines22:
        if "SK" in l and "Dekan" in l:
            out.write(f"2022: {l}\n")
    for l in lines23:
        if "SK" in l and "Dekan" in l:
            out.write(f"2023: {l}\n")
            
    # Check SKS and IPK requirements
    out.write("\n=== SYARAT SKS & IPK ===\n")
    for i, l in enumerate(lines22):
        if "sks" in l.lower() or "ipk" in l.lower() or "metode riset" in l.lower():
            out.write(f"2022 [L{i}]: {l}\n")
    for i, l in enumerate(lines23):
        if "sks" in l.lower() or "ipk" in l.lower() or "metode riset" in l.lower():
            out.write(f"2023 [L{i}]: {l}\n")

    # Check Plagiarism / Turnitin
    out.write("\n=== SIMILARITAS / TURNITIN / PLAGIARISME ===\n")
    for l in lines22:
        if any(w in l.lower() for w in ["turnitin", "plagiar", "similar"]):
            out.write(f"2022: {l}\n")
    for l in lines23:
        if any(w in l.lower() for w in ["turnitin", "plagiar", "similar"]):
            out.write(f"2023: {l}\n")

    # Check Margin, Spasi, Font
    out.write("\n=== FORMATTING (MARGIN, FONT, SPASI) ===\n")
    for l in lines22:
        if any(w in l.lower() for w in ["margin", "spasi", "times new roman", "font", "huruf", "kertas"]):
            out.write(f"2022: {l}\n")
    for l in lines23:
        if any(w in l.lower() for w in ["margin", "spasi", "times new roman", "font", "huruf", "kertas"]):
            out.write(f"2023: {l}\n")

print("Analysis script 1 finished.")

import re

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t23 = f.read()

idx22 = t22.find("Lampiran 1")
idx23 = t23.find("Lampiran 1")

lamps22 = re.findall(r'Lampiran\s+(\d+)\s*:\s*(.*)', t22[idx22:])
lamps23 = re.findall(r'Lampiran\s+(\d+)\s*:\s*(.*)', t23[idx23:])

with open("scratch/lampiran_compare.txt", "w", encoding="utf-8") as out:
    out.write("=== LAMPIRAN 2022 ===\n")
    for num, title in lamps22:
        out.write(f"{num}: {title.strip()}\n")
        
    out.write("\n=== LAMPIRAN 2023 ===\n")
    for num, title in lamps23:
        out.write(f"{num}: {title.strip()}\n")

print("Lampiran compare done")

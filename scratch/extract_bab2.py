with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t23 = f.read()

import re

idx22_start = t22.find("BAB 2\n\n### FORMAT SKRIPSI")
idx22_end = t22.find("BAB 3\n\n### TATA CARA PENULISAN")

idx23_start = t23.find("BAB 2** \n\n## **FORMAT TUGAS AKHIR**")
idx23_end = t23.find("BAB 3 TATA CARA PENULISAN**")

b2_22 = t22[idx22_start:idx22_end]
b2_23 = t23[idx23_start:idx23_end]

import difflib

# Clean lines
p22 = [l.strip() for l in b2_22.splitlines() if l.strip()]
p23 = [l.strip() for l in b2_23.splitlines() if l.strip()]

matcher = difflib.SequenceMatcher(None, p22, p23)
with open("scratch/bab2_difflib.txt", "w", encoding="utf-8") as out:
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != 'equal':
            out.write(f"\n--- {tag} 2022[{i1}:{i2}] vs 2023[{j1}:{j2}] ---\n")
            out.write("2022:\n" + "\n".join(p22[i1:i2]) + "\n")
            out.write("2023:\n" + "\n".join(p23[j1:j2]) + "\n")

print("Bab 2 difflib extracted.")

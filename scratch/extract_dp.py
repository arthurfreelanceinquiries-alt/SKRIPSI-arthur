with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t23 = f.read()

import re

def get_dp(text):
    m = re.search(r'Daftar\s+Pustaka.*?(?=Lampiran|###\s*BAB\s*4|##\s*\*\*BAB\s*4)', text, re.DOTALL | re.IGNORECASE)
    return m.group(0) if m else "Not found"

with open("scratch/dp_compare.txt", "w", encoding="utf-8") as out:
    out.write("=== 2022 DAFTAR PUSTAKA ===\n")
    out.write(get_dp(t22)[:3000] + "\n\n")
    out.write("=== 2023 DAFTAR PUSTAKA ===\n")
    out.write(get_dp(t23)[:3000] + "\n\n")

print("Daftar pustaka compare extracted.")

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t23 = f.read()

import re

def get_anatomi_model_b(text):
    m = re.search(r'MODEL\s+B\b.*?(?=MODEL\s+C\b)', text, re.DOTALL | re.IGNORECASE)
    return m.group(0) if m else "Not found"

with open("scratch/anatomi_model_b.txt", "w", encoding="utf-8") as out:
    out.write("=== 2022 MODEL B ===\n")
    out.write(get_anatomi_model_b(t22) + "\n\n")
    out.write("=== 2023 MODEL B ===\n")
    out.write(get_anatomi_model_b(t23) + "\n\n")

print("Anatomi Model B extracted.")

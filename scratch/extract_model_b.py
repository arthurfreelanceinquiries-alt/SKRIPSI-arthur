import difflib

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t23 = f.read()

import re

def get_model_b(text):
    m_start = re.search(r'MODEL\s*B', text, re.I)
    m_end = re.search(r'MODEL\s*C', text, re.I)
    return text[m_start.start():m_end.start()]

mb22 = get_model_b(t22)
mb23 = get_model_b(t23)

with open("scratch/model_b_diff.txt", "w", encoding="utf-8") as out:
    out.write("=== MODEL B 2022 ===\n")
    out.write(mb22 + "\n\n")
    out.write("=== MODEL B 2023 ===\n")
    out.write(mb23 + "\n\n")

print("Model B diff extracted")

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t23 = f.read()

import re

def get_bab3(text):
    m_start = re.search(r'(?:BAB\s*3\s*[\.\-]?\s*TATA\s*CARA|###\s*BAB\s*3|BAB\s*3\s*TATA\s*CARA)', text, re.IGNORECASE)
    if not m_start:
        return "Not found"
    start_idx = m_start.start()
    m_end = re.search(r'(?:BAB\s*4\b)', text[start_idx:], re.IGNORECASE)
    if not m_end:
        return text[start_idx:start_idx+6000]
    return text[start_idx:start_idx+m_end.start()]

b3_22 = get_bab3(t22)
b3_23 = get_bab3(t23)

with open("scratch/bab3_diff.txt", "w", encoding="utf-8") as out:
    out.write("=== BAB 3 2022 ===\n")
    out.write(b3_22 + "\n\n")
    out.write("=== BAB 3 2023 ===\n")
    out.write(b3_23 + "\n\n")

print("Bab 3 extraction done")

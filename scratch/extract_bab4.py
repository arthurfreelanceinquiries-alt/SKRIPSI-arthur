with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t23 = f.read()

import re

def get_section(text, start_pat, end_pat):
    m_start = re.search(start_pat, text, re.IGNORECASE)
    if not m_start:
        return "Start not found"
    start_idx = m_start.start()
    m_end = re.search(end_pat, text[start_idx:], re.IGNORECASE)
    if not m_end:
        return text[start_idx:start_idx+4000]
    return text[start_idx:start_idx+m_end.start()]

with open("scratch/bab4_compare.txt", "w", encoding="utf-8") as out:
    out.write("=== BAB 4: SYARAT SIDANG 2022 ===\n")
    out.write(get_section(t22, r'###\s*4\.1\.\s*Pendaftaran', r'###\s*4\.2') + "\n\n")

    out.write("=== BAB 4: SYARAT SIDANG 2023 ===\n")
    out.write(get_section(t23, r'##\s*\*\*4\.1\.\s*Pendaftaran', r'##\s*\*\*4\.2') + "\n\n")

    out.write("=== BAB 5: PEDOMAN PENILAIAN 2022 ===\n")
    out.write(get_section(t22, r'###\s*BAB\s*5', r'###\s*BAB\s*6') + "\n\n")

    out.write("=== BAB 5: PEDOMAN PENILAIAN 2023 ===\n")
    out.write(get_section(t23, r'##\s*\*\*BAB\s*5', r'##\s*\*\*BAB\s*6') + "\n\n")

    out.write("=== BAB 6: SANKSI 2022 ===\n")
    out.write(get_section(t22, r'###\s*BAB\s*6', r'Lampiran') + "\n\n")

    out.write("=== BAB 6: SANKSI 2023 ===\n")
    out.write(get_section(t23, r'##\s*\*\*BAB\s*6', r'Lampiran') + "\n\n")

print("bab4_compare done")

import re
import difflib

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t23 = f.read()

# Let's normalize text by:
# 1. replace 'skripsi' with 'tugas akhir' (conceptually, to isolate non-trivial changes)
# 2. collapse whitespace

def normalize(text):
    # remove markdown headings formatting, page marks, picture text
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'Universitas Kristen Krida Wacana\s*\|\s*\d+', '', text)
    text = re.sub(r'#+', '', text)
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'_+', '', text)
    # remove bullets
    text = re.sub(r'^\s*[\-\•\▪]\s*', '', text, flags=re.MULTILINE)
    # clean extra spaces
    lines = [re.sub(r'\s+', ' ', l).strip() for l in text.splitlines()]
    lines = [l for l in lines if l]
    return lines

n22 = normalize(t22)
n23 = normalize(t23)

matcher = difflib.SequenceMatcher(None, n22, n23)

with open("scratch/all_structural_diffs.txt", "w", encoding="utf-8") as out:
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != 'equal':
            chunk22 = "\n".join(n22[i1:i2])
            chunk23 = "\n".join(n23[j1:j2])
            # Only record if meaningful (ignore purely 'skripsi' vs 'tugas akhir' if identical otherwise)
            out.write(f"=== DIFF TYPE: {tag} (2022 lines {i1}-{i2} vs 2023 lines {j1}-{j2}) ===\n")
            out.write(f"--- 2022 ---\n{chunk22}\n")
            out.write(f"--- 2023 ---\n{chunk23}\n\n")

print("All structural diffs extracted.")

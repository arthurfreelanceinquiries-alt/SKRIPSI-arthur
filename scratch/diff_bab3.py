import difflib

with open("scratch/bab3_diff.txt", "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("=== BAB 3 2023 ===")
part22 = parts[0].replace("=== BAB 3 2022 ===", "").strip().splitlines()
part23 = parts[1].strip().splitlines()

# Clean lines
p22 = [l.strip() for l in part22 if l.strip()]
p23 = [l.strip() for l in part23 if l.strip()]

matcher = difflib.SequenceMatcher(None, p22, p23)
with open("scratch/bab3_difflib.txt", "w", encoding="utf-8") as out:
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != 'equal':
            out.write(f"\n--- {tag} 2022[{i1}:{i2}] vs 2023[{j1}:{j2}] ---\n")
            out.write("2022:\n" + "\n".join(p22[i1:i2]) + "\n")
            out.write("2023:\n" + "\n".join(p23[j1:j2]) + "\n")

print("Bab 3 difflib done")

with open("scratch/all_structural_diffs.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = text.split("=== DIFF TYPE: ")

with open("scratch/meaningful_diffs.txt", "w", encoding="utf-8") as out:
    for c in chunks:
        if not c.strip():
            continue
        # Check if the differences are just skripsi vs tugas akhir, or formatting of links
        # Let's inspect parts
        parts = c.split("--- 2023 ---")
        if len(parts) < 2:
            continue
        p22_str = parts[0].split("--- 2022 ---")[-1].strip().lower()
        p23_str = parts[1].strip().lower()
        
        # Test if removing 'skripsi' vs 'tugas akhir' makes them identical
        norm22 = p22_str.replace("skripsi", "tugas akhir").replace(" ", "").replace("\n", "").replace(".", "").replace(",", "").replace("-", "")
        norm23 = p23_str.replace(" ", "").replace("\n", "").replace(".", "").replace(",", "").replace("-", "")
        
        if norm22 != norm23:
            out.write("=== MEANINGFUL DIFF ===\n" + c + "\n" + "="*50 + "\n\n")

print("Meaningful diffs filtered.")

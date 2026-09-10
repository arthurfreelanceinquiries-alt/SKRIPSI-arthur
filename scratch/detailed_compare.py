import re

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    t22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    t23 = f.read()

out = open("scratch/full_comparison_detailed.txt", "w", encoding="utf-8")

# Let's inspect Chapter by Chapter differences
# 1. Links (URLs)
urls22 = set(re.findall(r'https?://\S+|cutt\.ly/\S+', t22))
urls23 = set(re.findall(r'https?://\S+|cutt\.ly/\S+', t23))
out.write("=== URLS in 2022 vs 2023 ===\n")
out.write("2022 URLs: " + str(urls22) + "\n")
out.write("2023 URLs: " + str(urls23) + "\n\n")

# 2. Pendaftaran Sidang / Ujian (Bab 4)
# Let's print the entire section of Syarat Sidang in 2022 and 2023
def find_syarat_sidang(text):
    match = re.search(r'(?:Pendaftaran Ujian|Syarat.*Sidang|4\.1\..*Pendaftaran).*?(?=4\.2|4\.3|##\s*4\.2)', text, re.DOTALL | re.IGNORECASE)
    return match.group(0) if match else "Not found"

out.write("=== SYARAT PENDAFTARAN SIDANG 2022 ===\n")
out.write(find_syarat_sidang(t22)[:2000] + "\n\n")
out.write("=== SYARAT PENDAFTARAN SIDANG 2023 ===\n")
out.write(find_syarat_sidang(t23)[:2000] + "\n\n")

# 3. Penilaian (Bab 5)
def find_penilaian(text):
    match = re.search(r'(?:BAB 5|PEDOMAN PENILAIAN).*?(?=BAB 6|Lampiran|$)', text, re.DOTALL | re.IGNORECASE)
    return match.group(0) if match else "Not found"

out.write("=== PENILAIAN 2022 ===\n")
out.write(find_penilaian(t22)[:2000] + "\n\n")
out.write("=== PENILAIAN 2023 ===\n")
out.write(find_penilaian(t23)[:2000] + "\n\n")

# 4. Sanksi / Plagiarisme (Bab 6)
def find_bab6(text):
    match = re.search(r'(?:BAB 6|SANKSI).*?(?=Lampiran|$)', text, re.DOTALL | re.IGNORECASE)
    return match.group(0) if match else "Not found"

out.write("=== BAB 6 / SANKSI 2022 ===\n")
out.write(find_bab6(t22)[:2000] + "\n\n")
out.write("=== BAB 6 / SANKSI 2023 ===\n")
out.write(find_bab6(t23)[:2000] + "\n\n")

# 5. List of Lampiran
lamps22 = re.findall(r'Lampiran\s+\d+.*', t22)
lamps23 = re.findall(r'Lampiran\s+\d+.*', t23)
out.write("=== LAMPIRAN 2022 ===\n")
for l in lamps22:
    out.write(l + "\n")
out.write("\n=== LAMPIRAN 2023 ===\n")
for l in lamps23:
    out.write(l + "\n")

out.close()
print("full comparison script finished")

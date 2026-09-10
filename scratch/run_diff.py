import re
import difflib

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md", "r", encoding="utf-8") as f:
    text22 = f.read()

with open("05_Pedoman_&_Referensi/Buku Pedoman Penyusunan Tugas Akhir 2023.md", "r", encoding="utf-8") as f:
    text23 = f.read()

# Normalize spacing/line endings for cleaner comparison
def get_clean_paragraphs(text):
    # Remove excessive blank lines
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return lines

lines22 = get_clean_paragraphs(text22)
lines23 = get_clean_paragraphs(text23)

out_file = open("scratch/diff_analysis_detailed.txt", "w", encoding="utf-8")

def check_topic(title, regex_pattern):
    out_file.write(f"\n=======================================================\n")
    out_file.write(f"TOPIC: {title}\n")
    out_file.write(f"=======================================================\n")
    
    pat = re.compile(regex_pattern, re.IGNORECASE)
    
    out_file.write("--- 2022 Matches ---\n")
    for i, l in enumerate(lines22):
        if pat.search(l):
            context = " | ".join(lines22[max(0, i-1):min(len(lines22), i+2)])
            out_file.write(f"Line {i}: {context}\n\n")
            
    out_file.write("--- 2023 Matches ---\n")
    for i, l in enumerate(lines23):
        if pat.search(l):
            context = " | ".join(lines23[max(0, i-1):min(len(lines23), i+2)])
            out_file.write(f"Line {i}: {context}\n\n")

topics = [
    ("SK Dekan & Landasan", r"SK Dekan|350a"),
    ("Syarat SKS & IPK Awal", r"126\s*sks|130\s*sks|ipk"),
    ("Masa Bimbingan & Semester", r"semester|masa berlaku|perpanjangan|bulan"),
    ("Jumlah Bimbingan / Frekuensi", r"bimbingan|kartu bimbingan|tatap muka|kali"),
    ("Proposal Skripsi / TA", r"proposal"),
    ("Struktur Bab (Isi)", r"Bab 1|Bab 2|Bab 3|Bab 4|Bab 5"),
    ("Tata Cara Pengetikan (Font, Spasi)", r"Times New Roman|Arial|Calibri|12 pt|spasi|1\.5"),
    ("Ukuran Kertas & Margin", r"kertas|HVS|A4|margin|tepi|kiri|kanan|atas|bawah"),
    ("Penomoran Halaman", r"halaman|romawi|arab|tengah|kanan"),
    ("Daftar Pustaka & Sitasi", r"APA|daftar pustaka|referensi|edisi|mendeley|zotero"),
    ("Persyaratan Sidang & Turnitin", r"turnitin|plagiarism|35%|30%|syarat sidang|daftar ujian"),
    ("Kriteria Nilai & Kelulusan", r"kelulusan|nilai|skor|A-|B\+|predikat|yudisium"),
    ("Lampiran & Format", r"lampiran|persetujuan|pengesahan|pernyataan")
]

for title, pat in topics:
    check_topic(title, pat)

out_file.close()
print("Topic analysis completed.")

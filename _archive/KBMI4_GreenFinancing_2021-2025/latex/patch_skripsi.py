"""
Python script to perform precision patching of latex/Skripsi_Arthur.tex
"""
import re

def patch():
    tex_path = r"z:\Skripsi\latex\Skripsi_Arthur.tex"
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Front matter commands
    content = content.replace(r"\newcommand{\nahamahasiswa}{Arthur Reezan}", r"\newcommand{\nahamahasiswa}{Arthur Reezan}")
    content = content.replace(r"\newcommand{\nim}{312023002}", r"\newcommand{\nim}{312023002}")
    content = content.replace(r"\newcommand{\dosbim}{[Nama Dosen Pembimbing]}", r"\newcommand{\dosbim}{Dr. Diana Frederica, S.E., M.Ak., CFP\textsuperscript{\textregistered}., CHCP-A}")
    content = content.replace(r"\newcommand{\nidn}{[NIDN Dosen Pembimbing]}", r"\newcommand{\nidn}{0315088201}")

    # 2. Typos & Duplicate headings
    content = content.replace("batas batas toleransi", "batas toleransi")
    content = content.replace("antarbang", "antarbank")
    content = content.replace(r"\subsubsection{Analisis Tren Kuartalan dan Profil Finansial Perbankan KBMI 4 (2021--2025)}", "")

    # 3. POJK 60/2017 -> POJK 18/2023
    content = content.replace("POJK Nomor 60/POJK.04/2017", "POJK Nomor 18 Tahun 2023 (menggantikan POJK 60/POJK.04/2017)")
    content = content.replace("POJK 60/POJK.04/2017", "POJK 18/2023")

    # 4. Save intermediate
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Initial patches applied successfully!")

if __name__ == '__main__':
    patch()


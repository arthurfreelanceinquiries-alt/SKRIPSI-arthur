"""
Script to synchronize PROPOSAL_SKRIPSI_POKEMON_TCG.md from the validated Proposal_Arthur_PokemonTCG.tex.
Ensures publication-grade Markdown formatting matching FEB UKRIDA 2023 standards (Lampiran 10 Model B).
"""
import os
import re

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    naskah_dir = os.path.join(repo_root, "01_Naskah_Utama")

    tex_path = os.path.join(naskah_dir, "Proposal_Arthur_PokemonTCG.tex")
    bbl_path = os.path.join(naskah_dir, "Proposal_Arthur_PokemonTCG.bbl")
    md_path = os.path.join(naskah_dir, "PROPOSAL_SKRIPSI_POKEMON_TCG.md")
    aux_path = os.path.join(naskah_dir, "Proposal_Arthur_PokemonTCG.aux")

    with open(tex_path, 'r', encoding='utf-8') as f:
        tex = f.read()

    cite_dict = {}
    if os.path.exists(aux_path):
        with open(aux_path, 'r', encoding='utf-8') as f:
            aux_content = f.read()
            matches = re.findall(r'\\bibcite\{([^}]+)\}\{\{\d+\}\{(\d{4})\}\{(.*?)\}\}', aux_content)
            for key, year, author in matches:
                author = author.strip('{}')
                author = author.replace('~', ' ').replace(r'{\"u}', 'ü').replace(r'{\"O}', 'Ö')
                author = author.replace('et~al.', 'et al.')
                cite_dict[key] = (author, year)
    # Self-anneal 18 Sep 2026 (R3 humanisasi): aux basi (mis. sebelum xelatex+bibtex)
    # tidak memuat \bibcite sehingga sitasi bocor sebagai kunci mentah di MD/DOCX.
    # Gagal lantang di sini, jangan tulis MD rusak. Urutan wajib: xelatex -> bibtex
    # -> xelatex x2 -> sync ini -> build word.
    cited_keys = set(k.strip() for grp in re.findall(r'\\cite[ptalp]*\{([^}]+)\}', tex) for k in grp.split(','))
    if cited_keys and not cite_dict:
        raise SystemExit('FATAL: 0 \\bibcite terparse dari .aux — jalankan xelatex+bibtex+2x xelatex dulu sebelum sync.')
    missing = sorted(cited_keys - set(cite_dict))
    if missing:
        raise SystemExit('FATAL: %d kunci sitasi tanpa pemetaan author-year: %s' % (len(missing), ', '.join(missing[:8])))

    # Read bbl if available
    bbl_entries = []
    if os.path.exists(bbl_path):
        with open(bbl_path, 'r', encoding='utf-8') as f:
            bbl = f.read()
            items = re.findall(r'\\bibitem\[(.*?)\]\{(.*?)\}\s*(.*?)(?=\\bibitem|\\end\{thebibliography\}|$)', bbl, re.DOTALL)
            for label, key, content in items:
                clean_entry = re.sub(r'\\newblock\s*', ' ', content)
                clean_entry = re.sub(r'\{\\em\s+([^}]+)\}', r'*\1*', clean_entry)
                clean_entry = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', clean_entry)
                clean_entry = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', clean_entry)
                clean_entry = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', clean_entry)
                clean_entry = clean_entry.replace('~', ' ')
                clean_entry = clean_entry.replace(r'\%', '%').replace(r'\_', '_').replace(r'\&', '&')
                clean_entry = clean_entry.replace('--', '–')
                clean_entry = clean_entry.replace(r'{\"u}', 'ü').replace(r'{\"O}', 'Ö')
                clean_entry = clean_entry.replace('{', '').replace('}', '')
                clean_entry = re.sub(r'\s+', ' ', clean_entry).strip()
                bbl_entries.append(clean_entry)

    md_lines = []
    md_lines.append("# PROPOSAL SKRIPSI LENGKAP — UNIVERSITAS KRISTEN KRIDA WACANA")
    md_lines.append("**Fakultas Ekonomi dan Bisnis | Program Studi S1 Manajemen**  ")
    md_lines.append("**Konsentrasi:** Manajemen Keuangan  ")
    md_lines.append("**Penulis:** Arthur Reezan (NIM: 312023002)  ")
    md_lines.append("**Dosen Pembimbing:** Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A (NIDN: [NIDN_DOSEN])  ")
    md_lines.append("")
    md_lines.append("> **Judul Proposal Skripsi:**  ")
    md_lines.append("> **PENGARUH *HEDONIC MOTIVATION*, *DESIRE FOR COMPLETENESS*, DAN *SPECULATIVE MOTIVE* TERHADAP *IMPULSIVE BUYING* BOOSTER PACK KARTU POKÉMON TCG DENGAN *SELF-CONTROL* SEBAGAI VARIABEL MODERASI**  ")
    md_lines.append(">  ")
    md_lines.append("> *Format Dokumen: Teks Lengkap Proposal BAB 1–3 Sesuai Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 (Lampiran 10 Model B)*")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## DAFTAR ISI NASKAH PROPOSAL")
    md_lines.append("")
    md_lines.append("- [HALAMAN SAMPUL / JUDUL PROPOSAL](#halaman-sampul--judul-proposal)")
    md_lines.append("- [BAB 1 PENDAHULUAN](#bab-1-pendahuluan)")
    md_lines.append("  - [1.1 Latar Belakang Penelitian](#11-latar-belakang-penelitian)")
    md_lines.append("  - [1.2 Perumusan Masalah](#12-perumusan-masalah)")
    md_lines.append("  - [1.3 Tujuan Penelitian](#13-tujuan-penelitian)")
    md_lines.append("  - [1.4 Manfaat Penelitian](#14-manfaat-penelitian)")
    md_lines.append("    - [1.4.1 Manfaat Teoritis](#141-manfaat-teoritis)")
    md_lines.append("    - [1.4.2 Manfaat Praktis](#142-manfaat-praktis)")
    md_lines.append("- [BAB 2 KAJIAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS](#bab-2-kajian-pustaka-dan-pengembangan-hipotesis)")
    md_lines.append("  - [2.1 Landasan Teori](#21-landasan-teori)")
    md_lines.append("    - [2.1.1 Grand Theory: Keuangan Perilaku (Behavioral Finance)](#211-grand-theory-keuangan-perilaku-behavioral-finance)")
    md_lines.append("    - [2.1.2 Teori Pendukung (Supporting Theories)](#212-teori-pendukung-supporting-theories)")
    md_lines.append("    - [2.1.3 Impulsive Buying (Pembelian Impulsif)](#213-impulsive-buying-pembelian-impulsif)")
    md_lines.append("    - [2.1.4 Hedonic Motivation (Motivasi Hedonis)](#214-hedonic-motivation-motivasi-hedonis)")
    md_lines.append("    - [2.1.5 Desire for Completeness (Hasrat Melengkapi Koleksi)](#215-desire-for-completeness-hasrat-melengkapi-koleksi)")
    md_lines.append("    - [2.1.6 Speculative Motive (Motif Spekulasi Finansial)](#216-speculative-motive-motif-spekulasi-finansial)")
    md_lines.append("    - [2.1.7 Self-Control (Kontrol Diri)](#217-self-control-kontrol-diri)")
    md_lines.append("  - [2.2 Penelitian Sebelumnya](#22-penelitian-sebelumnya)")
    md_lines.append("  - [2.3 Pengembangan Hipotesis](#23-pengembangan-hipotesis)")
    md_lines.append("    - [2.3.1 Pengaruh Hedonic Motivation terhadap Impulsive Buying](#231-pengaruh-hedonic-motivation-terhadap-impulsive-buying)")
    md_lines.append("    - [2.3.2 Pengaruh Desire for Completeness terhadap Impulsive Buying](#232-pengaruh-desire-for-completeness-terhadap-impulsive-buying)")
    md_lines.append("    - [2.3.3 Pengaruh Speculative Motive terhadap Impulsive Buying](#233-pengaruh-speculative-motive-terhadap-impulsive-buying)")
    md_lines.append("    - [2.3.4 Peran Moderasi Self-Control pada Pengaruh Hedonic Motivation terhadap Impulsive Buying](#234-peran-moderasi-self-control-pada-pengaruh-hedonic-motivation-terhadap-impulsive-buying)")
    md_lines.append("    - [2.3.5 Peran Moderasi Self-Control pada Pengaruh Desire for Completeness terhadap Impulsive Buying](#235-peran-moderasi-self-control-pada-pengaruh-desire-for-completeness-terhadap-impulsive-buying)")
    md_lines.append("    - [2.3.6 Peran Moderasi Self-Control pada Pengaruh Speculative Motive terhadap Impulsive Buying](#236-peran-moderasi-self-control-pada-pengaruh-speculative-motive-terhadap-impulsive-buying)")
    md_lines.append("  - [2.4 Rerangka Penelitian](#24-rerangka-penelitian)")
    md_lines.append("- [BAB 3 METODE PENELITIAN](#bab-3-metode-penelitian)")
    md_lines.append("  - [3.1 Jenis dan Sumber Data](#31-jenis-dan-sumber-data)")
    md_lines.append("  - [3.2 Populasi dan Sampel](#32-populasi-dan-sampel)")
    md_lines.append("    - [3.2.1 Populasi](#321-populasi)")
    md_lines.append("    - [3.2.2 Sampel dan Penentuan Ukuran Sampel](#322-sampel-dan-penentuan-ukuran-sampel)")
    md_lines.append("  - [3.3 Model Penelitian](#33-model-penelitian)")
    md_lines.append("  - [3.4 Operasionalisasi Variabel](#34-operasionalisasi-variabel)")
    md_lines.append("  - [3.5 Metode Analisis Data](#35-metode-analisis-data)")
    md_lines.append("    - [3.5.1 Uji Kualitas Data (Validitas dan Reliabilitas)](#351-uji-kualitas-data-validitas-dan-reliabilitas)")
    md_lines.append("    - [3.5.2 Uji Asumsi Klasik](#352-uji-asumsi-klasik)")
    md_lines.append("    - [3.5.3 Analisis Regresi Linear Berganda (Model 1)](#353-analisis-regresi-linear-berganda-model-1)")
    md_lines.append("    - [3.5.4 Moderated Regression Analysis (MRA) (Model 2)](#354-moderated-regression-analysis-mra-model-2)")
    md_lines.append("    - [3.5.5 Uji Kelayakan Model (Goodness of Fit)](#355-uji-kelayakan-model-goodness-of-fit)")
    md_lines.append("    - [3.5.6 Uji Signifikansi Parsial (Uji t)](#356-uji-signifikansi-parsial-uji-t)")
    md_lines.append("- [DAFTAR PUSTAKA](#daftar-pustaka)")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("### HALAMAN SAMPUL / JUDUL PROPOSAL")
    md_lines.append("")
    md_lines.append("<div align=\"center\">")
    md_lines.append("")
    md_lines.append("# PROPOSAL SKRIPSI")
    md_lines.append("")
    md_lines.append("## PENGARUH *HEDONIC MOTIVATION*, *DESIRE FOR COMPLETENESS*, DAN *SPECULATIVE MOTIVE* TERHADAP *IMPULSIVE BUYING* BOOSTER PACK KARTU POKÉMON TCG DENGAN *SELF-CONTROL* SEBAGAI VARIABEL MODERASI")
    md_lines.append("")
    md_lines.append("Diajukan Kepada Program Studi S1 Manajemen  ")
    md_lines.append("Untuk Menyusun Skripsi Sarjana Manajemen (S.M.)  ")
    md_lines.append("")
    md_lines.append("Diajukan Oleh:  ")
    md_lines.append("**Arthur Reezan**  ")
    md_lines.append("**NIM: 312023002**  ")
    md_lines.append("")
    md_lines.append("### FAKULTAS EKONOMI DAN BISNIS  ")
    md_lines.append("### UNIVERSITAS KRISTEN KRIDA WACANA  ")
    md_lines.append("### JAKARTA  ")
    md_lines.append("### 2026")
    md_lines.append("")
    md_lines.append("</div>")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    # Modular 23 Sep 2026: Pernyataan/Persetujuan/Pengesahan/Kata Pengantar/
    # Abstrak/Abstract hidup mandiri di 01_Lembar_Persetujuan_Proposal/ dan
    # SUDAH dihapus dari TeX master — tidak lagi disinkron ke MD.

    # Extract Chapters from TeX
    # BAB 1
    bab1_match = re.search(r'\\section\*\{BAB 1.*?PENDAHULUAN\}(.*?)(?=\\section\*\{BAB 2|\Z)', tex, re.DOTALL)
    if bab1_match:
        bab1_text = bab1_match.group(1)
        md_lines.append("# BAB 1 PENDAHULUAN")
        md_lines.append("")
        md_lines.append(convert_tex_section(bab1_text, 1, cite_dict))
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    # BAB 2
    bab2_match = re.search(r'\\section\*\{BAB 2.*?\}(.*?)(?=\\section\*\{BAB 3|\Z)', tex, re.DOTALL)
    if bab2_match:
        bab2_text = bab2_match.group(1)
        md_lines.append("# BAB 2 KAJIAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS")
        md_lines.append("")
        md_lines.append(convert_tex_section(bab2_text, 2, cite_dict))
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    # BAB 3
    bab3_match = re.search(r'\\section\*\{BAB 3.*?METODE PENELITIAN\}(.*?)(?=\\renewcommand\{\\refname\}|\\bibliography|\Z)', tex, re.DOTALL)
    if bab3_match:
        bab3_text = bab3_match.group(1)
        md_lines.append("# BAB 3 METODE PENELITIAN")
        md_lines.append("")
        md_lines.append(convert_tex_section(bab3_text, 3, cite_dict))
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    # DAFTAR PUSTAKA
    md_lines.append("# DAFTAR PUSTAKA")
    md_lines.append("")
    if bbl_entries:
        for i, entry in enumerate(bbl_entries, 1):
            md_lines.append(f"{i}. {entry}")
            md_lines.append("")
    else:
        md_lines.append("*Lihat file `references.bib` untuk data bibliografi lengkap.*")

    output_text = "\n".join(md_lines)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(output_text)

    print(f"Successfully generated {md_path} ({len(output_text.splitlines())} lines)")

def convert_tex_section(tex_str, chapter_num, cite_dict=None):
    s = tex_str
    if cite_dict is None:
        cite_dict = {}

    # Strip LaTeX comments and page breaks early
    # Lindungi \% \& \_ dulu agar tidak dimakan penghapus komentar (self-anneal Sylvia 23 Sep 2026)
    s = s.replace(r'\%', '___PCT___').replace(r'\&', '___AMP___').replace(r'\_', '___US___')
    s = re.sub(r'%.*?\n', '\n', s)
    s = re.sub(r'\\newpage', '', s)
    s = re.sub(r'\\pagebreak', '', s)
    s = re.sub(r'\\clearpage', '', s)
    s = re.sub(r'\\addlinespace(\[[^\]]*\])?', '', s)
    s = re.sub(r'\\centering', '', s)
    s = re.sub(r'\\raggedright', '', s)

    # Normalize Pokémon
    s = s.replace(r"Pok\'emon", "Pokémon")
    s = s.replace(r"Pokemon", "Pokémon")

    # Clean LaTeX macros & counters
    s = re.sub(r'\\addcontentsline\{toc\}.*?\n', '', s)
    s = re.sub(r'\\addcontentsline\{[^}]+\}\{[^}]+\}\{[^}]+\}', '', s)
    s = re.sub(r'\\setcounter\{[^}]+\}\{[^}]+\}', '', s)
    s = re.sub(r'\\texorpdfstring\{([^}]+)\}\{[^}]+\}', r'\1', s)
    s = s.replace(r'\judulskripsi', 'PENGARUH *HEDONIC MOTIVATION*, *DESIRE FOR COMPLETENESS*, DAN *SPECULATIVE MOTIVE* TERHADAP *IMPULSIVE BUYING* BOOSTER PACK KARTU POKÉMON TCG DENGAN *SELF-CONTROL* SEBAGAI VARIABEL MODERASI')
    s = s.replace("``", "“").replace("''", "”")

    # Convert Table 1.1 (Matriks Research Gap)
    if r"\caption{Matriks Kesenjangan Penelitian Empiris" in s:
        tab11_pattern = re.compile(r'\\begingroup.*?\\caption\{Matriks Kesenjangan Penelitian Empiris.*?\}.*?\\endgroup', re.DOTALL)
        tab11_md = """**Tabel 1.1: Matriks Kesenjangan Penelitian Empiris (*Research Gap*) pada 7 Subjek Hubungan Model Penelitian**

| No | Subjek Hubungan | Kelompok Temuan Positif / Meredam | Kelompok Temuan Negatif / Lemah | Inti Kesenjangan Kausal (*The Why*) |
|:---:|:---|:---|:---|:---|
| 1 | X1 terhadap Y (*Hedonic Motivation*) | Arnold dan Reynolds (2003); Gultekin dan Ozer (2012); Pranggabayu dan Andjarwati (2022); Gong *et al.* (2024); Tirtayasa *et al.* (2020); Zheng *et al.* (2019) (positif signifikan). | Batas Thaler (1985); Thaler dan Shefrin (1981) (tertahan anggaran; bukan temuan tidak signifikan pada kolektibel). | Elastisitas anggaran dan orientasi utiliter vs afektif. |
| 2 | X2 terhadap Y (*Desire for Completeness*) | Gao *et al.* (2014); Barasz *et al.* (2017); Dewi *et al.* (2026) (positif signifikan). | Long dan Schiffman (2000); Spero dan Stone (2004) (kolektor matang pilih single; bukan temuan tidak signifikan). | Kematangan kolektor dan kalkulasi probabilitas. |
| 3 | X3 terhadap Y (*Speculative Motive*) | Baur *et al.* (2018); Aryadi dan Lingga (2024) (analogi partisipasi TCG); Colline (2024) (herding; kualitatif). Shiller (2000) sebagai grand theory. | Barber dan Odean (2008); Fama (1970) (analogi saham; bukan temuan tidak signifikan pada kolektibel). | Asimetri informasi dan ilusi kendali vs evaluasi risiko. |
| 4 | M terhadap Y (*Self-Control*) | Baumeister (2002); Tangney *et al.* (2004); Vohs dan Faber (2007); Sultan *et al.* (2012) (negatif signifikan). | Hirschman (1982); Stern (1962) (cognitive bypass; bukan regresi). | Ego depletion saat stimulus intens. |
| 5 | Moderasi M pada X1 terhadap Y | Lienardy dan Panasea (2026) (MRA H4 diterima); Katauke *et al.* (2023) (tak langsung). | Gagal-moderasi Apidana dan Kholifah (2022) (p=0,597) dan Artadita dan Firmialy (2024) (beta=0,092, n.s.). | Ambang intensitas hedonis vs kapasitas volisional. |
| 6 | Moderasi M pada X2 terhadap Y | Parsial: Artadita dan Firmialy (2024) (kontrol kognitif; moderasi keseluruhan ditolak); Apidana dan Kholifah (2022) (adjacent). | Teori Belk (1995); Barasz *et al.* (2017) + Artadita dan Firmialy (2024) H3 ditolak. | Keterikatan koleksi: kasual vs fanatik. |
| 7 | Moderasi M pada X3 terhadap Y | Tak langsung: Katauke *et al.* (2023) + Planner-Doer. | Teoritis Shiller (2000); Aryadi dan Lingga (2024) (bukan uji interaksi). | Herding dan FOMO saat euforia. |

*Sumber: Data diolah dari sintesis kajian literatur empiris terdahulu (2026).*"""
        s = tab11_pattern.sub(lambda m: tab11_md, s)

    # Convert Table 2.1
    if r"\caption{Ringkasan Penelitian Sebelumnya}" in s:
        tab21_pattern = re.compile(r'\\begingroup.*?\\caption\{Ringkasan Penelitian Sebelumnya\}.*?\\endgroup', re.DOTALL)
        tab21_md = """**Tabel 2.1 Ringkasan Penelitian Sebelumnya**

| No | Peneliti (Tahun) | Judul Penelitian | Variabel & Metode | Hasil Utama Penelitian |
|:---:|:---|:---|:---|:---|
| 1 | Arnold & Reynolds (2003) | *Hedonic Shopping Motivations* | Motivasi hedonis; Analisis faktor | Mengidentifikasi 6 dimensi hedonis; kesenangan emosional memicu belanja spontan. |
| 2 | Gültekin & Özer (2012) | *The Influence of Hedonic Motives on Impulse Buying* | X: *Hedonic motives*; Y: *Impulse buying*; Regresi | Motivasi hedonis berpengaruh positif signifikan terhadap *impulsive buying*. |
| 3 | Gao, Huang, & Simonson (2014) | *The "Completing the Set" Effect* | X: *Set framing*; Y: Niat beli; Desain eksperimen | Hasrat melengkapi set secara signifikan memicu pembelian terburu-buru dan spontan. |
| 4 | Barasz et al. (2017) | *Pseudo-Set Framing toward Completeness* | X: *Pseudo-set*; Y: Keputusan beli; Eksperimen | Pembingkaian item sebagai kesatuan himpunan menciptakan dorongan melengkapi item. |
| 5 | Shiller (2000) | *Irrational Exuberance* | X: Spekulasi, psikologi pasar; Y: Gelembung harga | Bias optimisme pasar memicu euforia transaksi spekulatif spontan berlebihan. |
| 6 | Baur, Hong, & Lee (2018) | *Alternative Collectibles Speculative Dynamics* | X: Motif spekulasi; Y: Volume transaksi | Pasar aset alternatif memperlihatkan dinamika transaksi spekulatif mirip aset finansial. |
| 7 | Vohs & Faber (2007) | *Self-Regulatory Resource Depletion* | X: Penipisan kontrol diri; Y: *Impulse buying*; Eksperimen | Kegagalan kontrol diri meningkatkan belanja impulsif; kontrol diri tinggi membatasi belanja spontan. |
| 8 | Sultan, Joireman, & Sprott (2012) | *Building Consumers' Impulsive Buying Model* | X: Stimulus emosi; Y: *Impulse*; Mod: *Self-control*; SEM | Kontrol diri secara signifikan memperlemah pengaruh dorongan emosional terhadap *impulse buying*. |
| 9 | Fitriyani, Widodo, & Fauzi (2022) | Hubungan *Hedonic Shopping* dengan *Impulse Buying* | X: *Hedonic motivation*; Y: *Impulse buying*; Regresi | Motivasi hedonis berkorelasi positif signifikan dengan perilaku belanja impulsif konsumen muda. |
| 10 | Tangney, Baumeister, & Boone (2004) | *High Self-Control Predicts Good Adjustment* | *Trait self-control*; Skala BSCS; Validasi psikometri | Mengembangkan skala kontrol diri baku; individu kontrol diri tinggi mampu menunda kepuasan. |

*Sumber: Data diolah dari publikasi jurnal ilmiah bereputasi (2026).*"""
        s = tab21_pattern.sub(tab21_md, s)

    # Convert Figure 2.1
    if r"\caption{Model Rerangka Konseptual Penelitian}" in s:
        fig21_pattern = re.compile(r'\\begin\{figure\}\[H\].*?\\caption\{Model Rerangka Konseptual Penelitian\}.*?\\end\{figure\}', re.DOTALL)
        fig21_md = """```
                     Pengaruh Langsung (H1, H2, H3)
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   [ X1: Hedonic Motivation     ] ──── H1 (+) ────┐          │
    │                                                  │          │
    │   [ X2: Desire for Completeness] ──── H2 (+) ────┼────►  [ Y: Impulsive Buying ]
    │                                                  │          │
    │   [ X3: Speculative Motive     ] ──── H3 (+) ────┘          │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
                                                       ▲
                                                       │
                           H4, H5, H6 (Memperlemah / -)
                                                       │
                                           [ M: Self-Control ]
                                           (Variabel Moderasi)
```
**Gambar 2.1 Model Rerangka Konseptual Penelitian**

*Keterangan: Garis lurus menunjukkan pengaruh langsung (H1, H2, H3); Garis putus-putus menunjukkan efek moderasi kontrol diri yang memperlemah (H4, H5, H6).*"""
        s = fig21_pattern.sub(fig21_md, s)

    # Convert Table 3.1
    if r"\caption{Skala Pengukuran Likert 5 Poin}" in s:
        tab31_pattern = re.compile(r'\\begin\{table\}\[H\].*?\\caption\{Skala Pengukuran Likert 5 Poin\}.*?\\end\{table\}', re.DOTALL)
        tab31_md = """**Tabel 3.1 Skala Pengukuran Likert 5 Poin**

| Skor | Pernyataan Sikap | Singkatan |
|:---:|:---|:---:|
| 1 | Sangat Tidak Setuju | STS |
| 2 | Tidak Setuju | TS |
| 3 | Netral / Ragu-ragu | N |
| 4 | Setuju | S |
| 5 | Sangat Setuju | SS |

*Sumber: Dikembangkan untuk instrumen kuesioner penelitian, 2026.*"""
        s = tab31_pattern.sub(tab31_md, s)

    # Convert Table 3.2
    if r"\caption{Operasionalisasi Variabel Penelitian}" in s:
        tab32_pattern = re.compile(r'\\begingroup.*?\\caption\{Operasionalisasi Variabel Penelitian\}.*?\\endgroup', re.DOTALL)
        tab32_md = """**Tabel 3.2 Operasionalisasi Variabel Penelitian**

| Variabel | Definisi Operasional | Dimensi | Indikator Pernyataan | Skala |
|:---|:---|:---|:---|:---:|
| **Impulsive Buying ($Y$)** | Kecenderungan membeli *booster pack* Pokémon TCG tanpa rencana awal dan didorong emosi sesaat (Rook, 1987; Verplanken & Herabadi, 2001). | Kognitif | Y1. Saya sering membeli *booster pack* kartu Pokémon tanpa rencana anggaran sebelumnya. | Likert 1–5 |
| | | Kognitif | Y2. Saya tidak mempertimbangkan dampak finansial saat membeli kartu Pokémon di toko. | Likert 1–5 |
| | | Afektif | Y3. Saya merasa terdorong secara spontan untuk membeli *pack* saat melihatnya di etalase toko. | Likert 1–5 |
| | | Afektif | Y4. Saya merasakan kegembiraan sesaat ketika memutuskan membeli kartu secara mendadak. | Likert 1–5 |
| | | Kognitif | Y5. Saya sering membeli *pack* lebih banyak dari yang semula saya niatkan. | Likert 1–5 |
| | | Afektif | Y6. Saya sulit menahan hasrat berbelanja kartu Pokémon saat rilis seri baru. | Likert 1–5 |
| **Hedonic Motivation ($X_1$)** | Motivasi belanja untuk kesenangan emosional dan sensasi petualangan (Arnold & Reynolds, 2003). | *Adventure* | X1.1. Membuka kemasan *booster pack* memberikan sensasi petualangan dan kejutan mendebarkan. | Likert 1–5 |
| | | *Adventure* | X1.2. Saya menikmati sensasi penasaran terhadap kartu acak di dalam kemasan bungkus. | Likert 1–5 |
| | | *Gratification* | X1.3. Membeli kartu Pokémon adalah cara saya memanjakan diri atau melepas penat stres. | Likert 1–5 |
| | | *Gratification* | X1.4. Menemukan kartu dengan ilustrasi langka (*SAR*) membuat saya sangat bahagia. | Likert 1–5 |
| | | *Idea* | X1.5. Saya senang mengikuti tren rilis seri kartu Pokémon dan inovasi desain terbarunya. | Likert 1–5 |
| **Desire for Completeness ($X_2$)** | Dorongan psikologis menuntaskan set koleksi akibat *Zeigarnik Effect* (Belk, 1995; Gao et al., 2014; Barasz et al., 2017). | *Cognitive Tension* | X2.1. Saya merasa tidak nyaman ketika album koleksi kartu Pokémon saya memiliki slot kosong. | Likert 1–5 |
| | | *Drive for Closure* | X2.2. Saya terdorong untuk terus membeli *booster pack* agar dapat melengkapi seluruh kartu dalam satu seri. | Likert 1–5 |
| | | *Cognitive Tension* | X2.3. Mengetahui ada kartu yang belum saya miliki dalam suatu seri membuat saya ingin segera membelinya. | Likert 1–5 |
| | | *Wholeness* | X2.4. Melengkapi satu set penuh kartu Pokémon memberikan perasaan pencapaian dan kepuasan batin. | Likert 1–5 |
| | | *Drive for Closure* | X2.5. Semakin sedikit kartu yang kurang dalam satu seri, semakin kuat desakan saya membeli *pack* baru. | Likert 1–5 |
| **Speculative Motive ($X_3$)** | Ekspektasi memperoleh keuntungan finansial dari apresiasi harga di pasar sekunder (Shiller, 2000; Baur et al., 2018). | Ekspektasi Cuan | X3.1. Saya membeli *pack* dengan harapan menarik kartu langka bernilai jual tinggi. | Likert 1–5 |
| | | Likuiditas | X3.2. Likuiditas pasar sekunder yang aktif mendorong saya membeli kartu sebagai aset berharga. | Likert 1–5 |
| | | *Capital Gain* | X3.3. Saya memantau kenaikan harga pasar kartu langka untuk dijual kembali demi keuntungan. | Likert 1–5 |
| | | Potensi Nilai | X3.4. Saya memandang modal membeli beberapa *pack* sebanding dengan potensi laba kartu langka. | Likert 1–5 |
| | | *Grading Value* | X3.5. Saya tertarik dengan sertifikasi keaslian (*grading*) kartu demi menaikkan nilai investasi lelang. | Likert 1–5 |
| **Self-Control ($M$)** | Kapasitas volisional menolak godaan belanja spontan dan menunda kepuasan sesaat (Tangney et al., 2004; Vohs & Faber, 2007; Sultan et al., 2012). | Tahan Godaan | M1. Saya mampu menolak godaan membeli barang menarik jika di luar perencanaan anggaran saya. | Likert 1–5 |
| | | Non-Impulsif | M2. Saya terbiasa berpikir tenang dan mempertimbangkan dampak pengeluaran sebelum bertransaksi. | Likert 1–5 |
| | | Tunda Kepuasan | M3. Saya mampu menahan diri dari kesenangan belanja saat ini demi menjaga tujuan keuangan masa depan. | Likert 1–5 |
| | | Disiplin Diri | M4. Saya memiliki disiplin diri yang kuat untuk tidak membeli barang secara mendadak di kasir toko. | Likert 1–5 |
| | | Kontrol Emosi | M5. Saya tidak mudah terhanyut oleh suasana hati atau kegembiraan sesaat dalam membelanjakan uang. | Likert 1–5 |
| | | Taat Anggaran | M6. Saya secara konsisten mematuhi alokasi batas pengeluaran hobi yang telah saya rencanakan. | Likert 1–5 |

*Sumber: Diadaptasi dari instrumen penelitian terdahulu yang tervalidasi (2026).*"""
        s = tab32_pattern.sub(tab32_md, s)

    # Hierarchical section and subsection numbering via split
    parts = re.split(r'\\subsection\{(.+)\}', s)
    new_text = parts[0]
    subsec_idx = 1
    for i in range(1, len(parts), 2):
        sub_title = parts[i].strip()
        sub_title = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', sub_title)
        sub_title = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', sub_title)
        
        sub_body = parts[i + 1]
        subsubsec_idx = 1
        
        def replace_subsub(m):
            nonlocal subsubsec_idx
            sstitle = m.group(1).strip()
            sstitle = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', sstitle)
            sstitle = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', sstitle)
            res = f"\n### {chapter_num}.{subsec_idx}.{subsubsec_idx} {sstitle}\n"
            subsubsec_idx += 1
            return res
        
        sub_body = re.sub(r'\\subsubsection\{(.+)\}', replace_subsub, sub_body)
        new_text += f"\n## {chapter_num}.{subsec_idx} {sub_title}\n" + sub_body
        subsec_idx += 1
    
    s = new_text
    s = re.sub(r'\\paragraph\{([^}]+)\}', r'\n**\1**\n', s)

    # Convert citations using bibcite mapping
    def resolve_citep(match):
        keys = [k.strip() for k in match.group(1).split(',')]
        res = []
        for k in keys:
            if k in cite_dict:
                res.append(f"{cite_dict[k][0]}, {cite_dict[k][1]}")
            else:
                res.append(k)
        return f"({'; '.join(res)})"

    def resolve_citet(match):
        keys = [k.strip() for k in match.group(1).split(',')]
        res = []
        for k in keys:
            if k in cite_dict:
                res.append(f"{cite_dict[k][0]} ({cite_dict[k][1]})")
            else:
                res.append(k)
        return "; ".join(res)

    def resolve_citealp(match):
        keys = [k.strip() for k in match.group(1).split(',')]
        res = []
        for k in keys:
            if k in cite_dict:
                res.append(f"{cite_dict[k][0]}, {cite_dict[k][1]}")
            else:
                res.append(k)
        return '; '.join(res)

    s = re.sub(r'\\citealp\{([^}]+)\}', resolve_citealp, s)
    s = re.sub(r'\\citep\{([^}]+)\}', resolve_citep, s)
    s = re.sub(r'\\citet\{([^}]+)\}', resolve_citet, s)
    s = re.sub(r'\\cite\{([^}]+)\}', resolve_citep, s)

    # Convert math equations
    s = re.sub(r'\\begin\{equation\}\s*(.*?)\s*\\label\{[^}]+\}\s*\\end\{equation\}', r'\n$$\1$$\n', s, flags=re.DOTALL)
    s = re.sub(r'\\begin\{equation\}\s*(.*?)\s*\\end\{equation\}', r'\n$$\1$$\n', s, flags=re.DOTALL)
    s = re.sub(r'\\\[\s*(.*?)\s*\\\]', r'\n$$\1$$\n', s, flags=re.DOTALL)

    # Convert formatting
    s = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', s)
    s = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', s)
    s = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', s)
    s = re.sub(r'\\textsuperscript\{([^}]+)\}', r'^\1^', s)
    s = s.replace(r'\%', '%')
    s = s.replace(r'\_', '_')
    s = s.replace(r'\&', '&')
    s = s.replace('___PCT___', '%').replace('___AMP___', '&').replace('___US___', '_')
    s = s.replace(r'--', '–')
    s = s.replace(r'---', '—')
    # Restore table markdown separator dashes if affected
    cleaned_lines = []
    for l in s.splitlines():
        if l.strip().startswith('|') and ('--' in l or '–' in l) and not any(c.isalnum() for c in l):
            l = l.replace('–', '-')
        cleaned_lines.append(l)
    s = '\n'.join(cleaned_lines)
    s = s.replace(r'\noindent', '')
    # Self-anneal 18 Sep 2026 (Simple Slopes DOCX): '\par' hanya sebagai perintah
    # mandiri — replace naif merusak '\partial' (turunan parsial), '\parindent',
    # '\parskip' sehingga rumus \frac bocor sebagai teks mentah di MD/DOCX.
    s = re.sub(r'\\par(?![A-Za-z])', '\n', s)
    s = re.sub(r'\\vspace\{[^}]+\}', '', s)
    s = re.sub(r'\\hspace\{[^}]+\}', '', s)

    # Clean lists
    s = re.sub(r'\\begin\{enumerate\}', '', s)
    s = re.sub(r'\\end\{enumerate\}', '', s)
    s = re.sub(r'\\begin\{itemize\}', '', s)
    s = re.sub(r'\\end\{itemize\}', '', s)
    s = re.sub(r'\\item\s*', '\n- ', s)
    s = re.sub(r'\n\s*\n\s*-\s*', '\n- ', s)
    # Pedoman/kakak tingkat 23 Sep 2026: Rumusan Masalah (1.2) & Tujuan (1.3)
    # wajib penomoran angka 1-6 (bukan bullet) — selaras enumerate PDF.
    s = _number_rumusan_tujuan(s)

    # Clean table refs and figure refs
    s = re.sub(r'Tabel~\\ref\{tab:penelitian_terdahulu\}', 'Tabel 2.1', s)
    s = re.sub(r'Tabel~\\ref\{tab:ringkasan_penelitian\}', 'Tabel 2.1', s)
    s = re.sub(r'Tabel~\\ref\{tab:skala_likert\}', 'Tabel 3.1', s)
    s = re.sub(r'Tabel~\\ref\{tab:operasionalisasi\}', 'Tabel 3.2', s)
    s = re.sub(r'Gambar~\\ref\{fig:rerangka_penelitian\}', 'Gambar 2.1', s)
    s = re.sub(r'Gambar~\\ref\{fig:rerangka\}', 'Gambar 2.1', s)
    s = re.sub(r'Persamaan~\\ref\{eq:model1_regresi\}', 'Persamaan (3.3)', s)
    s = re.sub(r'Persamaan~\\ref\{eq:model2_mra\}', 'Persamaan (3.4)', s)
    s = re.sub(r'Persamaan~\\ref\{eq:f_change\}', 'Persamaan (3.5)', s)
    s = re.sub(r'Gambar~\\ref\{fig:alur_penelitian\}', 'Gambar 3.1', s)
    s = re.sub(r'Tabel~\\ref\{tab:jadwal_penelitian\}', 'Tabel 3.3', s)
    s = re.sub(r'Gambar~\\ref\{fig:media_franchise_ranking\}', 'Gambar 1.1', s)
    s = re.sub(r'Gambar~\\ref\{fig:pokemon_card_growth\}', 'Gambar 1.2', s)
    s = re.sub(r'Gambar~\\ref\{fig:pricecharting_disparity\}', 'Gambar 1.3', s)
    s = re.sub(r'Tabel~\\ref\{tab:research_gap\}', 'Tabel 1.1', s)
    s = re.sub(r'~\\ref\{[^}]+\}', '', s)

    # Clean extra blank lines
    s = re.sub(r'\n{3,}', '\n\n', s)

    return s.strip()


def _number_rumusan_tujuan(s: str) -> str:
    """Renumber `- ` items to `1.`-`6.` inside 1.2 & 1.3 sections only."""
    lines = s.splitlines()
    out = []
    in_target = False
    counter = 0
    for ln in lines:
        stripped = ln.strip()
        if stripped.startswith('## '):
            in_target = stripped in ('## 1.2 Perumusan Masalah',
                                     '## 1.3 Tujuan Penelitian')
            counter = 0
            out.append(ln)
            continue
        if in_target and stripped.startswith('- '):
            counter += 1
            out.append('%d. %s' % (counter, stripped[2:].lstrip()))
            continue
        out.append(ln)
    return '\n'.join(out)

if __name__ == '__main__':
    main()

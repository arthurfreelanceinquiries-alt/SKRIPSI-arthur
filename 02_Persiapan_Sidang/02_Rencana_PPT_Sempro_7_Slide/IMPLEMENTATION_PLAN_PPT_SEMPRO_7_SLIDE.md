# 🛠️ IMPLEMENTATION PLAN: Eksekusi Teknis Slide Deck Sempro 7 Slide
### *Panduan Implementasi Multi-Platform untuk AI Generator (Python, HTML, Marp, atau Office)*

> [!SUMMARY] Tujuan & Solusi Dokumen Ini
> - **Untuk Apa:** Dokumen rencana implementasi teknis (*Technical Implementation Plan*) yang memandu AI mana pun dalam membangun slide deck 7 slide secara presisi, baik menggunakan skrip Python (`python-pptx`), kode web (HTML/CSS), format Marp Markdown, maupun integrasi aplikasi presentasi.
> - **Masalah yang Diselesaikan:** Menghilangkan kebingungan tata letak, koordinat elemen grafis, kontras warna, dan hierarki font; menyediakan resep kode siap jalan tanpa dependensi eksternal yang rumit.
> - **Keputusan/Output:** Spesifikasi teknis desain sistem, variabel warna/font, blueprint koordinat visual, serta contoh implementasi skrip generator otomatis.

---

## 📐 1. Spesifikasi Format & Desain Sistem

* **Aspek Rasio:** 16:9 Widescreen (1920 × 1080 px atau 13,33 × 7,5 inci di PowerPoint).
* **Palet Warna (FinTech Dark Mode):**
  - `COLOR_BG`: `#0B0F19` (Deep Navy Black)
  - `COLOR_CARD_BG`: `#1E293B` (Slate Container)
  - `COLOR_CARD_BORDER`: `#334155` (Subtle Slate Border)
  - `COLOR_TEXT_PRIMARY`: `#F8FAFC` (Pure White, 95% opacity)
  - `COLOR_TEXT_SECONDARY`: `#94A3B8` (Cool Slate Muted)
  - `COLOR_ACCENT_CYAN`: `#06B6D4` (Electric Cyan — Variabel Independen X & Metrik)
  - `COLOR_ACCENT_GREEN`: `#10B981` (Emerald Green — Variabel Dependen Y & Sukses)
  - `COLOR_ACCENT_PURPLE`: `#8B5CF6` (Violet / Purple — Variabel Moderasi Z)
  - `COLOR_ACCENT_AMBER`: `#F59E0B` (Amber Gold — Fenomena Pasar & Peringatan)
* **Tipografi:**
  - Font Judul: `Plus Jakarta Sans`, `Montserrat`, atau `Arial Black` (Bold / SemiBold).
  - Font Isi / Data: `Inter`, `Roboto`, atau `Calibri` (Regular / Medium).

---

## 🏗️ 2. Pilihan Opsi Arsitektur Teknis bagi AI Penerima

AI penerima dapat memilih salah satu dari 3 metode implementasi di bawah ini sesuai kapabilitas eksekusinya:

### 🌟 Opsi A: Skrip Python `python-pptx` (Sangat Direkomendasikan untuk File `.pptx` Native)
* **Keunggulan:** Menghasilkan berkas `.pptx` yang 100% dapat diedit (*fully editable*) di Microsoft PowerPoint, Google Slides, maupun Keynote.
* **Dependensi:** `pip install python-pptx`
* **Fitur:** Widescreen 16:9, shape cards dengan solid color fill, formatted text frames, multi-level paragraphs, dan catatan pembicara (*speaker notes*) otomatis tertanam di setiap slide.

### 🌐 Opsi B: Slide Web Interaktif (HTML5 + CSS Grid / Flexbox)
* **Keunggulan:** Tampilan visual piksel sempurna (*pixel-perfect*), dapat dibuka langsung di browser web apa pun, mendukung navigasi tombol keyboard panah kiri/kanan, dan siap diekspor ke PDF via tombol `Ctrl + P`.
* **Fitur:** Dark mode native, gradient border, responsive cards, zero-runtime framework (hanya 1 file `index.html` tunggal yang mandiri).

### 📝 Opsi C: Marp / Deckset Markdown
* **Keunggulan:** Ringan, mudah dibaca, berbasis sintaks Markdown standar.

---

## 📋 3. Blueprint Data Teknis per Slide (Kode Konten)

AI yang mengeksekusi harus menginjeksi data presisi berikut ke dalam ke-7 slide:

```python
SLIDES_DATA = [
    # SLIDE 1
    {
        "slide_number": 1,
        "type": "cover",
        "badge": "SEMINAR PROPOSAL SKRIPSI — S1 MANAJEMEN KEUANGAN",
        "title": "PENGARUH HEDONIC MOTIVATION, DESIRE FOR COMPLETENESS, DAN SPECULATIVE MOTIVE TERHADAP IMPULSIVE BUYING BOOSTER PACK KARTU POKÉMON TCG DENGAN SELF-CONTROL SEBAGAI VARIABEL MODERASI",
        "author": {
            "name": "Arthur Reezan",
            "nim": "312023002",
            "role": "Mahasiswa Peneliti"
        },
        "supervisor": {
            "name": "Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A",
            "role": "Dosen Pembimbing"
        },
        "institution": "Fakultas Ekonomi dan Bisnis — Universitas Kristen Krida Wacana — Jakarta 2026",
        "notes": "Selamat pagi/siang Bapak/Ibu Dewan Penguji dan Dosen Pembimbing, Ibu Dr. Fredella Colline. Terima kasih atas waktu dan kesempatan yang diberikan. Hari ini saya, Arthur Reezan, akan mempresentasikan usulan proposal skripsi saya mengenai faktor pendorong impulsive buying kartu Pokémon TCG dan peran moderasi self-control."
    },
    # SLIDE 2
    {
        "slide_number": 2,
        "type": "background_context",
        "title": "LATAR BELAKANG: FENOMENA BISNIS & MASALAH",
        "subtitle": "Pergeseran TCG Menjadi Komoditas Investasi & Maraknya Pembelian Impulsif",
        "cards": [
            {
                "title": "Pasar Pokémon TCG Masif",
                "accent": "#F59E0B",
                "highlight": "> 64,8 Miliar Kartu",
                "points": [
                    "Penjualan global kartu Pokémon melampaui 64,8 miliar unit (The Pokémon Company, 2024).",
                    "Pasar Indonesia berkembang pesat pasca rilis resmi kartu berbahasa Indonesia (2019)."
                ]
            },
            {
                "title": "Mekanisme Blind-Box / Gacha",
                "accent": "#06B6D4",
                "highlight": "Probabilistic Reward",
                "points": [
                    "Booster pack dijual tertutup; konsumen membeli ketidakpastian kartu.",
                    "Memicu sensasi dopamin, near-miss effect, dan dorongan berburu kartu langka (secret rare)."
                ]
            },
            {
                "title": "Masalah: Impulsive Buying",
                "accent": "#EF4444",
                "highlight": "Finansial Terancam",
                "points": [
                    "Pembelian spontan (unplanned), emosional, dan berulang tanpa evaluasi konsekuensi finansial.",
                    "Berpotensi mengorbankan alokasi keuangan pribadi. (JANGAN klaim dana darurat/paylater — tidak ada di naskah!)"
                ]
            }
        ],
        "notes": "Bapak dan Ibu penguji, fenomena bisnis berakar dari ledakan Pokémon TCG yang kini bernilai miliaran rupiah dengan penjualan global 64,8 miliar kartu. Masalahnya, sistem gacha/blind-box memicu impulsivitas pembelian yang membuat kolektor mengabaikan rasionalitas ekonomi."
    },
    # SLIDE 3
    {
        "slide_number": 3,
        "type": "research_gap",
        "title": "LATAR BELAKANG: RESEARCH GAP & KEBATUAN",
        "subtitle": "Kesenjangan Temuan Empiris Terdahulu & Novelty Model Riset",
        "cards": [
            {
                "title": "Inkonsistensi Gap Empiris",
                "accent": "#06B6D4",
                "items": [
                    "Gap X1 (Hedonis): Pranggabayu (2022) menemukan pengaruh positif, namun Apidana (2022) menemukan faktor utilitas tetap dominan pada produk hobi mahal.",
                    "Gap X2 (Kelengkapan): Efek pseudo-set framing Barasz et al. (2017) belum diuji pada produk fisik berbasis kartu acak di Indonesia.",
                    "Gap X3 (Spekulasi): Aryadi & Lingga (2024) mencatat PSA 10 memicu FOMO, sementara Colline (2024) menemukan investor rasional bersikap kalkulatif."
                ]
            },
            {
                "title": "Kebaruan Penelitian (Novelty)",
                "accent": "#10B981",
                "items": [
                    "Tiga anteseden (hedonis, kelengkapan set, spekulasi) diuji simultan pada satu komoditas hobi berpasar sekunder aktif.",
                    "Self-Control (M) sebagai Variabel Moderasi: menguji kapasitas pengendalian diri dalam meredam impulsivitas belanja kartu fisik.",
                    "Studi pionir kartu Pokemon TCG berbahasa Indonesia di FEB UKRIDA."
                ]
            }
        ],
        "notes": "Penelitian ini memiliki landasan empiris kuat karena terdapat perbedaan hasil studi sebelumnya mengenai motif hedonis dan spekulatif. Kebaruan riset saya adalah menguji efek penyelesaian set kartu dan menghadirkan Self-Control sebagai pemoderasi penahan impulsivitas."
    },
    # SLIDE 4
    {
        "slide_number": 4,
        "type": "literature_review",
        "title": "TINJAUAN PUSTAKA: TEORI & VARIABEL",
        "subtitle": "Pijakan Teoretis Multidisiplin & Pengukuran Skala Baku",
        "theories": [
            "Grand Theory: Behavioral Finance (Simon, 1955; Kahneman & Tversky, 1979; Shiller, 2000; Thaler & Shefrin, 1981) — Menjelaskan bias psikologis keputusan keuangan.",
            "Supporting Theory: S-O-R (Mehrabian & Russell, 1974), Completing the Set / Zeigarnik Effect (Gao, 2014; Barasz et al., 2017), Teori Regulasi Diri (Baumeister, 2002)."
        ],
        "variables": [
            {"var": "Y: Impulsive Buying", "scale": "IBTS (Verplanken & Herabadi, 2001)", "desc": "Pembelian spontan tanpa evaluasi konsekuensi."},
            {"var": "X1: Hedonic Motivation", "scale": "Arnold & Reynolds (2003), 5 dimensi diadaptasi", "desc": "Belanja untuk kesenangan & pelepasan stres."},
            {"var": "X2: Desire for Completeness", "scale": "Gao (2014); Barasz et al. (2017)", "desc": "Dorongan melengkapi master set koleksi."},
            {"var": "X3: Speculative Motive", "scale": "Keynes (1936); Shiller (2000)", "desc": "Ekspektasi keuntungan arbitrase pasar sekunder."},
            {"var": "M: Self-Control (Moderasi)", "scale": "BSCS (Tangney et al., 2004)", "desc": "Kapasitas menahan dorongan sesaat."}
        ],
        "notes": "Riset ini berakar pada Grand Theory Behavioral Finance, didukung teori regulasi diri Baumeister dan pseudo-set framing Barasz. Seluruh variabel operasional diukur menggunakan instrumen baku internasional yang valid dan reliabel."
    },
    # SLIDE 5
    {
        "slide_number": 5,
        "type": "conceptual_model",
        "title": "KERANGKA KONSEPTUAL & HIPOTESIS",
        "subtitle": "Model Moderated Regression Analysis (MRA) dengan TEPAT 6 Hipotesis",
        "hypotheses": [
            "H1 (+): Hedonic Motivation berpengaruh positif terhadap Impulsive Buying.",
            "H2 (+): Desire for Completeness berpengaruh positif terhadap Impulsive Buying.",
            "H3 (+): Speculative Motive berpengaruh positif terhadap Impulsive Buying.",
            "H4 (Meredam -): Self-Control memoderasi (meredam) pengaruh Hedonic Motivation terhadap Impulsive Buying.",
            "H5 (Meredam -): Self-Control memoderasi (meredam) pengaruh Desire for Completeness terhadap Impulsive Buying.",
            "H6 (Meredam -): Self-Control memoderasi (meredam) pengaruh Speculative Motive terhadap Impulsive Buying."
        ],
        "notes": "Dari telaah pustaka, saya merumuskan TEPAT 6 hipotesis. H1 hingga H3 menguji pengaruh langsung variabel X terhadap Y, H4 hingga H6 menguji peran moderasi Self-Control yang dihipotesiskan meredam belanja impulsif. DILARANG membuat H7; DILARANG menggambar panah langsung M ke Y sebagai hipotesis."
    },
    # SLIDE 6
    {
        "slide_number": 6,
        "type": "methodology",
        "title": "METODE PENELITIAN & ANALISIS DATA",
        "subtitle": "Desain Riset Kuantitatif & Strategi Analisis MRA",
        "quadrants": [
            {
                "title": "1. Desain & Skala",
                "items": ["Kuantitatif Asosiatif Kausal", "Kuesioner Google Forms", "Skala Likert 5 Poin (1-5)"]
            },
            {
                "title": "2. Populasi & Sampel",
                "items": ["Kolektor WNI, populasi infinite", "Purposive Sampling, target N = 120-150 (+ pilot n = 30)", "Kriteria: WNI domisili Indonesia, Usia >= 17 th, beli pack fisik min. 1x/12 bln (diutamakan 6 bln)"]
            },
            {
                "title": "3. Uji Kualitas Data",
                "items": ["Validitas Pearson Product Moment", "Reliabilitas Cronbach's Alpha (>= 0.70)", "Asumsi Klasik: Normalitas, Multikolinearitas, Heteroskedastisitas"]
            },
            {
                "title": "4. Analisis Data (MRA)",
                "items": ["MRA dengan teknik Mean-Centering (cegah multikolinearitas struktural)", "Uji t parsial, Uji F simultan", "Koefisien Determinasi R2 & Delta R2"]
            }
        ],
        "notes": "Riset menggunakan metode kuantitatif asosiatif dengan purposive sampling target 120-150 responden kolektor WNI (plus pilot n = 30). Analisis menggunakan MRA dengan teknik mean-centering guna mereduksi multikolinearitas non-esensial prediktor-interaksi."
    },
    # SLIDE 7
    {
        "slide_number": 7,
        "type": "closing",
        "badge": "SESI TANYA JAWAB (Q&A)",
        "title": "SEKIAN & TERIMA KASIH",
        "subtitle": "Usulan Penelitian Proposal Skripsi — S1 Manajemen FEB UKRIDA",
        "contribution": "Penelitian ini diharapkan memperkaya literatur Behavioral Finance pada pasar hobi alternatif serta menjadi landasan praktis penguatan literasi keuangan generasi muda.",
        "contact": "Arthur Reezan | NIM: 312023002 | FEB UKRIDA",
        "notes": "Demikian paparan usulan proposal skripsi saya. Saya sangat menantikan saran, koreksi, dan masukan konstruktif dari Bapak dan Ibu Dewan Penguji. Terima kasih, waktu saya kembalikan kepada Ketua Sidang."
    }
]
```

---

## 🚀 4. Template Skrip Generator Python (`generate_sempro_7slides.py`)

Jika AI memilih eksekusi Python (`python-pptx`), gunakan pola implementasi berikut:

```python
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def create_deck(output_path="Proposal_Arthur_Sempro_7Slide_PokemonTCG.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # Warna Palet FinTech
    BG_COLOR = RGBColor(11, 15, 25)
    CARD_COLOR = RGBColor(30, 41, 59)
    TEXT_WHITE = RGBColor(248, 250, 252)
    TEXT_MUTED = RGBColor(148, 163, 184)
    ACCENT_CYAN = RGBColor(6, 182, 212)
    ACCENT_GREEN = RGBColor(16, 185, 129)
    ACCENT_AMBER = RGBColor(245, 158, 11)
    
    # Loop SLIDES_DATA dan render masing-masing slide
    # ... (Gunakan prs.slides.add_slide(blank_layout))
    
    prs.save(output_path)
    print(f"File berhasil dibuat: {output_path}")

if __name__ == "__main__":
    create_deck()
```

---

## 🔍 5. Verification & Quality Gates (QA)

Sebelum menyerahkan hasil akhir kepada Arthur, AI pembuat harus memvalidasi 4 gerbang kualitas:
1. **Gate 1 (Slide Count):** Total slide tepat berjumlah 7. Tidak boleh ada slide pembuka ganda atau slide lampiran yang tidak diminta.
2. **Gate 2 (Typography & Style):** Semua istilah asing (*impulsive buying*, *booster pack*, *hedonic motivation*, dll.) harus dicetak miring (*italic*).
3. **Gate 3 (No Wall of Text):** Tidak ada slide yang memiliki paragraf melebihi 3 baris berturut-turut. Harus berupa kartu informasi dengan poin ringkas.
4. **Gate 4 (Speaker Notes Embedded):** Setiap slide harus menyertakan *speaker notes* yang dapat dibaca presenter saat mode presentasi PowerPoint aktif.

# Mandatory Rule: Zero AI Telltale Markers in Final Deliverables

> **STATUS: INVIOLABLE PERMANENT DIRECTIVE**
> Every assistant, agent, and subagent producing user-facing files MUST read, comply with, and verify against this rule.
> Sibling rules: [[.agents/rules/mandatory_no_raw_latex_in_docx.md]] (raw LaTeX), [[.agents/rules/mandatory_thesis_sync_and_quality.md]] (parity).

---

## 1. Scope: Source vs Final

- **Source files** (`*.tex`, `*.md`, `*.py`) NATURALLY contain `$`, `*`, `#`, backticks — that is correct and untouched.
- **Final deliverables** (`*.pdf`, `*.docx`, `*.pptx`, rendered `*.html`) must read as human academic writing. No reader — especially an examiner — may ever see markup syntax. One visible marker = BUILD DIRTY.

## 2. Prohibited Markers in Finals (zero tolerance)

| # | Marker | Asal khas | Contoh bocor |
|:---:|:---|:---|:---|
| M1 | `$...$` / `$$...$$` math enclosure | LaTeX / Markdown AI | `$Y = \alpha + \beta_1 X_1$` tercetak harfiah |
| M2 | Perintah LaTeX harfiah | Konverter lalai | `\alpha`, `\beta_1`, `\bar{X}`, `\cdot`, `\begin{...}` |
| M3 | Bold/italic markdown | `**teks**`, `*teks*`, `__teks__` tercetak |
| M4 | Backtick / code fence | `` `kode` ``, ` ``` ` |
| M5 | Header markdown | `# Judul`, `## Sub` tercetak |
| M6 | Checkbox mentah | `- [ ]`, `- [x]` (di cetakan harus menjadi `☐`/`☑`) |
| M7 | Backslash yatim | `\ ` sisa escaping, `n.s.\ ` |
| M8 | Emoji di dokumen formal | Skripsi PDF/DOCX (nol emoji; materi belajar boleh secukupnya bila mesin render mendukungnya, jika tidak — buang) |
| M9 | Mustache/placeholder AI | `{{...}}`, `[Insert ...]`, `TODO`, `Lorem ipsum` |

## 3. Explicit Allowlist (legit academic content — NOT violations)

| Simbol | Status | Alasan |
|:---|:---|:---|
| `US$ 100,0 miliar`, `US$ 100B` | ✅ LEGIT | Notasi mata uang baku |
| `#SV107`, `#21`, `#1` | ✅ LEGIT | Nomor kartu / peringkat (huruf-angka menempel) |
| `X1*`, `X2*`, `X3*`, `M*`, `X₁*·M*` | ✅ LEGIT | Notasi statistik *mean-centered* (Bab 3) |
| Unicode `α β Δ → ≥ ≤ · × ₁ ₂ ₃ ² R² ΔR² −` | ✅ LEGIT | Tipografi ilmiah hasil konversi (bukan sintaks) |
| `Rp20.000`, `%`, `&` (dan), `1–5`, `±` | ✅ LEGIT | Teks normal Indonesia |
| `☐` / `☑` / `( )` / `(x)` | ✅ LEGIT | Checkbox cetak hasil konversi (`( )` untuk mesin tanpa glyph ☐) |

## 4. Conversion Mapping (wajib dipakai generator)

| Sumber | Cetakan final |
|:---|:---|
| `$X_1$`, `$Y$`, `$M$` | *X*₁, *Y*, *M* (italic + subscript unicode; di mesin tanpa italic: `X₁`, `Y`, `M`) |
| `$\alpha$`, `$\beta_1$`, `$\Delta R^2$` | `α`, `β₁`, `ΔR²` |
| `$\bar{X}$`, `$X^*$` | `X̄` / `X*` (notasi terpusat baku naskah) |
| `$\cdot$`, `$\ge$`, `$\le$` | `·`, `≥`, `≤` |
| `$$...$$` display math | Kalimat + simbol unicode (TIDAK boleh lolos bersarang `$`) |
| `**bold**`, `` `code` `` | Bold / teks polos |
| `- [ ]` | `☐` (atau `( )` pada PDF Helvetica/WinAnsi — ☐ tofu; hasil probe font 23 Sep 2026) |

## 5. Mandatory Verification Gate

```bash
python execution/verify_no_ai_markers.py
```

Exit `0` (`[PASS] Zero AI markers`) wajib sebelum file diserahkan ke user/pembimbing. Skrip memindai: DOCX utama + DOCX modular, PDF skripsi (teks ekstrak), PDF panduan belajar, PPTX sempro — dengan allowlist §3 agar tidak false alarm. Temuan = perbaiki di generator (prinsip self-anneal), bukan di file jadi.

r"""
generate_bab1_figures.py
Deterministic Python script (Layer 3) to generate publication-grade, 300 DPI
empirical graphics supporting Bab 1 of Arthur Reezan's Skripsi:
1. Gambar 1.1: Peringkat 10 Waralaba Media Berpendapatan Tertinggi di Dunia Sepanjang Masa
2. Gambar 1.2: Pertumbuhan Kumulatif Produksi Kartu Pokémon TCG Global (2019–2024)
3. Gambar 1.3: Estimasi Pangsa Pasar Industri Trading Card Game (TCG) Global (Donut Chart)

Adheres strictly to Buku Pedoman Penyusunan Tugas Akhir FEB UKRIDA 2023 (Model B):
- Typography: Times New Roman
- Resolution: 300 DPI PNG
- Elegant, non-distracting academic color palette
"""

import os
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Configure Matplotlib Global Typography
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'Times']
plt.rcParams['axes.edgecolor'] = '#CCCCCC'
plt.rcParams['axes.linewidth'] = 0.8

# Palette
NAVY_PRIMARY = '#1A365D'
GOLD_ACCENT = '#D69E2E'
SLATE_MUTED = '#4A5568'
SLATE_LIGHT = '#718096'
BG_LIGHT = '#F8FAFC'
CRIMSON_ACCENT = '#9B2C2C'
BLUE_ACCENT = '#2B6CB0'

OUTPUT_DIR = Path(r"d:\Perkuliahan\Skripsi\SKRIPSI-arthur\01_Naskah_Utama\images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_figure_1_1():
    """Gambar 1.1: 10 Waralaba Media Berpendapatan Tertinggi di Dunia"""
    print("[1/3] Generating Gambar 1.1: Top 10 Media Franchises Worldwide...")

    franchises = [
        "Spider-Man",
        "Harry Potter",
        "Super Mario",
        "Marvel Cinematic U.",
        "Anpanman",
        "Disney Princess",
        "Star Wars",
        "Winnie the Pooh",
        "Mickey Mouse",
        "Pokémon"
    ]
    
    revenues = [31.8, 34.5, 38.0, 38.5, 44.9, 45.4, 46.7, 48.5, 52.2, 105.0]
    owners = [
        "Marvel / Sony",
        "Warner Bros.",
        "Nintendo",
        "Disney / Marvel",
        "Froebel-kan",
        "Disney",
        "Lucasfilm / Disney",
        "Disney",
        "Disney",
        "The Pokémon Co. / Nintendo"
    ]

    fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    y_pos = np.arange(len(franchises))
    
    # Colors: Highlight Pokemon with Dark Navy + Gold border
    bar_colors = [SLATE_MUTED] * 9 + [NAVY_PRIMARY]
    edge_colors = [SLATE_MUTED] * 9 + [GOLD_ACCENT]
    edge_widths = [0.8] * 9 + [2.0]

    bars = ax.barh(y_pos, revenues, color=bar_colors, edgecolor=edge_colors, linewidth=edge_widths, height=0.65)

    # Add data labels
    for i, (bar, rev, owner) in enumerate(zip(bars, revenues, owners)):
        width = bar.get_width()
        if i == 9:  # Pokémon
            label_text = f"US$ {rev:.1f} Miliar (No. 1)"
            ax.text(width + 1.5, bar.get_y() + bar.get_height() / 2, label_text,
                    va='center', ha='left', fontsize=10, fontweight='bold', color=NAVY_PRIMARY)
        else:
            label_text = f"US$ {rev:.1f} M ({owner})"
            ax.text(width + 1.2, bar.get_y() + bar.get_height() / 2, label_text,
                    va='center', ha='left', fontsize=8.5, color='#333333')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(franchises, fontsize=10, fontweight='normal')
    # Bold the Pokemon label
    ax.get_yticklabels()[9].set_fontweight('bold')
    ax.get_yticklabels()[9].set_color(NAVY_PRIMARY)

    ax.set_xlabel("Estimasi Pendapatan Kumulatif Sepanjang Masa (Miliar Dolar AS / US$ Billion)", 
                  fontsize=9.5, fontweight='bold', labelpad=8)
    ax.set_xlim(0, 125)
    
    # Clean grid
    ax.xaxis.grid(True, linestyle='--', alpha=0.5, color='#E2E8F0')
    ax.yaxis.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#A0AEC0')
    ax.spines['bottom'].set_color('#A0AEC0')

    # Sub-annotation
    ax.text(0.98, 0.04, "*Estimasi mencakup penjualan merchandise, TCG, box office, & video game.",
            transform=ax.transAxes, fontsize=7.5, fontstyle='italic', color='#718096', ha='right')

    plt.tight_layout()
    output_path = OUTPUT_DIR / "gambar1_1_media_franchise_ranking.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"    -> Saved successfully: {output_path}")


def generate_figure_1_2():
    """Gambar 1.2: Pertumbuhan Kumulatif Produksi Kartu Pokémon TCG Global (2019–2024)"""
    print("[2/3] Generating Gambar 1.2: Cumulative Card Production Growth...")

    years = ["2019\n(Mar)", "2020\n(Mar)", "2021\n(Mar)", "2022\n(Mar)", "2023\n(Mar)", "2024\n(Mar)"]
    cards = [28.8, 30.4, 34.1, 43.2, 52.9, 64.8]
    annual_add = ["-", "+1.6 M", "+3.7 M", "+9.1 M", "+9.7 M", "+11.9 M"]

    fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    x_pos = np.arange(len(years))
    
    # Bars
    bar_colors = ['#CBD5E0', '#CBD5E0', '#90CDF4', '#63B3ED', '#3182CE', NAVY_PRIMARY]
    bars = ax.bar(x_pos, cards, color=bar_colors, edgecolor='#A0AEC0', linewidth=1.0, width=0.55, zorder=3)

    # Line plot overlay
    ax.plot(x_pos, cards, color=CRIMSON_ACCENT, marker='o', markersize=7, linewidth=2.2, zorder=4, label="Tren Akumulasi Produksi")

    # Add data labels
    for i, (bar, val, add) in enumerate(zip(bars, cards, annual_add)):
        height = bar.get_height()
        # Top value
        ax.text(bar.get_x() + bar.get_width()/2, height + 1.2, f"{val:.1f} Miliar",
                ha='center', va='bottom', fontsize=9.5, fontweight='bold', 
                color=NAVY_PRIMARY if i == 5 else '#2D3748', zorder=5)
        # Delta value inside bar
        if i > 0:
            ax.text(bar.get_x() + bar.get_width()/2, height / 2, f"({add})",
                    ha='center', va='center', fontsize=8, color='#FFFFFF' if i >= 3 else '#2D3748', 
                    fontweight='bold', zorder=5)

    # Annotations for Milestones
    # 2020: Masuk ke Indonesia
    ax.annotate("Agustus 2019/2020:\nEkspansi Resmi Versi\nBahasa Indonesia (AKG Games)",
                xy=(1, 30.4), xytext=(0.5, 50),
                arrowprops=dict(arrowstyle="->", color=CRIMSON_ACCENT, lw=1.2),
                fontsize=7.8, fontweight='bold', color=CRIMSON_ACCENT,
                bbox=dict(boxstyle="round,pad=0.3", fc="#FFF5F5", ec=CRIMSON_ACCENT, lw=0.8),
                ha='center')

    # 2023-2024: Penetrasi Ritel Indomaret & Seri 151
    ax.annotate("2023–2024:\nPenetrasi Gerai Indomaret\n& Ledakan Seri 151",
                xy=(5, 64.8), xytext=(4.1, 73),
                arrowprops=dict(arrowstyle="->", color=NAVY_PRIMARY, lw=1.2),
                fontsize=7.8, fontweight='bold', color=NAVY_PRIMARY,
                bbox=dict(boxstyle="round,pad=0.3", fc="#EBF8FF", ec=NAVY_PRIMARY, lw=0.8),
                ha='center')

    ax.set_xticks(x_pos)
    ax.set_xticklabels(years, fontsize=9.5)
    ax.set_ylabel("Akumulasi Produksi Kartu Fisik (Miliar Lembar)", fontsize=9.5, fontweight='bold', labelpad=8)
    ax.set_ylim(0, 82)

    ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='#E2E8F0', zorder=0)
    ax.xaxis.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#A0AEC0')
    ax.spines['bottom'].set_color('#A0AEC0')

    # Note
    ax.text(0.98, 0.03, "*Data mencakup seluruh pencetakan resmi kartu Pokémon TCG global per akhir tahun fiskal (Maret).",
            transform=ax.transAxes, fontsize=7.5, fontstyle='italic', color='#718096', ha='right')

    plt.tight_layout()
    output_path = OUTPUT_DIR / "gambar1_2_pokemon_tcg_production_growth.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"    -> Saved successfully: {output_path}")


def generate_figure_1_3():
    """Gambar 1.3: Estimasi Pangsa Pasar Industri Trading Card Game (TCG) Global (Donut Chart)"""
    print("[3/3] Generating Gambar 1.3: Global TCG Market Share Donut Chart...")

    labels = [
        "Pokémon TCG",
        "Yu-Gi-Oh!",
        "Magic: The Gathering",
        "One Piece Card Game",
        "Lainnya (Digimon, dll.)"
    ]
    sizes = [41.5, 23.8, 21.2, 8.5, 5.0]
    colors = [NAVY_PRIMARY, '#3182CE', '#805AD5', '#DD6B20', '#A0AEC0']

    fig, ax = plt.subplots(figsize=(7.5, 4.6), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        pctdistance=0.75,
        textprops=dict(color="#2D3748", fontsize=9),
        wedgeprops=dict(width=0.45, edgecolor='#FFFFFF', linewidth=2)
    )

    # Format autotexts (percentages inside donut ring)
    for i, autotext in enumerate(autotexts):
        autotext.set_color('#FFFFFF')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(8.5)
        if i == 0:  # Pokemon
            autotext.set_fontsize(10)

    # Center text in hole
    ax.text(0, 0.08, "Pangsa Pasar\nTCG Global", ha='center', va='center', 
            fontsize=10, fontweight='bold', color=NAVY_PRIMARY)
    ax.text(0, -0.15, "2024", ha='center', va='center', 
            fontsize=9, color=SLATE_MUTED)

    ax.axis('equal')
    plt.tight_layout()
    output_path = OUTPUT_DIR / "gambar1_3_tcg_market_share_donut.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"    -> Saved successfully: {output_path}")


def main():
    print("=" * 60)
    print("GENERATING BAB 1 EMPIRICAL FIGURES (300 DPI, TIMES NEW ROMAN)")
    print("=" * 60)
    generate_figure_1_1()
    generate_figure_1_2()
    generate_figure_1_3()
    print("=" * 60)
    print("ALL 3 FIGURES GENERATED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    main()

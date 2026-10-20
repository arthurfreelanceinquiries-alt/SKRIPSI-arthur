"""
audit_difficult_words.py
Audit script to scan Proposal_Arthur_PokemonTCG.tex for overly heavy, pretentious,
pseudo-intellectual, or unnatural Indonesian phrases that can be simplified
for an undergraduate (S1) thesis defense, while preserving 100% of citations,
statistical terms, and empirical facts.
"""

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
TEX_FILE = ROOT / "01_Naskah_Utama" / "Proposal_Arthur_PokemonTCG.tex"

# List of precise replacements: (Target exact substring, Replacement, Explanation)
REPLACEMENTS = [
    # 1. Abstrak
    (
        "guna mereduksi multikolinearitas non-esensial",
        "guna mengurangi multikolinearitas non-esensial",
        "Penyederhanaan kata serapan 'mereduksi' menjadi 'mengurangi' yang lebih alami."
    ),
    
    # 2. Bab 1: Latar Belakang - pilar & antusiasme
    (
        "memegang peranan yang paling sentral",
        "memegang peranan yang sangat penting",
        "Menghilangkan hiperbola 'paling sentral' menjadi 'sangat penting'."
    ),
    (
        "mengonfirmasi terjadinya gelombang antusiasme belanja yang masif di kalangan konsumen.",
        "membuktikan tingginya antusiasme belanja di kalangan konsumen.",
        "Penyederhanaan frasa klise 'gelombang antusiasme belanja yang masif' menjadi lebih wajar."
    ),
    (
        "Minat masyarakat, khususnya mahasiswa dan Generasi Z, didorong oleh konvergensi fungsi rekreasi, prestise sosial, hobi koleksi kartu langka, dan motif spekulasi finansial.",
        "Minat masyarakat, khususnya mahasiswa dan Generasi Z, didorong oleh perpaduan antara fungsi hiburan, prestise sosial, hobi mengoleksi kartu langka, dan motif spekulasi finansial.",
        "Penggantian 'konvergensi' -> 'perpaduan antara fungsi hiburan...'."
    ),
    
    # 3. Bab 1: Latar Belakang - harga pasar sekunder
    (
        "mengalami apresiasi nilai pasar sekunder yang spektakuler, berkisar antara 2,0 kali lipat pada kartu langka utama (\\emph{Charizard VMAX \\#SV107}) hingga menembus 23,7 kali lipat (\\emph{Kyogre \\#21}) dan 26,0 kali lipat (\\emph{Reshiram \\#17}) dibandingkan kondisi kartu mentah tanpa sertifikasi \\citep{pricecharting2024}.",
        "mengalami lonjakan harga yang sangat tinggi di pasar sekunder, mulai dari 2,0 kali lipat pada kartu langka utama (\\emph{Charizard VMAX \\#SV107}) hingga menembus 23,7 kali lipat (\\emph{Kyogre \\#21}) dan 26,0 kali lipat (\\emph{Reshiram \\#17}) dibandingkan kondisi kartu mentah tanpa sertifikasi \\citep{pricecharting2024}.",
        "Menyederhanakan 'apresiasi nilai pasar sekunder yang spektakuler' menjadi 'lonjakan harga yang sangat tinggi di pasar sekunder'."
    ),
    (
        "Disparitas nilai yang ekstrem dan mekanisme kemasan acak berbasis probabilitas tersebut mendorong transaksi berlebihan: setiap seri baru diluncurkan, gerai diserbu antrean dan produk ludes dalam waktu singkat, sementara pembeli membeli \\emph{booster pack} berulang kali secara mendadak di kasir tanpa perencanaan anggaran.",
        "Perbedaan harga yang sangat jauh dan sistem kemasan acak berbasis probabilitas tersebut memicu pembelian berulang: setiap seri baru diluncurkan, gerai dipadati antrean dan produk terjual habis dalam waktu singkat, sementara konsumen membeli \\emph{booster pack} berulang kali secara spontan di kasir tanpa perencanaan anggaran.",
        "Penyederhanaan 'Disparitas nilai yang ekstrem' -> 'Perbedaan harga yang sangat jauh', 'ludes' -> 'terjual habis', 'secara mendadak' -> 'secara spontan'."
    ),
    
    # 4. Bab 1: Poin Novelty
    (
        "\\item \\textbf{Komoditas hibrida:} Riset terdahulu umumnya meneliti busana, makanan, atau belanja daring umum. Penelitian ini mengkaji kartu fisik koleksi berlisensi resmi yang memiliki pasar sekunder likuid terstandardisasi (\\emph{PSA 10 Gem Mint}).",
        "\\item \\textbf{Karakteristik Produk Bernilai Ganda:} Riset terdahulu umumnya meneliti busana, makanan, atau belanja daring umum. Penelitian ini meneliti kartu fisik koleksi berlisensi resmi yang memiliki pasar sekunder terstandardisasi (\\emph{PSA 10 Gem Mint}).",
        "Mengganti istilah 'Komoditas hibrida' menjadi 'Karakteristik Produk Bernilai Ganda' agar mudah dipertahankan mahasiswa."
    ),
    
    # 5. Bab 1: Narasi Anteseden (Keluhan Utama User: literatur perilaku konsumen & konvergensi)
    (
        "Secara teoretis, literatur perilaku konsumen mengonfirmasi bahwa keputusan pembelian impulsif dipicu oleh konvergensi antara stimulus lingkungan situasional dan kondisi psikologis internal individu \\citep{amos2014meta, iyer2020impulse, stern1962significance}. Dalam ekosistem kartu Pok\\'emon TCG fisik, cara kerja berbagai pendorong tersebut dapat dipahami secara nyata melalui skenario pengalaman sehari-hari konsumen berikut.",
        "Secara teoretis, berbagai penelitian tentang perilaku konsumen menunjukkan bahwa keputusan pembelian impulsif muncul karena perpaduan antara situasi di tempat belanja dan kondisi psikologis di dalam diri pembeli \\citep{amos2014meta, iyer2020impulse, stern1962significance}. Dalam pembelian kartu Pok\\'emon TCG fisik, cara kerja berbagai dorongan tersebut dapat dipahami secara nyata melalui skenario pengalaman sehari-hari konsumen berikut.",
        "Menyederhanakan frasa kaku 'literatur perilaku konsumen mengonfirmasi bahwa... dipicu oleh konvergensi...' menjadi kalimat bahasa Indonesia yang jernih dan wajar."
    ),
    
    # 6. Bab 1: Narasi Skenario (luapan dopamin, disparitas harga, rem volisional)
    (
        "melainkan membeli sensasi kejutan (\\emph{unboxing thrill}): luapan dopamin saat merobek kemasan foil acak demi menemukan kartu langka di dalamnya. Pemicu berdimensi \\textbf{afektif} atau pencarian kenikmatan emosional inilah yang dalam penelitian ini disebut",
        "melainkan membeli sensasi kejutan (\\emph{unboxing thrill}), yaitu rasa senang dan penasaran saat membuka kemasan acak demi menemukan kartu langka di dalamnya. Pemicu berdimensi \\textbf{afektif} atau pencarian kenikmatan emosional inilah yang dalam penelitian ini disebut",
        "Mengganti 'luapan dopamin saat merobek kemasan' (pop-neuroscience) menjadi kalimat deskriptif wajar."
    ),
    (
        "kartu tertentu dapat terjual hingga jutaan rupiah per lembar (lih.\\ disparitas harga pada Gambar 1.3). Realitas ini menyuntikkan pemicu berdimensi \\textbf{finansial}, yakni ilusi optimisme pasar dan ekspektasi keuntungan modal (\\emph{capital gain}) yang disebut",
        "kartu tertentu dapat terjual hingga jutaan rupiah per lembar (lih.\\ perbedaan harga pada Gambar 1.3). Realitas ini memberikan pemicu berdimensi \\textbf{finansial}, yakni ekspektasi keuntungan finansial (\\emph{capital gain}) yang disebut",
        "Mengganti 'disparitas harga' -> 'perbedaan harga' dan 'menyuntikkan pemicu' -> 'memberikan pemicu'."
    ),
    (
        "Di sinilah \\textbf{\\emph{Self-Control}} ($M$) memainkan peran krusial sebagai rem volisional: konsumen dengan kontrol diri yang prima mampu mengabaikan godaan visual kemasan dan menahan dorongan belanja spontan, sedangkan mereka yang lemah kontrol dirinya akan mudah terjerumus dalam transaksi berulang kali tanpa kendali \\citep{tangney2004high, baumeister2002yield}.",
        "Di sinilah \\textbf{\\emph{Self-Control}} ($M$) memegang peranan penting sebagai pengendali perilaku: konsumen dengan kontrol diri yang baik mampu menahan dorongan belanja spontan di gerai ritel, sedangkan konsumen dengan kontrol diri yang rendah akan lebih rentan melakukan pembelian berulang kali tanpa perencanaan yang matang \\citep{tangney2004high, baumeister2002yield}.",
        "Mengganti 'peran krusial sebagai rem volisional' -> 'memegang peranan penting sebagai pengendali perilaku', 'kontrol diri yang prima' -> 'kontrol diri yang baik', dan 'terjerumus dalam transaksi' -> 'rentan melakukan pembelian'."
    ),
    
    # 7. Bab 1: Tabel 1.1 Sumber
    (
        "\\footnotesize\\textit{Sumber: Data diolah dari sintesis kajian literatur empiris terdahulu (2026).}",
        "\\footnotesize\\textit{Sumber: Data diolah dari sintesis penelitian terdahulu (2026).}",
        "Menyederhanakan 'sintesis kajian literatur empiris terdahulu' menjadi 'sintesis penelitian terdahulu'."
    ),
    
    # 8. Bab 1: Alasan Geografis & Urgensi
    (
        "yang didistribusikan secara masif di area kasir gerai ritel modern",
        "yang dijual secara luas di area kasir gerai ritel modern",
        "Mengganti 'didistribusikan secara masif' menjadi 'dijual secara luas'."
    ),
    (
        "Berdasarkan latar belakang permasalahan, urgensi empiris, dan kebaruan konseptual tersebut, penelitian ini memberikan kebaruan dalam bidang manajemen keuangan perilaku dan perilaku konsumen di Indonesia.",
        "Berdasarkan latar belakang masalah, arti penting secara empiris, dan kebaruan konsep tersebut, penelitian ini memberikan kontribusi dalam bidang manajemen keuangan perilaku dan perilaku konsumen di Indonesia.",
        "Menghaluskan 'urgensi empiris' dan 'kebaruan konseptual' agar lebih wajar."
    ),
    (
        "\\item \\textbf{Pengayaan Literatur Moderasi Kontrol Diri (\\emph{Self-Control}):} Memperdalam pemahaman teoretis mengenai mekanisme regulasi diri",
        "\\item \\textbf{Kontribusi terhadap Kajian Kontrol Diri (\\emph{Self-Control}):} Memperdalam pemahaman teoretis mengenai peran pengendalian diri",
        "Menyederhanakan judul butir manfaat teoretis."
    ),
    
    # 9. Bab 2: Tinjauan Variabel Y & Tabel 2.1
    (
        "\\citet{verplanken2001individual} mengidentifikasi dua dimensi utama: (1) dimensi kognitif (ketiadaan perencanaan dan pengabaian anggaran); dan (2) dimensi afektif (luapan kegembiraan dan dorongan emosional tak tertahankan). \\citet{amos2014meta} menegaskan bahwa pembelian impulsif dipicu oleh konvergensi stimulus afektif, faktor kognitif internal, dan situasi pasar.",
        "\\citet{verplanken2001individual} mengidentifikasi dua dimensi utama: (1) dimensi kognitif (kurangnya perencanaan belanja dan pertimbangan anggaran); dan (2) dimensi afektif (kegembiraan mendadak dan dorongan emosional seketika). \\citet{amos2014meta} menegaskan bahwa pembelian impulsif dipicu oleh perpaduan antara dorongan emosi (afektif), pertimbangan kognitif internal, dan situasi pasar.",
        "Menyederhanakan 'luapan kegembiraan dan dorongan emosional tak tertahankan' dan 'konvergensi stimulus afektif'."
    ),
    (
        "kesenangan berbelanja menurunkan deliberasi rasional konsumen.",
        "kesenangan berbelanja menurunkan pertimbangan rasional konsumen.",
        "Mengganti 'deliberasi rasional' menjadi 'pertimbangan rasional'."
    ),
    
    # 10. Bab 2: Hipotesis & Dinamika Perilaku
    (
        "\\noindent\\textbf{Keterkaitan dengan Objek (Pok\\'emon TCG):} Disparitas harga antara harga resmi \\emph{pack} (Rp20.000--Rp30.000) dan potensi nilai kartu langka bergradasi \\emph{PSA 10 Gem Mint} (ratusan ribu hingga puluhan juta rupiah menurut pantauan pasar sekunder \\citep{pricecharting2024}) melahirkan ilusi keuntungan instan (\\emph{grading arbitrage}). Persepsi ini melumpuhkan kehati-hatian finansial dan memicu aksi borong \\emph{pack} secara spontan.",
        "\\noindent\\textbf{Keterkaitan dengan Objek (Pok\\'emon TCG):} Perbedaan harga antara harga resmi \\emph{pack} (Rp20.000--Rp30.000) dan potensi harga kartu langka bersertifikasi \\emph{PSA 10 Gem Mint} (ratusan ribu hingga puluhan juta rupiah menurut pantauan pasar sekunder \\citep{pricecharting2024}) melahirkan harapan keuntungan finansial (\\emph{grading arbitrage}). Harapan ini menurunkan kehati-hatian finansial konsumen dan mendorong pembelian banyak \\emph{pack} secara spontan.",
        "Mengganti 'Disparitas harga' -> 'Perbedaan harga', 'melumpuhkan kehati-hatian finansial' -> 'menurunkan kehati-hatian finansial', dan 'aksi borong' -> 'pembelian banyak'."
    ),
    (
        "tidak terjebak dalam euforia transaksi spekulatif berlebihan",
        "tidak terbawa antusiasme spekulasi yang berlebihan",
        "Menyederhanakan 'terjebak dalam euforia transaksi spekulatif berlebihan'."
    ),
    (
        "\\noindent\\textbf{Kajian Empiris Terdahulu:} Dukungan tak langsung (dinyatakan eksplisit): \\citet{katauke2023financial} membuktikan kapasitas literasi finansial berhubungan negatif dengan impulsivitas diskonto hiperbolik (Jepang, probit + IV), proksi regulasi rasional, bukan uji interaksi. \\citet{aryadi2024personal} dan \\citet{colline2024biases} mendokumentasikan kuatnya motif investasi koleksi (CM p=0,000) dan bias \\emph{herding} investor, keduanya bukti sisi pendorong spekulasi (ranah H3), bukan bukti efek meredam kontrol diri.",
        "\\noindent\\textbf{Kajian Empiris Terdahulu:} Dukungan tidak langsung (dinyatakan secara terbuka): \\citet{katauke2023financial} membuktikan bahwa literasi finansial berhubungan negatif dengan perilaku impulsif diskonto hiperbolik (Jepang, probit + IV), sebagai indikator pengendalian diri rasional, bukan pengujian interaksi moderasi. \\citet{aryadi2024personal} dan \\citet{colline2024biases} mendokumentasikan kuatnya motif investasi pada produk koleksi (CM $p = 0{,}000$) dan kecenderungan ikut-ikutan (\\emph{herding}) investor, keduanya merupakan bukti sisi pendorong spekulasi (pada hipotesis H3), bukan bukti peran kontrol diri dalam meredam pembelian.",
        "Menyederhanakan 'ranah H3' -> 'pada hipotesis H3', 'dinyatakan eksplisit' -> 'dinyatakan secara terbuka', dan 'efek meredam' -> 'peran kontrol diri dalam meredam pembelian'."
    ),
    
    # 11. Bab 3: Metode, Sampel & Operasionalisasi
    (
        "agar memori kognitif dan luapan afektif saat bertransaksi masih tersimpan segar dalam ingatan responden, sehingga data yang dilaporkan lebih dapat diandalkan.",
        "agar pengalaman dan dorongan saat bertransaksi masih tersimpan jelas dalam ingatan responden, sehingga data yang diperoleh lebih akurat.",
        "Menyederhanakan 'memori kognitif dan luapan afektif saat bertransaksi'."
    ),
    (
        "\\subsubsection{Prosedur Distribusi Kuesioner: Pendekatan Hibrida Dua Jalur}",
        "\\subsubsection{Prosedur Distribusi Kuesioner: Pendekatan Gabungan Dua Jalur (Daring dan Luring)}",
        "Memperjelas judul subsubbab distribusi kuesioner."
    ),
    (
        "pengumpulan data dilaksanakan melalui strategi \\textbf{distribusi hibrida dua jalur} yang saling melengkapi:",
        "pengumpulan data dilaksanakan melalui strategi \\textbf{distribusi gabungan dua jalur (daring dan luring)} yang saling melengkapi:",
        "Menghilangkan istilah kaku 'distribusi hibrida dua jalur'."
    ),
    (
        "Literatur metodologi kuantitatif \\citep{sekaran2016research, sugiyono2019metode} membagi pengambilan sampel ke dalam dua rumpun utama: \\emph{Probability Sampling} dan \\emph{Non-Probability Sampling}:",
        "Kajian metodologi penelitian kuantitatif \\citep{sekaran2016research, sugiyono2019metode} membagi teknik pengambilan sampel ke dalam dua kelompok utama: \\emph{Probability Sampling} dan \\emph{Non-Probability Sampling}:",
        "Menyederhanakan 'Literatur metodologi kuantitatif'."
    ),
    (
        "Operasionalisasi variabel penelitian disajikan secara komprehensif pada Tabel 3.2.",
        "Operasionalisasi variabel penelitian disajikan secara rinci pada Tabel 3.2.",
        "Mengganti kata pengisi 'secara komprehensif' menjadi 'secara rinci'."
    ),
    (
        "Dalam pengujian model penelitian kuantitatif eksplanatori yang melibatkan efek moderasi, terdapat beberapa alternatif metode analisis dalam literatur statistik:",
        "Dalam pengujian model penelitian kuantitatif yang menguji hubungan antarvariabel dengan efek moderasi, terdapat beberapa pilihan metode analisis dalam ilmu statistik:",
        "Menyederhanakan pembuka metode analisis MRA."
    ),
    (
        "\\item Prosedur pemusatan nilai rata-rata (\\emph{mean-centering}) diterapkan pada prediktor dan pemoderasi (skor asli dikurangi rata-ratanya), yang secara efektif mereduksi multikolinearitas non-esensial antara variabel prediktor dengan produk interaksinya tanpa mengubah nilai prediksi model ($R^2$) maupun koefisien interaksi, serta memfasilitasi interpretasi koefisien efek utama $\\beta_1, \\beta_2, \\beta_3$ pada nilai rata-rata pemoderasi ($M^* = 0$) \\citep{aiken1991multiple, hayes2018introduction}.",
        "\\item Prosedur pemusatan nilai rata-rata (\\emph{mean-centering}) diterapkan pada prediktor dan pemoderasi (skor asli dikurangi rata-ratanya), yang secara efektif mengurangi multikolinearitas non-esensial antara variabel prediktor dengan produk interaksinya tanpa mengubah nilai prediksi model ($R^2$) maupun koefisien interaksi, serta mempermudah interpretasi koefisien efek utama $\\beta_1, \\beta_2, \\beta_3$ pada nilai rata-rata pemoderasi ($M^* = 0$) \\citep{aiken1991multiple, hayes2018introduction}.",
        "Mengganti 'mereduksi' -> 'mengurangi' dan 'memfasilitasi interpretasi' -> 'mempermudah interpretasi'."
    ),
    (
        "dan \\emph{centering} hanya mereduksi multikolinearitas non-esensial);",
        "dan pemusatan nilai rata-rata (\\emph{centering}) hanya mengurangi multikolinearitas non-esensial);",
        "Mengganti 'mereduksi' -> 'mengurangi'."
    ),
    (
        "Observasi antrean rilis kartu fisik, \\emph{gacha booster pack}, disparitas harga lelang, dan \\emph{grading} PSA.",
        "Observasi antrean rilis kartu fisik, sistem acak (\\emph{gacha}) kemasan kartu, perbedaan harga lelang, dan sertifikasi kondisi kartu (\\emph{grading} PSA).",
        "Menjelaskan istilah visual diagram alir."
    ),
    (
        "Masukan berupa observasi antrean rilis dan disparitas harga; keluaran berupa rumusan fenomena",
        "Masukan berupa observasi antrean rilis dan perbedaan harga pasar; keluaran berupa rumusan fenomena",
        "Mengganti 'disparitas harga' -> 'perbedaan harga pasar'."
    ),
    (
        "2 & Studi kepustakaan dan telaah literatur jurnal &",
        "2 & Studi kepustakaan dan telaah jurnal ilmiah &",
        "Menyederhanakan 'telaah literatur jurnal' -> 'telaah jurnal ilmiah'."
    )
]

def apply_replacements(dry_run=True):
    content = TEX_FILE.read_text(encoding='utf-8')
    modified = content
    applied_count = 0
    
    print(f"Running audit on: {TEX_FILE.name}")
    print("=" * 80)
    
    for idx, (target, repl, explanation) in enumerate(REPLACEMENTS, 1):
        if target in modified:
            applied_count += 1
            print(f"[{idx:02d}] MATCH FOUND:")
            print(f"     Penjelasan : {explanation}")
            print(f"     Target     : {target[:70]}...")
            print(f"     Pengganti  : {repl[:70]}...")
            if not dry_run:
                modified = modified.replace(target, repl, 1)
        else:
            print(f"[{idx:02d}] NO MATCH: {target[:60]}...")
            
    print("=" * 80)
    print(f"Total Replacement Candidates Found: {applied_count} / {len(REPLACEMENTS)}")
    
    if not dry_run and applied_count > 0:
        TEX_FILE.write_text(modified, encoding='utf-8')
        print(f"SUCCESS: Changes written to {TEX_FILE.name}")
        
    return applied_count

if __name__ == "__main__":
    dry_run = "--apply" not in sys.argv
    apply_replacements(dry_run=dry_run)

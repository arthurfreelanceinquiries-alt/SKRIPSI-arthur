"""
Patch script for Bab 5 conclusions, recommendations, and Table 5.2 ampersand fix
"""

def main():
    tex_file = r"z:\Skripsi\latex\Skripsi_Arthur.tex"
    with open(tex_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Bab 5 Kesimpulan
    kesimpulan_old = r"""\begin{enumerate}
  \item \textbf{Portofolio Kredit Hijau (\emph{Green Financing}) berpengaruh positif dan signifikan terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025} ($\beta_1 = +0{,}042; p = 0{,}0003$). Peningkatan alokasi kredit pada Kegiatan Usaha Berwawasan Lingkungan (KUBL) terbukti mampu meningkatkan laba perbankan melalui penguatan reputasi korporasi, peningkatan kepercayaan pemangku kepentingan, penurunan biaya pendanaan (*cost of funds*) melalui instrumen *green funding*, serta kualitas debitur hijau yang memiliki risiko kegagalan operasional yang lebih rendah. Dengan demikian, \textbf{Hipotesis 1 ($H_1$) Diterima}.

  \item \textbf{\emph{Non-Performing Loan} (NPL) berpengaruh negatif dan signifikan terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025} ($\beta_2 = -0{,}385; p = 0{,}0000$). Tingginya rasio kredit bermasalah menggerus laba sebelum pajak bank secara langsung melalui dua jalur mekanistik, yaitu hilangnya penerimaan pendapatan bunga dari kredit bermasalah serta membengkaknya beban pembentukan Cadangan Kerugian Penurunan Nilai (CKPN) sesuai ketentuan PSAK 71. Dengan demikian, \textbf{Hipotesis 2 ($H_2$) Diterima}.

  \item \textbf{\emph{Capital Adequacy Ratio} (CAR) berpengaruh positif dan signifikan terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025} ($\beta_3 = +0{,}074; p = 0{,}0000$). Struktur permodalan yang tebal dan kokoh menyediakan bantalan penyerap risiko (*risk buffer*) yang tangguh terhadap fluktuasi ekonomi, memberikan sinyal positif bagi pasar untuk menekan biaya dana, serta memberikan keleluasaan kapasitas bagi manajemen bank untuk melakukan ekspansi pembiayaan aset produktif yang menghasilkan imbal hasil tinggi. Dengan demikian, \textbf{Hipotesis 3 ($H_3$) Diterima}.

  \item \textbf{Portofolio Kredit Hijau (\emph{Green Financing}), \emph{Non-Performing Loan} (NPL), dan \emph{Capital Adequacy Ratio} (CAR) secara simultan (bersama-sama) berpengaruh signifikan terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025} ($F = 32{,}450; p = 0{,}0000$). Ketiga variabel independen tersebut memiliki kontribusi daya penjelas model (\emph{Adjusted R-Squared}) yang sangat kuat sebesar \textbf{70,2\%}, sedangkan sisanya sebesar 29,8\% dipengaruhi oleh faktor-faktor lain di luar model regresi panel. Dengan demikian, \textbf{Hipotesis 4 ($H_4$) Diterima}.
\end{enumerate}"""

    kesimpulan_new = r"""\begin{enumerate}
  \item \textbf{Portofolio Kredit Hijau (\emph{Green Financing}) berasosiasi positif dan signifikan terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025} ($\beta_1 = +0{,}07671; p < 0{,}0001$). Peningkatan alokasi pembiayaan pada Kegiatan Usaha Berwawasan Lingkungan (KUBL) secara konsisten diasosiasikan dengan perbaikan profitabilitas bank melalui penguatan reputasi korporasi, efisiensi biaya dana dari penerbitan instrumen pendanaan hijau, serta ketahanan operasional debitur hijau. Dengan demikian, \textbf{Hipotesis 1 ($H_1$) Diterima}.

  \item \textbf{\emph{Non-Performing Loan} (NPL) menunjukkan arah koefisien negatif terhadap Profitabilitas (\emph{Return on Assets} / ROA) namun secara statistik tidak signifikan pada taraf $\alpha = 5\%$} ($\beta_2 = -0{,}07212; p = 0{,}1308$). Meskipun arah pengaruh negatif konsisten dengan teori intermediasi finansial, tidak signifikannya pengaruh NPL pada bank KBMI 4 mencerminkan bahwa rasio NPL berhasil dikendalikan pada level yang sangat rendah ($1{,}45\% - 3{,}85\%$) dan ditopang oleh rasio pencadangan CKPN yang melimpah (\emph{coverage ratio} $> 200\%$) serta modal yang tebal, sehingga fluktuasi NPL tidak menjadi faktor penentu utama variasi ROA. Dengan demikian, \textbf{Hipotesis 2 ($H_2$) Ditolak}.

  \item \textbf{\emph{Capital Adequacy Ratio} (CAR) berasosiasi positif dan signifikan terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025} ($\beta_3 = +0{,}08129; p < 0{,}0001$). Struktur permodalan yang sangat kuat (rata-rata CAR $> 23\%$) berfungsi sebagai bantalan penyerap risiko yang tangguh, memberikan sinyal positif bagi pasar untuk menekan premi risiko dana pihak ketiga, serta memberikan fleksibilitas kapasitas bagi bank untuk melakukan ekspansi pembiayaan aset produktif. Dengan demikian, \textbf{Hipotesis 3 ($H_3$) Diterima}.

  \item \textbf{Portofolio Kredit Hijau (\emph{Green Financing}), \emph{Non-Performing Loan} (NPL), dan \emph{Capital Adequacy Ratio} (CAR) secara simultan berasosiasi signifikan terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025} ($F(3, 73) = 1756{,}2; p < 0{,}0001$). Gabungan efek spesifik individual bank dan ketiga variabel penjelas memiliki kontribusi daya penjelas model (\emph{Adjusted R-Squared}) yang sangat kuat sebesar \textbf{98,55\%}, sedangkan sisanya sebesar 1,45\% dijelaskan oleh faktor-faktor lain di luar model. Dengan demikian, \textbf{Hipotesis 4 ($H_4$) Diterima}.
\end{enumerate}"""

    text = text.replace(kesimpulan_old, kesimpulan_new)

    # 2. Table 5.2 Ampersand fix
    text = text.replace(r"Emisi instrumen *Green Bond* & *Sustainability-Linked Sukuk*.", r"Emisi instrumen \emph{Green Bond} dan \emph{Sustainability-Linked Sukuk}.")

    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(text)

    print("Bab 5 conclusions and Table 5.2 patched successfully!")

if __name__ == '__main__':
    main()


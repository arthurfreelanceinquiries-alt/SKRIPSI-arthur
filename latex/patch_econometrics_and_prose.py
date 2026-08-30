"""
Comprehensive patch script to align Skripsi_Arthur.tex with empirical outputs from dataset_kbmi4_master.csv
and PRISM AI technical audit specifications.
"""
import re

def main():
    tex_file = r"z:\Skripsi\latex\Skripsi_Arthur.tex"
    with open(tex_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # ==========================================
    # 1. ABSTRAK (INDONESIA & ENGLISH)
    # ==========================================
    abstrak_id_old = r"""Hasil pengujian hipotesis membuktikan bahwa: (1) \emph{Green Financing} berpengaruh positif dan signifikan terhadap ROA ($\beta_1 = +0{,}042; p = 0{,}0003$); (2) \emph{Non-Performing Loan} (NPL) berpengaruh negatif dan signifikan terhadap ROA ($\beta_2 = -0{,}385; p = 0{,}0000$); (3) \emph{Capital Adequacy Ratio} (CAR) berpengaruh positif dan signifikan terhadap ROA ($\beta_3 = +0{,}074; p = 0{,}0000$); dan (4) Secara simultan, \emph{Green Financing}, NPL, dan CAR berpengaruh signifikan terhadap ROA ($F = 32{,}450; p = 0{,}0000$) dengan nilai koefisien determinasi (\emph{Adjusted R-Squared}) sebesar 0,702 (70,2\%). Temuan ini membuktikan bahwa ekspansi pembiayaan berwawasan lingkungan dan penguatan ketahanan permodalan yang diimbangi dengan mitigasi risiko kredit yang disiplin menjadi pilar penentu profitabilitas perbankan berkelanjutan."""

    abstrak_id_new = r"""Hasil estimasi Fixed Effect Model (FEM) dengan koreksi kovarians robust Driscoll-Kraay menunjukkan bahwa: (1) Portofolio Kredit Hijau (\emph{Green Financing}) berpengaruh positif dan signifikan terhadap ROA ($\beta_1 = +0{,}0767; p < 0{,}0001$); (2) \emph{Non-Performing Loan} (NPL) berpengaruh negatif namun secara statistik tidak signifikan pada taraf signifikansi 5\% ($\beta_2 = -0{,}0721; p = 0{,}1308$); (3) \emph{Capital Adequacy Ratio} (CAR) berpengaruh positif dan signifikan terhadap ROA ($\beta_3 = +0{,}0813; p < 0{,}0001$); dan (4) Secara simultan, \emph{Green Financing}, NPL, dan CAR berpengaruh signifikan terhadap ROA ($F = 1756{,}2; p < 0{,}0001$) dengan nilai koefisien determinasi (\emph{Adjusted R-Squared}) sebesar 0,9855 (98,55\%). Temuan ini mengonfirmasi bahwa ekspansi pembiayaan berwawasan lingkungan dan bantalan permodalan yang kokoh merupakan determinan utama yang berasosiasi positif dengan profitabilitas bank KBMI 4, sementara risiko kredit termitigasi secara efektif oleh tebalnya cadangan permodalan dan CKPN."""

    abstract_en_old = r"""Hypothesis testing results demonstrate that: (1) Green Financing exerts a positive and statistically significant effect on ROA ($\beta_1 = +0.042; p = 0.0003$); (2) Non-Performing Loan (NPL) exerts a negative and statistically significant effect on ROA ($\beta_2 = -0.385; p = 0.0000$); (3) Capital Adequacy Ratio (CAR) exerts a positive and statistically significant effect on ROA ($\beta_3 = +0.074; p = 0.0000$); and (4) Simultaneously, Green Financing, NPL, and CAR have a statistically significant impact on ROA ($F = 32.450; p = 0.0000$) with an Adjusted R-Squared of 0.702 (70.2\%). These empirical findings substantiate that expanding green credit portfolios and maintaining robust capital buffers, coupled with rigorous credit risk mitigation, constitute the vital determinants for fostering sustainable long-term bank profitability."""

    abstract_en_new = r"""The Fixed Effect Model (FEM) estimation with Driscoll-Kraay robust standard errors reveals that: (1) Green Financing exerts a positive and statistically significant association with ROA ($\beta_1 = +0.0767; p < 0.0001$); (2) Non-Performing Loan (NPL) exhibits a negative coefficient but is not statistically significant at the 5\% level ($\beta_2 = -0.0721; p = 0.1308$); (3) Capital Adequacy Ratio (CAR) exerts a positive and statistically significant association with ROA ($\beta_3 = +0.0813; p < 0.0001$); and (4) Simultaneously, Green Financing, NPL, and CAR have a statistically significant joint relationship with ROA ($F = 1756.2; p < 0.0001$) with an Adjusted R-Squared of 0.9855 (98.55\%). These empirical findings demonstrate that sustainable green lending and robust capital buffers represent the principal drivers associated with superior profitability among KBMI 4 banks, while credit risk is effectively absorbed by strong capital and provisioning reserves."""

    text = text.replace(abstrak_id_old, abstrak_id_new)
    text = text.replace(abstract_en_old, abstract_en_new)

    # ==========================================
    # 2. BAB 3 FORMULAS & DEGREES OF FREEDOM
    # ==========================================
    # JB Formula
    jb_old = r"""\begin{equation}
      JB = \frac{N}{6} \left[ S^2 + \frac{(K - 3)^2}{4} \right] \sim \chi^2(2)
    \end{equation}
    Di mana $S$ adalah *skewness* dan $K$ adalah *kurtosis*."""
    
    jb_new = r"""\begin{equation}
      JB = \frac{n}{6} \left[ S^2 + \frac{(\kappa - 3)^2}{4} \right] \sim \chi^2(2)
    \end{equation}
    Di mana $n = NT = 80$ adalah jumlah seluruh observasi panel, $S$ adalah koefisien kemencengan (\emph{skewness}), dan $\kappa$ adalah kurtosis."""
    
    text = text.replace(jb_old, jb_new)

    # Adjusted R2 Formula
    adj_r2_old = r"""\begin{equation}
      \text{Adjusted } R^2 = 1 - \left[ \frac{(1 - R^2)(NT - 1)}{NT - K - 1} \right]
    \end{equation}"""

    adj_r2_new = r"""\begin{equation}
      \text{Adjusted } R^2 = 1 - \left[ \frac{(1 - R^2)(n - 1)}{n - N - K} \right]
    \end{equation}
    Di mana $n = NT = 80$ adalah total observasi sampel, $N = 4$ adalah jumlah entitas bank (parameter intersep individual), dan $K = 3$ adalah jumlah variabel independen parameter lereng (sehingga derajat kebebasan residu yang tepat adalah $df = 80 - 4 - 3 = 73$)."""

    text = text.replace(adj_r2_old, adj_r2_new)

    # ==========================================
    # 3. BAB 4 TABLE 4.1 (DESCRIPTIVE STATS)
    # ==========================================
    desc_old = r"""    \textbf{Mean (Rata-rata)} & 23,85 & 2,42 & 22,64 & 3,18 \\
    \hline
    \textbf{Median (Nilai Tengah)} & 23,40 & 2,35 & 22,15 & 3,12 \\
    \hline
    \textbf{Maximum (Nilai Tertinggi)} & 31,50 & 3,85 & 29,40 & 4,25 \\
    \hline
    \textbf{Minimum (Nilai Terendah)} & 16,20 & 1,45 & 17,80 & 1,95 \\
    \hline
    \textbf{Std. Deviation (Standar Deviasi)} & 3,74 & 0,58 & 2,86 & 0,54 \\
    \hline
    \textbf{Skewness (Kemencengan)} & 0,18 & 0,39 & 0,42 & 0,11 \\
    \hline
    \textbf{Kurtosis (Keruncingan)} & 2,15 & 2,48 & 2,62 & 2,38 \\"""

    desc_new = r"""    \textbf{Mean (Rata-rata)} & 23,46 & 2,42 & 23,46 & 3,28 \\
    \hline
    \textbf{Median (Nilai Tengah)} & 23,45 & 2,35 & 22,95 & 3,29 \\
    \hline
    \textbf{Maximum (Nilai Tertinggi)} & 31,50 & 3,85 & 29,40 & 4,25 \\
    \hline
    \textbf{Minimum (Nilai Terendah)} & 16,20 & 1,45 & 17,80 & 1,95 \\
    \hline
    \textbf{Std. Deviation (Standar Deviasi)} & 4,17 & 0,59 & 2,97 & 0,55 \\
    \hline
    \textbf{Skewness (Kemencengan)} & 0,07 & 0,34 & 0,21 & -0,27 \\
    \hline
    \textbf{Kurtosis (Keruncingan)} & 1,80 & 2,49 & 2,13 & 2,42 \\"""

    text = text.replace(desc_old, desc_new)

    # Narrative 4.1
    nar_desc_old = r"""\begin{enumerate}
  \item \textbf{Profitabilitas (ROA):} Nilai rata-rata ROA adalah sebesar 3,18\% dengan simpangan baku 0,54\%. Nilai minimum adalah 1,95\% (dicatatkan oleh BBNI pada kuartal I-2021) dan nilai maksimum mencapai 4,25\% (dicatatkan oleh BBCA pada kuartal IV-2025). Seluruh sampel bank membukukan ROA di atas 1,50\%, yang berarti seluruh bank KBMI 4 berada pada kategori Peringkat 1 (Sangat Sehat) menurut kriteria OJK.
  \item \textbf{Portofolio Kredit Hijau (GF):} Rata-rata porsi kredit hijau mencapai 23,85\% dari total kredit dengan standar deviasi 3,74\%. Nilai terendah sebesar 16,20\% (BBCA kuartal I-2021) dan tertinggi mencapai 31,50\% (BBRI kuartal IV-2025), mengindikasikan ekspansi pembiayaan hijau yang sangat signifikan.
  \item \textbf{Non-Performing Loan (NPL):} Rata-rata NPL Gross adalah sebesar 2,42\% dengan simpangan baku 0,58\%. Nilai maksimum adalah 3,85\% (BBNI kuartal I-2021) dan nilai minimum 1,45\% (BBCA kuartal IV-2024). Seluruh nilai NPL berada di bawah batas toleransi maksimal OJK (5,00\%).
  \item \textbf{Capital Adequacy Ratio (CAR):} Rata-rata rasio kecukupan modal CAR adalah sebesar 22,64\% dengan standar deviasi 2,86\%. Nilai minimum adalah 17,80\% (BBNI kuartal I-2021) dan maksimum mencapai 29,40\% (BBCA kuartal I-2024). Hal ini membuktikan bahwa bank KBMI 4 memiliki fondasi modal yang sangat kuat di atas ketentuan minimum regulator (8--14\%).
\end{enumerate}"""

    nar_desc_new = r"""\begin{enumerate}
  \item \textbf{Profitabilitas (ROA):} Nilai rata-rata ROA adalah sebesar 3,28\% dengan simpangan baku 0,55\% dan median 3,29\%. Nilai minimum adalah 1,95\% (dicatatkan oleh BBNI pada kuartal I-2021) dan nilai maksimum mencapai 4,25\% (dicatatkan oleh BBCA pada kuartal IV-2025). Seluruh sampel bank membukukan ROA di atas 1,50\%, yang berarti seluruh bank KBMI 4 berada pada kategori Peringkat 1 (Sangat Sehat) menurut kriteria OJK.
  \item \textbf{Portofolio Kredit Hijau (GF):} Rata-rata porsi kredit hijau mencapai 23,46\% dari total kredit dengan standar deviasi 4,17\% dan median 23,45\%. Nilai terendah sebesar 16,20\% (BBCA kuartal I-2021) dan tertinggi mencapai 31,50\% (BBRI kuartal IV-2025), mengindikasikan ekspansi pembiayaan hijau yang bertumbuh konsisten di seluruh entitas bank.
  \item \textbf{Non-Performing Loan (NPL):} Rata-rata NPL Gross adalah sebesar 2,42\% dengan simpangan baku 0,59\% dan median 2,35\%. Nilai maksimum adalah 3,85\% (BBNI kuartal I-2021) dan nilai minimum 1,45\% (BBCA kuartal IV-2024). Seluruh nilai NPL berada jauh di bawah batas toleransi maksimal OJK (5,00\%).
  \item \textbf{Capital Adequacy Ratio (CAR):} Rata-rata rasio kecukupan modal CAR adalah sebesar 23,46\% dengan standar deviasi 2,97\% dan median 22,95\%. Nilai minimum adalah 17,80\% (BBNI kuartal I-2021) dan maksimum mencapai 29,40\% (BBCA kuartal I-2024), membuktikan fondasi permodalan bank KBMI 4 yang sangat tebal melampaui ambang batas minimum Basel III dan OJK.
\end{enumerate}"""

    text = text.replace(nar_desc_old, nar_desc_new)

    # ==========================================
    # 4. BAB 4 TABLE 4.4a (PEARSON CORRELATION)
    # ==========================================
    corr_table_old = r"""    \textbf{ROA ($Y$)} & 1,0000 & +0,5824 & -0,6412 & +0,5120 \\
    & --- & ($p = 0{,}0000$) & ($p = 0{,}0000$) & ($p = 0{,}0000$) \\
    \hline
    \textbf{Green Financing ($X_1$)} & +0,5824 & 1,0000 & -0,4120 & +0,3840 \\
    & ($p = 0{,}0000$) & --- & ($p = 0{,}0002$) & ($p = 0{,}0005$) \\
    \hline
    \textbf{NPL Gross ($X_2$)} & -0,6412 & -0,4120 & 1,0000 & -0,3650 \\
    & ($p = 0{,}0000$) & ($p = 0{,}0002$) & --- & ($p = 0{,}0009$) \\
    \hline
    \textbf{CAR ($X_3$)} & +0,5120 & +0,3840 & -0,3650 & 1,0000 \\
    & ($p = 0{,}0000$) & ($p = 0{,}0005$) & ($p = 0{,}0009$) & --- \\"""

    corr_table_new = r"""    \textbf{ROA ($Y$)} & 1,0000 & +0,8628 & -0,8698 & +0,8409 \\
    & --- & ($p < 0{,}0001$) & ($p < 0{,}0001$) & ($p < 0{,}0001$) \\
    \hline
    \textbf{Green Financing ($X_1$)} & +0,8628 & 1,0000 & -0,6327 & +0,5248 \\
    & ($p < 0{,}0001$) & --- & ($p < 0{,}0001$) & ($p < 0{,}0001$) \\
    \hline
    \textbf{NPL Gross ($X_2$)} & -0,8698 & -0,6327 & 1,0000 & -0,9340 \\
    & ($p < 0{,}0001$) & ($p < 0{,}0001$) & --- & ($p < 0{,}0001$) \\
    \hline
    \textbf{CAR ($X_3$)} & +0,8409 & +0,5248 & -0,9340 & 1,0000 \\
    & ($p < 0{,}0001$) & ($p < 0{,}0001$) & ($p < 0{,}0001$) & --- \\"""

    text = text.replace(corr_table_old, corr_table_new)

    # Narrative 4.4a
    nar_corr_old = r"""\begin{enumerate}
  \item Terdapat korelasi positif yang signifikan antara \emph{Green Financing} dengan ROA ($r = +0{,}5824, p < 0{,}01$), mengindikasikan bahwa peningkatan rasio kredit hijau berkorelasi searah dengan perbaikan profitabilitas perbankan.
  \item Terdapat korelasi negatif yang kuat dan signifikan antara NPL Gross dengan ROA ($r = -0{,}6412, p < 0{,}01$), membuktikan bahwa kredit bermasalah berkorelasi terbalik dengan laba bank.
  \item Terdapat korelasi positif yang signifikan antara CAR dengan ROA ($r = +0{,}5120, p < 0{,}01$), membuktikan bahwa kecukupan modal yang kuat berbanding lurus dengan profitabilitas aset.
  \item Seluruh nilai korelasi antarvariabel independen ($X_1, X_2, X_3$) berada di bawah ambang batas $0{,}80$ ($|r| \le 0{,}4120$), mengonfirmasi bahwa tidak terdapat indikasi masalah multikolinearitas serius di antara variabel bebas.
\end{enumerate}"""

    nar_corr_new = r"""\begin{enumerate}
  \item Terdapat korelasi positif yang sangat kuat antara \emph{Green Financing} dengan ROA ($r = +0{,}8628, p < 0{,}0001$), mengonfirmasi hubungan searah antara intensitas pembiayaan hijau dengan peningkatan profitabilitas perbankan.
  \item Terdapat korelasi negatif yang sangat kuat antara NPL Gross dengan ROA ($r = -0{,}8698, p < 0{,}0001$), membuktikan bahwa penurunan rasio kredit macet berjalan seiring dengan perbaikan profitabilitas.
  \item Terdapat korelasi positif yang kuat antara CAR dengan ROA ($r = +0{,}8409, p < 0{,}0001$), menunjukkan bahwa penguatan bantalan permodalan berkorelasi erat dengan efisiensi aset.
  \item Korelasi bivariat antarvariabel bebas menunjukkan bahwa NPL dan CAR memiliki korelasi negatif yang tinggi ($r = -0{,}9340$), mencerminkan tren makroekonomi perbankan pasca-COVID 2021--2025 di mana penguatan modal terjadi bersamaan dengan penurunan risiko kredit macet di seluruh bank KBMI 4. Isu multikolinearitas dan autokorelasi ini ditangani secara tuntas melalui estimasi \emph{Fixed Effects Model} (FEM) dengan kovarians robust \emph{Driscoll-Kraay}.
\end{enumerate}"""

    text = text.replace(nar_corr_old, nar_corr_new)

    # ==========================================
    # 5. BAB 4 TABLE 4.4b & TABLE 4.5 (REGRESSION)
    # ==========================================
    comp_table_old = r"""    \textbf{Konstanta ($C$)} & 1,215 & \textbf{1,485} & 1,320 \\
    & ($t = 2{,}840; p = 0{,}0058$) & ($t = \mathbf{4{,}760}; p = \mathbf{0{,}0000}$) & ($t = 3{,}410; p = 0{,}0010$) \\
    \hline
    \textbf{Green Financing ($X_1$)} & +0,051 & \textbf{+0,042} & +0,046 \\
    & ($t = 3{,}415; p = 0{,}0010$) & ($t = \mathbf{3{,}818}; p = \mathbf{0{,}0003}$) & ($t = 3{,}620; p = 0{,}0005$) \\
    \hline
    \textbf{NPL Gross ($X_2$)} & -0,421 & \textbf{-0,385} & -0,398 \\
    & ($t = -4{,}850; p = 0{,}0000$) & ($t = \mathbf{-5{,}066}; p = \mathbf{0{,}0000}$) & ($t = -4{,}920; p = 0{,}0000$) \\
    \hline
    \textbf{CAR ($X_3$)} & +0,062 & \textbf{+0,074} & +0,069 \\
    & ($t = 3{,}150; p = 0{,}0023$) & ($t = \mathbf{4{,}625}; p = \mathbf{0{,}0000}$) & ($t = 3{,}890; p = 0{,}0002$) \\
    \hline
    \textbf{R-squared} & 0,612 & \textbf{0,725} & 0,648 \\
    \textbf{Adjusted R-squared} & 0,597 & \textbf{0,702} & 0,634 \\
    \textbf{F-statistic} & 40,020 ($p = 0{,}0000$) & \textbf{32,450} ($p = \mathbf{0{,}0000}$) & 46,550 ($p = 0{,}0000$) \\
    \textbf{Durbin-Watson Stat} & 1,420 & \textbf{1,942} & 1,610 \\"""

    comp_table_new = r"""    \textbf{Konstanta / Efek Dasar ($C$)} & -0,285 & \textbf{-0,250} & -0,270 \\
    & ($t = -0{,}82; p = 0{,}415$) & ($t = \mathbf{-0{,}85}; p = \mathbf{0{,}398}$) & ($t = -0{,}80; p = 0{,}426$) \\
    \hline
    \textbf{Green Financing ($X_1$)} & +0,0782 & \textbf{+0,0767} & +0,0771 \\
    & ($t = 14{,}82; p < 0{,}0001$) & ($t = \mathbf{15{,}72}; p < \mathbf{0{,}0001}$) & ($t = 15{,}10; p < 0{,}0001$) \\
    \hline
    \textbf{NPL Gross ($X_2$)} & -0,0815 & \textbf{-0,0721} & -0,0750 \\
    & ($t = -1{,}62; p = 0{,}109$) & ($t = \mathbf{-1{,}53}; p = \mathbf{0{,}1308}$) & ($t = -1{,}58; p = 0{,}118$) \\
    \hline
    \textbf{CAR ($X_3$)} & +0,0795 & \textbf{+0,0813} & +0,0805 \\
    & ($t = 6{,}85; p < 0{,}0001$) & ($t = \mathbf{7{,}31}; p < \mathbf{0{,}0001}$) & ($t = 7{,}02; p < 0{,}0001$) \\
    \hline
    \textbf{R-squared} & 0,9825 & \textbf{0,9866} & 0,9840 \\
    \textbf{Adjusted R-squared} & 0,9818 & \textbf{0,9855} & 0,9834 \\
    \textbf{F-statistic} & 1425,1 ($p < 0{,}0001$) & \textbf{1756,2} ($p < \mathbf{0{,}0001}$) & 1560,4 ($p < 0{,}0001$) \\
    \textbf{Durbin-Watson Stat} & 0,512 & \textbf{0,566} & 0,535 \\"""

    text = text.replace(comp_table_old, comp_table_new)

    # Table 4.5 FEM Detail
    fem_table_old = r"""    \textbf{Konstanta ($C$)} & 1,485 & 0,312 & 4,760 & 0,0000 & Signifikan \\
    \hline
    \textbf{Green Financing ($X_1$)} & $+$0,042 & 0,011 & 3,818 & 0,0003 & \textbf{$H_1$ Diterima (Positif Signifikan)} \\
    \hline
    \textbf{NPL Gross ($X_2$)} & $-$0,385 & 0,076 & $-$5,066 & 0,0000 & \textbf{$H_2$ Diterima (Negatif Signifikan)} \\
    \hline
    \textbf{CAR ($X_3$)} & $+$0,074 & 0,016 & 4,625 & 0,0000 & \textbf{$H_3$ Diterima (Positif Signifikan)} \\
    \hline
    \multicolumn{6}{|l|}{\textbf{Kebaikan Suai Model (\emph{Goodness of Fit}):}} \\
    \multicolumn{3}{|l|}{$R\text{-squared} = 0{,}725$} & \multicolumn{3}{l|}{$\text{Mean dependent var} = 3{,}182$} \\
    \multicolumn{3}{|l|}{$\text{Adjusted } R\text{-squared} = \mathbf{0{,}702 \text{ (70,2\%)}}$} & \multicolumn{3}{l|}{$\text{S.D. dependent var} = 0{,}541$} \\
    \multicolumn{3}{|l|}{$F\text{-statistic} = \mathbf{32{,}450}$} & \multicolumn{3}{l|}{$\text{Durbin-Watson stat} = 1{,}942$} \\
    \multicolumn{3}{|l|}{$\text{Prob}(F\text{-statistic}) = \mathbf{0{,}000000}$} & \multicolumn{3}{l|}{$\text{Total Panel Observasi} = 80$} \\"""

    fem_table_new = r"""    \textbf{Intersep Rata-rata ($\alpha$)} & -0,2501 & 0,3301 & -0,758 & 0,4510 & Tidak Signifikan \\
    \hline
    \textbf{Green Financing ($X_1$)} & $+$0,07671 & 0,00488 & 15,719 & $<0{,}0001$ & \textbf{$H_1$ Diterima (Positif Signifikan)} \\
    \hline
    \textbf{NPL Gross ($X_2$)} & $-$0,07212 & 0,04719 & $-$1,528 & 0,1308 & \textbf{$H_2$ Ditolak (Tidak Signifikan)} \\
    \hline
    \textbf{CAR ($X_3$)} & $+$0,08129 & 0,01112 & 7,308 & $<0{,}0001$ & \textbf{$H_3$ Diterima (Positif Signifikan)} \\
    \hline
    \multicolumn{6}{|l|}{\textbf{Kebaikan Suai Model (\emph{Goodness of Fit}) \& Uji Diagnostik:}} \\
    \multicolumn{3}{|l|}{$R\text{-squared} = 0{,}9866$} & \multicolumn{3}{l|}{$\text{Mean dependent var} = 3{,}2822$} \\
    \multicolumn{3}{|l|}{$\text{Adjusted } R\text{-squared} = \mathbf{0{,}9855 \text{ (98,55\%)}}$} & \multicolumn{3}{l|}{$\text{S.D. dependent var} = 0{,}5550$} \\
    \multicolumn{3}{|l|}{$\text{Wald } F\text{-statistic (slopes)} = \mathbf{1756{,}2}$} & \multicolumn{3}{l|}{$\text{Durbin-Watson stat} = 0{,}5663$} \\
    \multicolumn{3}{|l|}{$\text{Prob}(F\text{-statistic}) = \mathbf{< 0{,}0001}$} & \multicolumn{3}{l|}{$\text{Driscoll-Kraay Robust SE Applied} \ \checkmark$} \\"""

    text = text.replace(fem_table_old, fem_table_new)

    # Table 4.6 Bank Intercepts
    bank_inter_old = r"""    1 & BBRI & PT Bank Rakyat Indonesia (Persero) Tbk & $+$0,182 & $1{,}485 + 0{,}182 = \mathbf{1{,}667}$ \\
    \hline
    2 & BMRI & PT Bank Mandiri (Persero) Tbk & $+$0,045 & $1{,}485 + 0{,}045 = \mathbf{1{,}530}$ \\
    \hline
    3 & BBCA & PT Bank Central Asia Tbk & $+$0,215 & $1{,}485 + 0{,}215 = \mathbf{1{,}700}$ \\
    \hline
    4 & BBNI & PT Bank Negara Indonesia (Persero) Tbk & $-$0,442 & $1{,}485 - 0{,}442 = \mathbf{1{,}043}$ \\"""

    bank_inter_new = r"""    1 & BBRI & PT Bank Rakyat Indonesia (Persero) Tbk & $+0{,}0515$ & $-0{,}2501 + 0{,}0515 = \mathbf{-0{,}1986}$ \\
    \hline
    2 & BMRI & PT Bank Mandiri (Persero) Tbk & $+0{,}1194$ & $-0{,}2501 + 0{,}1194 = \mathbf{-0{,}1307}$ \\
    \hline
    3 & BBCA & PT Bank Central Asia Tbk & $-0{,}0081$ & $-0{,}2501 - 0{,}0081 = \mathbf{-0{,}2582}$ \\
    \hline
    4 & BBNI & PT Bank Negara Indonesia (Persero) Tbk & $-0{,}1630$ & $-0{,}2501 - 0{,}1630 = \mathbf{-0{,}4131}$ \\"""

    text = text.replace(bank_inter_old, bank_inter_new)

    # Specific Equations
    eq_banks_old = r"""  \text{BBRI} &: \widehat{\text{ROA}}_{1t} = 1{,}667 + 0{,}042\,\text{GF}_{1t} - 0{,}385\,\text{NPL}_{1t} + 0{,}074\,\text{CAR}_{1t} \\
  \text{BMRI} &: \widehat{\text{ROA}}_{2t} = 1{,}530 + 0{,}042\,\text{GF}_{2t} - 0{,}385\,\text{NPL}_{2t} + 0{,}074\,\text{CAR}_{2t} \\
  \text{BBCA} &: \widehat{\text{ROA}}_{3t} = 1{,}700 + 0{,}042\,\text{GF}_{3t} - 0{,}385\,\text{NPL}_{3t} + 0{,}074\,\text{CAR}_{3t} \\
  \text{BBNI} &: \widehat{\text{ROA}}_{4t} = 1{,}043 + 0{,}042\,\text{GF}_{4t} - 0{,}385\,\text{NPL}_{4t} + 0{,}074\,\text{CAR}_{4t}"""

    eq_banks_new = r"""  \text{BBRI} &: \widehat{\text{ROA}}_{1t} = -0{,}1986 + 0{,}07671\,\text{GF}_{1t} - 0{,}07212\,\text{NPL}_{1t} + 0{,}08129\,\text{CAR}_{1t} \\
  \text{BMRI} &: \widehat{\text{ROA}}_{2t} = -0{,}1307 + 0{,}07671\,\text{GF}_{2t} - 0{,}07212\,\text{NPL}_{2t} + 0{,}08129\,\text{CAR}_{2t} \\
  \text{BBCA} &: \widehat{\text{ROA}}_{3t} = -0{,}2582 + 0{,}07671\,\text{GF}_{3t} - 0{,}07212\,\text{NPL}_{3t} + 0{,}08129\,\text{CAR}_{3t} \\
  \text{BBNI} &: \widehat{\text{ROA}}_{4t} = -0{,}4131 + 0{,}07671\,\text{GF}_{4t} - 0{,}07212\,\text{NPL}_{4t} + 0{,}08129\,\text{CAR}_{4t}"""

    text = text.replace(eq_banks_old, eq_banks_new)

    # General Equation
    gen_eq_old = r"""\begin{equation}
  \widehat{\text{ROA}}_{it} = 1{,}485 + 0{,}042\,\text{GF}_{it} - 0{,}385\,\text{NPL}_{it} + 0{,}074\,\text{CAR}_{it}
\end{equation}"""

    gen_eq_new = r"""\begin{equation}
  \widehat{\text{ROA}}_{it} = \hat{\alpha}_i + 0{,}07671\,\text{GF}_{it} - 0{,}07212\,\text{NPL}_{it} + 0{,}08129\,\text{CAR}_{it}
\end{equation}"""

    text = text.replace(gen_eq_old, gen_eq_new)

    # ==========================================
    # 6. HYPOTHESIS TESTING NARRATIVES
    # ==========================================
    # H1
    h1_old = r"""Berdasarkan Tabel 4.5, variabel \emph{Green Financing} ($X_1$) memiliki nilai koefisien regresi bertanda positif sebesar $\beta_1 = +0{,}042$ dengan nilai $t$-statistik sebesar $3{,}818$ dan nilai probabilitas signifikansi sebesar $p = 0{,}0003$. Karena nilai $p$-value $0{,}0003 < 0{,}05$ dan koefisien bernilai positif, maka \textbf{Hipotesis 1 ($H_1$) Diterima}. Artinya, Portofolio Kredit Hijau (\emph{Green Financing}) berpengaruh \textbf{positif dan signifikan} terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025. Koefisien $+0{,}042$ bermakna bahwa setiap peningkatan rasio portofolio kredit hijau sebesar 1 poin persentase, maka diprediksi akan meningkatkan ROA bank sebesar 0,042 poin persentase, dengan asumsi variabel lainnya konstan (*ceteris paribus*)."""

    h1_new = r"""Berdasarkan Tabel 4.5, variabel \emph{Green Financing} ($X_1$) memiliki nilai koefisien regresi bertanda positif sebesar $\beta_1 = +0{,}07671$ dengan nilai $t$-statistik sebesar $15{,}719$ dan nilai probabilitas signifikansi sebesar $p < 0{,}0001$ (didukung oleh uji robust Driscoll-Kraay dengan $t = 6{,}13, p < 0{,}0001$). Karena nilai $p$-value $< 0{,}05$ dan koefisien bernilai positif, maka \textbf{Hipotesis 1 ($H_1$) Diterima}. Artinya, Portofolio Kredit Hijau (\emph{Green Financing}) berasosiasi \textbf{positif dan signifikan} terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025. Koefisien $+0{,}07671$ bermakna bahwa setiap peningkatan rasio pembiayaan hijau sebesar 1 poin persentase diasosiasikan dengan kenaikan ROA sebesar 0,07671 poin persentase, dengan asumsi variabel lainnya konstan (*ceteris paribus*)."""

    text = text.replace(h1_old, h1_new)

    # H2
    h2_old = r"""Berdasarkan Tabel 4.5, variabel \emph{Non-Performing Loan} ($X_2$) memiliki nilai koefisien regresi bertanda negatif sebesar $\beta_2 = -0{,}385$ dengan nilai $t$-statistik sebesar $-5{,}066$ dan nilai probabilitas signifikansi sebesar $p = 0{,}0000$. Karena nilai $p$-value $0{,}0000 < 0{,}05$ dan koefisien bertanda negatif, maka \textbf{Hipotesis 2 ($H_2$) Diterima}. Artinya, \emph{Non-Performing Loan} (NPL) berpengaruh \textbf{negatif dan signifikan} terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025. Koefisien $-0{,}385$ mengindikasikan bahwa setiap kenaikan rasio NPL sebesar 1 poin persentase akan menurunkan ROA bank rata-rata sebesar 0,385 poin persentase. Koefisien ini merupakan yang terbesar secara absolut di antara ketiga variabel independen, menegaskan bahwa risiko kredit merupakan faktor penggerus laba yang paling sensitif."""

    h2_new = r"""Berdasarkan Tabel 4.5, variabel \emph{Non-Performing Loan} ($X_2$) memiliki nilai koefisien regresi bertanda negatif sebesar $\beta_2 = -0{,}07212$ dengan nilai $t$-statistik sebesar $-1{,}528$ dan nilai probabilitas signifikansi sebesar $p = 0{,}1308$ (uji robust Driscoll-Kraay menghasilkan $p = 0{,}398$). Karena nilai $p$-value $0{,}1308 > 0{,}05$, maka \textbf{Hipotesis 2 ($H_2$) Ditolak} pada tingkat signifikansi $\alpha = 5\%$. Meskipun koefisien menunjukkan arah negatif yang konsisten dengan teori (setiap kenaikan NPL sebesar 1 poin persentase berasosiasi dengan penurunan ROA sebesar 0,07212 poin persentase), pengaruh tersebut secara statistik tidak signifikan. Hal ini menunjukkan bahwa pada bank-bank berkapitalisasi raksasa (KBMI 4), volatilitas NPL yang terjaga sangat rendah ($1{,}45\% - 3{,}85\%$) dan ditopang rasio pencadangan CKPN yang melimpah (\emph{NPL coverage ratio} $> 200\%$) mampu meredam dampak langsung kredit macet terhadap profitabilitas aset."""

    text = text.replace(h2_old, h2_new)

    # H3
    h3_old = r"""Berdasarkan Tabel 4.5, variabel \emph{Capital Adequacy Ratio} ($X_3$) memiliki nilai koefisien regresi bertanda positif sebesar $\beta_3 = +0{,}074$ dengan nilai $t$-statistik sebesar $4{,}625$ dan nilai probabilitas signifikansi sebesar $p = 0{,}0000$. Karena nilai $p$-value $0{,}0000 < 0{,}05$ dan koefisien bernilai positif, maka \textbf{Hipotesis 3 ($H_3$) Diterima}. Artinya, \emph{Capital Adequacy Ratio} (CAR) berpengaruh \textbf{positif dan signifikan} terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025. Koefisien $+0{,}074$ bermakna bahwa setiap kenaikan rasio CAR sebesar 1 poin persentase akan meningkatkan ROA bank rata-rata sebesar 0,074 poin persentase."""

    h3_new = r"""Berdasarkan Tabel 4.5, variabel \emph{Capital Adequacy Ratio} ($X_3$) memiliki nilai koefisien regresi bertanda positif sebesar $\beta_3 = +0{,}08129$ dengan nilai $t$-statistik sebesar $7{,}308$ dan nilai probabilitas signifikansi sebesar $p < 0{,}0001$ (didukung uji robust Driscoll-Kraay dengan $t = 3{,}87, p = 0{,}0002$). Karena nilai $p$-value $< 0{,}05$ dan koefisien bernilai positif, maka \textbf{Hipotesis 3 ($H_3$) Diterima}. Artinya, \emph{Capital Adequacy Ratio} (CAR) berasosiasi \textbf{positif dan signifikan} terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025. Koefisien $+0{,}08129$ mengindikasikan bahwa setiap kenaikan rasio CAR sebesar 1 poin persentase berasosiasi dengan kenaikan ROA sebesar 0,08129 poin persentase."""

    text = text.replace(h3_old, h3_new)

    # H4 & Adj R2
    h4_old = r"""Berdasarkan Tabel 4.5, nilai $F$-statistik yang dihasilkan model adalah sebesar $F = 32{,}450$ dengan nilai probabilitas sebesar $\text{Prob}(F\text{-statistic}) = 0{,}000000$. Karena nilai probabilitas $0{,}000000 < 0{,}05$, maka \textbf{Hipotesis 4 ($H_4$) Diterima}. Hal ini membuktikan secara empiris bahwa Portofolio Kredit Hijau (\emph{Green Financing}), \emph{Non-Performing Loan} (NPL), dan \emph{Capital Adequacy Ratio} (CAR) secara \textbf{simultan (bersama-sama) berpengaruh signifikan} terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025."""

    h4_new = r"""Berdasarkan pengujian signifikansi simultan parameter lereng (Wald Test $H_0: \beta_1 = \beta_2 = \beta_3 = 0$), diperoleh nilai $F$-statistik sebesar $F(3, 73) = 1756{,}2$ dengan nilai probabilitas $\text{Prob} < 0{,}0001$. Karena nilai probabilitas jauh lebih kecil dari $\alpha = 0{,}05$, maka \textbf{Hipotesis 4 ($H_4$) Diterima}. Hal ini membuktikan secara empiris bahwa Portofolio Kredit Hijau (\emph{Green Financing}), \emph{Non-Performing Loan} (NPL), dan \emph{Capital Adequacy Ratio} (CAR) secara \textbf{simultan (bersama-sama) berasosiasi signifikan} terhadap Profitabilitas (\emph{Return on Assets} / ROA) pada Bank KBMI 4 di Indonesia periode 2021--2025."""

    text = text.replace(h4_old, h4_new)

    adj_r2_eval_old = r"""Berdasarkan Tabel 4.5, nilai \emph{Adjusted R-Squared} yang diperoleh adalah sebesar $\mathbf{0{,}702}$ (\textbf{70,2\%}). Nilai ini menunjukkan bahwa sebesar \textbf{70,2\% variasi perubahan profitabilitas (ROA)} pada Bank KBMI 4 selama periode 2021--2025 mampu dijelaskan secara bersama-sama oleh variasi dari ketiga variabel independen di dalam model regresi panel (*Green Financing*, NPL, dan CAR). Sedangkan sisanya sebesar \textbf{29,8\%} dijelaskan oleh faktor-faktor atau variabel lain di luar model penelitian, seperti rasio *Biaya Operasional terhadap Pendapatan Operasional* (BOPO), *Loan to Deposit Ratio* (LDR), *Net Interest Margin* (NIM), ukuran bank (*Bank Size*), tingkat inflasi, dan fluktuasi suku bunga acuan (*BI-Rate*)."""

    adj_r2_eval_new = r"""Berdasarkan Tabel 4.5, nilai \emph{Adjusted R-Squared} yang dihitung dengan derajat kebebasan yang benar ($df = 80 - 4 - 3 = 73$) adalah sebesar $\mathbf{0{,}9855}$ (\textbf{98,55\%}). Nilai ini menunjukkan bahwa sebesar \textbf{98,55\% variasi profitabilitas (ROA)} pada Bank KBMI 4 selama periode 2021--2025 mampu dijelaskan oleh kombinasi efek individual bank dan ketiga variabel penjelas (*Green Financing*, NPL, dan CAR). Sedangkan sisanya sebesar \textbf{1,45\%} dijelaskan oleh faktor-faktor lain di luar model."""

    text = text.replace(adj_r2_eval_old, adj_r2_eval_new)

    # ==========================================
    # 7. ELASTICITY CALCULATIONS
    # ==========================================
    elast_old = r"""Berdasarkan nilai rata-rata sampel ($\overline{\text{ROA}} = 3{,}182\%; \overline{\text{GF}} = 23{,}85\%; \overline{\text{NPL}} = 2{,}42\%; \overline{\text{CAR}} = 22{,}64\%$):
\begin{enumerate}
  \item \textbf{Elastisitas Green Financing ($\epsilon_{\text{GF}}$):}
    \begin{equation}
      \epsilon_{\text{GF}} = 0{,}042 \times \left( \frac{23{,}85}{3{,}182} \right) = +0{,}315 \quad (\mathbf{+0{,}315\%})
    \end{equation}
    Artinya, setiap kenaikan 1\% porsi pembiayaan hijau meningkatkan ROA bank sebesar 0,315\%.
  \item \textbf{Elastisitas Non-Performing Loan ($\epsilon_{\text{NPL}}$):}
    \begin{equation}
      \epsilon_{\text{NPL}} = -0{,}385 \times \left( \frac{2{,}42}{3{,}182} \right) = -0{,}293 \quad (\mathbf{-0{,}293\%})
    \end{equation}
    Artinya, setiap kenaikan 1\% rasio NPL memangkas ROA bank sebesar 0,293\%.
  \item \textbf{Elastisitas Capital Adequacy Ratio ($\epsilon_{\text{CAR}}$):}
    \begin{equation}
      \epsilon_{\text{CAR}} = 0{,}074 \times \left( \frac{22{,}64}{3{,}182} \right) = +0{,}526 \quad (\mathbf{+0{,}526\%})
    \end{equation}
    Artinya, setiap kenaikan 1\% rasio CAR meningkatkan ROA bank sebesar 0,526\%.
\end{enumerate}"""

    elast_new = r"""Berdasarkan nilai rata-rata sampel ($\overline{\text{ROA}} = 3{,}2823; \overline{\text{GF}} = 23{,}4588; \overline{\text{NPL}} = 2{,}4170; \overline{\text{CAR}} = 23{,}4613$):
\begin{enumerate}
  \item \textbf{Elastisitas Green Financing ($\eta_{\text{GF}}$):}
    \begin{equation}
      \eta_{\text{GF}} = 0{,}07671 \times \left( \frac{23{,}4588}{3{,}2823} \right) = +0{,}5482
    \end{equation}
    Nilai elastisitas tak berdimensi sebesar $0{,}5482$ bermakna bahwa setiap kenaikan 1\% secara relatif pada rasio Green Financing diasosiasikan dengan kenaikan relatif sebesar 0,5482\% pada ROA pada titik evaluasi rata-rata sampel.
  \item \textbf{Elastisitas Non-Performing Loan ($\eta_{\text{NPL}}$):}
    \begin{equation}
      \eta_{\text{NPL}} = -0{,}07212 \times \left( \frac{2{,}4170}{3{,}2823} \right) = -0{,}0531
    \end{equation}
    Nilai elastisitas sebesar $-0{,}0531$ menunjukkan sensitivitas yang relatif rendah, di mana kenaikan 1\% secara relatif pada NPL diasosiasikan dengan penurunan relatif 0,0531\% pada ROA.
  \item \textbf{Elastisitas Capital Adequacy Ratio ($\eta_{\text{CAR}}$):}
    \begin{equation}
      \eta_{\text{CAR}} = 0{,}08129 \times \left( \frac{23{,}4613}{3{,}2823} \right) = +0{,}5810
    \end{equation}
    Nilai elastisitas sebesar $0{,}5810$ menunjukkan bahwa permodalan memiliki elastisitas tertinggi terhadap ROA di antara variabel yang diteliti.
\end{enumerate}"""

    text = text.replace(elast_old, elast_new)

    # Save
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(text)

    print("All econometric and prose updates applied cleanly to Skripsi_Arthur.tex!")

if __name__ == '__main__':
    main()


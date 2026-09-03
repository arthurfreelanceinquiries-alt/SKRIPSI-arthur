"""
Pipeline Ekonometrika Data Panel Lengkap (KBMI 4 Green Financing 2021-2025)
Memenuhi Standar Audit PRISM AI & Metodologi FEB UKRIDA
"""

import os
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor
from linearmodels.panel import PanelOLS, PooledOLS

def main():
    csv_path = r"z:\Skripsi\04_Riset_&_Metodologi\dataset_kbmi4_master.csv"
    df = pd.read_csv(csv_path)
    print(f"Loaded dataset: {len(df)} rows.")

    # 1. Descriptive Statistics
    vars_list = ['ROA', 'GF', 'NPL', 'CAR']
    desc_rows = []
    for v in vars_list:
        data = df[v]
        n = len(data)
        mean_val = np.mean(data)
        median_val = np.median(data)
        std_val = np.std(data, ddof=1)
        min_val = np.min(data)
        max_val = np.max(data)
        skew_val = float(stats.skew(data, bias=False))
        kurt_val = float(stats.kurtosis(data, fisher=False, bias=False)) # Pearson kurtosis (normal=3)
        jb_stat, jb_p = stats.jarque_bera(data)
        desc_rows.append({
            'Variabel': v,
            'Mean': mean_val,
            'Median': median_val,
            'Std_Dev': std_val,
            'Min': min_val,
            'Max': max_val,
            'Skewness': skew_val,
            'Kurtosis': kurt_val,
            'Jarque_Bera': jb_stat,
            'JB_p_val': jb_p
        })
    df_desc = pd.DataFrame(desc_rows)
    print("\n--- STATISTIK DESKRIPTIF ---")
    print(df_desc.to_string(index=False))

    # 2. Correlation Matrix
    corr_matrix = df[vars_list].corr()
    print("\n--- MATRIKS KORELASI PEARSON ---")
    print(corr_matrix)

    # 3. Multicollinearity / VIF
    X_reg = df[['GF', 'NPL', 'CAR']]
    X_with_const = sm.add_constant(X_reg)
    vif_data = []
    for i, col in enumerate(X_reg.columns):
        vif = variance_inflation_factor(X_with_const.values, i+1)
        vif_data.append({'Variabel': col, 'VIF': vif, 'Tolerance': 1/vif})
    df_vif = pd.DataFrame(vif_data)
    print("\n--- VARIANCE INFLATION FACTOR (VIF) ---")
    print(df_vif.to_string(index=False))

    # 4. Panel Setup
    quarters = {'Q1': '-03-31', 'Q2': '-06-30', 'Q3': '-09-30', 'Q4': '-12-31'}
    df['Date'] = pd.to_datetime(df['Tahun'].astype(str) + df['Kuartal'].map(quarters))
    df_panel = df.set_index(['Bank', 'Date'])

    # 5. Model Estimations
    # CEM (Pooled OLS)
    cem_model = PooledOLS.from_formula('ROA ~ 1 + GF + NPL + CAR', data=df_panel).fit()
    print("\n--- COMMON EFFECT MODEL (CEM) ---")
    print(cem_model.summary)

    # FEM (Entity Effects)
    fem_model = PanelOLS.from_formula('ROA ~ GF + NPL + CAR + EntityEffects', data=df_panel).fit()
    print("\n--- FIXED EFFECT MODEL (FEM) - Default Covariance ---")
    print(fem_model.summary)

    # FEM with Driscoll-Kraay Robust Standard Errors
    fem_dk = PanelOLS.from_formula('ROA ~ GF + NPL + CAR + EntityEffects', data=df_panel).fit(cov_type='kernel', kernel='bartlett')
    print("\n--- FIXED EFFECT MODEL (FEM) - Driscoll-Kraay Robust ---")
    print(fem_dk.summary)

    # 6. Model Selection Tests
    rss_cem = np.sum(cem_model.resids ** 2)
    rss_fem = np.sum(fem_model.resids ** 2)
    N = 4
    T = 20
    NT = 80
    K = 3
    df_num_chow = N - 1
    df_den_chow = NT - N - K
    f_chow = ((rss_cem - rss_fem) / df_num_chow) / (rss_fem / df_den_chow)
    p_chow = 1.0 - stats.f.cdf(f_chow, df_num_chow, df_den_chow)
    print(f"\n--- UJI CHOW (CEM vs FEM) ---")
    print(f"F-statistic: {f_chow:.5f}, df: ({df_num_chow}, {df_den_chow}), p-value: {p_chow:.6e}")

    # 7. Exact Degrees of Freedom & Adjusted R^2 for FEM (LSDV)
    ols_lsdv = smf.ols('ROA ~ GF + NPL + CAR + C(Bank)', data=df).fit()
    r2_lsdv = ols_lsdv.rsquared
    adj_r2_correct = 1.0 - ((1.0 - r2_lsdv) * (NT - 1)) / (NT - N - K)
    print(f"\n--- LSDV DECOMPOSITION & DEGREES OF FREEDOM ---")
    print(f"R-squared: {r2_lsdv:.5f}")
    print(f"Adjusted R-squared (Correct df={NT-N-K}): {adj_r2_correct:.5f}")
    print(ols_lsdv.summary())

    # Wald Test for slopes (H0: beta_GF = beta_NPL = beta_CAR = 0)
    wald_slopes = ols_lsdv.wald_test('GF = 0, NPL = 0, CAR = 0')
    print(f"\n--- WALD TEST FOR SLOPES ONLY ---")
    print(wald_slopes)

    # 8. Elasticity Calculations at the Means
    mean_roa = np.mean(df['ROA'])
    mean_gf = np.mean(df['GF'])
    mean_npl = np.mean(df['NPL'])
    mean_car = np.mean(df['CAR'])
    b_gf = ols_lsdv.params['GF']
    b_npl = ols_lsdv.params['NPL']
    b_car = ols_lsdv.params['CAR']
    
    eta_gf = b_gf * (mean_gf / mean_roa)
    eta_npl = b_npl * (mean_npl / mean_roa)
    eta_car = b_car * (mean_car / mean_roa)
    
    print("\n--- ELASTISITAS PADA NILAI RATA-RATA ---")
    print(f"Elastisitas Green Financing (eta_GF): {eta_gf:.4f}")
    print(f"Elastisitas NPL (eta_NPL):             {eta_npl:.4f}")
    print(f"Elastisitas CAR (eta_CAR):             {eta_car:.4f}")

    # Save structured summary markdown
    out_dir = r"z:\Skripsi\04_Riset_&_Metodologi"
    with open(os.path.join(out_dir, "ECONOMETRIC_RESULTS_V2.md"), "w", encoding="utf-8") as f:
        f.write("# Econometric Results Master Summary (v2.0)\n\n")
        f.write("## 1. Descriptive Statistics\n\n")
        f.write(df_desc.to_markdown(index=False) + "\n\n")
        f.write("## 2. Correlation Matrix\n\n")
        f.write(corr_matrix.to_markdown() + "\n\n")
        f.write("## 3. Multicollinearity (VIF)\n\n")
        f.write(df_vif.to_markdown(index=False) + "\n\n")
        f.write("## 4. LSDV Model Estimation (FEM)\n\n")
        f.write("```\n" + str(ols_lsdv.summary()) + "\n```\n\n")
        f.write("## 5. Elasticities\n\n")
        f.write(f"- $\\eta_{{\\text{{GF}}}}$: {eta_gf:.4f}\n")
        f.write(f"- $\\eta_{{\\text{{NPL}}}}$: {eta_npl:.4f}\n")
        f.write(f"- $\\eta_{{\\text{{CAR}}}}$: {eta_car:.4f}\n")

    print("\nSuccessfully generated ECONOMETRIC_RESULTS_V2.md!")

if __name__ == '__main__':
    main()

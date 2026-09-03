"""
Pure Python Econometric Verification Engine (Zero Dependencies)
Calculates exact panel metrics, LSDV dummy regression, descriptive stats, and correlations.
"""
import csv
import math

def main():
    csv_path = r"z:\Skripsi\04_Riset_&_Metodologi\dataset_kbmi4_master.csv"
    data = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'Bank': row['Bank'],
                'Periode': row['Periode'],
                'GF': float(row['GF']),
                'NPL': float(row['NPL']),
                'CAR': float(row['CAR']),
                'ROA': float(row['ROA'])
            })
    
    n = len(data)
    print(f"Total Observations: {n}")
    
    # 1. Descriptive Stats
    vars_ = ['GF', 'NPL', 'CAR', 'ROA']
    for v in vars_:
        vals = [d[v] for d in data]
        mean_v = sum(vals) / n
        s_vals = sorted(vals)
        med_v = (s_vals[n//2 - 1] + s_vals[n//2]) / 2.0 if n % 2 == 0 else s_vals[n//2]
        var_v = sum((x - mean_v)**2 for x in vals) / (n - 1)
        std_v = math.sqrt(var_v)
        min_v = min(vals)
        max_v = max(vals)
        # Skewness & Kurtosis
        m3 = sum((x - mean_v)**3 for x in vals) / n
        m4 = sum((x - mean_v)**4 for x in vals) / n
        m2 = sum((x - mean_v)**2 for x in vals) / n
        skew = m3 / (m2 ** 1.5)
        kurt = m4 / (m2 ** 2)
        jb = (n / 6.0) * (skew**2 + ((kurt - 3.0)**2) / 4.0)
        print(f"{v:5s} | Mean: {mean_v:.5f} | Median: {med_v:.5f} | Std: {std_v:.5f} | Min: {min_v:.5f} | Max: {max_v:.5f} | Skew: {skew:.4f} | Kurt: {kurt:.4f} | JB: {jb:.4f}")

    # 2. Pearson Correlations
    print("\n--- Pearson Correlation Matrix ---")
    for v1 in vars_:
        row_str = f"{v1:5s} "
        for v2 in vars_:
            vals1 = [d[v1] for d in data]
            vals2 = [d[v2] for d in data]
            m1 = sum(vals1)/n
            m2 = sum(vals2)/n
            cov = sum((x - m1)*(y - m2) for x, y in zip(vals1, vals2))
            s1 = math.sqrt(sum((x - m1)**2 for x in vals1))
            s2 = math.sqrt(sum((y - m2)**2 for y in vals2))
            r = cov / (s1 * s2)
            row_str += f"{r:9.4f} "
        print(row_str)

    # 3. OLS / LSDV Matrix Algebra
    # Model: ROA = d_BBRI*D1 + d_BMRI*D2 + d_BBCA*D3 + d_BBNI*D4 + b1*GF + b2*NPL + b3*CAR
    # X matrix: 80 x 7 (4 bank dummies + 3 slopes)
    X = []
    y = []
    for d in data:
        y.append(d['ROA'])
        d1 = 1.0 if d['Bank'] == 'BBRI' else 0.0
        d2 = 1.0 if d['Bank'] == 'BMRI' else 0.0
        d3 = 1.0 if d['Bank'] == 'BBCA' else 0.0
        d4 = 1.0 if d['Bank'] == 'BBNI' else 0.0
        X.append([d1, d2, d3, d4, d['GF'], d['NPL'], d['CAR']])
    
    # X^T X
    k = 7
    XtX = [[0.0]*k for _ in range(k)]
    Xty = [0.0]*k
    for row_x, val_y in zip(X, y):
        for i in range(k):
            Xty[i] += row_x[i] * val_y
            for j in range(k):
                XtX[i][j] += row_x[i] * row_x[j]
    
    # Invert XtX (Gaussian elimination)
    # Augmented matrix [XtX | I]
    aug = [XtX[i][:] + [1.0 if i==j else 0.0 for j in range(k)] for i in range(k)]
    for i in range(k):
        # Pivot
        pivot = aug[i][i]
        if abs(pivot) < 1e-12:
            for r in range(i+1, k):
                if abs(aug[r][i]) > abs(pivot):
                    aug[i], aug[r] = aug[r], aug[i]
                    pivot = aug[i][i]
                    break
        for j in range(2*k):
            aug[i][j] /= pivot
        for r in range(k):
            if r != i:
                factor = aug[r][i]
                for j in range(2*k):
                    aug[r][j] -= factor * aug[i][j]
    
    inv_XtX = [aug[i][k:] for i in range(k)]
    beta = [sum(inv_XtX[i][j] * Xty[j] for j in range(k)) for i in range(k)]
    
    labels = ['D_BBRI', 'D_BMRI', 'D_BBCA', 'D_BBNI', 'b_GF', 'b_NPL', 'b_CAR']
    print("\n--- LSDV Estimates (Bank Intercepts + Slopes) ---")
    
    # Residuals & Sum of Squares
    resids = []
    y_pred = []
    for row_x, val_y in zip(X, y):
        y_hat = sum(row_x[j] * beta[j] for j in range(k))
        y_pred.append(y_hat)
        resids.append(val_y - y_hat)
    
    rss = sum(e**2 for e in resids)
    mean_y = sum(y)/n
    tss = sum((val_y - mean_y)**2 for val_y in y)
    r2 = 1.0 - (rss / tss)
    df_e = n - k # 80 - 7 = 73
    s2 = rss / df_e
    se = [math.sqrt(s2 * inv_XtX[i][i]) for i in range(k)]
    t_stat = [beta[i] / se[i] for i in range(k)]
    
    adj_r2 = 1.0 - ((1.0 - r2)*(n - 1)) / df_e
    
    # Durbin Watson
    dw = sum((resids[t] - resids[t-1])**2 for t in range(1, n)) / rss
    
    for i in range(k):
        print(f"{labels[i]:10s} | Coef: {beta[i]:10.5f} | SE: {se[i]:10.5f} | t: {t_stat[i]:10.4f}")
    
    print(f"\nRSS: {rss:.5f} | TSS: {tss:.5f} | R-squared: {r2:.5f} | Adj R-squared: {adj_r2:.5f} | Durbin-Watson: {dw:.5f}")

if __name__ == '__main__':
    main()

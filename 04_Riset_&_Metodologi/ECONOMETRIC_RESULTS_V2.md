# Econometric Results Master Summary (v2.0)

## 1. Descriptive Statistics

| Variabel   |     Mean |   Median |   Std_Dev |   Min |   Max |   Skewness |   Kurtosis |   Jarque_Bera |   JB_p_val |
|:-----------|---------:|---------:|----------:|------:|------:|-----------:|-----------:|--------------:|-----------:|
| ROA        |  3.28225 |     3.29 |  0.554961 |  1.95 |  4.25 | -0.273155  |    2.46338 |       2.07031 |  0.355172  |
| GF         | 23.4588  |    23.45 |  4.16662  | 16.2  | 31.5  |  0.0734796 |    1.79514 |       4.90889 |  0.0859107 |
| NPL        |  2.417   |     2.35 |  0.588208 |  1.45 |  3.85 |  0.349342  |    2.53743 |       2.42744 |  0.29709   |
| CAR        | 23.4612  |    22.95 |  2.97008  | 17.8  | 29.4  |  0.2184    |    2.15074 |       3.14203 |  0.207834  |

## 2. Correlation Matrix

|     |       ROA |        GF |       NPL |       CAR |
|:----|----------:|----------:|----------:|----------:|
| ROA |  1        |  0.862798 | -0.869754 |  0.840853 |
| GF  |  0.862798 |  1        | -0.63269  |  0.524797 |
| NPL | -0.869754 | -0.63269  |  1        | -0.934038 |
| CAR |  0.840853 |  0.524797 | -0.934038 |  1        |

## 3. Multicollinearity (VIF)

| Variabel   |      VIF |   Tolerance |
|:-----------|---------:|------------:|
| GF         |  1.76868 |   0.565392  |
| NPL        | 10.0458  |   0.0995442 |
| CAR        |  8.31436 |   0.120274  |

## 4. LSDV Model Estimation (FEM)

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    ROA   R-squared:                       0.987
Model:                            OLS   Adj. R-squared:                  0.986
Method:                 Least Squares   F-statistic:                     896.3
Date:                Sun, 30 Aug 2026   Prob (F-statistic):           3.01e-66
Time:                        13:06:58   Log-Likelihood:                 106.62
No. Observations:                  80   AIC:                            -199.2
Df Residuals:                      73   BIC:                            -182.6
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
Intercept          -0.2582      0.338     -0.765      0.447      -0.931       0.415
C(Bank)[T.BBNI]    -0.1549      0.067     -2.315      0.023      -0.288      -0.022
C(Bank)[T.BBRI]     0.0596      0.056      1.069      0.289      -0.052       0.171
C(Bank)[T.BMRI]     0.1275      0.055      2.315      0.023       0.018       0.237
GF                  0.0767      0.005     15.719      0.000       0.067       0.086
NPL                -0.0721      0.047     -1.528      0.131      -0.166       0.022
CAR                 0.0813      0.011      7.308      0.000       0.059       0.103
==============================================================================
Omnibus:                        0.852   Durbin-Watson:                   0.566
Prob(Omnibus):                  0.653   Jarque-Bera (JB):                0.841
Skew:                          -0.237   Prob(JB):                        0.657
Kurtosis:                       2.833   Cond. No.                     1.53e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.53e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

## 5. Elasticities

- $\eta_{\text{GF}}$: 0.5483
- $\eta_{\text{NPL}}$: -0.0531
- $\eta_{\text{CAR}}$: 0.5811

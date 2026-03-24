# Econometric Report — Yearly Data

## Model Selection
Model selected: VECM

## Cointegration (Johansen)
|   Cointegration Rank |   Trace Statistic |   Trace 5% Critical |   Max-Eigen Statistic |   Max-Eigen 5% Critical |
|---------------------:|------------------:|--------------------:|----------------------:|------------------------:|
|                    0 |         79.9284   |             69.8189 |             36.9071   |                 33.8777 |
|                    1 |         43.0213   |             47.8545 |             25.2556   |                 27.5858 |
|                    2 |         17.7657   |             29.7961 |             10.6257   |                 21.1314 |
|                    3 |          7.14002  |             15.4943 |              6.7324   |                 14.2639 |
|                    4 |          0.407618 |              3.8415 |              0.407618 |                  3.8415 |

## Pairwise Granger Causality
| Direction                   |   Lag |   F-statistic |    p-value |
|:----------------------------|------:|--------------:|-----------:|
| log_gold_usd → log_oil_usd  |     1 |     0.703023  | 0.407626   |
| log_gold_usd → log_oil_usd  |     2 |     4.30976   | 0.0223107  |
| log_usd_inr → log_oil_usd   |     1 |     1.82264   | 0.185919   |
| log_usd_inr → log_oil_usd   |     2 |     1.76237   | 0.188401   |
| log_oil_inr → log_oil_usd   |     1 |     1.82264   | 0.185919   |
| log_oil_inr → log_oil_usd   |     2 |     1.76237   | 0.188401   |
| log_gold_inr → log_oil_usd  |     1 |     1.99509   | 0.166898   |
| log_gold_inr → log_oil_usd  |     2 |     2.34145   | 0.112973   |
| log_oil_usd → log_gold_usd  |     1 |     6.20016   | 0.0178237  |
| log_oil_usd → log_gold_usd  |     2 |     2.02432   | 0.149178   |
| log_usd_inr → log_gold_usd  |     1 |     3.45284   | 0.0718196  |
| log_usd_inr → log_gold_usd  |     2 |     3.13648   | 0.0574781  |
| log_oil_inr → log_gold_usd  |     1 |     7.85462   | 0.00831068 |
| log_oil_inr → log_gold_usd  |     2 |     3.71481   | 0.0357917  |
| log_gold_inr → log_gold_usd |     1 |     3.45284   | 0.0718196  |
| log_gold_inr → log_gold_usd |     2 |     3.13648   | 0.0574781  |
| log_oil_usd → log_usd_inr   |     1 |     1.55274   | 0.221249   |
| log_oil_usd → log_usd_inr   |     2 |     1.11413   | 0.340988   |
| log_gold_usd → log_usd_inr  |     1 |     3.86304   | 0.0575719  |
| log_gold_usd → log_usd_inr  |     2 |     7.81438   | 0.00178637 |
| log_oil_inr → log_usd_inr   |     1 |     1.55274   | 0.221249   |
| log_oil_inr → log_usd_inr   |     2 |     1.11413   | 0.340988   |
| log_gold_inr → log_usd_inr  |     1 |     3.86304   | 0.0575719  |
| log_gold_inr → log_usd_inr  |     2 |     7.81438   | 0.00178637 |
| log_oil_usd → log_oil_inr   |     1 |     1.25011   | 0.271369   |
| log_oil_usd → log_oil_inr   |     2 |     1.75805   | 0.189134   |
| log_gold_usd → log_oil_inr  |     1 |     0.287798  | 0.595128   |
| log_gold_usd → log_oil_inr  |     2 |     2.48802   | 0.0995173  |
| log_usd_inr → log_oil_inr   |     1 |     1.25011   | 0.271369   |
| log_usd_inr → log_oil_inr   |     2 |     1.75805   | 0.189134   |
| log_gold_inr → log_oil_inr  |     1 |     1.53893   | 0.223269   |
| log_gold_inr → log_oil_inr  |     2 |     1.64502   | 0.209413   |
| log_oil_usd → log_gold_inr  |     1 |     3.88616   | 0.0568684  |
| log_oil_usd → log_gold_inr  |     2 |     1.64052   | 0.210266   |
| log_gold_usd → log_gold_inr |     1 |     0.0672891 | 0.79689    |
| log_gold_usd → log_gold_inr |     2 |     4.84637   | 0.0147433  |
| log_usd_inr → log_gold_inr  |     1 |     0.0672891 | 0.79689    |
| log_usd_inr → log_gold_inr  |     2 |     4.84637   | 0.0147433  |
| log_oil_inr → log_gold_inr  |     1 |     2.98027   | 0.0933628  |
| log_oil_inr → log_gold_inr  |     2 |     1.41723   | 0.257655   |

## Block Exogeneity
| Caused   | Causing        |   F-stat |   p-value |
|:---------|:---------------|---------:|----------:|
| y1       | y2, y3, y4, y5 | 1.22912  |  0.274983 |
| y2       | y1, y3, y4, y5 | 0.604318 |  0.833671 |
| y3       | y1, y2, y4, y5 | 1.02662  |  0.431337 |
| y4       | y1, y2, y3, y5 | 1.01175  |  0.444568 |
| y5       | y1, y2, y3, y4 | 0.931298 |  0.519509 |

## Volatility Spillovers (DCC)
|   Time | Pair                     |   Correlation |
|-------:|:-------------------------|--------------:|
|      0 | oil_usd_ret-gold_usd_ret |    0.199078   |
|      0 | oil_usd_ret-usd_inr_ret  |   -0.353233   |
|      0 | oil_usd_ret-oil_inr_ret  |    0.965218   |
|      0 | oil_usd_ret-gold_inr_ret |    0.00802641 |
|      0 | gold_usd_ret-usd_inr_ret |   -0.398529   |


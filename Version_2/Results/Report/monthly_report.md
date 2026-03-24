# Econometric Report — Monthly Data

## Model Selection
Model selected: VECM

## Cointegration (Johansen)
|   Cointegration Rank |   Trace Statistic |   Trace 5% Critical |   Max-Eigen Statistic |   Max-Eigen 5% Critical |
|---------------------:|------------------:|--------------------:|----------------------:|------------------------:|
|                    0 |       1998.67     |             69.8189 |           1972.3      |                 33.8777 |
|                    1 |         26.3658   |             47.8545 |             14.5545   |                 27.5858 |
|                    2 |         11.8113   |             29.7961 |             11.1968   |                 21.1314 |
|                    3 |          0.61446  |             15.4943 |              0.372265 |                 14.2639 |
|                    4 |          0.242196 |              3.8415 |              0.242196 |                  3.8415 |

## Pairwise Granger Causality
| Direction                   |   Lag |   F-statistic |   p-value |
|:----------------------------|------:|--------------:|----------:|
| log_gold_usd → log_oil_usd  |     1 |     2.59224   | 0.108082  |
| log_gold_usd → log_oil_usd  |     2 |     4.22924   | 0.015144  |
| log_usd_inr → log_oil_usd   |     1 |     1.59172   | 0.207727  |
| log_usd_inr → log_oil_usd   |     2 |     2.99183   | 0.0511906 |
| log_oil_inr → log_oil_usd   |     1 |     1.59172   | 0.207727  |
| log_oil_inr → log_oil_usd   |     2 |     2.99183   | 0.0511906 |
| log_gold_inr → log_oil_usd  |     1 |     3.18597   | 0.0749392 |
| log_gold_inr → log_oil_usd  |     2 |     3.59303   | 0.0283036 |
| log_oil_usd → log_gold_usd  |     1 |     1.04119   | 0.308087  |
| log_oil_usd → log_gold_usd  |     2 |     0.47661   | 0.621197  |
| log_usd_inr → log_gold_usd  |     1 |     3.9792    | 0.0466614 |
| log_usd_inr → log_gold_usd  |     2 |     2.65837   | 0.0711578 |
| log_oil_inr → log_gold_usd  |     1 |     3.47507   | 0.0629439 |
| log_oil_inr → log_gold_usd  |     2 |     1.47333   | 0.23026   |
| log_gold_inr → log_gold_usd |     1 |     3.9792    | 0.0466614 |
| log_gold_inr → log_gold_usd |     2 |     2.65837   | 0.0711578 |
| log_oil_usd → log_usd_inr   |     1 |     2.03418   | 0.154483  |
| log_oil_usd → log_usd_inr   |     2 |     1.1432    | 0.319717  |
| log_gold_usd → log_usd_inr  |     1 |     3.29917   | 0.0699729 |
| log_gold_usd → log_usd_inr  |     2 |     2.53838   | 0.0801197 |
| log_oil_inr → log_usd_inr   |     1 |     2.03418   | 0.154483  |
| log_oil_inr → log_usd_inr   |     2 |     1.1432    | 0.319717  |
| log_gold_inr → log_usd_inr  |     1 |     3.29917   | 0.0699729 |
| log_gold_inr → log_usd_inr  |     2 |     2.53838   | 0.0801197 |
| log_oil_usd → log_oil_inr   |     1 |     1.37524   | 0.241528  |
| log_oil_usd → log_oil_inr   |     2 |     3.26424   | 0.0391292 |
| log_gold_usd → log_oil_inr  |     1 |     1.55752   | 0.212671  |
| log_gold_usd → log_oil_inr  |     2 |     2.50492   | 0.0828153 |
| log_usd_inr → log_oil_inr   |     1 |     1.37524   | 0.241528  |
| log_usd_inr → log_oil_inr   |     2 |     3.26424   | 0.0391292 |
| log_gold_inr → log_oil_inr  |     1 |     3.351     | 0.0678182 |
| log_gold_inr → log_oil_inr  |     2 |     3.44616   | 0.0327076 |
| log_oil_usd → log_gold_inr  |     1 |     0.496001  | 0.481623  |
| log_oil_usd → log_gold_inr  |     2 |     0.266156  | 0.766439  |
| log_gold_usd → log_gold_inr |     1 |     0.0907247 | 0.763395  |
| log_gold_usd → log_gold_inr |     2 |     0.0447411 | 0.956249  |
| log_usd_inr → log_gold_inr  |     1 |     0.0907247 | 0.763395  |
| log_usd_inr → log_gold_inr  |     2 |     0.0447411 | 0.956249  |
| log_oil_inr → log_gold_inr  |     1 |     0.267069  | 0.605556  |
| log_oil_inr → log_gold_inr  |     2 |     0.162246  | 0.850282  |

## Block Exogeneity
| Caused   | Causing        |   F-stat |   p-value |
|:---------|:---------------|---------:|----------:|
| y1       | y2, y3, y4, y5 | 0.910392 |  0.535579 |
| y2       | y1, y3, y4, y5 | 0.639163 |  0.810059 |
| y3       | y1, y2, y4, y5 | 0.606676 |  0.838247 |
| y4       | y1, y2, y3, y5 | 0.973411 |  0.471999 |
| y5       | y1, y2, y3, y4 | 0.272934 |  0.993222 |

## Volatility Spillovers (DCC)
|   Time | Pair                     |   Correlation |
|-------:|:-------------------------|--------------:|
|      0 | oil_usd_ret-gold_usd_ret |      0.139576 |
|      0 | oil_usd_ret-usd_inr_ret  |     -0.132566 |
|      0 | oil_usd_ret-oil_inr_ret  |      0.973751 |
|      0 | oil_usd_ret-gold_inr_ret |      0.080393 |
|      0 | gold_usd_ret-usd_inr_ret |     -0.208469 |


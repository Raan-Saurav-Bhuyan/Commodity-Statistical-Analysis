import pandas as pd
from statsmodels.tsa.vector_ar.vecm import coint_johansen

def johansen_test(df: pd.DataFrame, det_order: int = 0, k_ar_diff: int = 1) -> pd.DataFrame:
    """
    det_order:
        -1: no deterministic terms
         0: constant in cointegration relation
         1: linear trend

    k_ar_diff: Number of lagged differences
    """

    result = coint_johansen(
        df,
        det_order = det_order,
        k_ar_diff = k_ar_diff,
    )

    rows = []

    for i in range(len(result.lr1)):
        rows.append({
            "Cointegration Rank": i,
            "Trace Statistic": result.lr1[i],
            "Trace 5% Critical": result.cvt[i, 1],
            "Max-Eigen Statistic": result.lr2[i],
            "Max-Eigen 5% Critical": result.cvm[i, 1],
        })

    return pd.DataFrame(rows)

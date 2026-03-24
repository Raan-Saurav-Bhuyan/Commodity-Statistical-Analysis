import pandas as pd
from statsmodels.tsa.vector_ar.vecm import coint_johansen

def johansen_test(df: pd.DataFrame, det_order: int, k_ar_diff: int) -> pd.DataFrame:
    """
    Johansen cointegration test (trace & max-eigen).
    """
    test = coint_johansen(df, det_order, k_ar_diff)

    results = []

    for i in range(len(test.lr1)):
        results.append(
            [
                i,
                test.lr1[i],
                test.cvt[i, 1],
                test.lr2[i],
                test.cvm[i, 1]
            ]
        )

    return pd.DataFrame(
        results,
        columns = [
            "Cointegration Rank",
            "Trace Statistic",
            "Trace 5% Critical",
            "Max-Eigen Statistic",
            "Max-Eigen 5% Critical"
        ]
    )

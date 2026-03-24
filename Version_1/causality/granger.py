import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

def granger_test(
    df: pd.DataFrame,
    caused: str,
    causing: str,
    max_lag: int
) -> dict:
    """
    Run Granger causality test and extract Wald statistic.
    """
    test = grangercausalitytests(
        df[[caused, causing]],
        maxlag = max_lag,
        verbose = False
    )

    stats = [
        (
            lag,
            test[lag][0]["ssr_ftest"][0],
            test[lag][0]["ssr_ftest"][1]
        )
        for lag in range(1, max_lag + 1)
    ]

    return stats

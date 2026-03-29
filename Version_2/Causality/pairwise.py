import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

def run_pairwise_granger(data: pd.DataFrame, max_lag: int = 2) -> pd.DataFrame:
    results = []

    variables = data.columns

    for caused in variables:
        for causing in variables:
            if caused == causing:
                continue

            test_data = data[[caused, causing]]

            test_result = grangercausalitytests(
                test_data,
                maxlag = max_lag,
                verbose = False,
            )

            for lag in range(1, max_lag + 1):
                f_stat = test_result[lag][0]["ssr_ftest"][0]
                p_val = test_result[lag][0]["ssr_ftest"][1]

                results.append({
                    "Direction": f"{causing} → {caused}",
                    "Lag": lag,
                    "F-statistic": f_stat,
                    "p-value": p_val,
                })

    return pd.DataFrame(results)

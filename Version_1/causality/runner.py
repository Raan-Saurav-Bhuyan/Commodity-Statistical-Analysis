import pandas as pd
from causality.lag_selection import select_var_lag
from causality.granger import granger_test

def run_granger_tests(filepath: str) -> None:
    df = pd.read_csv(filepath, index_col = 0, parse_dates = True)

    returns = df[["oil_log_return", "gold_log_return"]].dropna()

    lag = select_var_lag(returns)

    oil_to_gold = granger_test(
        returns,
        caused = "gold_log_return",
        causing = "oil_log_return",
        max_lag = lag
    )

    gold_to_oil = granger_test(
        returns,
        caused = "oil_log_return",
        causing = "gold_log_return",
        max_lag = lag
    )

    records = []

    for lag_i, stat, p in oil_to_gold:
        records.append(
            [
                "Oil → Gold",
                lag_i,
                stat,
                p
            ]
        )

    for lag_i, stat, p in gold_to_oil:
        records.append(
            [
                "Gold → Oil",
                lag_i,
                stat,
                p
            ]
        )

    out = pd.DataFrame(
        records,
        columns = [
            "Direction",
            "Lag",
            "F-statistic",
            "p-value"
        ]
    )

    out.to_csv("Results/Tables/granger_causality_results.csv", index = False)

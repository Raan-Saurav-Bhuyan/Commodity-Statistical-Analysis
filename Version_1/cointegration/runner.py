import pandas as pd
from cointegration.lag_selection import select_lag
from cointegration.engle_granger import engle_granger_test
from cointegration.johansen import johansen_test

def run_cointegration_tests(filepath: str) -> None:
    df = pd.read_csv(filepath, index_col = 0, parse_dates = True)

    prices = df[["oil_log_price", "gold_log_price"]].dropna()

    lag = select_lag(prices)

    eg_og = engle_granger_test(
        y=prices["oil_log_price"],
        x=prices["gold_log_price"]
    )

    eg_go = engle_granger_test(
        y=prices["gold_log_price"],
        x=prices["oil_log_price"]
    )

    eg_table = pd.DataFrame([
        ["Oil ~ Gold", eg_og["stat"], eg_og["pvalue"]],
        ["Gold ~ Oil", eg_go["stat"], eg_go["pvalue"]]
    ], columns = ["Regression", "ADF Stat", "p-value"])

    eg_table.to_csv("Results/Tables/engle_granger_results.csv", index = False)

    johansen = johansen_test(
        df = prices,
        det_order = 0,
        k_ar_diff = lag
    )

    johansen.to_csv("Results/Tables/johansen_results.csv", index = False)

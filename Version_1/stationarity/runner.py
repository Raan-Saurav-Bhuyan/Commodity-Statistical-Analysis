# file: src/stationarity/runner.py

import pandas as pd
from stationarity.tests import adf_test, pp_test
from stationarity.integration import integration_order


def run_stationarity_tests(filepath: str) -> None:
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)

    series_list = {
        "oil_log_price": df["oil_log_price"],
        "gold_log_price": df["gold_log_price"],
        "oil_log_return": df["oil_log_return"],
        "gold_log_return": df["gold_log_return"],
    }

    results = []

    for name, series in series_list.items():
        series = series.dropna()
        diff = series.diff().dropna()

        adf_lvl = adf_test(series)
        adf_diff = adf_test(diff)

        pp_lvl = pp_test(series)
        pp_diff = pp_test(diff)

        order = integration_order(adf_lvl["pvalue"], adf_diff["pvalue"])

        results.append([
            name,
            adf_lvl["stat"], adf_lvl["pvalue"],
            adf_diff["stat"], adf_diff["pvalue"],
            pp_lvl["stat"], pp_lvl["pvalue"],
            pp_diff["stat"], pp_diff["pvalue"],
            order
        ])

    out = pd.DataFrame(
        results,
        columns = [
            "Series",
            "ADF Level Stat", "ADF Level p",
            "ADF Diff Stat", "ADF Diff p",
            "PP Level Stat", "PP Level p",
            "PP Diff Stat", "PP Diff p",
            "Integration Order"
        ]
    )

    out.to_csv("Results/Tables/stationarity_tests.csv", index = False)

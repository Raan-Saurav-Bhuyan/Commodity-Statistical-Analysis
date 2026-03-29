from pathlib import Path
import pandas as pd

# Import custom modules: --->
from Stationarity.integration import determine_integration
from Stationarity.exporter import export_results
from Stationarity.adf_pp import (
    run_unit_root_tests,
    run_diff_tests,
)

PROCESSED_DIR = Path("Datasets/Processed")
RESULTS_DIR = Path("Results/Tables")

def run_stationarity(frequency: str) -> None:
    """
    frequency: 'monthly' or 'yearly'
    """

    prices_path = PROCESSED_DIR / f"{frequency}_prices.csv"
    returns_path = PROCESSED_DIR / f"{frequency}_returns.csv"

    df_prices = pd.read_csv(prices_path, index_col=0, parse_dates=True)
    df_returns = pd.read_csv(returns_path, index_col=0, parse_dates=True)

    results = []

    # Test log prices:  --->
    for col in df_prices.columns:
        level_results = run_unit_root_tests(df_prices[col])
        diff_results = run_diff_tests(df_prices[col])

        row = {"Series": col}
        row.update(level_results)
        row.update(diff_results)
        row["Integration Order"] = determine_integration(row)

        results.append(row)

    # Test returns (already diffed): --->
    for col in df_returns.columns:
        level_results = run_unit_root_tests(df_returns[col])
        diff_results = run_diff_tests(df_returns[col])

        row = {"Series": col}
        row.update(level_results)
        row.update(diff_results)
        row["Integration Order"] = determine_integration(row)

        results.append(row)

    df_results = pd.DataFrame(results)

    export_results(
        df_results,
        RESULTS_DIR / f"{frequency}_unit_root_tests.csv",
    )

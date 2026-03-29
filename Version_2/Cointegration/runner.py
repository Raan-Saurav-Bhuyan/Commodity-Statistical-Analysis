from pathlib import Path
import pandas as pd

# Import custom modules: --->
from Cointegration.engle_granger import run_pairwise_engle_granger
from Cointegration.johansen import johansen_test
from Cointegration.rank_selection import select_rank
from Cointegration.exporter import export_results

PROCESSED_DIR = Path("Datasets/Processed")
RESULTS_DIR = Path("Results/Tables")


def run_cointegration(frequency: str) -> None:
    """
    frequency: 'monthly' or 'yearly'
    """

    prices_path = PROCESSED_DIR / f"{frequency}_prices.csv"

    df = pd.read_csv(prices_path, index_col=0, parse_dates=True)

    # Use only log INR prices for cointegration: --->
    df_prices = df[[col for col in df.columns if "log_" in col]]

    # Engle-Granger (Pairwise): --->
    eg_results = run_pairwise_engle_granger(df_prices)

    export_results(
        eg_results,
        RESULTS_DIR / f"{frequency}_engle_granger.csv",
    )

    # Johansen (System-wide): --->
    johansen_results = johansen_test(
        df_prices,
        det_order=0,
        k_ar_diff=1,
    )

    export_results(
        johansen_results,
        RESULTS_DIR / f"{frequency}_johansen.csv",
    )

    # Rank selection: --->
    rank = select_rank(johansen_results)

    with open(RESULTS_DIR / f"{frequency}_cointegration_rank.txt", "w") as f:
        f.write(f"Selected cointegration rank: {rank}")

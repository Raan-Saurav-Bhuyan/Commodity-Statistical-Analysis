# Import libraries: --->
import pandas as pd
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.tsa.vector_ar.vecm import VECM

# Import custom modules: --->
from .pairwise import run_pairwise_granger
from .block_exogeneity import run_block_exogeneity
from .exporter import export_results

PROCESSED_DIR = Path("Datasets/Processed")
RESULTS_DIR = Path("Results")


def load_model_type(frequency: str) -> str:
    with open(RESULTS_DIR / "Tables" / f"{frequency}_model_selected.txt") as f:
        return f.read().strip()

def run_causality(frequency: str) -> None:
    model_type = load_model_type(frequency)

    prices_path = PROCESSED_DIR / f"{frequency}_prices.csv"
    returns_path = PROCESSED_DIR / f"{frequency}_returns.csv"

    df_prices = pd.read_csv(prices_path, index_col = 0, parse_dates = True)
    df_returns = pd.read_csv(returns_path, index_col = 0, parse_dates = True)

    ########################################################
    # Case 1: VAR selected → use returns: --->
    if "VAR" in model_type:
        data = df_returns

        model = VAR(data).fit(2)
    ########################################################

    ########################################################
    # Case 2: VECM selected → use levels: --->
    else:
        data = df_prices

        model = VECM(
            data,
            k_ar_diff = 2,
            coint_rank = 1,
            deterministic = "co",
        ).fit()

    # Pairwise Granger: --->
    pairwise_results = run_pairwise_granger(
        data,
        max_lag = 2,
    )

    export_results(
        pairwise_results,
        RESULTS_DIR / "Tables" / f"{frequency}_pairwise_granger.csv",
    )

    # Block Exogeneity: --->
    block_results = run_block_exogeneity(model)

    export_results(
        block_results,
        RESULTS_DIR / "Tables" / f"{frequency}_block_exogeneity.csv",
    )

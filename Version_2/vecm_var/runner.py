from pathlib import Path
import pandas as pd

# Import custom modules: --->
from vecm_var.lag_selection import select_lag_length
from vecm_var.vecm_model import estimate_vecm
from vecm_var.var_model import estimate_var
from vecm_var.irf_fevd import compute_irf, compute_fevd
from vecm_var.exporter import export_summary
from vecm_var.diagnostics import (
    check_stability,
)

PROCESSED_DIR = Path("Datasets/Processed")
RESULTS_DIR = Path("Results")

def load_rank(frequency: str) -> int:
    with open(RESULTS_DIR / "Tables" / f"{frequency}_cointegration_rank.txt") as f:
        return int(f.read().split(":")[1].strip())

def run_vecm_var(frequency: str) -> None:
    prices_path = PROCESSED_DIR / f"{frequency}_prices.csv"
    returns_path = PROCESSED_DIR / f"{frequency}_returns.csv"

    df_prices = pd.read_csv(prices_path, index_col = 0, parse_dates = True)
    df_returns = pd.read_csv(returns_path, index_col = 0, parse_dates = True)

    rank = load_rank(frequency)

    model_type_path = RESULTS_DIR / "Tables" / f"{frequency}_model_selected.txt"

    #############################################################
    # Case 1: Cointegration Exists → VECM: --->
    if rank > 0:

        lags = select_lag_length(df_prices)

        vecm_res = estimate_vecm(df_prices,rank = rank, k_ar_diff = lags)

        export_summary(
            vecm_res.summary(),
            RESULTS_DIR / "Tables" / f"{frequency}_vecm_summary.txt",
        )

        with open(model_type_path, "w") as f:
            f.write("Model selected: VECM")

        model_res = vecm_res
    #############################################################

    #############################################################
    # CASE 2: No Cointegration → VAR in Returns: --->
    else:
        lags = select_lag_length(df_returns)

        var_res = estimate_var(df_returns, lags = lags)

        export_summary(
            var_res.summary(),
            RESULTS_DIR / "Tables" / f"{frequency}_var_summary.txt",
        )

        with open(model_type_path, "w") as f:
            f.write("Model selected: VAR (Differences)")

        model_res = var_res
    #############################################################

    # Diagnostics: --->
    stability = check_stability(model_res)

    with open(RESULTS_DIR / "Tables" / f"{frequency}_stability.txt", "w") as f:
        f.write(f"Stable: {stability}")

    # IRF: --->
    irf = compute_irf(model_res)

    if irf is not None:
        fig_irf = irf.plot(orth=False)
        fig_irf.savefig(RESULTS_DIR / "Figures" / f"{frequency}_irf.png")

        fig_irf.clf()

    # FEVD (only if available): --->
    fevd = compute_fevd(model_res)

    if fevd is not None:
        fig_fevd = fevd.plot()
        fig_fevd.savefig(RESULTS_DIR / "Figures" / f"{frequency}_fevd.png")

        fig_fevd.clf()

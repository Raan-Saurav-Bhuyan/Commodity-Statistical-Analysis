# Import libraries: --->
import os

# Import module runners: --->
from Preparation import run_preparation_pipeline
from Stationarity import run_stationarity
from Cointegration import run_cointegration

# Import custom modules: --->
from .lag_selection import select_lag
from .var_model import fit_var
from .vecm_model import fit_vecm
from .irf_fevd import compute_irf, compute_fevd
from .diagnostics import run_diagnostics
from .exporter import export_model_summary

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "Results", "Report")

def run_model_system(df, rank, name):
    """
    Decide VAR or VECM and run model
    """

    lags = select_lag(df)

    if rank >= 1:
        print("Running VECM model...")

        model = fit_vecm(df, rank, lags)
        model_type = "VECM"
    else:
        print("Running VAR model...")

        model = fit_var(df, lags)
        model_type = "VAR"

        irf = compute_irf(model)
        fevd = compute_fevd(model)

    diagnostics = run_diagnostics(model)

    # Export summary: --->
    export_model_summary(
        model.summary(),
        os.path.join(OUTPUT_DIR, f"{name}_{model_type}_summary.txt")
    )

    if rank >= 1:
        return {
            "system": name,
            "model_type": model_type,
            "lags": lags,
            "rank": rank,
            # "irf": irf,
            # "fevd": fevd,
            "diagnostics": diagnostics
        }
    else:
                return {
            "system": name,
            "model_type": model_type,
            "lags": lags,
            "rank": rank,
            "irf": irf,
            "fevd": fevd,
            "diagnostics": diagnostics
        }

def run_vecm_var(views = None, coint_results = None):
    """
    Main pipeline
    """

    # Load data: --->
    if views is None:
        views = run_preparation_pipeline()

    # Cointegration: --->
    if coint_results is None:
        stationarity = run_stationarity(views)
        coint_results = run_cointegration(views, stationarity)

    df = views["combined"]

    results = []

    for system in coint_results:
        cols = system["variables"]
        rank = system["rank"]

        sub_df = df[cols].dropna()

        results.append(run_model_system(sub_df, rank, system["system"]))

    print("VAR/VECM modeling completed.")

    return results

# Import libraries: --->
import os

# Import module runners: --->
from Preparation import run_preparation_pipeline

# Import custom modules: --->
from .garch import fit_garch
from .dcc import compute_standardized_residuals, compute_dcc
from .diagnostics import summarize_volatility
from .exporter import export_dcc

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "Results", "Tables", "dcc_results.npy")

def run_volatility():
    """
    Main DCC-GARCH pipeline with inflation
    """

    views = run_preparation_pipeline()

    df = views["combined"]

    # Select variables: --->
    cols = [
        "oil_usd_ret",
        "gold_usd_ret",
        "usd_inr_ret",
        "inflation_india"
    ]

    data = df[cols].dropna()

    # Fit GARCH: --->
    garch_results = []

    for col in cols:
        res = fit_garch(data[col])
        garch_results.append(res)

    # Compute DCC: --->
    residuals = compute_standardized_residuals(garch_results)
    dcc = compute_dcc(residuals)

    # Export DCC: --->
    export_dcc(dcc, OUTPUT_PATH)

    diagnostics = summarize_volatility(garch_results)

    print("✅ DCC-GARCH with inflation completed.")

    return {
        "dcc": dcc,
        "diagnostics": diagnostics
    }

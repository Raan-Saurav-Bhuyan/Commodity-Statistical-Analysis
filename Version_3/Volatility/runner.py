# Import libraries: --->
import os
import numpy as np
import traceback
import pandas as pd

# Import custom modules: --->
from .garch import fit_garch
from .dcc import compute_standardized_residuals, compute_dcc
from .diagnostics import summarize_volatility

from .exporter import (
    export_dcc,
    export_dcc_yearly,
    export_volatility_yearly
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NPY_PATH = os.path.join(
    BASE_DIR, "Results",
    "Tables",
    "dcc_results.npy"
)

TABLE_DIR = os.path.join(
    BASE_DIR,
    "Results",
    "Tables"
)


def run_volatility(views):
    """
    Full-sample DCC-GARCH pipeline (no yearly segmentation)
    """

    print("\n[Volatility] Running Full-Sample DCC-GARCH...\n")

    df = views["combined"].copy()

    # Ensure datetime index --->
    df.index = pd.to_datetime(df["Date"], format="%Y")

    # Variable selection --->
    cols = [
        "log_oil_usd_ret",
        "log_gold_usd_ret",
        "log_usd_inr_ret",
        "inflation_india",
        "inflation_usa",
        "log_oil_inr_ret",
        "log_gold_inr_ret",
        "log_cpi_india",
        "log_cpi_usa",
        "log_oil_usd_real_ret",
        "log_gold_usd_real_ret",
        "log_usd_inr_real_ret",
        "log_oil_inr_real_ret",
        "log_gold_inr_real_ret"
    ]

    # Filter available columns only --->
    available_cols = [c for c in cols if c in df.columns]
    missing_cols = [c for c in cols if c not in df.columns]

    print("Using columns:", available_cols)
    if missing_cols:
        print("Missing columns:", missing_cols)

    df = df[available_cols].dropna()

    print(f"Total observations after cleaning: {len(df)}")

    if len(df) < 30:
        raise ValueError("Not enough data for GARCH/DCC estimation.")

    # GARCH fitting: --->
    print("\n[Step 1] Fitting GARCH models...\n")

    garch_results = {}
    vol_series_dict = {}
    all_volatility = []

    for col in available_cols:
        try:
            res = fit_garch(df[col])
            garch_results[col] = res

            vol_series = res.conditional_volatility

            vol_series_dict[col] = vol_series

            for t, val in enumerate(vol_series):
                all_volatility.append({
                    "time_index": t,
                    "variable": col,
                    "volatility": float(val)
                })

        except Exception as e:
            print(f"\n[GARCH ERROR] {col}: {str(e)}\n")
            traceback.print_exc()

    if len(garch_results) == 0:
        raise RuntimeError("All GARCH models failed. Cannot proceed.")

    # Standardized residuals: --->
    print("\n[Step 2] Computing standardized residuals...\n")

    residuals = compute_standardized_residuals(garch_results)

    residuals = np.asarray(residuals)

    print("Residuals shape:", residuals.shape)

    # DCC estimation: --->
    print("\n[Step 3] Computing DCC correlations...\n")

    try:
        dcc_matrix = compute_dcc(residuals)
        dcc_matrix = np.asarray(dcc_matrix)

    except Exception as e:
        print("\n[DCC ERROR]\n")
        traceback.print_exc()
        raise e

    print("DCC matrix shape:", dcc_matrix.shape)

    # Pair-wise extraction: --->
    print("\n[Step 4] Extracting pairwise correlations...\n")

    all_dcc_pairs = []
    var_list = list(vol_series_dict.keys())
    n_vars = len(var_list)

    for t in range(dcc_matrix.shape[0]):
        corr_matrix = dcc_matrix[t]

        for i in range(n_vars):
            for j in range(i + 1, n_vars):

                all_dcc_pairs.append({
                    "time_index": t,
                    "pair": f"{var_list[i]}-{var_list[j]}",
                    "correlation": float(corr_matrix[i, j])
                })

    # Export results: --->
    print("\n[Step 5] Exporting results...\n")

    # Save raw DCC --->
    export_dcc({"full_sample": dcc_matrix}, NPY_PATH)

    # vol_df.to_csv(os.path.join(TABLE_DIR, "volatility_full.csv"), index = False)

    # Convert volatility to DataFrame --->
    export_volatility_yearly(all_volatility, os.path.join(TABLE_DIR, "volatility_yearly_full.csv"))

    # dcc_df = pd.DataFrame(all_dcc_pairs)
    # dcc_df.to_csv(os.path.join(TABLE_DIR, "dcc_pairwise_full.csv"), index = False)

    # Convert DCC pairs --->
    export_dcc_yearly(all_dcc_pairs, os.path.join(TABLE_DIR, "dcc_yearly_full.csv"))

    # Diagnostics: --->
    diagnostics = summarize_volatility(garch_results)

    print("\n[Volatility] Completed successfully.\n")

    return {
        "dcc_raw": dcc_matrix,
        "dcc_pairs": all_dcc_pairs,
        "volatility": all_volatility,
        "diagnostics": diagnostics
    }

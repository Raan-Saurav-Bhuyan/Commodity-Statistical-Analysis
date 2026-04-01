# Import libraries: --->
import os
import pandas as pd

# Import module runners: --->
from Preparation import run_preparation_pipeline

# Import custom modules: --->
from .pairwise import run_pairwise_granger
from .block_exogeneity import run_block_exogeneity

from .exporter import (
    export_pairwise_yearly,
    export_block_exogeneity_yearly
)

# Export file paths: --->
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAIRWISE_PATH = os.path.join(
    BASE_DIR, "Results", "Tables", "pairwise_granger_yearly.csv"
)

BLOCK_PATH = os.path.join(
    BASE_DIR, "Results", "Tables", "block_exogeneity_yearly.csv"
)


def run_causality(views=None):
    """
    Runs full causality pipeline

    Includes:
    - Pairwise Granger causality (rolling window)
    - Block exogeneity (VAR-based)
    """

    # Load data: --->
    if views is None:
        views = run_preparation_pipeline()

    df = views["combined"].copy()

    # Variable selection: --->
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

    data = df[cols].copy()
    data["year"] = df["Date"].astype(int).values

    # Clean data: --->
    data = data.dropna().reset_index(drop=True)

    pairwise_results = []
    block_results = []

    # Rolling window setup: --->
    window_size = 20
    n_obs = len(data)

    if n_obs < window_size:
        print("Not enough data for rolling causality.")
        return {
            "pairwise": [],
            "block_exogeneity": []
        }

    # Rolling causality: --->
    for start in range(0, n_obs - window_size + 1):

        end = start + window_size
        window = data.iloc[start:end]

        start_year = int(window["year"].iloc[0])
        end_year = int(window["year"].iloc[-1])

        group = window.drop(columns=["year"])

        # 🚨 HARD FILTER: skip tiny samples
        if len(group) < 8:
            continue

        # Pair-wise Granger: --->
        try:
            pw_df = run_pairwise_granger(group)

            if isinstance(pw_df, pd.DataFrame) and not pw_df.empty:
                pw_df["start_year"] = start_year
                pw_df["end_year"] = end_year
                pairwise_results.append(pw_df)

        except Exception as e:
            print(f"Pairwise failed for window {start_year}-{end_year}: {e}")

        # Block exogeneity: --->
        try:
            be_df = run_block_exogeneity(group)

            if isinstance(be_df, pd.DataFrame) and not be_df.empty:
                be_df["start_year"] = start_year
                be_df["end_year"] = end_year
                block_results.append(be_df)

        except Exception as e:
            print(f"Block exogeneity failed for window {start_year}-{end_year}: {e}")

    # Concatenate results: --->
    if len(pairwise_results) > 0:
        pairwise_final = pd.concat(pairwise_results, ignore_index=True)
    else:
        pairwise_final = pd.DataFrame()

    if len(block_results) > 0:
        block_final = pd.concat(block_results, ignore_index=True)
    else:
        block_final = pd.DataFrame()

    # Export results: --->
    if not pairwise_final.empty:
        export_pairwise_yearly(pairwise_final, PAIRWISE_PATH)
    else:
        print(f"No pairwise results to export.")

    if not block_final.empty:
        export_block_exogeneity_yearly(block_final, BLOCK_PATH)
    else:
        print(f"No block exogeneity results to export.")

    return {
        "pairwise": pairwise_final,
        "block_exogeneity": block_final
    }

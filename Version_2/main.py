"""
Main Execution File:
Trivariate System: Oil-Gold-USD<->INR

Pipeline Stages:
1. Data Preparation
2. Stationarity
3. Cointegration
4. VECM / VAR
5. Causality
6. Volatility
7. Reporting
"""

import time
import sys
from pathlib import Path

# Import custom modules: --->
from Preparation import run_all as run_preparation
from Stationarity import run_stationarity
from Cointegration import run_cointegration
from vecm_var import run_vecm_var
from Causality import run_causality
from Volatility import run_volatility
from Reporting import run_reporting

# Configuration: --->
FREQUENCIES = ["monthly", "yearly"]
BASE_DIR = Path(__file__).resolve().parent

# Helper Functions: --->
def print_stage(stage_name: str):
    print("\n" + "=" * 60)
    print(f"Running Stage: {stage_name}")
    print("=" * 60)

def run_pipeline_for_frequency(freq: str):
    print(f"\n\n********** {freq.upper()} DATA PIPELINE **********")

    # Stage 2 — Stationarity: --->
    print_stage("Stationarity Analysis")
    run_stationarity(freq)

    # Stage 3 — Cointegration: --->
    print_stage("Cointegration Analysis")
    run_cointegration(freq)

    # Stage 4 — VECM / VAR: --->
    print_stage("VECM / VAR Estimation")
    run_vecm_var(freq)

    # Stage 5 — Causality: --->
    print_stage("Granger Causality")
    run_causality(freq)

    # Stage 6 — Volatility Spillovers: --->
    print_stage("Volatility Spillovers (GARCH-DCC)")
    run_volatility(freq)

    # Stage 7 — Reporting: --->
    print_stage("Reporting & Compilation")
    run_reporting(freq)

# Main Execution: --->
if __name__ == "__main__":
    start_time = time.time()

    print("\n" + "#" * 60)
    print("STARTING FULL ECONOMETRIC PIPELINE")
    print("#" * 60)

    # try:
    # Stage 1 — Data Preparation: --->-
    print_stage("Data Preparation")
    run_preparation()

    # Remaining Stages Per Frequency: --->
    for freq in FREQUENCIES:
        run_pipeline_for_frequency(freq)

    print("\n" + "#" * 60)
    print("PIPELINE EXECUTED SUCCESSFULLY")
    print("#" * 60)

    # except Exception as e:
    #     print("\n" + "!" * 60)
    #     print("PIPELINE FAILED")
    #     print("Error:", e)
    #     print("!" * 60)

    #     sys.exit(1)

    end_time = time.time()
    total_time = round((end_time - start_time) / 60, 2)

    print(f"\nTotal Execution Time: {total_time} minutes\n")

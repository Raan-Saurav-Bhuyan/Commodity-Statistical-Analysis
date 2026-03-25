"""
Main Pipeline Runner

Executes the full Oil–Gold–USD-INR–Inflation econometric pipeline.

Order:
1. Preparation
2. Stationarity
3. Cointegration
4. VAR/VECM
5. Volatility (DCC-GARCH)
6. Reporting
"""
# Import libraries: --->
import os
import sys
import traceback
import pickle as pkl
from datetime import datetime

# Import module runners: --->
from Preparation import run_preparation_pipeline
from Stationarity import run_stationarity
from Cointegration import run_cointegration
from vecm_var import run_vecm_var as run_var
from Volatility import run_volatility
from Reporting import run_reporting

# Results directory configuration: --->
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_DIR = os.path.join(BASE_DIR, "Results", "Serialized")

def save_results(results, use_timestamp = True):
    """
    Save results dictionary to pickle file
    """

    os.makedirs(SAVE_DIR, exist_ok = True)

    if use_timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"pipeline_results_{timestamp}.pkl"
    else:
        filename = "pipeline_results.pkl"

    filepath = os.path.join(SAVE_DIR, filename)

    with open(filepath, "wb") as f:
        pkl.dump(results, f)

    print(f"💾 Results saved to: {filepath}")

if __name__ == "__main__":
    """
    Execute full econometric pipeline
    """

    print("\n" + "="*60)
    print("STARTING FULL ECONOMETRIC PIPELINE")
    print("="*60 + "\n")

    results = {}

    try:
        # Stage 1: Preparation: --->
        print("[1/6] Running Preparation Module...")
        results["preparation"] = run_preparation_pipeline()
        print("Preparation Completed\n")

        # Stage 2: Stationarity: --->
        print("[2/6] Running Stationarity Tests...")
        results["stationarity"] = run_stationarity()
        print("Stationarity Completed\n")

        # Stage 3: Cointegration: --->
        print("[3/6] Running Cointegration Analysis...")
        results["cointegration"] = run_cointegration()
        print("Cointegration Completed\n")

        # Stage 4: VECM / VAR: --->
        print("[4/6] Running VAR/VECM Models...")
        results["var"] = run_var()
        print("VAR/VECM Completed\n")

        # Stage 5: Volatility: --->
        print("[5/6] Running Volatility (DCC-GARCH)...")
        results["volatility"] = run_volatility()
        print("Volatility Completed\n")

        # Stage 6: Reporting: --->
        print("[6/6] Generating Reports...")
        results["reporting"] = run_reporting()
        print("Reporting Completed\n")

        print("="*60)
        print("PIPELINE COMPLETED SUCCESSFULLY")
        print("="*60 + "\n")

        print("Saving pipeline results...")
        save_results(results, use_timestamp = False)

    except Exception as e:
        print("\n" + "="*60)
        print("PIPELINE FAILED")
        print("="*60)

        print(f"\nError: {str(e)}\n")
        traceback.print_exc()

        sys.exit(1)

# Import libraries: --->
import os

# Import module runners: --->
from Preparation import run_preparation_pipeline
from Stationarity import run_stationarity

# Import custom modules: --->
from .johansen import run_johansen_test
from .rank_selection import select_rank
from .exporter import export_cointegration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "Results", "Tables", "cointegration_results.csv")

def filter_I1_variables(df, stationarity_results):
    """
    Keep only I(1) variables
    """

    i1_vars = stationarity_results[
        stationarity_results["integration_order"] == 1
    ]["variable"].tolist()

    return df[i1_vars]

def run_system(df, name):
    """
    Run Johansen test on given system
    """

    result = run_johansen_test(df)

    rank = select_rank(result["trace_stat"], result["trace_crit"])

    return {
        "system": name,
        "variables": list(df.columns),
        "rank": rank,
        "trace_stat": result["trace_stat"].tolist()
    }

def run_cointegration():
    """
    Main pipeline
    """

    views = run_preparation_pipeline()
    stationarity = run_stationarity()

    df = views["combined"]

    results = []

    # Nominal system: --->
    nominal_cols = ["log_oil_usd", "log_gold_usd", "log_usd_inr"]
    nominal_df = df[nominal_cols].dropna()

    nominal_df = filter_I1_variables(nominal_df, stationarity)

    if nominal_df.shape[1] >= 2:
        results.append(run_system(nominal_df, "nominal"))

    # Real system: --->
    real_cols = ["log_oil_usd_real", "log_gold_usd_real", "log_usd_inr_real"]
    real_df = df[real_cols].dropna()

    real_df = filter_I1_variables(real_df, stationarity)

    if real_df.shape[1] >= 2:
        results.append(run_system(real_df, "real"))

    # Inflation system: --->
    infl_cols = ["log_oil_usd", "log_gold_usd", "log_usd_inr", "inflation_india"]
    infl_df = df[infl_cols].dropna()

    infl_df = filter_I1_variables(infl_df, stationarity)

    if infl_df.shape[1] >= 2:
        results.append(run_system(infl_df, "inflation_augmented"))

    # Export: --->
    export_cointegration(results, OUTPUT_PATH)

    print("✅ Cointegration analysis completed.")

    return results

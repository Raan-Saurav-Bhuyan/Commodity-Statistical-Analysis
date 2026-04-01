# Import libraries: --->
import pandas as pd
import numpy as np

# Import custom modules: --->
from .adf_pp import run_stationarity_tests

SIGNIFICANCE = 0.05

def is_stationary(p_values):
    """
    Decide stationarity based on BOTH ADF and PP.
    """
    return all(p < SIGNIFICANCE for p in p_values)

def determine_integration_order(series, name):
    """
    Determines if a series is I(0), I(1), or I(2)
    """

    df = pd.DataFrame({"x": series}).dropna()

    # Level: --->
    level_tests = run_stationarity_tests(df)
    level_p = level_tests["p_value"].values

    if is_stationary(level_p):
        return name, 0

    # First Difference: --->
    diff1 = df["x"].diff().dropna()
    diff1_tests = run_stationarity_tests(pd.DataFrame({"x": diff1}))
    diff1_p = diff1_tests["p_value"].values

    if is_stationary(diff1_p):
        return name, 1

    # Second Difference: --->
    diff2 = diff1.diff().dropna()
    diff2_tests = run_stationarity_tests(pd.DataFrame({"x": diff2}))
    diff2_p = diff2_tests["p_value"].values

    if is_stationary(diff2_p):
        return name, 2

    return name, np.nan

def classify_variables(df):
    """
    Classify all variables by integration order.
    """

    results = []

    for col in df.columns:
        if col == "Date":
            continue

        name, order = determine_integration_order(df[col], col)

        results.append({
            "variable": name,
            "integration_order": order
        })

    return pd.DataFrame(results)

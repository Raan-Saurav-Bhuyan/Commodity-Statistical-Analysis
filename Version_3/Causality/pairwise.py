import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tsa.api import VAR


def select_optimal_lag(data: pd.DataFrame, max_lag: int = 5):
    """
    Select optimal lag using AIC from VAR model.
    Returns an integer lag or None if selection fails.
    """

    try:
        model = VAR(data)

        # Adjust max lag to avoid overfitting in small samples: --->
        safe_max_lag = min(max_lag, max(1, len(data) // 3))

        lag_order = model.select_order(maxlags=safe_max_lag)
        optimal_lag = lag_order.aic

        if optimal_lag is None or np.isnan(optimal_lag):
            return None

        return int(optimal_lag)

    except Exception:
        return None


def run_pairwise_granger(data: pd.DataFrame, max_lag: int = 5):
    """
    Run pairwise Granger causality tests with:
    - Automatic lag selection (AIC)
    - Robust error handling
    - Clean structured output

    Returns:
        DataFrame with columns:
        ['caused', 'causing', 'lag', 'p_value']
    """

    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")

    results = []
    variables = data.columns.tolist()

    for caused in variables:
        for causing in variables:

            if caused == causing:
                continue

            try:
                subset = data[[caused, causing]].dropna()

                # Skip if insufficient data: --->
                if len(subset) < (max_lag + 5):
                    continue

                # Select optimal lag: --->
                # optimal_lag = select_optimal_lag(subset, max_lag)
                # print(f"\n\nOptimal Lag: {optimal_lag}\n\n")

                # if optimal_lag is None or optimal_lag < 1:
                    # continue

                # Run Granger causality test: --->
                test_result = grangercausalitytests(
                    subset,
                    maxlag = max_lag
                )

                # Extract p-value (ssr F-test): --->
                p_value = test_result[max_lag][0]["ssr_ftest"][1]

                results.append({
                    "caused": caused,
                    "causing": causing,
                    "lag": int(max_lag),
                    "p_value": float(p_value)
                })

            except Exception:
                # Silently skip problematic pairs: --->
                continue

    # Return clean DataFrame: --->
    if len(results) == 0:
        return pd.DataFrame(columns = ["caused", "causing", "lag", "p_value"])

    return pd.DataFrame(results)

import pandas as pd
from statsmodels.tsa.vector_ar.var_model import VAR
import numpy as np

def select_lag_length(data: pd.DataFrame, maxlags: int = None) -> int:
    """
    Robust lag selection.

    Automatically restricts maxlags based on sample size
    to avoid singular covariance matrix issues.
    """

    T = len(data)
    k = data.shape[1]

    # Safe maximum lag rule: --->
    # Rule of thumb:
    # T > k * p + 10
    # => p < (T - 10) / k

    max_safe = max(1, int((T - 10) / k))

    if maxlags is None:
        maxlags = min(8, max_safe)
    else:
        maxlags = min(maxlags, max_safe)

    model = VAR(data)

    try:
        results = model.select_order(maxlags=maxlags)
        selected_lag = results.aic
    except Exception:
        # Fallback to lag = 1 if covariance not PD: --->
        selected_lag = 1

    return max(1, selected_lag)

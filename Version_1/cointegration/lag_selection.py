import pandas as pd
from statsmodels.tsa.api import VAR


def select_lag(df: pd.DataFrame, max_lags: int = 3) -> int:
    """
    Lag selection using information criteria.
    """
    model = VAR(df)
    res = model.select_order(max_lags)

    return res.aic

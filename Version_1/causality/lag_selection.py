import pandas as pd
from statsmodels.tsa.api import VAR

def select_var_lag(df: pd.DataFrame, max_lags: int = 3) -> int:
    """
    Select VAR lag length using AIC.
    """
    model = VAR(df)
    res = model.select_order(max_lags)

    return res.aic

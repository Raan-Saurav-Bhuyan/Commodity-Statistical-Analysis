import pandas as pd
from statsmodels.tsa.vector_ar.var_model import VAR

def estimate_var(data: pd.DataFrame, lags: int):
    model = VAR(data)

    return model.fit(lags)

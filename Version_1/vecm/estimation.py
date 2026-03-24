import pandas as pd
from statsmodels.tsa.vector_ar.vecm import VECM

def estimate_vecm_model(
    data: pd.DataFrame,
    rank: int,
    lags: int,
    deterministic: str
):
    """
    Estimate VECM model.
    """
    model = VECM(
        data,
        k_ar_diff = lags,
        coint_rank = rank,
        deterministic = deterministic
    )

    return model.fit()

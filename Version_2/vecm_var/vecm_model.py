import pandas as pd
from statsmodels.tsa.vector_ar.vecm import VECM

def estimate_vecm(data: pd.DataFrame, rank: int, k_ar_diff: int):
    model = VECM(
        data,
        k_ar_diff = k_ar_diff,
        coint_rank = rank,
        deterministic = "co",
    )

    return model.fit()

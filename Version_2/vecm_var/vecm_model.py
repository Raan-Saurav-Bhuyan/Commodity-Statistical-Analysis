from statsmodels.tsa.vector_ar.vecm import VECM

def fit_vecm(df, rank, lags):
    """
    Fit VECM model
    """

    model = VECM(df, k_ar_diff = lags, coint_rank = rank)
    results = model.fit()

    return results

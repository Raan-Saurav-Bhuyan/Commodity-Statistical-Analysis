from statsmodels.tsa.api import VAR

def fit_var(df, lags):
    """
    Fit VAR model
    """

    model = VAR(df)
    results = model.fit(lags)

    return results

from statsmodels.tsa.api import VAR

def select_lag(df, maxlags=5):
    """
    Select optimal lag using AIC
    """

    model = VAR(df)
    result = model.select_order(maxlags)

    return result.aic

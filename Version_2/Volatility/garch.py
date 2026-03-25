from arch import arch_model

def fit_garch(series):
    """
    Fit GARCH(1,1) model
    """

    model = arch_model(series, vol="Garch", p=1, q=1, dist="normal", rescale = False)
    result = model.fit(disp="off")

    return result

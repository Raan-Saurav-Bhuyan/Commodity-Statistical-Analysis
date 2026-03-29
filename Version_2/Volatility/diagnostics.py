def volatility_persistence(garch_result):
    params = garch_result.params
    alpha = params["alpha[1]"]
    beta = params["beta[1]"]

    return alpha + beta

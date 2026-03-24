def vecm_specification():
    """
    Centralized VECM specification.
    """
    return {
        "deterministic": "co",  # constant in cointegration relation
        "max_lags": 12
    }

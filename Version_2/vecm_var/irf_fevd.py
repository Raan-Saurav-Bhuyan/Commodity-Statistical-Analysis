import pandas as pd

def compute_irf(model_result, periods: int = 12):
    """
    Computes impulse response functions for VAR or VECM.
    """

    try:
        return model_result.irf(periods)
    except Exception:
        return None

def compute_fevd(model_result, periods: int = 12):
    """
    Computes FEVD only if available (VAR).
    For VECM, returns None since not directly implemented.
    """

    if hasattr(model_result, "fevd"):
        try:
            return model_result.fevd(periods)
        except Exception:
            return None
    else:
        return None

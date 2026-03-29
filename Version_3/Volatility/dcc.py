import numpy as np

def compute_standardized_residuals(garch_results):
    """
    Extract standardized residuals from GARCH models
    """

    residuals = []

    for res in garch_results:
        std_resid = res.resid / res.conditional_volatility
        residuals.append(std_resid)

    return np.column_stack(residuals)

def compute_dcc(residuals):
    """
    Simplified DCC approximation using rolling correlations
    """

    window = 5  # yearly data → small window

    T, N = residuals.shape
    dcc_matrices = []

    for t in range(window, T):
        sub = residuals[t-window:t]
        corr = np.corrcoef(sub.T)
        dcc_matrices.append(corr)

    return dcc_matrices

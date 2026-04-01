import numpy as np


def compute_standardized_residuals(garch_results):
    """
    Extract standardized residuals from GARCH models.

    Parameters:
    -----------
    garch_results : dict
        Dictionary of {variable: fitted GARCH result}

    Returns:
    --------
    np.ndarray
        Residual matrix of shape (T, N)
    """

    residuals = []
    var_names = []

    # Ensure consistent ordering
    for var, res in garch_results.items():
        try:
            resid = np.asarray(res.resid)
            vol = np.asarray(res.conditional_volatility)

            std_resid = resid / vol

            residuals.append(std_resid)
            var_names.append(var)

        except Exception as e:
            print(f"[Residual ERROR] {var}: {e}")

    if len(residuals) == 0:
        raise RuntimeError("No valid residuals computed from GARCH models.")

    # Align lengths (important!)
    min_len = min(len(r) for r in residuals)
    residuals = [r[-min_len:] for r in residuals]

    # Stack into (T, N)
    residual_matrix = np.column_stack(residuals)

    print("Standardized residuals shape:", residual_matrix.shape)

    return residual_matrix


def compute_dcc(residuals, window=5):
    """
    Simplified DCC approximation using rolling correlations.

    Parameters:
    -----------
    residuals : np.ndarray
        Standardized residuals (T, N)

    window : int
        Rolling window size

    Returns:
    --------
    np.ndarray
        DCC correlation matrices of shape (T-window, N, N)
    """

    residuals = np.asarray(residuals)

    if residuals.ndim != 2:
        raise ValueError("Residuals must be a 2D array (T, N).")

    T, N = residuals.shape

    if T <= window:
        raise ValueError(
            f"Not enough observations ({T}) for window size ({window})."
        )

    dcc_matrices = []

    for t in range(window, T):
        sub = residuals[t - window:t]

        try:
            corr = np.corrcoef(sub.T)

            # Numerical stability fix
            corr = np.nan_to_num(corr)

            dcc_matrices.append(corr)

        except Exception as e:
            print(f"[DCC ERROR] t={t}: {e}")

    if len(dcc_matrices) == 0:
        raise RuntimeError("DCC computation failed: no matrices generated.")

    dcc_array = np.asarray(dcc_matrices)

    print("DCC output shape:", dcc_array.shape)

    return dcc_array

import numpy as np
import pandas as pd
from arch.univariate import ConstantMean, GARCH
from scipy.optimize import minimize

def fit_univariate_garch(returns: pd.Series):
    """
    Fit GARCH(1,1) and return standardized residuals.
    """
    model = ConstantMean(returns)
    model.volatility = GARCH(1, 0, 1)
    res = model.fit(disp="off")

    std_resid = res.resid / res.conditional_volatility

    return std_resid.dropna()

def dcc_loglik(params, z):
    """
    DCC(1,1) negative log-likelihood.
    """
    a, b = params
    if a < 0 or b < 0 or a + b >= 1:
        return 1e6

    T, k = z.shape
    Qbar = np.cov(z.T)
    Qt = Qbar.copy()

    ll = 0.0

    for t in range(T):
        if t > 0:
            Qt = (1 - a - b) * Qbar + a * np.outer(z[t - 1], z[t - 1]) + b * Qt

        Dinv = np.diag(1.0 / np.sqrt(np.diag(Qt)))
        Rt = Dinv @ Qt @ Dinv

        ll += np.log(np.linalg.det(Rt)) + z[t].T @ np.linalg.inv(Rt) @ z[t]

    return 0.5 * ll

def estimate_dcc(returns: pd.DataFrame) -> pd.DataFrame:
    """
    Custom DCC-GARCH(1,1) estimation and dynamic correlation extraction.
    """
    std_resids = []

    for col in returns.columns:
        std_resids.append(fit_univariate_garch(returns[col]))

    z = pd.concat(std_resids, axis=1).dropna()
    z.columns = returns.columns
    z_np = z.values

    opt = minimize(
        dcc_loglik,
        x0 = np.array([0.05, 0.90]),
        args = (z_np,),
        bounds = ((1e-6, 1 - 1e-6), (1e-6, 1 - 1e-6)),
        method = "L-BFGS-B"
    )

    a, b = opt.x

    Qbar = np.cov(z_np.T)
    Qt = Qbar.copy()

    correlations = []

    for t in range(len(z_np)):
        if t > 0:
            Qt = (1 - a - b) * Qbar + a * np.outer(z_np[t - 1], z_np[t - 1]) + b * Qt

        Dinv = np.diag(1.0 / np.sqrt(np.diag(Qt)))
        Rt = Dinv @ Qt @ Dinv

        correlations.append(Rt[0, 1])

    return pd.DataFrame(
        {
            "DCC_Oil_Gold": correlations
        },
        index = z.index
    )

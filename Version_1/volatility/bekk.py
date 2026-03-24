import numpy as np
import pandas as pd
from scipy.optimize import minimize

def vech_to_matrix(params):
    """
    Construct BEKK matrices C, A, B from parameter vector.
    """
    c11, c12, c22, a11, a12, a21, a22, b11, b12, b21, b22 = params

    C = np.array(
        [
            [c11, c12],
            [0.0, c22]
        ]
    )

    A = np.array(
        [
            [a11, a12],
            [a21, a22]
        ]
    )

    B = np.array(
        [
            [b11, b12],
            [b21, b22]
        ]
    )

    return C, A, B


def bekk_loglik(params, returns):
    """
    BEKK(1,1) negative log-likelihood.
    """
    T, k = returns.shape
    C, A, B = vech_to_matrix(params)

    Ht = np.cov(returns.T)
    ll = 0.0

    for t in range(T):
        if t > 0:
            eps = returns[t - 1][:, None]
            Ht = (
                C.T @ C
                + A.T @ (eps @ eps.T) @ A
                + B.T @ Ht @ B
            )

        try:
            invHt = np.linalg.inv(Ht)
            detHt = np.linalg.det(Ht)
        except np.linalg.LinAlgError:
            return 1e6

        ll += np.log(detHt) + returns[t].T @ invHt @ returns[t]

    return 0.5 * ll


def estimate_bekk(returns: pd.DataFrame) -> pd.DataFrame:
    """
    Estimate BEKK-GARCH(1,1) via MLE.
    """
    r = returns.values
    init_params = np.array([
        0.1, 0.0, 0.1,
        0.1, 0.0, 0.0, 0.1,
        0.8, 0.0, 0.0, 0.8
    ])

    bounds = [(-2, 2)] * len(init_params)

    res = minimize(
        bekk_loglik,
        init_params,
        args = (r,),
        method = "L-BFGS-B",
        bounds = bounds
    )

    if not res.success:
        raise RuntimeError("BEKK optimization failed")

    param_names = [
        "C11", "C12", "C22",
        "A11", "A12", "A21", "A22",
        "B11", "B12", "B21", "B22"
    ]

    return pd.DataFrame(
        {
            "Parameter": param_names,
            "Estimate": res.x
        }
    )

import numpy as np
import pandas as pd
from scipy.optimize import minimize

class DCC:
    def __init__(self, std_resids: pd.DataFrame):
        self.eps = std_resids.values
        self.T, self.N = self.eps.shape
        self.Qbar = np.cov(self.eps.T)

    def _dcc_likelihood(self, params):
        a, b = params

        Q = self.Qbar.copy()
        loglik = 0

        for t in range(self.T):
            eps_t = self.eps[t][:, None]

            Q = (
                (1 - a - b) * self.Qbar
                + a * (eps_t @ eps_t.T)
                + b * Q
            )

            D_inv = np.diag(1 / np.sqrt(np.diag(Q)))
            R = D_inv @ Q @ D_inv

            loglik += (
                np.log(np.linalg.det(R))
                + self.eps[t] @ np.linalg.inv(R) @ self.eps[t]
            )

        return 0.5 * loglik

    def fit(self):
        bounds = [(1e-6, 0.999), (1e-6, 0.999)]

        constraint = {
            "type": "ineq",
            "fun": lambda x: 1 - x[0] - x[1],
        }

        result = minimize(
            self._dcc_likelihood,
            x0 = [0.05, 0.9],
            bounds = bounds,
            constraints = constraint,
        )

        self.a, self.b = result.x

        return result

    def compute_correlations(self):
        Q = self.Qbar.copy()
        correlations = []

        for t in range(self.T):
            eps_t = self.eps[t][:, None]

            Q = (
                (1 - self.a - self.b) * self.Qbar
                + self.a * (eps_t @ eps_t.T)
                + self.b * Q
            )

            D_inv = np.diag(1 / np.sqrt(np.diag(Q)))
            R = D_inv @ Q @ D_inv

            correlations.append(R)

        return correlations

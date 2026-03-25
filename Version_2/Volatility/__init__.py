"""
Volatility Module

Performs:
- Univariate GARCH modeling
- Dynamic Conditional Correlation (DCC)
- Volatility diagnostics
- Inflation-integrated volatility analysis
"""

from .garch import fit_garch
from .dcc import compute_dcc
from .runner import run_volatility

__all__ = [
    "fit_garch",
    "compute_dcc",
    "run_volatility",
]

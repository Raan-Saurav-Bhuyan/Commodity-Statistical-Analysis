"""
VAR/VECM Module

Performs:
- Lag selection
- VAR or VECM model estimation
- Impulse Response Functions (IRF)
- Forecast Error Variance Decomposition (FEVD)
- Model diagnostics
"""

from .lag_selection import select_lag
from .var_model import fit_var
from .vecm_model import fit_vecm
from .runner import run_vecm_var

__all__ = [
    "select_lag",
    "fit_var",
    "fit_vecm",
    "run_vecm_var",
]

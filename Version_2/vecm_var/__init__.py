"""
Stage 4 — VECM / VAR Estimation

If cointegration rank ≥ 1 → estimate VECM.
If rank = 0 → estimate VAR in first differences.
"""

from vecm_var.runner import run_vecm_var

__all__ = ["run_vecm_var"]

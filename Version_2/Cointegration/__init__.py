"""
Stage 3 — Cointegration Analysis

Performs:
- Pairwise Engle–Granger cointegration tests
- System-wide Johansen cointegration test
- Automatic cointegration rank selection
"""

from Cointegration.runner import run_cointegration

__all__ = ["run_cointegration"]

"""
Cointegration Module

Performs:
- Johansen cointegration tests
- Engle-Granger pairwise tests
- Cointegration rank selection
- System-wise analysis (nominal, real, inflation-augmented)
"""

from .johansen import run_johansen_test
from .engle_granger import run_engle_granger
from .rank_selection import select_rank
from .runner import run_cointegration

__all__ = [
    "run_johansen_test",
    "run_engle_granger",
    "select_rank",
    "run_cointegration",
]

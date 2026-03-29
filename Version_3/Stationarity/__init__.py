"""
Stationarity Module

Performs:
- ADF and Phillips-Perron tests
- Integration order detection (I(0), I(1), I(2))
- Variable classification for econometric modeling
"""

from .adf_pp import run_stationarity_tests
from .integration import classify_variables
from .runner import run_stationarity

__all__ = [
    "run_stationarity_tests",
    "classify_variables",
    "run_stationarity",
]

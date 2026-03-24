"""
Stage 1 — Data Preparation

This package loads raw oil, gold, and USD–INR price data,
constructs INR-denominated prices, computes log prices and
log returns, and exports analysis-ready datasets for
subsequent econometric stages.
"""

from Preparation.runner import run_preparation, run_all

__all__ = [
    "run_preparation",
    "run_all",
]

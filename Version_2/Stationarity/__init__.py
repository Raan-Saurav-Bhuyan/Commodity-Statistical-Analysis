"""
Stage 2 — Stationarity Analysis

Performs Augmented Dickey-Fuller (ADF) and
Phillips-Perron (PP) unit root tests on
log prices and log returns.
"""

from Stationarity.runner import run_stationarity

__all__ = ["run_stationarity"]

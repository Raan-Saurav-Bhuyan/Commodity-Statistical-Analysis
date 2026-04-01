import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def collect_all_results():
    """
    Collect outputs from all modules
    """

    results = {}

    # Stationarity: --->
    stationarity_path = os.path.join(BASE_DIR, "Results", "Tables", "stationarity_results.csv")
    if os.path.exists(stationarity_path):
        results["stationarity"] = pd.read_csv(stationarity_path)

    # Cointegration: --->
    coint_path = os.path.join(BASE_DIR, "Results", "Tables", "cointegration_results.csv")
    if os.path.exists(coint_path):
        results["cointegration"] = pd.read_csv(coint_path)

    # DCC: --->
    dcc_path = os.path.join(BASE_DIR, "Results", "Tables", "dcc_results.npy")
    if os.path.exists(dcc_path):
        raw_dcc = np.load(dcc_path, allow_pickle = True)
        # If saved as a dictionary, np.save wraps it in a 0-D array
        if raw_dcc.ndim == 0:
            dcc_dict = raw_dcc.item()
            results["dcc"] = dcc_dict.get("full_sample", [])
        else:
            results["dcc"] = raw_dcc

    # Yearly DCC Pairs: --->
    dcc_yearly_path = os.path.join(BASE_DIR, "Results", "Tables", "dcc_yearly_full.csv")
    if os.path.exists(dcc_yearly_path):
        results["dcc_yearly"] = pd.read_csv(dcc_yearly_path)

    # Yearly Volatility: --->
    vol_yearly_path = os.path.join(BASE_DIR, "Results", "Tables", "volatility_yearly_full.csv")
    if os.path.exists(vol_yearly_path):
        results["volatility_yearly"] = pd.read_csv(vol_yearly_path)

    # Pairwise Granger Causality (Yearly): --->
    granger_path = os.path.join(BASE_DIR, "Results", "Tables", "pairwise_granger_yearly.csv")
    if os.path.exists(granger_path):
        results["granger_yearly"] = pd.read_csv(granger_path)

    # Impulse Response Functions (IRF): --->
    irf_path = os.path.join(BASE_DIR, "Results", "Tables", "irf_results.csv")
    if os.path.exists(irf_path):
        results["irf"] = pd.read_csv(irf_path)

    return results

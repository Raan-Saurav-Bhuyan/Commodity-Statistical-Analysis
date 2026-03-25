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
        results["dcc"] = np.load(dcc_path, allow_pickle=True)

    return results

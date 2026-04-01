import os
import numpy as np
import pandas as pd

def export_dcc(dcc_matrices, path):
    """
    Save raw DCC matrices (for internal use)
    """
    os.makedirs(os.path.dirname(path), exist_ok = True)
    np.save(path, dcc_matrices)

def export_dcc_yearly(results, path):
    """
    Export pairwise yearly DCC correlations to CSV

    Expected format of results:
    [
        {
            "year": int,
            "pair": str,
            "time_index": int,
            "correlation": float
        },
        ...
    ]
    """

    if not results:
        print("No DCC results to export.")
        return

    df = pd.DataFrame(results)

    os.makedirs(os.path.dirname(path), exist_ok = True)
    df.to_csv(path, index = False)

    print(f"DCC yearly CSV saved to {path}")

def export_volatility_yearly(results, path):
    """
    Export yearly conditional volatility (GARCH) to CSV

    Expected format:
    [
        {
            "year": int,
            "variable": str,
            "time_index": int,
            "volatility": float
        },
        ...
    ]
    """

    if not results:
        print("No volatility results to export.")
        return

    df = pd.DataFrame(results)

    os.makedirs(os.path.dirname(path), exist_ok = True)
    df.to_csv(path, index = False)

    print(f"Volatility yearly CSV saved to {path}")

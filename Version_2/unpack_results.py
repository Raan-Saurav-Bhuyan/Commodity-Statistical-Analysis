import os
import pickle
import pandas as pd
import numpy as np

# Directory configurations: --->
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PICKLE_PATH = os.path.join(
    BASE_DIR,
    "Results",
    "Serialized",
    "pipeline_results.pkl"              # <--- change if timestamped
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "Results",
    "Tables",
    "With_Inflation"
)

# Helper functions: --->
def save_dataframe(df, name):
    path = os.path.join(OUTPUT_DIR, f"{name}.csv")
    df.to_csv(path, index = False)
    print(f"Saved: {name}.csv")

def save_dict(d, name):
    df = pd.DataFrame([d])
    save_dataframe(df, name)

def save_list_of_dicts(lst, name):
    df = pd.DataFrame(lst)
    save_dataframe(df, name)

def save_numpy_array(arr, name):
    df = pd.DataFrame(arr)
    save_dataframe(df, name)

def save_dcc(dcc_data):
    """
    Save DCC matrices as long-format CSV
    """

    records = []

    for t, mat in enumerate(dcc_data):
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                records.append({
                    "time": t,
                    "i": i,
                    "j": j,
                    "correlation": mat[i, j]
                })

    df = pd.DataFrame(records)
    save_dataframe(df, "dcc_correlations")

# Main function to unpack results appropriately: --->
def unpack_results(results):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Stationarity: --->
    if "stationarity" in results:
        stationarity = results["stationarity"]

        if isinstance(stationarity, pd.DataFrame):
            save_dataframe(stationarity, "stationarity")

        elif isinstance(stationarity, dict):
            save_dict(stationarity, "stationarity")

    # Cointegration: --->
    if "cointegration" in results:
        cointegration = results["cointegration"]

        if isinstance(cointegration, pd.DataFrame):
            save_dataframe(cointegration, "cointegration")

        elif isinstance(cointegration, dict):
            save_dict(cointegration, "cointegration")

    # VAR / VECM: --->
    if "var" in results:
        var_res = results["var"]

        if isinstance(var_res, dict):
            # Save only interpretable parts
            for key, value in var_res.items():

                if isinstance(value, pd.DataFrame):
                    save_dataframe(value, f"var_{key}")

                elif isinstance(value, dict):
                    save_dict(value, f"var_{key}")

                elif isinstance(value, list):
                    save_list_of_dicts(value, f"var_{key}")

                else:
                    print(f"Skipped VAR key: {key} (unsupported type)")

    # Volatility: --->
    if "volatility" in results:
        vol = results["volatility"]

        if isinstance(vol, dict):

            # DCC
            if "dcc" in vol:
                save_dcc(vol["dcc"])

            # Diagnostics
            if "diagnostics" in vol:
                save_list_of_dicts(vol["diagnostics"], "garch_diagnostics")

    # Reporting: --->
    if "reporting" in results:
        rep = results["reporting"]

        if isinstance(rep, dict):

            if "tables" in rep:
                for name, table in rep["tables"].items():
                    if isinstance(table, pd.DataFrame):
                        save_dataframe(table, f"report_{name}")

    print("\nAll extractable results saved successfully.")

if __name__ == "__main__":

    print("Loading pickle results...")

    if not os.path.exists(PICKLE_PATH):
        raise FileNotFoundError(f"Pickle file not found: {PICKLE_PATH}")

    with open(PICKLE_PATH, "rb") as f:
        results = pickle.load(f)

    print("Pickle loaded successfully.\n")

    unpack_results(results)

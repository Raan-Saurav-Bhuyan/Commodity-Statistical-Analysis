# Import libraries: --->
import pandas as pd

def export_results(results, path):
    """
    Exports causality results safely.

    Accepts:
    - list of dicts
    - pandas DataFrame
    """

    if isinstance(results, list):
        df = pd.DataFrame(results)
    elif isinstance(results, pd.DataFrame):
        df = results
    else:
        raise ValueError("Unsupported results format for export.")

    df.to_csv(path, index=False)

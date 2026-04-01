# Import libraries: --->
import os
import pandas as pd

def export_results(results, path, sort_by=None):
    """
    Exports causality results safely.

    Supports:
    - list of dicts
    - pandas DataFrame

    Parameters:
    - results : data to export
    - path : output CSV path
    - sort_by : optional column(s) to sort
    """

    if results is None or len(results) == 0:
        print(f"No results to export to {path}")
        return

    # Convert to DataFrame: --->
    if isinstance(results, list):
        df = pd.DataFrame(results)
    elif isinstance(results, pd.DataFrame):
        df = results.copy()
    else:
        raise ValueError("Unsupported results format for export.")

    # Auto-detect rolling vs yearly format: --->
    if sort_by is not None:
        available_cols = df.columns.tolist()

        # Keep only valid columns
        valid_sort_cols = [col for col in sort_by if col in available_cols]

        if valid_sort_cols:
            df = df.sort_values(by=valid_sort_cols)

    # Ensure directory exists: --->
    os.makedirs(os.path.dirname(path), exist_ok = True)

    # Save: --->
    df.to_csv(path, index = False)

    print(f"Results exported to {path}")


# Pair-wise causality export: --->
def export_pairwise_yearly(results, path):
    """
    Export pairwise Granger causality

    Supports both:
    - yearly format
    - rolling window format

    Expected columns (rolling):
    start_year, end_year, caused, causing, lag, p_value, test_stat
    """

    # Dynamic sorting: --->
    if isinstance(results, list) and len(results) > 0:
        sample = results[0]

        if "start_year" in sample:
            sort_cols = ["start_year", "end_year", "caused", "causing"]
        else:
            sort_cols = ["year", "caused", "causing"]
    else:
        sort_cols = None

    export_results(
        results,
        path,
        sort_by=sort_cols
    )


# Block exogeneity export: --->
def export_block_exogeneity_yearly(results, path):
    """
    Export block exogeneity (VECM-based causality)

    Supports both:
    - yearly format
    - rolling window format

    Expected columns (rolling):
    start_year, end_year, dependent, excluded, chi2_stat, p_value, df
    """

    # Dynamic sorting: --->
    if isinstance(results, list) and len(results) > 0:
        sample = results[0]

        if "start_year" in sample:
            sort_cols = ["start_year", "end_year", "dependent"]
        else:
            sort_cols = ["year", "dependent"]
    else:
        sort_cols = None

    export_results(
        results,
        path,
        sort_by=sort_cols
    )

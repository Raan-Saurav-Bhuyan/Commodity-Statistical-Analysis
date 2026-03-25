import pandas as pd

def build_summary_tables(results):
    tables = {}

    # Stationarity summary: --->
    if "stationarity" in results:
        tables["integration_counts"] = (
            results["stationarity"]
            .groupby("integration_order")
            .size()
            .reset_index(name="count")
        )

    # Cointegration summary: --->
    if "cointegration" in results:
        tables["cointegration"] = results["cointegration"]

    return tables

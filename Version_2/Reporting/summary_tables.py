import pandas as pd

def summarize_cointegration(johansen_df: pd.DataFrame):
    if johansen_df is None:
        return None

    significant = johansen_df[johansen_df["Trace Statistic"] > johansen_df["Trace 5% Critical"]]

    rank = len(significant)

    return pd.DataFrame({"Selected Cointegration Rank": [rank]})

def summarize_granger(granger_df: pd.DataFrame):
    if granger_df is None:
        return None

    significant = granger_df[granger_df["p-value"] < 0.05]

    return significant

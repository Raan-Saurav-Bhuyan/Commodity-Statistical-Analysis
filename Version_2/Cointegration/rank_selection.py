import pandas as pd

def select_rank(johansen_df: pd.DataFrame) -> int:
    """
    Rank determined using Trace test at 5% level.
    """

    significant = johansen_df[johansen_df["Trace Statistic"] > johansen_df["Trace 5% Critical"]]

    if significant.empty:
        return 0

    return int(significant["Cointegration Rank"].max() + 1)

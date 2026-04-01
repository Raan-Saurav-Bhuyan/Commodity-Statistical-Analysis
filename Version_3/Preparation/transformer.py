def merge_datasets(datasets):
    """
    Merge all datasets into one master dataframe.

    This is CRITICAL for:
    - VAR/VECM
    - DCC-GARCH
    - Causality tests
    """

    df = datasets["nominal_prices"].copy()

    # Merge real prices: --->
    df = df.merge(datasets["real_prices"], on="Date", suffixes=("", "_real"))

    # Merge returns: --->
    df = df.merge(datasets["nominal_returns"], on="Date", how="left")
    df = df.merge(datasets["real_returns"], on="Date", how="left", suffixes=("", "_real"))

    # Merge inflation: --->
    df = df.merge(datasets["inflation"], on="Date", how="left")

    return df


def split_views(df):
    """
    Create structured views for different model needs.
    """

    views = {
        "prices_nominal": df.filter(regex="^log_.*(?<!real)$|Date"),
        "prices_real": df.filter(regex="real|Date"),
        "returns_nominal": df.filter(regex="_ret$|Date"),
        "returns_real": df.filter(regex="_real_ret$|Date"),
        "inflation": df[["Date", "inflation_india", "inflation_usa"]],
        "combined": df
    }

    return views

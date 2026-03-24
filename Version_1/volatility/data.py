import pandas as pd

def load_returns(filepath: str) -> pd.DataFrame:
    """
    Load stationary log returns for volatility modeling.
    """
    df = pd.read_csv(filepath, index_col = 0, parse_dates = True)

    returns = df[["oil_log_return", "gold_log_return"]].dropna()
    returns.columns = ["Oil", "Gold"]

    return returns

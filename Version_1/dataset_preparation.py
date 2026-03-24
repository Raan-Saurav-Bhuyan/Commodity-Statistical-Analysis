import pandas as pd
import numpy as np
from pathlib import Path

def load_price_data(filepath: str) -> pd.DataFrame:
    """
    Load price data, parse dates, and enforce a clean time index.
    """
    df = pd.read_csv(filepath)
    df.columns = ["date", "price"]

    # df["date"] = pd.to_datetime(df["date"]).
    df = df.set_index("date").sort_index()

    if (df["price"] <= 0).any():
        raise ValueError("Prices must be strictly positive for log transformation.")

    return df

def transform_prices(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
    """
    Generate log prices and log returns.
    """
    out = pd.DataFrame(index = df.index)

    out[f"{prefix}_price"] = df["price"]
    out[f"{prefix}_log_price"] = np.log(df["price"])
    out[f"{prefix}_log_return"] = out[f"{prefix}_log_price"].diff()

    return out

def prepare_dataset(
    oil_path: str,
    gold_path: str,
    output_path: str
) -> None:
    """
    Full preparation pipeline:
    - load
    - align
    - transform
    - export
    """
    oil = load_price_data(oil_path)
    gold = load_price_data(gold_path)

    oil_t = transform_prices(oil, "oil")
    gold_t = transform_prices(gold, "gold")

    data = pd.concat([oil_t, gold_t], axis = 1, join = "inner")
    data = data.dropna()

    Path(output_path).parent.mkdir(parents = True, exist_ok = True)
    data.to_csv(output_path)

if __name__ == "__main__":
    prepare_dataset(
        oil_path = "Datasets/processed_oil_yearly.csv",
        gold_path = "Datasets/processed_gold_yearly.csv",
        output_path = "Datasets/prepared_oil_gold_yearly.csv"
    )

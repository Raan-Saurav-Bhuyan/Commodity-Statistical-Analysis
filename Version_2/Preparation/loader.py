import pandas as pd
from pathlib import Path

# Import custom modules: --->
# from Preparation.validators import (
#     validate_time_index,
#     validate_prices,
#     validate_fx,
# )

def load_price_series(filepath: Path, frequency: str, date_col: str = "Date", price_col: str = "Price") -> pd.Series:
    df = pd.read_csv(filepath)
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col).set_index(date_col)

    # Validate Date column: --->
    # validate_time_index(df.index, frequency)

    series = df[price_col].astype(float)

    # Validate Price column: --->
    # validate_prices(series, filepath.stem)

    return series

def load_frequency(raw_dir: Path, frequency: str) -> pd.DataFrame:
    oil = load_price_series(raw_dir / f"processed_oil_usd_{frequency}.csv", frequency = frequency)
    gold = load_price_series(raw_dir / f"processed_gold_usd_{frequency}.csv", frequency = frequency)
    fx = load_price_series(raw_dir / f"processed_usd_inr_{frequency}.csv", frequency = frequency)

    # validate_fx(fx)

    df = pd.concat(
        [oil, gold, fx],
        axis = 1,
        keys = ["oil_usd", "gold_usd", "usd_inr"],
    ).dropna()

    return df

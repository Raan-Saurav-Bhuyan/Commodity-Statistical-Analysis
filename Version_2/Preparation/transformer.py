import numpy as np
import pandas as pd

def build_inr_prices(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["oil_inr"] = df["oil_usd"] * df["usd_inr"]
    df["gold_inr"] = df["gold_usd"] * df["usd_inr"]

    return df

def build_log_prices(df: pd.DataFrame) -> pd.DataFrame:
    log_df = np.log(df)
    log_df.columns = [f"log_{c}" for c in df.columns]

    return log_df

def build_log_returns(df: pd.DataFrame) -> pd.DataFrame:
    returns = np.log(df).diff().dropna()
    returns.columns = [f"{c}_ret" for c in df.columns]

    return returns

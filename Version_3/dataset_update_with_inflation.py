import pandas as pd
import numpy as np
import os

# ============================
# PATH CONFIGURATION
# ============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_DIR = os.path.join(BASE_DIR, "Datasets", "Raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "Datasets", "Processed")

os.makedirs(PROCESSED_DIR, exist_ok = True)

# ============================
# LOAD DATA
# ============================

def load_data():
    oil = pd.read_csv(os.path.join(RAW_DIR, "processed_oil_usd_yearly.csv"))
    gold = pd.read_csv(os.path.join(RAW_DIR, "processed_gold_usd_yearly.csv"))
    usd_inr = pd.read_csv(os.path.join(RAW_DIR, "processed_usd_inr_yearly.csv"))
    cpi_india = pd.read_csv(os.path.join(RAW_DIR, "processed_india_inflation.csv"))
    cpi_usa = pd.read_csv(os.path.join(RAW_DIR, "processed_usa_inflation.csv"))

    return oil, gold, usd_inr, cpi_india, cpi_usa

# ============================
# PREPROCESSING
# ============================

def preprocess(df, col_name):
    df = df.copy()
    df.columns = ["Date", col_name]
    # df["Date"] = pd.to_datetime(df["Date"])
    return df

# ============================
# MERGE DATASETS
# ============================

def merge_data(oil, gold, usd_inr, cpi_india, cpi_usa):
    df = oil.merge(gold, on="Date") \
            .merge(usd_inr, on="Date") \
            .merge(cpi_india, on="Date") \
            .merge(cpi_usa, on="Date")

    return df.sort_values("Date").reset_index(drop=True)

# ============================
# TRANSFORMATIONS
# ============================

def compute_variables(df):
    df = df.copy()

    # Rename columns
    df.columns = [
        "Date",
        "oil_usd",
        "gold_usd",
        "usd_inr",
        "cpi_india",
        "cpi_usa"
    ]

    # ============================
    # LOG VARIABLES
    # ============================

    for col in ["oil_usd", "gold_usd", "usd_inr", "cpi_india", "cpi_usa"]:
        df[f"log_{col}"] = np.log(df[col])

    # ============================
    # INR PRICES
    # ============================

    df["oil_inr"] = df["oil_usd"] * df["usd_inr"]
    df["gold_inr"] = df["gold_usd"] * df["usd_inr"]

    df["log_oil_inr"] = np.log(df["oil_inr"])
    df["log_gold_inr"] = np.log(df["gold_inr"])

    # ============================
    # REAL VARIABLES
    # ============================

    # Deflate using India CPI: --->
    df["oil_usd_real"] = df["oil_usd"] / df["cpi_india"]
    df["gold_usd_real"] = df["gold_usd"] / df["cpi_india"]

    # Real Exchange Rate: --->
    df["usd_inr_real"] = df["usd_inr"] * (df["cpi_usa"] / df["cpi_india"])

    # INR real prices: --->
    df["oil_inr_real"] = df["oil_usd_real"] * df["usd_inr_real"]
    df["gold_inr_real"] = df["gold_usd_real"] * df["usd_inr_real"]

    # Log real variables: --->
    for col in ["oil_usd_real", "gold_usd_real", "usd_inr_real", "oil_inr_real", "gold_inr_real"]:
        df[f"log_{col}"] = np.log(df[col])

    # ============================
    # INFLATION
    # ============================

    df["inflation_india"] = df["log_cpi_india"].diff()
    df["inflation_usa"] = df["log_cpi_usa"].diff()

    return df

# ============================
# RETURNS
# ============================

def compute_returns(df, cols):
    returns = df[["Date"]].copy()

    for col in cols:
        returns[f"{col}_ret"] = df[col].diff()

    return returns.dropna()

# ============================
# SAVE DATASETS
# ============================

def save_datasets(df):

    # --- Nominal Prices ---
    nominal_cols = [
        "Date",
        "log_oil_usd",
        "log_gold_usd",
        "log_usd_inr",
        "log_oil_inr",
        "log_gold_inr"
    ]

    df[nominal_cols].to_csv(os.path.join(PROCESSED_DIR, "yearly_prices.csv"), index=False)

    # Real Prices: --->
    real_cols = [
        "Date",
        "log_oil_usd_real",
        "log_gold_usd_real",
        "log_usd_inr_real",
        "log_oil_inr_real",
        "log_gold_inr_real",
        "log_cpi_india",
        "log_cpi_usa"
    ]

    df[real_cols].to_csv(os.path.join(PROCESSED_DIR, "yearly_real_prices.csv"), index=False)

    # Inflation: --->
    inflation_cols = [
        "Date",
        "inflation_india",
        "inflation_usa"
    ]

    df[inflation_cols].dropna().to_csv(
        os.path.join(PROCESSED_DIR, "yearly_inflation.csv"),
        index=False
    )

    # Returns: --->
    nominal_returns = compute_returns(df, [
        "log_oil_usd",
        "log_gold_usd",
        "log_usd_inr",
        "log_oil_inr",
        "log_gold_inr"
    ])

    nominal_returns.to_csv(
        os.path.join(PROCESSED_DIR, "yearly_returns.csv"),
        index=False
    )

    real_returns = compute_returns(df, [
        "log_oil_usd_real",
        "log_gold_usd_real",
        "log_usd_inr_real",
        "log_oil_inr_real",
        "log_gold_inr_real"
    ])

    real_returns.to_csv(
        os.path.join(PROCESSED_DIR, "yearly_real_returns.csv"),
        index=False
    )

# ============================
# MAIN PIPELINE
# ============================

if __name__ == "__main__":
    oil, gold, usd_inr, cpi_india, cpi_usa = load_data()

    oil = preprocess(oil, "oil_usd")
    gold = preprocess(gold, "gold_usd")
    usd_inr = preprocess(usd_inr, "usd_inr")
    cpi_india = preprocess(cpi_india, "cpi_india")
    cpi_usa = preprocess(cpi_usa, "cpi_usa")

    df = merge_data(oil, gold, usd_inr, cpi_india, cpi_usa)

    df = compute_variables(df)

    save_datasets(df)

    print("All datasets updated with inflation successfully.")

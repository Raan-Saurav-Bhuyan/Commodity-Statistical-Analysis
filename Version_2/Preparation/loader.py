import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "Datasets", "Processed")


def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df


def load_all_datasets():
    """
    Loads all datasets required for inflation-integrated pipeline.
    """

    datasets = {
        "nominal_prices": load_csv("yearly_prices.csv"),
        "real_prices": load_csv("yearly_real_prices.csv"),
        "nominal_returns": load_csv("yearly_returns.csv"),
        "real_returns": load_csv("yearly_real_returns.csv"),
        "inflation": load_csv("yearly_inflation.csv"),
    }

    return datasets

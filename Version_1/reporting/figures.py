import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_returns(filepath: str) -> None:
    """
    Plot log returns of oil and gold.
    """
    df = pd.read_csv(filepath, index_col = 0, parse_dates = True)
    returns = df[["oil_log_return", "gold_log_return"]].dropna()

    plt.figure()

    returns.plot(ax = plt.gca())
    plt.title("Log Returns: Oil and Gold")

    plt.tight_layout()
    Path("Results/Figures").mkdir(parents = True, exist_ok = True)
    plt.savefig("Results/Figures/log_returns.png")

    plt.close()

def plot_dcc(filepath: str) -> None:
    """
    Plot DCC dynamic conditional correlation.
    """
    dcc = pd.read_csv(filepath, index_col = 0, parse_dates = True)

    plt.figure()

    plt.plot(dcc.index, dcc.iloc[:, 0])
    plt.title("Dynamic Conditional Correlation (Oil–Gold)")

    plt.tight_layout()
    Path("Results/Figures").mkdir(parents = True, exist_ok = True)
    plt.savefig("Results/Figures/dcc_correlation.png")

    plt.close()

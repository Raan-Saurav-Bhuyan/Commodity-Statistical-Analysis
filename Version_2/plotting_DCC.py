import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_dcc_from_csv(csv_path: str, save_path: str, frequency: str, date_index: pd.Index = None):
    """
    Plots DCC correlations from a long-format CSV file.

    Parameters
    ----------
    csv_path : str
        Path to DCC correlation CSV
    save_path : str
        Directory where figure will be saved
    frequency : str
        'monthly' or 'yearly'
    date_index : pd.Index (optional)
        If provided, replaces numeric Time with actual dates
    """

    # Load data: --->
    df = pd.read_csv(csv_path)

    # Pivot to wide format: rows = Time, columns = Pair: --->
    df_wide = df.pivot(index = "Time", columns = "Pair", values = "Correlation")

    # Replace numeric index with real dates if provided: --->
    if date_index is not None:
        if len(date_index) == len(df_wide):
            df_wide.index = date_index
        else:
            raise ValueError("Date index length does not match DCC length.")

    # Sort index just in case: --->
    df_wide = df_wide.sort_index()

    # Plot: --->
    n_pairs = len(df_wide.columns)
    fig, axes = plt.subplots(n_pairs, 1, figsize = (10, 2*n_pairs), sharex = True)

    for i, col in enumerate(df_wide.columns):
        axes[i].plot(df_wide.index, df_wide[col])
        axes[i].set_title(col)
        axes[i].set_ylabel("Corr")

    plt.tight_layout()

    save_path = Path(save_path)
    save_path.mkdir(parents = True, exist_ok = True)
    plt.savefig(save_path / f"{frequency}_dcc_subplots.png")
    plt.close()

    print("DCC plot saved successfully.")

if __name__ == '__main__':
    returns_df = pd.read_csv("Datasets/Processed/yearly_returns.csv", index_col = 0, parse_dates = True)

    plot_dcc_from_csv(
        csv_path = "Results/Tables/yearly_dcc_correlations.csv",
        save_path = "Results/Figures",
        frequency = "yearly",
        date_index = returns_df.index
    )

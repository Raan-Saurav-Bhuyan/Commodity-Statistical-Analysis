import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

def plot_dcc(dcc_data, output_dir, var_names=None):
    dcc_dir = os.path.join(output_dir, "DCC")
    os.makedirs(dcc_dir, exist_ok = True)

    if dcc_data is None:
        return

    # Failsafe: if a packed 0-d array or dictionary makes it this far: --->
    if isinstance(dcc_data, np.ndarray) and dcc_data.ndim == 0:
        dcc_data = dcc_data.item()
    if isinstance(dcc_data, dict):
        dcc_data = dcc_data.get("full_sample", [])

    if len(dcc_data) == 0:
        return

    N = dcc_data[0].shape[0]
    if var_names is None or len(var_names) != N:
        var_names = [f"Var_{i}" for i in range(N)]

    # Plot all correlation pairs over time: --->
    for i in range(N):
        for j in range(i + 1, N):
            series = [mat[i, j] for mat in dcc_data]
            pair_name = f"{var_names[i]} vs {var_names[j]}"

            plt.figure(figsize=(10, 5))
            plt.plot(series, color='teal')
            plt.title(f"Dynamic Correlation: {pair_name}")
            plt.xlabel("Time")
            plt.ylabel("Correlation")
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout()

            safe_pair_name = f"{var_names[i]}_vs_{var_names[j]}".replace('/', '_').replace('-', '_')
            plt.savefig(os.path.join(dcc_dir, f"dcc_{safe_pair_name}.png"))
            plt.close()

def plot_yearly_dcc(dcc_df, output_dir):
    if dcc_df is None or dcc_df.empty:
        return

    dcc_dir = os.path.join(output_dir, "DCC_Pairs")
    os.makedirs(dcc_dir, exist_ok = True)

    # Group by pair and generate a line plot for each
    pairs = dcc_df['pair'].unique()
    for pair in pairs:
        pair_data = dcc_df[dcc_df['pair'] == pair]

        plt.figure(figsize = (10, 5))
        plt.plot(pair_data['time_index'], pair_data['correlation'], marker = 'o', linestyle = '-', color = 'teal')
        plt.title(f"Yearly Dynamic Conditional Correlation: {pair}")
        plt.xlabel("Time Index")
        plt.ylabel("Correlation")
        plt.grid(True, linestyle = '--', alpha = 0.7)
        plt.tight_layout()

        # Clean filename characters
        safe_pair_name = pair.replace('/', '_').replace('-', '_vs_')
        plt.savefig(os.path.join(dcc_dir, f"dcc_{safe_pair_name}.png"))
        plt.close()

def plot_yearly_volatility(vol_df, output_dir):
    if vol_df is None or vol_df.empty:
        return

    vol_dir = os.path.join(output_dir, "Volatility")
    os.makedirs(vol_dir, exist_ok = True)

    variables = vol_df['variable'].unique()

    # 1. Combined Volatility Grid Plot
    num_vars = len(variables)
    cols = 3
    rows = (num_vars + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize = (15, 4 * rows))
    axes = axes.flatten()

    for i, var in enumerate(variables):
        var_data = vol_df[vol_df['variable'] == var]
        axes[i].plot(var_data['time_index'], var_data['volatility'], color = 'crimson', marker = '.')
        axes[i].set_title(f"Volatility: {var}")
        axes[i].set_xlabel("Time Index")
        axes[i].set_ylabel("Conditional Volatility")
        axes[i].grid(True, linestyle='--', alpha=0.6)

    # Hide unused axes to keep grid clean
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()

    plt.savefig(os.path.join(vol_dir, "combined_volatility.png"))
    plt.close()

def plot_granger_causality(granger_df, output_dir):
    if granger_df is None or granger_df.empty:
        return

    # Filter for significant causalities (e.g., p < 0.05)
    significant = granger_df[granger_df['p_value'] < 0.05]

    # Count significant rolling windows per pair (causing -> caused)
    counts = significant.groupby(['causing', 'caused']).size().reset_index(name='count')

    if counts.empty:
        print("No significant Granger causalities found to plot.")
        return

    pivot_counts = counts.pivot(index = 'causing', columns = 'caused', values = 'count').fillna(0)

    plt.figure(figsize = (14, 12))
    plt.imshow(pivot_counts.values, cmap = 'Blues', aspect = 'auto')

    threshold = pivot_counts.values.max() / 2
    for i in range(len(pivot_counts.index)):
        for j in range(len(pivot_counts.columns)):
            val = pivot_counts.values[i, j]
            if val > 0:
                color = 'white' if val > threshold else 'black'
                plt.text(j, i, int(val), ha='center', va='center', color=color)

    plt.colorbar(label = 'Count of Significant Windows (p < 0.05)')
    plt.xticks(ticks = np.arange(len(pivot_counts.columns)), labels=pivot_counts.columns, rotation = 45, ha = 'right')
    plt.yticks(ticks = np.arange(len(pivot_counts.index)), labels = pivot_counts.index)
    plt.title("Granger Causality Heatmap\n(Count of Significant Rolling Windows)")
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok = True)

    plt.savefig(os.path.join(output_dir, "granger_causality_heatmap.png"))
    plt.close()

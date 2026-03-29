from pathlib import Path
import pandas as pd
import numpy as np

def export_volatility(series_dict, path: Path):
    path.parent.mkdir(parents = True, exist_ok = True)

    df = pd.DataFrame(series_dict)
    df.to_csv(path)

def export_correlations(corr_list, columns, path: Path):
    path.parent.mkdir(parents = True, exist_ok = True)

    T = len(corr_list)
    records = []

    for t in range(T):
        R = corr_list[t]

        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):
                records.append({
                    "Time": t,
                    "Pair": f"{columns[i]}-{columns[j]}",
                    "Correlation": R[i, j],
                })

    pd.DataFrame(records).to_csv(path, index = False)

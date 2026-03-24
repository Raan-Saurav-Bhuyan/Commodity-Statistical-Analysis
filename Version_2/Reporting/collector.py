from pathlib import Path
import pandas as pd

RESULTS_DIR = Path("Results")

def load_table(filename: str):
    path = RESULTS_DIR / "Tables" / filename

    if path.exists():
        return pd.read_csv(path)

    return None

def load_text(filename: str):
    path = RESULTS_DIR / "Tables" / filename

    if path.exists():
        return path.read_text()

    return None

def collect_all(frequency: str):
    data = {
        "unit_root": load_table(f"{frequency}_unit_root_tests.csv"),
        "engle_granger": load_table(f"{frequency}_engle_granger.csv"),
        "johansen": load_table(f"{frequency}_johansen.csv"),
        "pairwise_granger": load_table(f"{frequency}_pairwise_granger.csv"),
        "block_exogeneity": load_table(f"{frequency}_block_exogeneity.csv"),
        "dcc": load_table(f"{frequency}_dcc_correlations.csv"),
        "model_selected": load_text(f"{frequency}_model_selected.txt"),
    }

    return data

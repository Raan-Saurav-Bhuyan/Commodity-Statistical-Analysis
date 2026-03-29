from pathlib import Path
import pandas as pd

# Import custom modules: --->
from Volatility.garch import estimate_garch
from Volatility.dcc import DCC
from Volatility.diagnostics import volatility_persistence
from Volatility.exporter import (
    export_volatility,
    export_correlations,
)

PROCESSED_DIR = Path("Datasets/Processed")
RESULTS_DIR = Path("Results")

def run_volatility(frequency: str):
    returns_path = PROCESSED_DIR / f"{frequency}_returns.csv"

    df = pd.read_csv(returns_path, index_col = 0, parse_dates = True)

    garch_results = {}
    std_resids = {}

    # Univariate GARCH: --->
    for col in df.columns:
        res = estimate_garch(df[col])

        garch_results[col] = res["conditional_vol"]
        std_resids[col] = res["std_resid"]

        persistence = volatility_persistence(res["model"])

        with open(RESULTS_DIR / "Tables" / f"{frequency}_{col}_garch_persistence.txt", "w") as f:
            f.write(f"Volatility Persistence (α+β): {persistence}")

    export_volatility(
        garch_results,
        RESULTS_DIR / "Tables" / f"{frequency}_conditional_volatility.csv",
    )

    # DCC Estimation: --->
    std_resids_df = pd.DataFrame(std_resids)

    dcc = DCC(std_resids_df)
    dcc.fit()

    correlations = dcc.compute_correlations()

    export_correlations(
        correlations,
        df.columns,
        RESULTS_DIR / "Tables" / f"{frequency}_dcc_correlations.csv",
    )

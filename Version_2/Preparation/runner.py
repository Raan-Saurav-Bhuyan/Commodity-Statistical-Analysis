from pathlib import Path

# Import custom modules: --->
from Preparation.loader import load_frequency
from Preparation.exporter import export_csv
from Preparation.transformer import (
    build_inr_prices,
    build_log_prices,
    build_log_returns,
)

RAW_DIR = Path("Datasets/Raw")
PROCESSED_DIR = Path("Datasets/Processed")

def run_preparation(frequency: str) -> None:
    # df_prices contains the core non-collinear variables (oil_usd, gold_usd, usd_inr).
    # The original dataframe from load_frequency is used directly.
    df_prices = load_frequency(RAW_DIR, frequency)

    # build_inr_prices() was removed from the main modeling pipeline.
    # Including derived prices (e.g., oil_inr) with base prices (oil_usd, usd_inr)
    # in the VECM creates perfect multicollinearity, leading to invalid model estimates.
    log_prices = build_log_prices(df_prices)
    log_returns = build_log_returns(log_prices)

    # Export the time-series prices: --->
    export_csv(
        log_prices,
        PROCESSED_DIR / f"{frequency}_prices.csv",
    )

    # Export the time-series returns: --->
    export_csv(
        log_returns,
        PROCESSED_DIR / f"{frequency}_returns.csv",
    )

def run_all() -> None:
    run_preparation("monthly")
    run_preparation("yearly")

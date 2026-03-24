from dataset_preparation import prepare_dataset
from stationarity import run_stationarity_tests
from cointegration import run_cointegration_tests
from vecm import estimate_vecm
from causality import run_granger_tests
from volatility import run_volatility_models
from reporting import generate_tables_and_figures

DATA_RAW_OIL = "Datasets/processed_oil_yearly.csv"
DATA_RAW_GOLD = "Datasets/processed_gold_yearly.csv"
DATA_PROCESSED = "Datasets/prepared_oil_gold_yearly.csv"

if __name__ == "__main__":
    """
    Full empirical pipeline runner:
    Stages 1–7 (Data → Econometrics → Reporting)
    """

    # Stage 1 — Data Preparation: --->
    # prepare_dataset(
    #     oil_path = DATA_RAW_OIL,
    #     gold_path = DATA_RAW_GOLD,
    #     output_path = DATA_PROCESSED
    # )

    # Stage 2 — Stationarity Analysis: --->
    run_stationarity_tests(DATA_PROCESSED)

    # Stage 3 — Cointegration Analysis: --->
    run_cointegration_tests(DATA_PROCESSED)

    # Stage 4 — VECM Estimation: --->
    estimate_vecm(DATA_PROCESSED)

    # Stage 5 — Granger Causality: --->
    run_granger_tests(DATA_PROCESSED)

    # Stage 6 — Volatility Spillovers: --->
    run_volatility_models(DATA_PROCESSED)

    # Stage 7 — Tables & Figures: --->
    generate_tables_and_figures(DATA_PROCESSED)

import pandas as pd
from vecm.specification import vecm_specification
from vecm.estimation import estimate_vecm_model
from vecm.diagnostics import extract_vecm_results

def estimate_vecm(filepath: str) -> None:
    df = pd.read_csv(filepath, index_col = 0, parse_dates = True)

    prices = df[["oil_log_price", "gold_log_price"]].dropna()

    johansen = pd.read_csv("Results/Tables/johansen_results.csv")

    #! Debugged Error (1): No fallback for rank = 0 cases. Corrected code is flagged below.
    # rank = int(johansen.loc[johansen["Trace Statistic"] > johansen["Trace 5% Critical"], "Cointegration Rank"].max() + 1)

    #* Corrected code (1)(a): --->
    rejected = johansen[johansen["Trace Statistic"] > johansen["Trace 5% Critical"]]["Cointegration Rank"]

    if rejected.empty:
        rank = 0
    else:
        rank = int(rejected.max() + 1)

    if rank == 0:
        print(
            "No cointegration detected (rank = 0). "
            "VECM is not appropriate. Use VAR in returns instead."
        )

    spec = vecm_specification()
    lags = spec["max_lags"]

    vecm_res = estimate_vecm_model(
        data = prices,
        rank = rank,
        lags = lags,
        deterministic = spec["deterministic"]
    )

    results = extract_vecm_results(vecm_res)

    results["alpha"].to_csv("Results/Tables/vecm_adjustment_coefficients.csv")

    results["beta"].to_csv("Results/Tables/vecm_cointegrating_vectors.csv")

    #* Corrected code (1)(b): --->
    # vecm_res.summary().as_csv().to_csv("Results/Tables/vecm_full_summary.csv")

    if rank > 0:
        vecm_res.summary().as_csv().to_csv(
            "results/tables/vecm_full_summary.csv"
        )

    if rank == 0:
        prices.diff().dropna().to_csv(
            "Results/Tables/vecm_not_estimated_no_cointegration.csv"
        )

        return

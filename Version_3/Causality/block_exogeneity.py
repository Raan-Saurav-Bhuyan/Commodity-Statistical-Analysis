# Import libraries: --->
from statsmodels.tsa.vector_ar.var_model import VAR

def run_block_exogeneity(data):
    """
    Block exogeneity (Granger causality) tests.

    Uses VAR model estimated from input data.
    """

    # Fit VAR model with lag selection: --->
    try:
        model = VAR(data)

        # Select optimal lag using AIC: --->
        lag_selection = model.select_order(maxlags = 1)
        selected_lag = lag_selection.aic

        # Fallback if selection fails: --->
        if selected_lag is None:
            selected_lag = 1

        var_model = model.fit(selected_lag)

    except Exception as e:
        raise RuntimeError(f"VAR fitting failed: {e}")

    variables = var_model.names
    results = []

    # Block exogeneity tests: --->
    for dependent in variables:
        excluded = [v for v in variables if v != dependent]

        try:
            test = var_model.test_causality(
                dependent,
                excluded,
                kind="f"
            )

            results.append({
                "dependent": dependent,
                "excluded": ", ".join(excluded),
                "chi2_stat": test.test_statistic,
                "df": test.df,
                "p_value": test.pvalue
            })

        except Exception as e:
            print(f"Block exogeneity failed for {dependent}: {e}")

    return results

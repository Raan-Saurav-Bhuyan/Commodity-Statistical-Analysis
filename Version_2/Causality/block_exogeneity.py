from statsmodels.tsa.vector_ar.var_model import VAR

def run_block_exogeneity(model_result):
    """
    Block exogeneity (Granger causality) tests.

    If VECM → re-estimate equivalent VAR in levels.
    """

    # Determine if VAR or VECM: --->
    if model_result.__class__.__name__ == "VECMResults":
        # Extract endogenous data used in VECM: --->
        endog = model_result.model.endog

        # Determine lag order used in VECM: --->
        k_ar = model_result.k_ar

        # Refit VAR in levels: --->
        var_model = VAR(endog).fit(k_ar)
    else:
        # Already VARResults: --->
        var_model = model_result

    variables = var_model.names
    results = []

    for caused in variables:
        causing = [v for v in variables if v != caused]

        test = var_model.test_causality(
            caused,
            causing,
            kind = "f"
        )

        results.append({
            "Caused": caused,
            "Causing": ", ".join(causing),
            "F-stat": test.test_statistic,
            "p-value": test.pvalue
        })

    return results

import pandas as pd
from statsmodels.tsa.vector_ar.vecm import coint_johansen

def run_johansen_test(df, det_order = 0, k_ar_diff = 1):
    """
    Runs Johansen cointegration test.

    Parameters:
    - det_order: deterministic terms
    - k_ar_diff: lag differences
    """

    result = coint_johansen(df, det_order, k_ar_diff)

    output = {
        "eigenvalues": result.eig,
        "trace_stat": result.lr1,
        "trace_crit": result.cvt,
        "maxeig_stat": result.lr2,
        "maxeig_crit": result.cvm,
    }

    return output

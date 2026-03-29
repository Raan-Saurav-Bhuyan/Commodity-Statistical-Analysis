# Import libraries: --->
from statsmodels.tsa.stattools import coint

def run_engle_granger(y, x):
    """
    Pairwise cointegration test.
    """

    score, pvalue, _ = coint(y, x)

    return {
        "stat": score,
        "p_value": pvalue
    }

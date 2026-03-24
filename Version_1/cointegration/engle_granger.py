import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant


def engle_granger_test(y: pd.Series, x: pd.Series) -> dict:
    """
    Engle-Granger two-step cointegration test.
    """
    x_const = add_constant(x)
    model = OLS(y, x_const).fit()
    resid = model.resid

    stat, pval, _, _, crit, _ = adfuller(resid)

    return {
        "stat": stat,
        "pvalue": pval,
        "crit_1": crit["1%"],
        "crit_5": crit["5%"],
        "crit_10": crit["10%"]
    }

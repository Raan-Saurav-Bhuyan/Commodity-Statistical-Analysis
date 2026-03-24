import pandas as pd
from statsmodels.tsa.stattools import adfuller
from arch.unitroot import PhillipsPerron


def adf_test(series: pd.Series) -> dict:
    stat, pval, lags, obs, _, _ = adfuller(series, autolag = "AIC")

    return {
        "stat": stat,
        "pvalue": pval,
        "lags": lags,
        "obs": obs
    }


def pp_test(series: pd.Series) -> dict:
    test = PhillipsPerron(series)

    return {
        "stat": test.stat,
        "pvalue": test.pvalue,
        "lags": test.lags
    }

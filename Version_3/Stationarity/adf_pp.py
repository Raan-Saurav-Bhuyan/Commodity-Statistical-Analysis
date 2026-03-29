# Import libraries: --->
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from arch.unitroot import PhillipsPerron

def adf_test(series, name):
    result = adfuller(series.dropna(), autolag="AIC")

    return {
        "variable": name,
        "test": "ADF",
        "stat": result[0],
        "p_value": result[1],
        "lags": result[2],
        "n_obs": result[3],
    }


def pp_test(series, name):
    pp = PhillipsPerron(series.dropna())

    return {
        "variable": name,
        "test": "PP",
        "stat": pp.stat,
        "p_value": pp.pvalue,
        "lags": pp.lags,
    }


def run_stationarity_tests(df):
    results = []

    for col in df.columns:
        if col == "Date":
            continue

        series = df[col]

        results.append(adf_test(series, col))
        results.append(pp_test(series, col))

    return pd.DataFrame(results)

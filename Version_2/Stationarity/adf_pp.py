import pandas as pd
from statsmodels.tsa.stattools import adfuller
from arch.unitroot import PhillipsPerron

def adf_test(series: pd.Series) -> tuple:
    result = adfuller(series, autolag = "AIC")
    return result[0], result[1]

def pp_test(series: pd.Series) -> tuple:
    result = PhillipsPerron(series)
    return result.stat, result.pvalue

def run_unit_root_tests(series: pd.Series) -> dict:
    adf_stat, adf_p = adf_test(series)
    pp_stat, pp_p = pp_test(series)

    return {
        "ADF Level Stat": adf_stat,
        "ADF Level p": adf_p,
        "PP Level Stat": pp_stat,
        "PP Level p": pp_p,
    }

def run_diff_tests(series: pd.Series) -> dict:
    diff_series = series.diff().dropna()

    adf_stat, adf_p = adf_test(diff_series)
    pp_stat, pp_p = pp_test(diff_series)

    return {
        "ADF Diff Stat": adf_stat,
        "ADF Diff p": adf_p,
        "PP Diff Stat": pp_stat,
        "PP Diff p": pp_p,
    }

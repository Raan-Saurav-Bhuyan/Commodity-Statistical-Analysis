import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

def engle_granger_test(y: pd.Series, x: pd.Series) -> dict:
    """
    Step 1: OLS regression
    Step 2: ADF test on residuals
    """

    x_const = sm.add_constant(x)
    model = sm.OLS(y, x_const).fit()
    residuals = model.resid

    adf_stat, p_value, _, _, _, _ = adfuller(residuals, autolag = "AIC")

    return {
        "Dependent": y.name,
        "Independent": x.name,
        "ADF Stat": adf_stat,
        "p-value": p_value,
    }

def run_pairwise_engle_granger(df: pd.DataFrame) -> pd.DataFrame:
    results = []

    columns = df.columns

    for i in range(len(columns)):
        for j in range(len(columns)):
            if i != j:
                result = engle_granger_test(
                    df[columns[i]],
                    df[columns[j]],
                )

                results.append(result)

    return pd.DataFrame(results)

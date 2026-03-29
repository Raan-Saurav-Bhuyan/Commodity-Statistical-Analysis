import pandas as pd
from arch import arch_model

def estimate_garch(series: pd.Series):
    model = arch_model(
        series,
        vol = "GARCH",
        p = 1,
        q = 1,
        dist = "normal",
        rescale = False,
    )

    result = model.fit(disp = "off")

    return {
        "model": result,
        "conditional_vol": result.conditional_volatility,
        "std_resid": result.resid / result.conditional_volatility,
    }

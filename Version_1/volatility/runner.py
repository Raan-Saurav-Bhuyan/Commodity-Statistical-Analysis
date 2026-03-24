from volatility.data import load_returns
from volatility.dcc import estimate_dcc
from volatility.bekk import estimate_bekk


def run_volatility_models(filepath: str) -> None:
    returns = load_returns(filepath)

    dcc = estimate_dcc(returns)
    dcc.to_csv("Results/Tables/dcc_dynamic_correlation.csv")

    bekk = estimate_bekk(returns)

    bekk.to_csv("Results/Tables/bekk_parameters.csv")

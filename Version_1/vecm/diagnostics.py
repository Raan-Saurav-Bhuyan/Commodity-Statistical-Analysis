import pandas as pd

def extract_vecm_results(vecm_res) -> dict:
    """
    Extract key VECM components.
    """
    return {
        "alpha": pd.DataFrame(
            vecm_res.alpha,
            columns = [f"CI_{i+1}" for i in range(vecm_res.alpha.shape[1])],
            index = vecm_res.names
        ),
        "beta": pd.DataFrame(
            vecm_res.beta,
            columns = [f"CI_{i+1}" for i in range(vecm_res.beta.shape[1])],
            index = vecm_res.names
        ),
        "gamma": pd.DataFrame(
            vecm_res.gamma.reshape(-1, vecm_res.gamma.shape[-1]),
        )
    }

import pandas as pd
import numpy as np

def validate_time_index(index: pd.DatetimeIndex, frequency: str) -> None:
    if not index.is_monotonic_increasing:
        raise ValueError("Time index is not sorted.")

    if index.has_duplicates:
        raise ValueError("Duplicate timestamps detected.")

    expected_freq = "MS" if frequency == "monthly" else "YS"
    inferred = pd.infer_freq(index)

    if inferred != expected_freq:
        raise ValueError(
            f"Expected frequency '{expected_freq}', "
            f"but inferred '{inferred}'. Missing dates likely."
        )

def validate_prices(series: pd.Series, name: str) -> None:
    if (series <= 0).any():
        bad = series[series <= 0]
        raise ValueError(f"{name} contains non-positive values:\n{bad.head()}")

    if series.isna().mean() > 0.05:
        raise ValueError(f"{name} has more than 5% missing values.")


def validate_fx(series: pd.Series) -> None:
    validate_prices(series, "USD-INR FX")

    if series.std() == 0:
        raise ValueError("USD-INR series is constant.")

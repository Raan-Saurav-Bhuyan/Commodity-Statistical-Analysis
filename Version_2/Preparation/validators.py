def validate_no_missing(df):
    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values after merging.")


def validate_alignment(df):
    if not df["Date"].is_monotonic_increasing:
        raise ValueError("Dates are not sorted properly.")


def validate_inflation(df):
    if "inflation_india" not in df.columns:
        raise ValueError("Inflation (India) missing.")
    if "inflation_usa" not in df.columns:
        raise ValueError("Inflation (USA) missing.")


def run_all_validations(df):
    validate_alignment(df)
    validate_no_missing(df)
    validate_inflation(df)

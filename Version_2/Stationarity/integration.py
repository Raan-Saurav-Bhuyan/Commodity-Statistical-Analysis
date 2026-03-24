def determine_integration(row: dict, alpha: float = 0.05) -> str:
    level_stationary = (
        row["ADF Level p"] < alpha
        and row["PP Level p"] < alpha
    )

    diff_stationary = (
        row["ADF Diff p"] < alpha
        and row["PP Diff p"] < alpha
    )

    if level_stationary:
        return "I(0)"
    elif diff_stationary:
        return "I(1)"
    else:
        return "Higher Order / Inconclusive"

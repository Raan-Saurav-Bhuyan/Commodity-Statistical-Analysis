def integration_order(level_p: float, diff_p: float, alpha: float = 0.05) -> str:
    """
    Decide integration order using standard econometric logic.
    """
    if level_p < alpha:
        return "I(0)"
    if diff_p < alpha:
        return "I(1)"

    return "Non-stationary"

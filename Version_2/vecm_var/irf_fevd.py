def compute_irf(model, steps = 10):
    """
    Compute Impulse Response Functions
    """
    return model.irf(steps)


def compute_fevd(model, steps = 10):
    """
    Compute Forecast Error Variance Decomposition
    """
    return model.fevd(steps)

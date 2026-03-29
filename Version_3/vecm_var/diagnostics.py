def run_diagnostics(model):
    """
    Run residual diagnostics
    """

    results = {}

    try:
        results["serial_correlation"] = model.test_serial_correlation().summary()
    except:
        results["serial_correlation"] = None

    try:
        results["normality"] = model.test_normality().summary()
    except:
        results["normality"] = None

    return results

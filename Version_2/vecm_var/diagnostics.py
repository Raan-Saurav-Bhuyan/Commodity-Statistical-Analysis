import numpy as np
from statsmodels.tsa.vector_ar.var_model import VARResults

def check_stability(model_result):
    """
    Stability check for VAR and VECM models.

    - VAR: The process is stable if all roots of the characteristic polynomial
      are outside the unit circle. `statsmodels` `VARResults.roots` returns these.
      So, for VAR, we check if |roots| > 1.

    - VECM: The process is stable if all roots of the companion matrix are
      inside or on the unit circle. `statsmodels` `VECMResults.roots` returns
      these eigenvalues. So, for VECM, we check if |roots| <= 1.

    Returns:
        dict with stability info
    """
    try:
        roots = model_result.roots
        modulus = np.abs(roots)

        if isinstance(model_result, VARResults):
            stable = np.all(modulus > 1)
        else:  # Assuming VECM or similar model where roots are eigenvalues
            stable = np.all(modulus <= 1.000001)  # Use a small tolerance

        return {
            "stable": bool(stable),
            "min_root_modulus": float(modulus.min()),
            "max_root_modulus": float(modulus.max())
        }
    except Exception:
        # If roots not available: --->
        return {
            "stable": None,
            "min_root_modulus": None,
            "max_root_modulus": None
        }

def serial_correlation_test(model_result):
    return model_result.test_serial_correlation()

def normality_test(model_result):
    return model_result.test_normality()

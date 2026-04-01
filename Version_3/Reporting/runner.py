# Import libraries: --->
import os

# Import custom modules: --->
from .collector import collect_all_results
from .figures import (
    plot_dcc,
    plot_yearly_dcc,
    plot_yearly_volatility,
    plot_granger_causality
)
from .vecm_visuals import plot_vecm_parameters

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(BASE_DIR, "Results", "Figures")
REPORT_DIR = os.path.join(BASE_DIR, "Results", "Report")

def run_reporting():
    """
    Full reporting pipeline
    """

    results = collect_all_results()

    os.makedirs(FIG_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok = True)

    #! Debugging: Only to be used with the yearly DCC data saved in NumPy array: --->
    # Extract variable names for labeling if available: --->
    # var_names = None
    # if "volatility_yearly" in results and not results["volatility_yearly"].empty:
    #     var_names = results["volatility_yearly"]["variable"].unique().tolist()

    #! Debugging: Only to be used with the yearly DCC data saved in NumPy array: --->
    # if "dcc" in results:
    #     print("[Reporting] Plotting Full-Sample DCC Pairs...")
    #     plot_dcc(results["dcc"], FIG_DIR, var_names=var_names)

    # Yearly DCC Figures: --->
    if "dcc_yearly" in results:
        print("[Reporting] Plotting Yearly DCC...")
        plot_yearly_dcc(results["dcc_yearly"], FIG_DIR)

    # Yearly Volatility Figures: --->
    if "volatility_yearly" in results:
        print("[Reporting] Plotting Yearly Volatility...")
        plot_yearly_volatility(results["volatility_yearly"], FIG_DIR)

    # Granger Causality Heatmap: --->
    if "granger_yearly" in results:
        print("[Reporting] Plotting Granger Causality Heatmap...")
        plot_granger_causality(results["granger_yearly"], FIG_DIR)

    # VECM Summary Visuals: --->
    print("[Reporting] Plotting VECM Summaries...")
    plot_vecm_parameters(REPORT_DIR, FIG_DIR)

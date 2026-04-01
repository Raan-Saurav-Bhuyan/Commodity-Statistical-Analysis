# Import libraries: --->
import os

# Import module runners: --->
from Preparation import run_preparation_pipeline

# Import custom modules: --->
from .integration import classify_variables
from .exporter import export_stationarity

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "Results", "Tables", "stationarity_results.csv")

def run_stationarity(views = None):
    """
    Main stationarity pipeline
    """

    # Load data: --->
    if views is None:
        views = run_preparation_pipeline()

    df = views["combined"]

    results = classify_variables(df)

    export_stationarity(results, OUTPUT_PATH)

    print("Stationarity analysis completed.")

    return results

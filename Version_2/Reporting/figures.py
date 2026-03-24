from pathlib import Path
import shutil

RESULTS_DIR = Path("Results")
REPORT_DIR = Path("Results/Report")

def copy_figures(frequency: str):

    REPORT_DIR.mkdir(parents = True, exist_ok = True)

    for fig in ["irf.png", "fevd.png"]:
        source = RESULTS_DIR / "Figures" / f"{frequency}_{fig}"

        if source.exists():
            shutil.copy(source, REPORT_DIR / source.name)

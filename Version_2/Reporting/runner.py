# Import libraries: --->
import os

# Import custom modules: --->
from .collector import collect_all_results
from .summary_tables import build_summary_tables
from .figures import plot_dcc
from .markdown_report import generate_markdown
from .latex_report import generate_latex

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(BASE_DIR, "Results", "Figures")
REPORT_DIR = os.path.join(BASE_DIR, "Results", "Report")

def run_reporting():
    """
    Full reporting pipeline
    """

    results = collect_all_results()
    tables = build_summary_tables(results)

    # Figures: --->
    if "dcc" in results:
        plot_dcc(results["dcc"], FIG_DIR)

    # Reports: --->
    os.makedirs(REPORT_DIR, exist_ok=True)

    md_report = generate_markdown(results, tables)
    with open(os.path.join(REPORT_DIR, "report.md"), "w") as f:
        f.write(md_report)

    latex_report = generate_latex(results, tables)
    with open(os.path.join(REPORT_DIR, "report.tex"), "w") as f:
        f.write(latex_report)

    print("✅ Reporting completed.")

    return {
        "tables": tables,
        "reports": {
            "markdown": md_report,
            "latex": latex_report
        }
    }

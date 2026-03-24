from pathlib import Path

# Import custom modules: --->
from Reporting.collector import collect_all
from Reporting.figures import copy_figures
from Reporting.latex_export import export_latex
from Reporting.markdown_report import generate_markdown_report
from Reporting.summary_tables import (
    summarize_cointegration,
    summarize_granger,
)

def run_reporting(frequency: str):
    collected = collect_all(frequency)

    # Summary Tables: --->
    cointegration_summary = summarize_cointegration(collected["johansen"])

    granger_summary = summarize_granger(collected["pairwise_granger"])

    # Export LaTeX: --->
    export_latex(
        cointegration_summary,
        Path("Results/Report") / f"{frequency}_cointegration.tex"
    )

    export_latex(
        granger_summary,
        Path("Results/Report") / f"{frequency}_granger_significant.tex"
    )

    # Copy Figures: --->
    copy_figures(frequency)

    # Markdown Compilation: --->
    generate_markdown_report(frequency, collected)

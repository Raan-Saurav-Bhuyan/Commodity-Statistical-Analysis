from reporting.tables import format_table
from reporting.figures import plot_returns, plot_dcc

def generate_tables_and_figures(data_path: str) -> None:
    """
    Final reporting stage: Tables & figures.
    """
    format_table(
        "Results/Tables/stationarity_tests.csv",
        "Results/Tables/final_stationarity_tests.csv"
    )

    format_table(
        "Results/Tables/engle_granger_results.csv",
        "Results/Tables/final_engle_granger_results.csv"
    )

    format_table(
        "Results/Tables/johansen_results.csv",
        "Results/Tables/final_johansen_results.csv"
    )

    format_table(
        "Results/Tables/vecm_adjustment_coefficients.csv",
        "Results/Tables/final_vecm_adjustment_coefficients.csv"
    )

    format_table(
        "Results/Tables/granger_causality_results.csv",
        "Results/Tables/final_granger_causality_results.csv"
    )

    format_table(
        "Results/Tables/bekk_parameters.csv",
        "Results/Tables/final_bekk_parameters.csv"
    )

    plot_returns(data_path)
    plot_dcc("Results/Tables/dcc_dynamic_correlation.csv")

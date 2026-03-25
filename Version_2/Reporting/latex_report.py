def generate_latex(results, tables):
    report = r"""
\section{Oil--Gold--USD/INR Analysis with Inflation}

\subsection{Stationarity}
"""

    if "integration_counts" in tables:
        report += tables["integration_counts"].to_latex(index=False)

    report += r"""
\subsection{Cointegration}
"""

    if "cointegration" in tables:
        report += tables["cointegration"].to_latex(index=False)

    return report

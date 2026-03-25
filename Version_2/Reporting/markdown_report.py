def generate_markdown(results, tables):
    report = "# Oil–Gold–USD-INR Analysis with Inflation\n\n"

    # Stationarity: --->
    if "integration_counts" in tables:
        report += "## Stationarity Summary\n"
        report += tables["integration_counts"].to_markdown(index=False)
        report += "\n\n"

    # Cointegration: --->
    if "cointegration" in tables:
        report += "## Cointegration Results\n"
        report += tables["cointegration"].to_markdown(index=False)
        report += "\n\n"

    report += "## Key Insights\n"
    report += "- Inflation integrated into system dynamics\n"
    report += "- Real vs nominal differences observed\n"
    report += "- Dynamic correlations vary with inflation\n"

    return report

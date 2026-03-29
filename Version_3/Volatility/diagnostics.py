def summarize_volatility(garch_results):
    summary = []

    for i, res in enumerate(garch_results):
        summary.append({
            "series_index": i,
            "aic": res.aic,
            "bic": res.bic
        })

    return summary

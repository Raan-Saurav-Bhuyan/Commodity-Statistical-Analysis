def summarize_volatility(garch_results):
    summary = []

    for var, res in garch_results.items():
        try:
            summary.append({
                "variable": var,
                "aic": res.aic,
                "bic": res.bic,
                "loglikelihood": res.loglikelihood
            })
        except Exception as e:
            print(f"[Diagnostics ERROR] {var}: {e}")

    return summary

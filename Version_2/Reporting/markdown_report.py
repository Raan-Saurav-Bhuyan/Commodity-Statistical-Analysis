from pathlib import Path

def generate_markdown_report(frequency: str, collected: dict):
    report_dir = Path("Results/Report")
    report_dir.mkdir(parents = True, exist_ok = True)

    report_path = report_dir / f"{frequency}_report.md"

    with open(report_path, "w") as f:

        f.write(f"# Econometric Report — {frequency.capitalize()} Data\n\n")

        f.write("## Model Selection\n")
        f.write(f"{collected['model_selected']}\n\n")

        f.write("## Cointegration (Johansen)\n")
        if collected["johansen"] is not None:
            f.write(collected["johansen"].to_markdown(index=False))
            f.write("\n\n")

        f.write("## Pairwise Granger Causality\n")
        if collected["pairwise_granger"] is not None:
            f.write(collected["pairwise_granger"].to_markdown(index=False))
            f.write("\n\n")

        f.write("## Block Exogeneity\n")
        if collected["block_exogeneity"] is not None:
            f.write(collected["block_exogeneity"].to_markdown(index=False))
            f.write("\n\n")

        f.write("## Volatility Spillovers (DCC)\n")
        if collected["dcc"] is not None:
            f.write(collected["dcc"].head().to_markdown(index=False))
            f.write("\n\n")

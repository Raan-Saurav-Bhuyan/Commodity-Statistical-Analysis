import os
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def parse_vecm_summary(filepath):
    alphas = {}
    betas = {}

    with open(filepath, 'r') as f:
        lines = f.readlines()

    current_section = None
    current_eq = None

    for line in lines:
        line = line.strip()

        # Check for Alpha (Error Correction) section: --->
        alpha_match = re.match(r"Loading coefficients \(alpha\) for equation (.*)", line)
        if alpha_match:
            current_section = "alpha"
            current_eq = alpha_match.group(1).strip()

            continue

        # Check for Beta (Cointegrating vector) section: --->
        if "Cointegration relations for loading-coefficients" in line:
            current_section = "beta"

            continue

        # Parse Alpha/ec1: --->
        if current_section == "alpha" and line.startswith("ec1"):
            parts = line.split()

            if len(parts) >= 5:
                alphas[current_eq] = {'coef': float(parts[1]), 'pval': float(parts[4])}
            current_section = None  # Reset after reading ec1

        # Parse Beta: --->
        if current_section == "beta" and line.startswith("beta."):
            parts = line.split()

            if len(parts) >= 5:
                betas[parts[0]] = {'coef': float(parts[1]), 'pval': float(parts[4])}

    return alphas, betas

def plot_vecm_parameters(report_dir, output_dir):
    if not os.path.exists(report_dir):
        print(f"[Reporting] Report directory not found: {report_dir}")

        return

    vecm_out_dir = os.path.join(output_dir, "VECM")
    os.makedirs(vecm_out_dir, exist_ok = True)

    for filename in os.listdir(report_dir):
        if filename.endswith("VECM_summary.txt"):
            filepath = os.path.join(report_dir, filename)
            model_name = filename.replace("_VECM_summary.txt", "")

            alphas, betas = parse_vecm_summary(filepath)

            if not alphas and not betas:
                continue

            # Custom Legend Patches: --->
            sig_patch = mpatches.Patch(color = 'seagreen', label = 'Significant (p < 0.05)')
            insig_patch = mpatches.Patch(color = 'lightcoral', label = 'Insignificant (p >= 0.05)')

            # 1. Plot Alphas (Speed of Adjustment): --->
            if alphas:
                plt.figure(figsize=(10, 6))
                eqs, coefs, pvals = list(alphas.keys()), [a['coef'] for a in alphas.values()], [a['pval'] for a in alphas.values()]
                colors = ['seagreen' if p < 0.05 else 'lightcoral' for p in pvals]

                bars = plt.bar(eqs, coefs, color = colors)
                plt.axhline(0, color='black', linewidth = 1)
                plt.title(f"Speed of Adjustment (Alpha / EC1) - {model_name.replace('_', ' ').title()}")
                plt.ylabel("Coefficient")
                plt.xticks(rotation=45, ha='right')
                plt.legend(handles=[sig_patch, insig_patch])

                plt.tight_layout()

                plt.savefig(os.path.join(vecm_out_dir, f"{model_name}_alphas.png"))
                plt.close()

            # 2. Plot Betas (Cointegrating Vector): --->
            if betas:
                plt.figure(figsize=(8, 5))
                b_names, b_coefs, b_pvals = list(betas.keys()), [b['coef'] for b in betas.values()], [b['pval'] for b in betas.values()]
                b_colors = ['seagreen' if p < 0.05 else 'lightcoral' for p in b_pvals]

                bars = plt.bar(b_names, b_coefs, color=b_colors)
                plt.axhline(0, color='black', linewidth=1)
                plt.title(f"Cointegrating Vector (Beta) - {model_name.replace('_', ' ').title()}")
                plt.ylabel("Coefficient")
                plt.legend(handles=[sig_patch, insig_patch])

                plt.tight_layout()

                plt.savefig(os.path.join(vecm_out_dir, f"{model_name}_betas.png"))
                plt.close()

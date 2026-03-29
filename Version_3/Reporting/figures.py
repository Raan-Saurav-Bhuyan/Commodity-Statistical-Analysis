import matplotlib.pyplot as plt
import os

def plot_dcc(dcc_data, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    if dcc_data is None or len(dcc_data) == 0:
        return

    # Plot first correlation pair over time: --->
    series = [mat[0, 1] for mat in dcc_data]

    plt.figure()
    plt.plot(series)
    plt.title("Dynamic Correlation (Oil vs Gold with Inflation Context)")

    plt.xlabel("Time")
    plt.ylabel("Correlation")

    plt.savefig(os.path.join(output_dir, "dcc_oil_gold.png"))
    plt.close()

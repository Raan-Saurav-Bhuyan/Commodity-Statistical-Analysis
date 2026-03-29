import os

def export_stationarity(results_df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    results_df.to_csv(output_path, index=False)

import os
import pandas as pd

def export_cointegration(results, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)

import pandas as pd
from pathlib import Path

def format_table(
    input_path: str,
    output_path: str,
    round_decimals: int = 4
) -> None:
    """
    Standardize numeric formatting for publication.
    """
    df = pd.read_csv(input_path)
    df = df.round(round_decimals)

    Path(output_path).parent.mkdir(parents = True, exist_ok = True)
    df.to_csv(output_path, index = False)

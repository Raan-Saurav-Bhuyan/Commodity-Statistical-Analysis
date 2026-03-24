from pathlib import Path

def export_latex(df, path: Path):
    if df is None:
        return

    path.parent.mkdir(parents = True, exist_ok =True)

    with open(path, "w") as f:
        f.write(df.to_latex(index = False))

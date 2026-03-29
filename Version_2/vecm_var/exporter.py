from pathlib import Path

def export_summary(summary_obj, path: Path):
    path.parent.mkdir(parents = True, exist_ok = True)

    with open(path, "w") as f:
        f.write(summary_obj.as_text())

import os
import numpy as np

def export_dcc(dcc_matrices, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    np.save(path, dcc_matrices)

"""
Preparation Module

This module is responsible for:
- Loading processed datasets
- Merging nominal, real, and inflation data
- Validating data integrity
- Providing structured dataset views for downstream modules
"""

from .loader import load_all_datasets
from .transformer import merge_datasets, split_views
from .validators import run_all_validations
from .runner import run_preparation_pipeline

__all__ = [
    "load_all_datasets",
    "merge_datasets",
    "split_views",
    "run_all_validations",
    "run_preparation_pipeline",
]

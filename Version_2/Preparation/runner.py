# Import custom modules: --->
from .loader import load_all_datasets
from .transformer import merge_datasets, split_views
from .validators import run_all_validations

def run_preparation_pipeline():
    """
    Main entry point for all downstream modules.
    """

    datasets = load_all_datasets()

    merged_df = merge_datasets(datasets)

    run_all_validations(merged_df)

    views = split_views(merged_df)

    return views

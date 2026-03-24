import pandas as pd
import os

OLD_FILE_PATH = '/home/raan_saurav_bhuyan/Programs/ML_Projects/Oil_vs_Gold/Datasets/gold_yearly.csv'
NEW_FILE_PATH = '/home/raan_saurav_bhuyan/Programs/ML_Projects/Oil_vs_Gold/Datasets/processed_gold_yearly.csv'

if __name__ == "__main__":
    if not os.path.exists(OLD_FILE_PATH):
        raise FileNotFoundError(f"File not found: {OLD_FILE_PATH}")

    try:
        # Read the CSV file: --->
        df = pd.read_csv(OLD_FILE_PATH)

        # Convert the 'Date' column to datetime objects and extract the year: --->
        df['Date'] = pd.to_datetime(df['Date']).dt.year

        # Write the modified DataFrame back to the CSV file: --->
        df.to_csv(NEW_FILE_PATH, index = False)

    except Exception as e:
        print(f"An error occurred: {e}")

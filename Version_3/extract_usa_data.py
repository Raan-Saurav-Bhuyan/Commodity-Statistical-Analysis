import pandas as pd
import os

INPUT_FILE = 'Version_2/Datasets/API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_84.csv'
OUTPUT_FILE = 'Version_2/Datasets/Raw/processed_india_inflation.csv'

if __name__ == "__main__":
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"Error: File not found at {INPUT_FILE}")

    # The World Bank CSV format contains 4 lines of metadata at the beginning.
    # We skip these rows so that the 5th line correctly becomes the header: --->
    df = pd.read_csv(INPUT_FILE, skiprows=4)

    # Drop the trailing empty column usually created by a trailing comma in World Bank CSVs: --->
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Filter the DataFrame for United States: --->
    usa_df = df[(df['Country Name'] == 'India') & (df['Country Code'] == 'IND')]

    # Set the index to 'Country Name' to use it as the column header upon transposing: --->
    usa_df = usa_df.set_index('Country Name')

    # Transpose the dataframe (rows become columns, columns become rows): --->
    transposed_df = usa_df.T

    # Export the transposed DataFrame: --->
    transposed_df.to_csv(OUTPUT_FILE)
    print(f"Data successfully extracted and transposed. Saved to:\n{OUTPUT_FILE}")

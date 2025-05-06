# src/load_data.py

import pandas as pd

def load_customer_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())
    return df
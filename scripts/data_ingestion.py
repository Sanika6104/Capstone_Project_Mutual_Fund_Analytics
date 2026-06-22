import os
import pandas as pd

DATA_FOLDER = "data/raw"

print("=" * 50)
print("MUTUAL FUND DATA INGESTION")
print("=" * 50)

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

for file in csv_files:
    print(f"\nProcessing: {file}")

    path = os.path.join(DATA_FOLDER, file)

    try:
        df = pd.read_csv(path)

        print("Shape:", df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print("Error:", e)

print("\nData Ingestion Complete")
import os
import pandas as pd

folder="data/silver"

print("="*60)
print("DATA QUALITY REPORT")
print("="*60)

for file in os.listdir(folder):
    if file.endswith(".parquet"):
        print(f"\nDataset : {file}")
        df = pd.read_parquet(os.path.join(folder, file))
        print("-"*50)

        print("Rows :", len(df))
        print("Columns :", len(df.columns))
        duplicates=df.duplicated().sum()
        print("Duplicate Rows :", duplicates)
        missing=df.isnull().sum()

        print("Missing Values")
        for col, value in missing.items():
            print(f"{col:35} {value}")
        print("-"*50)
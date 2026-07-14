import os
import pandas as pd

folder="data/silver"

print("DATA QUALITY REPORT :-")

for file in os.listdir(folder):
    if file.endswith(".parquet"):
        print(f"\nDataset : {file}")
        df=pd.read_parquet(os.path.join(folder, file))
        print("----------")

        print("Rows :", len(df))
        print("Columns :", len(df.columns))
        duplicates=df.duplicated().sum()
        print("Duplicate Rows :", duplicates)
        missing=df.isnull().sum()

        print("Missing Values")
        for col, value in missing.items():
            print(f"{col:35} {value}")
        print("----------")

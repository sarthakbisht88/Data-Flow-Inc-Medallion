import os
import pandas as pd
from utils import create_folder

BRONZE="data/bronze"
SILVER="data/silver"

create_folder(SILVER)

print("==========")
print("Creating Silver Layer")
print("==========")

for file in os.listdir(BRONZE):
    if not file.endswith(".parquet"):
        continue
    print(f"\nProcessing {file}")

    df = pd.read_parquet(os.path.join(BRONZE, file))
    before=len(df)
    df=df.drop_duplicates()
    duplicates_removed = before - len(df)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )


    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            pass
        else:
            df[col] = df[col].fillna("Unknown")
            df[col] = df[col].astype(str).str.strip()

    output=os.path.join(SILVER, file)
    df.to_parquet(output, index=False)

    print(f"Rows : {len(df)}")
    print(f"Duplicates Removed : {duplicates_removed}")
print("\nSilver Layer Created Successfully")

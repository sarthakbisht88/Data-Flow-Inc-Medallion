import os
import pandas as pd
from utils import create_folder

RAW="data/raw"
BRONZE="data/bronze"

create_folder(BRONZE)

print("Creating Bronze Layer...")

for file in os.listdir(RAW):
    if file.endswith(".csv"):
        path = os.path.join(RAW, file)
        df = pd.read_csv(path)
        print(f"Loaded {file}")
        print("Rows :", len(df))

        output = file.replace(".csv", ".parquet")
        df.to_parquet(
            os.path.join(BRONZE, output),
            index=False
        )
print("\nBronze Layer Created")
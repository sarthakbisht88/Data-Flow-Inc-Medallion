import os
import json
import pandas as pd

SCHEMA_FILE="schema.json"
current_schema = {}
folder="data/silver"

for file in os.listdir(folder):
    if file.endswith(".parquet"):
        df=pd.read_parquet(os.path.join(folder, file))
        current_schema[file]={
            column: str(dtype)
            for column, dtype in df.dtypes.items()
        }

if os.path.exists(SCHEMA_FILE):
    with open(SCHEMA_FILE) as f:
        old_schema = json.load(f)

    print("="*50)
    print("Schema Drift Report")
    print("="*50)

    for table in current_schema:
        print(f"\n{table}")
        old=old_schema.get(table, {})
        new=current_schema[table]
        added = set(new.keys()) - set(old.keys())
        removed = set(old.keys()) - set(new.keys())
        if added:
            print("Added Columns :", list(added))
        if removed:
            print("Removed Columns :", list(removed))
        if not added and not removed:
            print("No Schema Changes")
else:
    print("First execution. Saving schema.")
with open(SCHEMA_FILE, "w") as f:
    json.dump(current_schema, f, indent=4)
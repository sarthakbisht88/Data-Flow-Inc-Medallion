import os
import pandas as pd
from datetime import datetime

SILVER="data/silver"
OUTPUT="output"

os.makedirs(OUTPUT, exist_ok=True)
customers=pd.read_parquet(
    os.path.join(SILVER, "olist_customers_dataset.parquet")
)
customers["effective_date"]=datetime.today().strftime("%Y-%m-%d")
customers["expiry_date"]=None
customers["is_current"]=True
customers.to_csv(
    os.path.join(OUTPUT, "customer_history.csv"),
    index=False
)
print("SCD Type-2 History Created")

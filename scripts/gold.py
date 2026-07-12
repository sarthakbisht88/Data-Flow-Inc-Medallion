import os
import pandas as pd
from utils import create_folder

SILVER = "data/silver"
GOLD = "data/gold"

create_folder(GOLD)

print("=" * 60)
print("Creating Gold Layer")
print("=" * 60)

customers = pd.read_parquet("data/silver/olist_customers_dataset.parquet")
orders = pd.read_parquet("data/silver/olist_orders_dataset.parquet")
payments = pd.read_parquet("data/silver/olist_order_payments_dataset.parquet")

print("Customers :", customers.shape)
print("Orders :", orders.shape)
print("Payments :", payments.shape)

# Remove duplicate keys
customers = customers.drop_duplicates(subset="customer_id")

orders = orders.drop_duplicates(subset="order_id")

payments = (
    payments
    .groupby("order_id", as_index=False)["payment_value"]
    .sum()
)

sales = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="left",
    validate="one_to_one"
)

sales = pd.merge(
    sales,
    payments,
    on="order_id",
    how="left",
    validate="one_to_one"
)

sales.to_parquet(
    "data/gold/customer_sales.parquet",
    index=False
)

print("customer_sales.parquet created")

state_sales = (
    sales.groupby("customer_state", as_index=False)
    .agg(
        Total_Orders=("order_id", "count"),
        Total_Revenue=("payment_value", "sum"),
        Average_Order_Value=("payment_value", "mean")
    )
)

state_sales.to_parquet(
    "data/gold/state_sales.parquet",
    index=False
)

print("state_sales.parquet created")

payment_summary = (
    sales.groupby("order_status", as_index=False)
    .agg(
        Orders=("order_id", "count"),
        Revenue=("payment_value", "sum")
    )
)

payment_summary.to_parquet(
    "data/gold/order_summary.parquet",
    index=False
)

print("order_summary.parquet created")

print("\nGold Layer Created Successfully")
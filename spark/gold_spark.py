from pyspark.sql import SparkSession

spark=(
    SparkSession.builder
    .appName("Gold Layer")
    .getOrCreate()
)
orders = spark.read.parquet("data/silver/orders_spark")
payments = spark.read.csv(
    "data/raw/olist_order_payments_dataset.csv",
    header=True,
    inferSchema=True
)
gold = orders.join(payments, "order_id")
gold.write.mode("overwrite").parquet("data/gold/customer_sales_spark")
print("Gold Layer Created")
spark.stop()
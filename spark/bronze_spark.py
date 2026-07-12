from pyspark.sql import SparkSession

spark=(
    SparkSession.builder
    .appName("DataFlow Bronze Layer")
    .getOrCreate()
)
df=spark.read.option("header", True).csv("data/raw/olist_orders_dataset.csv")
df.write.mode("overwrite").parquet("data/bronze/orders_spark")
print("Bronze Layer Created Using Spark")
spark.stop()
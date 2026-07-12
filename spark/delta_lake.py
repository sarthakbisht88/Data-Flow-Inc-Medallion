from pyspark.sql import SparkSession

spark=(
    SparkSession.builder
    .appName("Delta Lake")
    .config(
        "spark.sql.extensions",
        "io.delta.sql.DeltaSparkSessionExtension"
    )
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    )
    .getOrCreate()
)
df = spark.read.parquet("data/gold/customer_sales_spark")
df.write.format("delta").mode("overwrite").save("delta/customer_sales")
print("Delta Table Created")
spark.stop()
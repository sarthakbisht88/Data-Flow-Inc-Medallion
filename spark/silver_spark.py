from pyspark.sql import SparkSession
from pyspark.sql.functions import trim,col

spark=(
    SparkSession.builder
    .appName("DataFlow Silver Layer")
    .getOrCreate()
)
df = spark.read.parquet("data/bronze/orders_spark")
df = df.dropDuplicates()
for c in df.columns:
    df = df.withColumn(c, trim(col(c)))
df.write.mode("overwrite").parquet("data/silver/orders_spark")
print("Silver Layer Created")
spark.stop()
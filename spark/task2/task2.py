import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, min, concat
from pyspark.sql.types import IntegerType

if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()

    edges_df = spark.read.text("%s" % sys.argv[1]).toDF("data")
    edges_df = edges_df.selectExpr("split(data, '\t') as columns").selectExpr("columns[0] as user", "columns[1] as follower")
    edges_df = edges_df.withColumn("user", col("user").cast(IntegerType())).withColumn("follower", col("follower").cast(IntegerType())).cache()

    x = 12
    y = 34
    d = 0
    distances_df = spark.createDataFrame([(x, x, d)], ["path", "vertex", "distance"])

    while True:
        expanded_df = distances_df.join(edges_df, on=edges_df["follower"] == distances_df["vertex"])
        expanded_df = expanded_df.select(
            concat(col("path"), lit(","), col("user")).alias("path"), col("user").alias("vertex"),
            (col("distance") + 1).alias("distance")
        )
        distances_df = expanded_df.na.drop().groupBy("path", "vertex").agg(min("distance").alias("distance"))

        y_count = distances_df.filter(col("vertex") == y).count()
        if y_count > 0:
            vertices_34 = distances_df.filter(col("vertex") == y).collect()
            for vertex in vertices_34:
                print(vertex['path'])
            break

        d += 1
        count = distances_df.filter(col("distance") == d).count()
        if count == 0:
            break
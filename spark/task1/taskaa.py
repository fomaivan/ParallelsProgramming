import re
import sys
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    config = SparkConf().setAppName("bigramm_task").setMaster("yarn")
    spark_context = SparkContext(conf=config)

    lines = spark_context.textFile("%s" % sys.argv[1])

    aoaoa = [(u'narodnaya_gazeta', 1),
             (u'narodnaya_volya', 9)]
    for line in aoaoa:
        print("%s %d" % (line[0], line[1]))

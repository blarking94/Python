from pyspark.sql import SQLContext, Row
from pyspark import SparkContext, SparkConf
from pyspark.sql.functions import col

import collections

# Create a Spark Session (the config bit is only for windows)
#conf = SparkConf().setAppName("SQL App").setMaster("local")
sc = SparkContext()

sqlCtx = SQLContext(sc)

def mapper(line):
	fields = line.split(",")
	return Row(ID = int(fields[0]), name = fields[1].encode("utf-8"), age = int(fields[2]), numFriends = int(fields[3]))

lines = sc.textFile("fakefriends.csv")
people = lines.map(mapper)

# Infer the schema and register the DataFrame as a table
schemaPeople = sqlCtx.createDataFrame(people).cache()
schemaPeople.registerTempTable("people")

# SQL can be run over DataFrames that have been registered as a table
teenagers = sqlCtx.sql("SELECT * FROM people WHERE age >= 13 AND age <= 19")
print(teenagers.dtypes)

for teen in teenagers.collect():
	print(teen)

schemaPeople.groupBy("age").count().orderBy(col("age").desc()).show()


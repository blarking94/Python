from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *
import re

conf = SparkConf().setAppName("olympics").setMaster("local")
sc = SparkContext(conf = conf)
sqlctx = SQLContext(sc)

def transform(x):
	
	#return Row(int(x[0]), x[1], x[2], int(x[3]), float(x[4]), float(x[5]), x[6], x[7], x[8], int(x[9]), x[10], x[11], x[12], x[13], x[14])
	return Row(x[0], x[1], x[2], x[3], float(x[4]), float(x[5]), x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14])

raw = sc.textFile("file:///SparkCourse/athlete_events.csv")

header = raw.first()

print(header)

raw_no_header = raw.filter(lambda x : x != header)

transformed = raw_no_header.map(transform)

print(raw_no_header.take(5))
print(transformed.take(5))

schema = StructFields([
		StructType("ID", StringType, False),
		StructType("Name", StringType, False),
		StructType("Sex", StringType, False),
		StructType("Age", StringType, False),
		StructType("Height", StringType, False),
		StructType("Weight", StringType, False),
		StructType("Team", StringType, False),
		StructType("NOC", StringType, False),
		StructType("Games", StringType, False),
		StructType("Year", StringType, False),
		StructType("Season", StringType, False),
		StructType("City", StringType, False),
		StructType("Sport", StringType, False),
		StructType("Event", StringType, False),
		StructType("Medal", StringType, False)
	])




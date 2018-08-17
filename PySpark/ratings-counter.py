from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

def f(x): print(x)
# Read in each line from the file 
lines = sc.textFile("file:///SparkCourse/ml-100k/u.data")

# from the 100k rows take 0.0001% of the data (10 records) and print
lines.sample(False, 0.0001).foreach(f)

# Split the lines on a white space and just take the second element
ratings = lines.map(lambda x: x.split()[2])
# Map each rating to number 1 and then reduce by key to count
result = ratings.map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b )

# Create a schema and then a dataframe
schema = StructType([
	StructField("rating", StringType(), False),
	StructField("count", IntegerType(), False)
	])

df = sqlContext.createDataFrame(result, schema)

df.orderBy(col("count").desc()).show()

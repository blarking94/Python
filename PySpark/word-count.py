from pyspark import SparkConf, SparkContext, StorageLevel
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
import re


conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

def f(x): print(x)

# Imported regular expression lib. Break up the text based on words (r'\W') stating that this might have unicode characters in it (, re.UNICODE). and split on words that have been changed to lower
def normalizeWords(text):
	return re.compile(r'\W+', re.UNICODE).split(text.lower())

lines = sc.textFile("file:///SparkCourse/Book.txt")

# Flat Map can return many RDD's. By performing this split on white spaces we split each single row that represents a line into many rows that represent a word each/ 
words = lines.flatMap(normalizeWords).map(lambda x: (x, 1))

# Basic flat map split won't remove capitals or grammer
#words = lines.flatMap(lambda x: x.split())

# Map each word to the number 1 and reduce by word key to get a count of each word. Could just countByValue().

mapped_words = words.reduceByKey(lambda row_x_value, row_y_value: row_x_value + row_y_value)

# Sort as an RDD is a little complicated. We have sortByKey but that would sort by the words. So we can use a map function to reverse the data. 
reversed_rdd = mapped_words.map(lambda (x,y) : (y,x)).sortByKey()

reversed_rdd.persist(storageLevel=StorageLevel(True, True, False, True, 1))

print(reversed_rdd.takeSample(False, 10))

# This is how we could use a data frame to sort the values 
schema = StructType([
	StructField("word", StringType(), False),
	StructField("count", IntegerType(), False)
	])

df = sqlContext.createDataFrame(mapped_words, schema)

df.orderBy(col("count").desc()).limit(25).show()

df.filter((df.count > 500) and (df.word.isin("to","you","and"))).show()

best_results = df.filter((col("count") > 500) & (df.word != ""))

best_results.show()

best_rdd = best_results.rdd.map(lambda x: (x[0] + "\t" + str(x[1])))
header = sc.parallelize(["word\tcount"])
joined = header.union(best_rdd)

print(joined.take(10))

joined.saveAsTextFile("file:///SparkCourse/counts")


acc = sc.accumulator(0)

for row in words.collect():
	if row[0] == "and":
		acc.add(1)

print("the word 'and' appears " + str(acc.value) + " times")





from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("Basic Lambda")
sc = SparkContext(conf = conf)

def f(x):
	print(x)

rdd = sc.parallelize([1,2,3,4,5])

#Multiplies each member of the RDD by itself
results = rdd.map(lambda x : x*x)

results.foreach(f)

# Reads in two lines
rdd = sc.parallelize(["hello hi bye hello hello hi bye hello hello hi", "hello hi bye hello hello hi bye hello hello hi"])

# Turn the lines into indivisual words, this increases the size of the rdd
lines = rdd.flatMap(lambda x : x.split(" "))

# Map each word with the number 1 
results = lines.map(lambda x: (x, 1))

# Reduce by key
results.reduceByKey(lambda a, b: a + b).foreach(f)


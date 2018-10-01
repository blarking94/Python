from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row
from pyspark.sql.functions import col

conf = SparkConf().setAppName("Popular Movie SQL").setMaster("local")
sc = SparkContext(conf = conf)
sqlCtx = SQLContext(sc)

def loadMovies():
	names = {}
	with open("ml-100k/u.ITEM") as f:
		for line in f:
			fields = line.split("|")
			names[int(fields[0])] = fields[1]
	return names

nameDict = loadMovies()

lines = sc.textFile("file:///SparkCourse/ml-100k/u.data")

movies = lines.map(lambda x: Row(movieID = int(x.split()[1])))

movieDF = sqlCtx.createDataFrame(movies)

topMovie = movieDF.groupBy("movieID").count().orderBy(col("count").desc()).cache()

topMovie.show()

top10 = topMovie.take(10)

for record in top10:
	print("%s: %d") % (nameDict[record[0]], record[1])


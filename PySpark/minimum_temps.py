from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FindMinTemp")
sc = SparkContext(conf = conf)


def f(x): print(x)

# Schema is Weather Station ID, date in yyyymmdd, type (TMIN, TMAX), Temperature in 10th degrees
temp_data = sc.textFile("file:///SparkCourse/1800.csv")

def parseLines(x):
	splits = x.split(",")
	station = splits[0]
	temp = float(splits[3])
	return (station, temp)

# We only want rows with type TMIN. Parse them to get the station id and the temp
rdd = temp_data.filter(lambda x : "TMIN" in x).map(parseLines)

# Reduce by station id and take the minimum temperature
minTemps = rdd.reduceByKey(lambda row_x_value, row_y_value, : min(row_x_value, row_y_value))

minTemps.foreach(f)
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MaxTemps")
sc = SparkContext(conf = conf)

# Schema is Weather Station ID, date in yyyymmdd, type (TMIN, TMAX), Temperature in 10th degrees
raw_temp_data = sc.textFile("file:///SparkCourse/1800.csv")

def parseLines(x):
	splits = x.split(",")
	station = splits[0]
	temp = float(splits[3])
	return(station, temp)

# Filter temp data to get the max temperatures then parse the lines to just get station id and temp
rdd = raw_temp_data.filter(lambda x: "TMAX" in x).map(parseLines)

# Reduce by the station id as key and find the max temperature
max_temps = rdd.reduceByKey(lambda row_x_value, row_y_value: max(row_x_value, row_y_value))

# Using collect rather than map and function to print all the data
results = max_temps.collect()

for result in results:
	print("Station: " + result[0] + ", Temperature : " + str(result[1]))
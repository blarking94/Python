# Schema is customer_id, product_id, spend
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("totalCustomerSpend")
sc = SparkContext(conf = conf)

def parseLine(x):
	items = x.split(",")
	customer_id = items[0]
	spend = float(items[2])
	return (customer_id, spend)

raw_rdd = sc.textFile("file:///SparkCourse/customer-orders.csv")

lines = raw_rdd.map(parseLine)

summed_rdd = lines.reduceByKey(lambda x , y: x + y).map(lambda (x, y) : (y, x)).sortByKey().map(lambda (x, y) : (y, x))

for spend in summed_rdd.collect():
	print(spend)
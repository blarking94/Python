from pyspark import SparkContext
from pyspark.sql import HiveContext
import csv

sc = SparkContext()
hc = HiveContext(sc)

data = hc.sql("Put Your Query Here")

# This will show us the results 
data.show()

# Open and create the file
with open("file:///larkingb/home/filename.csv", "wb") as file:
		writer = csv.writer(file, delimiter=",")
		# Turns all the data into an array and loops through the array
		for row in data.collect():
			writer.writerow(row)
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row
import csv


conf = SparkConf().setAppName("colours").setMaster("local")
sc = SparkContext(conf = conf)
sqlCtx = SQLContext(sc)

# Reading a multi line json file
raw_json = sqlCtx.read.option("multiline", "true").format('json').load("file:///SparkCourse/colours.json")

print(raw_json.dtypes)

def parse(x):
	new_colour = x[1].replace("#", "")
	return (x[0], new_colour)

# Convert to RDD
raw_rdd = raw_json.rdd.map(lambda x : parse(x))


english_Row = Row('colour', 'hash_value')
# Convert to Rows
tidy_rdd = raw_rdd.map(lambda x : english_Row(*x))


print(tidy_rdd.take(7))

#with open("C:\SparkCourse\english_colours.csv", "wb") as file:
		#writer = csv.writer(file, delimiter=",")
		#for row in tidy_rdd.collect():
		#	writer.writerow(row)

print("\t *** Part 2 Changing Delimiter ***")

with_comma_csv = sc.textFile("file:///SparkCourse/english_colours.csv")
print(with_comma_csv.take(5))
with_bar_csv = with_comma_csv.map(lambda x: x.split(",")).map(lambda x : (x[0] + "|" + x[1]))
print(with_bar_csv.take(5))

with_bar_csv.saveAsTextFile("file:///SparkCourse/with_bar")

print("\t *** Part 3 Read In Bar and Write as JSON ***")
#tidy_rdd.saveAsTextFile("file:///SparkCourse/english_colours_parts.csv", compressionCodecClass="org.apache.hadoop.io.compress.GzipCodec")
bar_frame = sqlCtx.read.text("file:///SparkCourse/with_bar")
bar_frame.show()
bar_rdd = bar_frame.rdd.map(lambda x : x[0].split("|"))
print(bar_rdd.take(5))

bar_rdd.map(lambda x : english_Row(*x)).toDF().write.format("json").save("file:///SparkCourse/with_json")

back_in_json = sqlCtx.read.format("json").load("file:///SparkCourse/with_json")
back_in_json.show()


print("\t *** Part 4 Create Dataframe, save as ORC and Read as ORC ***")

sqlCtx.sql("create table colours (colour STRING, hash_value STRING) stored as parquet")

back_in_json.write.format("parquet").save("colours")

my_data = sqlCtx.sql("SELECT * from colours")
mydata.show()









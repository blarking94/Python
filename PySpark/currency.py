from pyspark import SparkContext, SparkConf;
from pyspark.sql import SQLContext;
from pyspark.sql.types import *;
from pyspark.sql.functions import *;
import time;


conf = SparkConf().setMaster("local").setAppName("currency")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

def parseRaw(line):
	split = line.split(",")
	date = split[0]
	gbp = split[1]
	usd = split[2]
	yen = split[3]
	return(date, gbp, usd, yen)

raw = sc.textFile("file:///SparkCourse/test_data/currency.csv")

header = raw.first()

c_rdd = raw.filter(lambda x: x != header).map(lambda x: parseRaw(x))

print(c_rdd.take(10))

schema = StructType([
	StructField("date", StringType(), False),
	StructField("gbp", StringType(), False),
	StructField("usd", StringType(), False),
	StructField("yen", StringType(), False)
	])


#c_df = sqlContext.createDataFrame(c_rdd, schema)

c_df = c_rdd.toDF(["date", "gbp", "usd", "yen"])

c_df.show()
print(c_df.dtypes)



latest_gbp_year = c_df.filter(year('date') == "2012").select('gbp')
latest_yen_year = c_df.filter(year('date') == "2012").select('yen')

latest_gbp_year.show()
latest_yen_year.show()

avg_gbp = latest_gbp_year.agg({"gbp": "avg"}).withColumn("id", lit(1))
avg_yen = latest_yen_year.agg({"yen": "avg"}).withColumn("id", lit(1))

avg_gbp.show()
avg_yen.show()

joined = avg_gbp.join(avg_yen, "id", "outer").drop("id")

joined.rdd.map(lambda x: (str(x[0]) + "\t" + str(x[1]))).saveAsTextFile("file:///SparkCourse/test_data/currency")

joined.show()


min_gbp = latest_gbp_year.agg({"gbp": "min"}).withColumn("id", lit(1))
max_gbp = latest_gbp_year.agg({"gbp": "max"}).withColumn("id", lit(1))

min_gbp.show()
max_gbp.show()


headers = sc.parallelize(["avg_gbp\tavg_yen"])

final = headers.union(joined.rdd.map(lambda x: (str(x[0]) + "\t" + str(x[1]))))

final.saveAsTextFile("file:///SparkCourse/test_data/currency_headers")

#joined.saveAsTextFile("file:///SparkCourse/test_data/currency")






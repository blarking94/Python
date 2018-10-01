from pyspark import SparkContext, SparkConf


conf = SparkConf().setMaster("local[*]")
sc = SparkContext(conf = conf)

data = sc.parallelize([1,2,3], 3)

for row in data.collect():
	print(row)

data2 = sc.parallelize([1,2,3], 5).glom()

for row in data2.collect():
	print(row)

accum = sc.accumulator(0)

data.foreach(lambda x : accum.add(1))

print(accum.value)


broad = sc.broadcast([1,2,3])

print(data2.map(lambda x: (x , broad.value)).take(20))






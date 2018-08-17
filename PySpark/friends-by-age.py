from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("friendsbyage")
sc = SparkContext(conf = conf)

def f(x): print(x)

# schema is ID, Name, Age, Number Of Friends
lines = sc.textFile("file:///SparkCourse/fakefriends.csv")

def getLines(x):
	words = x.split(",")
	age = int(words[2])
	no_friends = int(words[3])
	return (age,  no_friends)

# Take each line and split on the ",". Then just take the age and number of friends e.g (18, 165)
rdd = lines.map(getLines)

# Use mapValues to map the number of friends with the number 1. e.g (18, (165, 1))
mapped = rdd.mapValues(lambda x : (x, 1))

# Count how many times each age appears and total up the number of friends e.g (18, (400, 2))
reduced = mapped.reduceByKey(lambda row_x, row_y: (row_x[0] + row_y[0], row_x[1] + row_y[1]))

# Find the avarage amount of friends e.g (18, 200)
results = reduced.mapValues(lambda x: x[0] / x[1])

results.foreach(f)


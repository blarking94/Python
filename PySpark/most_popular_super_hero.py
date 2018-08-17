from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("MostPopularSuperHero")
sc = SparkContext(conf = conf)

def parseNames(x):
	# Split on " to remove the grammer and get id and name
	words = x.split("\"")
	hero_id = int(words[0])
	name = words[1]
	return (hero_id, name)

def friends(x):
	items = x.split()
	# After splitting on white space get the hero id and, using the len function, get the number of co-appearances
	hero_id = int(items[0])
	num_friends = len(items[1:])
	return (hero_id, num_friends)

# Read in the id and name of all the marvel super heros. Schema is hero_id "hero_name"
names = sc.textFile("file:///SparkCourse/Marvel-Names.txt").map(parseNames)

# Find the most popular hero. Read in the graph file. Schema hero_id co-appearance-id's...[]. Map to get the total number of friends they appear with and reduce by key.
# Then perform a flip to get total_co_occurances hero_id. Then use the max function to find the maxiumum key value (i.e the highest count)
most_popular = sc.textFile("file:///SparkCourse/Marvel-Graph.txt").map(friends).reduceByKey(lambda x, y: x + y).map(lambda (x,y): (y,x)).max()

# To find the most popular id's name use the look up function on the names rdd passing in the id of the most popular super hero
most_popular_name = names.lookup(most_popular[1])[0]

print(most_popular_name + " is the most popular superhero with " + str(most_popular[0]) + " co-apparances")





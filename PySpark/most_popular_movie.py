from pyspark import SparkConf, SparkContext

# Uses broadcast variables

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)


def loadMovieNames():
	movie_names = {}
	# Schema : movie id | movie title
	# with this file as f read each line split on pipe and get the movie id and movie title
	with open("ml-100k/u.ITEM") as f:
		for line in f:
				fields = line.split('|')
				# in our movie name dict we want to add into movie id position the movie title
				movie_names[int(fields[0])] = fields[1]
	return movie_names

name_dict = sc.broadcast(loadMovieNames())


# Read in each line from the file. 
# Schema is UserID MovieID Rating Timestamp
lines = sc.textFile("file:///SparkCourse/ml-100k/u.data")

# We just want to get the movie id here so in a lambda function we can split and take the id
movie_ids = lines.map(lambda x: int(x.split()[1]))

def flip(x):
	return (x[1], x[0])

# Take the movie id's and reduce by key to count how many times each movie appeard. Then flip to get count, movie_id and sort to get an ordered list of popular movies
sorted = movie_ids.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y).map(flip).sortByKey()

# Find the movie name by searching the dict for the movie id
sortedMoviesWithName = sorted.map(lambda (count, movie_id) : (name_dict.value[movie_id], count))

results = sortedMoviesWithName.collect()

for result in results:
	print(result)




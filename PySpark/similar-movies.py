from pyspark import SparkContext, SparkConf 
import sys
from math import sqrt


def loadMovieNames():
	movies = {}

	with open("ml-100k/u.ITEM") as f:
		for line in f:
			items = line.split("|")
			movie_id = int(items[0])
			move_name = items[1].decode("ascii", "ignore")
			movies[movie_id] = movie_name

	return movies

# This will sort our movies and eliminate movies that are the same
def filterDuplicates( (user_id, ratings) ):
	(movie1, rating1) = ratings[0]
	(movie2, rating2) = ratings[1]
	return movie1 < movie2

def makePairs((user, ratings)):
	(movie1, rating1) = ratings[0]
	(movie2, rating2) = ratings[1]
	return ((movie1, movie2), (rating1, rating2)

def computeCosineSimilarity(ratingsPairs):
	numPairs = 0 
	sum_xx = sum_yy = sum_xy
	for ratingX, ratingY in ratingsPairs:
		sum_xx += ratingX * ratingX
		sum_yy += ratingY * ratingY
		sum_xy += ratingX * ratingY
		numPairs+=1

	numerator = sum_xy
	denominator = sqrt(sum_xx) * sqrt(sum_yy)

	score = 0 
	if (denominator):
		score = (numerator / (float(denominator)))

	return (score, numPairs	)



# Notice the local[*] here rather than local as we're going to create a large data set so want to use
# as many CPU's as possible.
conf = SparkConf().setMaster("local[*]").setAppName("SimilarMovies")
sc = SparkContext(sc)

movie_names = sc.broadcast(loadMovieNames())

data = sc.textFile("file:///SparkCourse/ml-100k/u.data")

# From the raw data split on white space and map to user_id, (movie_id, rating)  	
parsed = data.map(lambda x: x.split()).map(lambda x: (int(x[0]), (int(x[0]),float(x[0]))))

# Perform a self join to give us something like user_id ((movie_id, rating),(movie_id,rating))
joined = parsed.join(parsed)

# user might have given multiple ratings to same movie
unique_joined = joined.filter(filterDuplicates)

# We only want to know what movies are similar
movie_pairs = unique_joined.map(makePairs)

# now collect all ratings for each movie pair 
movie_pairs_rating.groupByKey()

# Now we can compute similarities. As this requries lots of computing we want to cache the result
movie_pairs_similarities = movie_pairs_rating.mapValues(computeCosineSimilarity).cache()

movie_pairs_similarities.sortByKey().saveAsTextFile("movie-sims")



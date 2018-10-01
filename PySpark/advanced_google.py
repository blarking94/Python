###
# This file is designed to show some of the more advanced apache spark functions
# The data has been sourced from Kaggle. https://www.kaggle.com/lava18/google-play-store-apps
# The data relates to google play store apps and their reviews
###

from pyspark import SparkContext, SparkConf
import re

conf = SparkConf().setMaster("local").setAppName("advanced_google")
sc = SparkContext(conf = conf)

#logger = sc._jvm.org.apache.log4j
#logger.LogManager.getLogger("org"). setLevel( logger.Level.INFO )
#logger.LogManager.getLogger("akka").setLevel( logger.Level.INFO )


def parseRawApps(line):
	if line[0] == "\"":
		split = line.split("\"", 2)

		print("hello")
		print(split)
		print("Hello")
		app = re.sub(u"\u2013", "-", split[1])
		print(app)
		params = split[2].split(",")
		print(params)

		cat = params[1]
		rating = float(params[2])
		reviews = int(params[3])
		size = params[4]
		installs = int(params[5].replace("\"", "").replace(",", "").replace("+", ""))
		type = params[6]
		price = float(params[7].replace("Free", "0.0"))
		android_var = params[12].replace("and up", "")
		return(app,cat,rating,reviews,size,installs,type,price,android_var)
	else:
		split = line.split(",")
		app = split[0].replace("\"", "")
		cat = split[1]
		rating = float(split[2])
		reviews = int(split[3])
		size = split[4]
		installs = int(split[5].replace("\"", "").replace(",", "").replace("+", ""))
		type = split[6]
		price = float(split[7].replace("Free", "0.0"))
		android_var = split[12].replace("and up", "")
		return(app,cat,rating,reviews,size,installs,type,price,android_var)

# This file is comma delimited and has a header
# App,Category,Rating,Reviews,Size,Installs,Type,Price,Content Rating,Genres,Last Updated,Current Ver,Android Ver
# Coloring book moana,ART_AND_DESIGN,3.9,967,14M,"500,000+",Free,0,Everyone,Art & Design;Pretend Play,"January 15, 2018",2.0.0,4.0.3 and up
# Floor Plan Creator,ART_AND_DESIGN,4.1,36639,Varies with device,"5,000,000+",Free,0,Everyone,Art & Design,"July 14, 2018",Varies with device,2.3.3 and up
raw_apps = sc.textFile("file:///SparkCourse/google_data/googleplaystore.csv")

# Remove the header of raw apps
header = raw_apps.first()

# Parse the data into comma seperated and drop non interesting fields
apps = raw_apps.filter(lambda x : x != header)

print(apps.take(10))

clean_apps = apps.map(lambda x: parseRawApps(x))

print(clean_apps.take(10))

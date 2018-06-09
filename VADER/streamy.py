import json
import tweepy
from datetime import datetime

from elasticsearch import Elasticsearch

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from secret_config import access_token_key, access_token_secret, consumer_key, consumer_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

analyzer = SentimentIntensityAnalyzer()

# create instance of elasticsearch
es = Elasticsearch()

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):

        #text to json
        dict_data = json.loads(data)
        print(dict_data)

        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])

        print(tweet)

        # output sentiment polarity for Text Blob
        print("The TextBlob Score : " + str(tweet.sentiment.polarity))

        # output sentiment polarity for Vader
        vs = analyzer.polarity_scores(dict_data["text"])
        print("The Vader Score : " + str(vs['compound']))

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            blob_sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            blob_sentiment = "neutral"
        else:
            blob_sentiment = "positive"

        # output blob_sentiment
        print(blob_sentiment)

        # determine if sentiment is positive, negative, or neutral
        if float(vs['compound']) < 0:
            vader_sentiment = "negative"
        elif float(vs['compound']) == 0:
            vader_sentiment = "neutral"
        else:
            vader_sentiment = "positive"

        # output blob_sentiment
        print(vader_sentiment)

        # add text and sentiment info to elasticsearch
        es.index(index="sentiment",
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       #"posted": dict_data['created_at'],
                       "posted":  datetime.strptime(dict_data['created_at'], '%a %b %d %H:%M:%S +0000 %Y'),
                       "message": dict_data["text"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "blob_sentiment": blob_sentiment,
                       "vader_sentiment": vader_sentiment})
        return True


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = auth, listener=myStreamListener)

myStream.filter(track=['trump'])


#[49.979,-10.393,58.813,2.351]

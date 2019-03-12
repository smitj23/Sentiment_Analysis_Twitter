import tweepy
import re
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):

    def __init__(self):
        '''Class Constructor'''
        key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
        secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

        #authentication
        try:
            self.auth = OAuthHandler(key,secret)
            self.auth.set_access_token(access_token,access_token_secret)
            self.api = Tweepy.API(self.auth)
        except:
            print('Authentication Failed!!')

    def tweet_sentiment(self, tweet):
    '''classify sentiment of the parsed tweet using TextBolb'''
        analysis = TextBlob(self.clean_tweet(tweet))

        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else :
            return 'negative'


import tweepy
import re
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):

    def __init__(self):
        '''Class Constructor'''
        consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
        consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

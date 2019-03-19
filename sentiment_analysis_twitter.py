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

    try:
        def get_tweets(self, query, count = 10):
    
            tweets = []
    # call the twitter api to fetch the tweets and parse them
            tweets_fetched = self.api.search(query =query, count = count )

            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                tweets_parsed = {} 
  
                # saving text of tweet 
                tweets_parsed['text'] = tweet.text 
                # saving sentiment of tweet 
                tweets_parsed['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if tweets_parsed not in tweets: 
                        tweets.append(tweets_parsed) 
                else: 
                    tweets.append(tweets_parsed) 
  
            # return parsed tweets 
            return tweets         

	#catching the exception and shows an error when tweets not parsed
    except tweepy.TweepError as e:
        print('Error:' + str(e))



main():

api = TwitterClient()
tweets = api.get_tweets(query = "Elon Muck", count = 400)

#positive tweets from the query 

positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

print("Positive tweets percentage: {} %".format(100*len(positive_tweets)/len(tweets)))

negative_tweets = [tweet for tweet in tweets if tweet['sentimen't] == negative]

print("Negative tweets percentage: {} %".format(100*len(negative_tweets)/len(tweets)))


#first 5 tweets from the query 
print('\nPositive Tweets')
for tweet in positive_tweets[:10]:
    print(tweet['text'])

 
# 5 negative tweets from the query 

print('\n Negative Tweets')
for tweet in negative_tweets[:10]:
    print(tweet['text'])

if __name__== '__main__':
    main()



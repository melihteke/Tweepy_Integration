import tweepy

# Replace these values with your own credentials
API_KEY = 'API_KEY'
API_KEY_SECRET = 'API_KEY_SECRET'
ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'
BEARER_TOKEN = 'BEARER_TOKEN'

# Authenticate to Twitter using OAuth 2.0 Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN, 
                       consumer_key=API_KEY, 
                       consumer_secret=API_KEY_SECRET, 
                       access_token=ACCESS_TOKEN, 
                       access_token_secret=ACCESS_TOKEN_SECRET)

# Post a tweet
tweet = "Hello, world! This is a tweet from Tweepy using Twitter API v2."
response = client.create_tweet(text=tweet)

print("Tweet posted successfully!", response)

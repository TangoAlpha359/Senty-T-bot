import tweepy
from textblob import TextBlob
from secrets import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

if __name__ == '__main__':
    print("What's going on?")
    keyword = input()

    public_tweets = api.search(keyword)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0] > 0:
        print('Positive')
    elif analysis.sentiment[0] == 0:
        print("Neutral")
    elif analysis.sentiment[0] < 0:
        print("Negative")
    print("")

# Original

# import tweepy
# from textblob import TextBlob

# consumer_key = 'Keyhere'
# consumer_key_secret = 'EnterKey'

# access_token = 'TokenHere'
# access_token_secret = 'EnterToken'

# auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# public_tweets = api.search('Penguins')

# for tweet in public_tweets:
# 	print(tweet.text)
# 	analysis = TextBlob(tweet.text)
# 	print(analysis.sentiment)
# 	if analysis.sentiment[0]>0:
# 		print ('Positive')
# 	else:
# 		print ('Negative')
# 	print("")

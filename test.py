import json

from Twitter.Keys import *
from Twitter.TwitterApi import Twitter

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'

t = Twitter(consumer_key, consumer_secret)
fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular'}

tweets = t.search_tweets_videos(2, fields,TWEET_VIDEOS_KEYS)
print(json.dumps(tweets,indent=4,default=str))
print(len(tweets))



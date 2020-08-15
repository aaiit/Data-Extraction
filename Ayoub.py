import json

from pandas import DataFrame

from Twitter.Keys import *
from Twitter.TwitterApi import Twitter

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'

t = Twitter(consumer_key, consumer_secret)


def gettweetstext(fields):
    # fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular'}
    type = fields.pop('type', 'json')
    keys = fields.pop('output', TWEET_KEYS)
    tweets = t.search_tweets_images(fields.pop('len', 10), fields, keys)
    return json.dumps(tweets, default=str, indent=4) if type == 'json' else DataFrame(tweets).to_csv(index=False)

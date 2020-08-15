import json
from Twitter.Keys import *
from Twitter.TwitterApi import Twitter

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'

t = Twitter(consumer_key, consumer_secret)


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def gettweetstext(fields):
    # fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular'}
    type = fields.pop('type', 'json')
    tweets = t.search_tweets_images(fields.pop('len', 10), fields, TWEET_IMAGES_KEYS)
    return json.dumps(tweets, default=str, indent=4) if type == 'json' else flatten_json(tweets)

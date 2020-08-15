import json

from pandas import DataFrame

from Twitter.Keys import *
from Twitter.TwitterApi import Twitter

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'

t = Twitter(consumer_key, consumer_secret)


def get_tweets_text(fields):
    # fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular'}
    type = fields.pop('type', 'json')
    keys = fields.pop('output', TWEET_KEYS)
    tweets = t.search_tweets_images(fields.pop('len', 10), fields, keys)
    return json.dumps(tweets, default=str, indent=4) if type == 'json' else DataFrame(tweets).to_csv(index=False)


def get_comments(fields):
    name = fields('username', '')
    tweet_id = fields('id', '')
    count = fields('count', 10)
    keys = fields('output', REPLIES_KEYS)
    type = fields.pop('type', 'json')
    replies = t.get_replies(name, tweet_id, keys, count=count)
    return json.dumps(replies, default=str, indent=4) if type == 'json' else DataFrame(replies).to_csv(index=False)

import csv
from time import sleep
import json
import pandas as pd
import tweepy

# Constants
from Twitter.Keys import TWEET_KEYS

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'
# Authentificate and construct the api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, timeout=11)

count = 100


def comments(fields):
    list = []
    name = fields('username', 'calvinklein')
    tweet_id = fields('id', '1293259670531039232')
    count = fields('count', 100)
    keys = fields('output', TWEET_KEYS)
    replies = []
    for tweet in tweepy.Cursor(api.search, q='to:' + name, since_id=tweet_id, result_type='mixed',
                               timeout=999999).items(count):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id_str == str(tweet_id) and tweet.in_reply_to_status_id == int(tweet_id):
                list.append(tweet)
                if len(replies) >= count:
                    break
    mx = max(l[0] for l in list)
    if int(mx) == 0:
        return "{}"
    else:
        final_list = []
        for t in list:
            if int(mx) == int(t[0]):
                final_list.append((t[0], t[5]))
        df = pd.DataFrame(final_list)
        df.to_csv('commentmostlikes.csv', index=False)
        return open("filename.csv").read()


def likes(fieds):
    for tweet in tweepy.Cursor(api.search, q="aida",
                               lang="en", result_type='popular').items(count):
        list.append((tweet.id, tweet.favorite_count, tweet.user.name, tweet.created_at, tweet.lang, tweet.retweet_count,
                     tweet.source,
                     tweet.truncated, str(tweet.text)))
    list.sort(key=lambda x: x[1])
    df = pd.DataFrame(list)
    df.to_csv('filename.csv', index=False)
    return open("filename.csv").read()

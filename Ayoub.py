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


'''

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


'''

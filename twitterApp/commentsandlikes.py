import json
from fire import upload
import pandas as pd
import tweepy

# Constants
from Twitter.Keys import TWEET_KEYS

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'
# Authentificate and construct the api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, timeout=11)


def comments(fields):
    count = 100
    list = []
    type = fields.pop('type', 'csv')
    name = fields.pop('username', '')
    tweet_id = fields.pop('id', '')
    for tweet in tweepy.Cursor(api.search, q='to:' + name, since_id=tweet_id, result_type='mixed',
                               timeout=999999).items(500):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id_str == str(tweet_id):
                list.append((tweet.favorite_count, tweet.id, tweet.in_reply_to_status_id_str, tweet.user.name,
                             tweet.user.id, tweet.text))
                if len(list) >= count:
                    break
    if len(list) == 0:
        return '{}'
    mx = max(l[0] for l in list)
    if int(mx) == 0:
        return "{}"
    else:
        final_list = []
        for t in list:
            if int(mx) == int(t[0]):
                final_list.append((t[0], t[3], t[5]))
        return upload(pd.DataFrame(final_list, columns=['favorite_count', 'User', 'Comment']).to_csv(
            index=False))


def likes(fields):
    count = fields.pop('count', 100)
    q = fields.pop('q', 'aida')
    lang = fields.pop('lang', 'en')
    result_type = fields.pop('result_type', 'popular')
    type = fields.pop('type', 'json')
    keys = fields.pop('output', TWEET_KEYS)
    # if not check_date_format(fields['since'] ):
    #     fields.pop('since', '')
    # if not check_date_format(fields['until']):
    #     fields.pop('until', '')
    l = []
    print(q, lang, result_type)
    for tweet in tweepy.Cursor(api.search, q=q, **fields, lang=lang, result_type=result_type).items(100):
        print("->>>>>>>>>>>  ")
        l.append({'id': tweet.id, 'favorite': tweet.favorite_count, 'username': tweet.user.name,
                  'create at': tweet.created_at, 'language': tweet.lang, 'retweets': tweet.retweet_count,
                  'source': tweet.source, 'text': str(tweet.text)})
    if len(l) == 0:
        return '[]'
    l = sorted(l, key=lambda x: x[1])
    return upload(pd.DataFrame(l[0]).to_csv(index=False))

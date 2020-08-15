import json

from pandas import DataFrame

from Twitter.Keys import *
from Twitter.TwitterApi import Twitter, check_date_format

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'

t = Twitter(consumer_key, consumer_secret)


def get_tweets_text(fields):
    # fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular'}
    type = fields.pop('type', 'json')
    keys = fields.pop('output', TWEET_KEYS)
    tweets = t.search_tweets_text(fields.pop('len', 10), fields, keys)
    return json.dumps(tweets, default=str, indent=4) if type == 'json' else DataFrame(tweets).to_csv(index=False)


def get_comments(fields):
    name = fields.pop('username', '')
    tweet_id = fields.pop('id', '')
    count = fields.pop('count', 10)
    keys = fields.pop('output', REPLIES_KEYS)
    type = fields.pop('type', 'csv')
    replies = t.get_replies(name, tweet_id, keys, count=count)
    return json.dumps(replies, default=str, indent=4) if type == 'json' else DataFrame(replies).to_csv(index=False)


def get_tweets_video(fields):
    if check_date_format(fields['since']):
        fields.pop('since', '')
    if check_date_format(fields['until']):
        fields.pop('until', '')
    type = fields.pop('type', 'json')
    keys = fields.pop('output', TWEET_VIDEOS_VIDEO_KEY)
    videos = t.search_tweets_videos(fields.pop('len', 10), fields, keys)
    vids = []
    for vid in videos:
        vv = vid[TWEET_VIDEOS_VIDEO_KEY[0]][0]
        vv = [v for v in vv if 'mp4' in v['content_type']]
        vv = sorted(vv, key=lambda x: x['bitrate'])
        vids.append(vv[0]['url'])
    return '\n'.join(vids)

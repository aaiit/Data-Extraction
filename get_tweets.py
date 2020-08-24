import json
from fire import upload
from pandas import DataFrame

from Twitter.Keys import *
from Twitter.TwitterApi import Twitter, check_date_format

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'

t = Twitter(consumer_key, consumer_secret)


def get_tweets_text(fields):
    type = fields.pop('type', 'json')
    keys = fields.pop('output', TWEET_KEYS)
    tweets = t.search_tweets_text(fields.pop('len', 10), fields, keys)

    jsondata=json.dumps(tweets, default=str, indent=4)
    if(type=="url"):return  upload(jsondata)
    return jsondata if type == 'json' else DataFrame(tweets).to_csv(index=False)


def get_comments(fields):
    name = fields.pop('username', '')
    tweet_id = fields.pop('id', '')
    count = fields.pop('count', 10)
    keys = fields.pop('output', REPLIES_KEYS)
    type = fields.pop('type', 'csv')
    replies = t.get_replies(name, tweet_id, keys, count=count)
    return json.dumps(replies, default=str, indent=4) if type == 'json' else DataFrame(replies).to_csv(index=False)


def get_tweets_video(fields):
    # if not check_date_format(fields['since']):
    #     fields.pop('since', '')
    # if not check_date_format(fields['until']):
    #     fields.pop('until', '')
    type = fields.pop('type', 'json')
    keys = fields.pop('output', TWEET_VIDEOS_KEYS)
    videos = t.search_tweets_videos(fields.pop('len', 10), fields, keys)
    if type == 'json':
        return videos
    elif type == 'zip':
        return json.dumps([tt['extended_entities.media.video_info.variants.url'][0] for tt in videos])
    else:
        return DataFrame(videos).to_csv(index=False)

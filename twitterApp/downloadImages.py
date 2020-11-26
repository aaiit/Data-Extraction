import os
import tweepy

consumer_key = "UFkzPnRg6teYYVpopicJlHu2L"
consumer_secret = "CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P"

callback_url = 'oob'
authen = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_url)
redirect_url = authen.get_authorization_url()

authen = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(authen, timeout=11)


def downloadImages(fields):
    type = fields['type']
    media_files = []
    count=fields.pop('len',20)
    for status in tweepy.Cursor(api.search,**fields).items():
        media = status.entities.get('media', [])
        if len(media) > 0:
            media_files.append(media[0]['media_url'])
            if count == len(media_files):
                break
    return media_files


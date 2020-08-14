import json
from Twitter.Keys import *
from Twitter.TwitterApi import Twitter

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'

t = Twitter(consumer_key, consumer_secret)
# keys=['id_str','user.id','retweet_count','full_text','entities.media','entities.urls']
# tweet=tweets[0]['id_str']
# print(tweets[0]['retweet_count'],tweet)
# user=t.get_user(tweets[0]['user.id'],['screen_name'])['screen_name']
# print(user)
# replies=t.get_replies(user,tweet,count=100,keys=['favorite_count'],max_explored=1000)
# trends=t.get_closest_locations_with_trends_to('34.021992','-6.837620')
# trends=t.get_trends_in(1)
# trends=trends[0]['trends']
# trends=t.get_available_places_with_trends()
# print(json.dumps(sorted(trends,key=lambda x: x['tweet_volume'] if x['tweet_volume'] else 1,reverse=True),indent=4))

def test(fields):
	# fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular'}
	tweets = t.search_tweets_images(fields["len"], fields, TWEET_IMAGES_KEYS)
	return json.dumps(tweets, default=str, indent=4)


import tweepy

from Twitter.HelperFunctions import *


class Twitter:

    def __init__(self, consumer_key, consumer_secret, timeout=20):
        self.api = tweepy.API(tweepy.OAuthHandler(consumer_key, consumer_secret)
                              , retry_count=2, retry_delay=10, wait_on_rate_limit=False, timeout=timeout)
        if not self.api:
            raise ReferenceError('cannot build the object check your internet or the consumer keys!!')

    def search_tweets(self, count, fields: dict, keys=None):
        '''
        api: tweepy api after requesting the Beacon.
        fields: tweepy search fields: q=,lang=,geocode=,result_type=,since_id=,max_id=,until=,. !!! q is required.
        count: how many tweets to return.
        keys: json keys to return.
        '''
        fields['q'] += ' -filter:retweets'
        results = list(tweepy.Cursor(self.api.search, **fields, trim_user=False, include_entities=True,
                                     tweet_mode='extended').items(count))
        if not keys:
            return [tweet._json for tweet in results]
        return [{k: res[1] for k in keys for res in get_attr(tweet, k) if res[0]} for tweet in results]

    def search_tweets_text(self, count, fields: dict, keys=None):
        '''
        api: tweepy api after requesting the Beacon.
        fields: tweepy search fields: q=,lang=,geocode=,result_type=,since_id=,max_id=,until=,. !!! q is required.
        count: how many tweets to return.
        keys: json keys to return.
        '''
        fields['q'] += ' -filter:retweets -filter:media'
        results = list(tweepy.Cursor(self.api.search, **fields, trim_user=False, include_entities=True,
                                     tweet_mode='extended').items(count))
        if not keys:
            return [tweet._json for tweet in results]
        return [{k: res[1] for k in keys for res in get_attr(tweet, k) if res[0]} for tweet in results]

    def search_tweets_images(self, count, fields: dict, keys=None):
        '''
        api: tweepy api after requesting the Beacon.
        fields: tweepy search fields: q=,lang=,geocode=lat,long,radius,result_type=,since_id=,max_id=,until=,. !!! q is required.
        count: how many tweets to return.
        keys: json keys to return.
        '''
        fields['q'] += ' -filter:retweets filter:twimg filter:images'
        results = list(tweepy.Cursor(self.api.search, **fields, trim_user=False, include_entities=True,
                                     tweet_mode='extended').items(count))
        if not keys:
            return [tweet._json for tweet in results]
        return [{k: res[1] for k in keys for res in get_attr(tweet, k) if res[0]} for tweet in results]

    def search_tweets_videos(self, count, fields: dict, keys=None):
        '''
        fields: tweepy search fields: q=,lang=,geocode=,result_type=,since_id=,max_id=,until=,. !!! q is required.
        count: how many tweets to return.
        keys: json keys to return.
        '''
        fields['q'] += ' -filter:retweets filter:native_video -filter:images -filter:twimg'
        results = list(tweepy.Cursor(self.api.search, **fields, trim_user=False, include_entities=True,
                                     tweet_mode='extended').items(count))
        if not keys:
            return [tweet._json for tweet in results]
        return [{k: res[1] for k in keys for res in get_attr(tweet, k) if res[0]} for tweet in results]

    def get_replies(self, user_screen_name, tweet_id, keys=None, query='', count=10):
        '''
        replies == comments.
        user_screen_name: username of the one who published that tweet.
        '''
        replies = []
        for reply in tweepy.Cursor(self.api.search, q=f'to:{user_screen_name}', since_id=tweet_id,
                                   trim_user=True, tweet_mode='extended', result_type='mixed').items():
            # check if this tweet is a reply     and     it's a reply to 'tweet_id'      and       it's related to the 'query'.
            if hasattr(reply,
                       'in_reply_to_status_id') and reply.in_reply_to_status_id == int(
                tweet_id) and query in reply.full_text:
                replies.append(reply)
                # After getting 'count' tweets related to 'query', return them
                if len(replies) >= count:
                    break
        if not keys:
            return [t._json for t in replies]
        return [{k: res[1] for k in keys for res in get_attr(tweet, k) if res[0]} for tweet in replies]

    def get_user_timeline(self, user, count, keys, fields={}):
        '''
        Get the user own tweets. it excluded retweets.
        fields: since_id=,max_id=
        '''
        results = [t for t in tweepy.Cursor(self.api.user_timeline,
                                            **fields,
                                            id=user,
                                            include_entities=True,
                                            tweet_mode='extended',
                                            trim_user=True,
                                            exclude_replies=True,
                                            ).items(count)]
        return [{k: res[1] for k in keys for res in get_attr(tweet, k) if res[0]} for tweet in results]

    def get_user(self, user_id, keys):
        # Get detailed informations about user_id.
        infos = self.api.get_user(user_id=user_id)
        return {k: res[1] for k in keys for res in get_attr(infos, k) if res[0]}

    def get_retweeters(self, tweet_id, count):
        # return the id of users retweeting tweet_id
        return [t for t in tweepy.Cursor(self.api.retweeters, id=tweet_id, stringify_ids=True).items(count)]

    def get_relationship(self, id1, id2, keys):
        # is id1 following id2 and vice versa.
        relation = self.api.show_friendship(source_id=id1, target_id=id2)[0]
        return {k: res[1] for k in keys for res in get_attr(relation, k) if res[0]}

    def get_user_favorites(self, user, count, keys):
        # Tweets that the user favorited (liked)
        tweets = list(tweepy.Cursor(self.api.favorites, id=user).items(count))
        return [{k: res[1] for k in keys for res in get_attr(tweet, k) if res[0]} for tweet in tweets]

    # Trends
    def get_available_places_with_trends(self):
        return self.api.trends_available()

    def get_trends_in(self, loc):
        return self.api.trends_place(loc)

    def get_closest_places_with_trends_to(self, lat, long):
        return self.api.trends_closest(lat, long)

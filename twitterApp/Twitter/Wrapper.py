from copy import deepcopy

from fire import uploadimage
from twitterApp.Twitter.DataStructures.GraphBase import GraphBase
from twitterApp.Twitter.DataStructures.TableBase import TableBase
from twitterApp.Twitter.TwitterApi.TwitterApi import Twitter
from twitterApp.Twitter.TwitterApi.Keys import *
from twitterApp.Twitter.Plot import plot_unweighted_graph as pug

consumer_key = 'UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret = 'CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'


class Wrapper(Twitter):
    # TWEET_TABLE='tweet_table.csv'
    # USER_TABLE='user_table.csv'
    QUERIES_TWEETS = 'queries_tweets'
    TWEETS_HASTHTAGS = 'tweets_hashtags'
    TWEETS_RETWEETERS = 'tweets_retweeters'
    TWEETS_MENTIONED_USERS = 'tweets_mentionned_users'
    TWEETS_LINKS = 'tweets_links'
    TWEETS_RESPONDENTS = 'tweets_respondents'
    USER_USER = 'user_user'
    USERS_FAVORITES = 'users_favorites'

    def __init__(self, consumer_key, consumer_secret, timeout=20):
        super(Wrapper, self).__init__(consumer_key, consumer_secret, timeout)
        self.graph = GraphBase()
        self.table = TableBase()

    def search_tweets(self, count, fields: dict, replies=None, **kwargs):
        '''
        Todo
        '''
        keys = TWEET_KEYS
        query = deepcopy(fields['q'])
        tweets = super(Wrapper, self).search_tweets(count, fields, replies, keys)
        self.save_tweets(tweets, query=query)
        return tweets

    def search_tweets_text(self, count, fields: dict, replies=None, **kwargs):
        '''
        Todo
        :param **kwargs:
        '''
        keys = TWEET_KEYS
        query = deepcopy(fields['q'])
        tweets = super(Wrapper, self).search_tweets_text(count, fields, replies, keys)
        self.save_tweets(tweets, query=query)
        return tweets

    def search_tweets_images(self, count, fields: dict, replies=None, **kwargs):
        '''
        Todo
        :param **kwargs:
        '''
        keys = TWEET_IMAGE_KEYS
        query = deepcopy(fields['q'])
        tweets = super(Wrapper, self).search_tweets_images(count, fields, replies, keys)
        self.save_tweets(tweets, query=query)
        return tweets

    def search_tweets_videos(self, count, fields: dict, replies=None, **kwargs):
        '''
        Todo
        '''
        keys = TWEET_VIDEO_KEYS
        query = deepcopy(fields['q'])
        tweets = super(Wrapper, self).search_tweets_videos(count, fields, replies, keys)
        self.save_tweets(tweets, query=query)
        return tweets

    def get_user_favorites(self, user, count, **kwargs):
        keys = TWEET_KEYS
        tweets = super(Wrapper, self).get_user_favorites(user, count, keys)
        self.save_tweets(tweets, user_favorite=user)
        return tweets

    def get_replies(self, user_screen_name, tweet_id, query='', count=10, max_explored=100, fields={}, **kwargs):
        '''
        Todo:
        :param **kwargs:
        '''
        keys = REPLY_KEYS
        replies = super(Wrapper, self).get_replies(user_screen_name, tweet_id, keys=keys, query=query, count=count,
                                                   max_explored=max_explored, fields=fields)

        self.save_tweets(replies, tweet_id_reply=tweet_id)
        return replies

    def get_retweeters(self, tweet_id, count):
        # return the id of users retweeting tweet_id
        users = super(Wrapper, self).get_retweeters(tweet_id, count)
        self.save_retweeters(users, tweet_id)
        return users

    def construct_friendships(self):
        users = list(self.table.users.users.keys())
        for i in range(len(users)):
            for j in range(i + 1, len(users)):
                rltship = super().get_relationship(users[i], users[j], FRIENDSHIP_KEYS)
                if rltship['following']:
                    self.graph.user_user.add_node(users[j])
                    self.graph.user_user.add_edge(users[j], users[i])
                if rltship['followed_by']:
                    self.graph.user_user.add_node(users[i])
                    self.graph.user_user.add_edge(users[i], users[j])

    def save_tweets(self, tweets, query=None, user_favorite=None, tweet_id_reply=None):
        ' TODO: From time to time update informations about users and tweets in the table. '

        ######## Here save the informations about the tweets/replies.
        for tweet in tweets:
            #### Skip this tweet if it has already been processed.
            if tweet['id_str'] in self.table.tweets:
                continue
            # Third step: save tweet_hashtags tree.
            if 'entities.hashtags.text' in tweet:
                self.graph.tweet_hashtag.add_list_edges(tweet['id_str'], [t for t in tweet['entities.hashtags.text']])

            # Fourth step: save tweet_mentioned tree.
            if 'entities.user_mentions.id_str' in tweet:
                self.graph.tweet_mentioned.add_list_edges(tweet['id_str'],
                                                          [t for t in tweet['entities.user_mentions.id_str']])

            # Fifth step: save tweet_link tree.
            if 'entities.urls.expanded_url' in tweet:
                self.graph.tweet_link.add_list_edges(tweet['id_str'], [t for t in tweet['entities.urls.expanded_url']])

        # First step: save the tweets and users in the  table.
        for tweet in tweets:
            # Save the tweet.
            #### Skip this tweet.
            if tweet['id_str'] in self.table.tweets:
                continue
            self.table.tweets.add_row(tweet['id_str'], tweet)
            if tweet['user.id_str'] in self.table.users:
                continue
            keys = USER_KEYS
            user = super(Wrapper, self).get_user(tweet['user.id_str'], keys)
            # Save the tweet creator.
            self.table.users.add_row(user['id_str'], user)

        if query:
            # Second step: save the query_tweet tree.
            self.graph.query_tweet.add_list_edges(query, [tweet['id_str'] for tweet in tweets])
        elif user_favorite:
            # Second step: save the user_favorite tweets tree.
            self.graph.user_favorite.add_list_edges(user_favorite, [tweet['id_str'] for tweet in tweets])
        elif tweet_id_reply:
            # Second step: save the tweet_respondent tree.
            self.graph.tweet_respondent.add_list_edges(tweet_id_reply,
                                                       [tweet['user.id_str'] for tweet in tweets],
                                                       [tweet['id_str'] for tweet in tweets])

    def save_retweeters(self, users_ids, tweet_id):
        # tweet_id is supposed to be already in the data base.
        for user in users_ids:
            if user in self.table.users:
                continue
            keys = USER_KEYS
            user = super(Wrapper, self).get_user(user, keys)
            # Save the tweet creator.
            self.table.users.add_row(user['id_str'], user)

        # Now save the tweet_retweeter tree.
        self.graph.tweet_retweeter.add_list_edges(tweet_id, users_ids)

    def save_data(self):
        self.graph.save_graph()
        self.table.save_table()

    def load_data(self):
        self.graph.load_graph()
        self.table.load_table()

    def return_all_data(self):
        # Get user favorited tweets.
        for user in self.table.users.table:
            self.get_user_favorites(user, 30)
        # Get tweet retweeters and replies
        for tweet in self.table.tweets.table:
            self.get_retweeters(tweet, 100)
            self.get_replies(self.table.users.get_row(tweet['user.id_str'])['screen_name'], tweet, count=10)
        # TODO: this  may take a very long time, so it is ignored for now.
        # self.construct_friendships()

        results = {'table1': self.table.users.table, 'table2': self.table.tweets.table}
        self.construct_friendships()
        # pug(self.graph.user_user.graph, self.USER_USER)
        pug(self.graph.user_favorite.graph, self.USERS_FAVORITES)
        pug(self.graph.query_tweet.graph, self.QUERIES_TWEETS)
        pug(self.graph.tweet_hashtag.graph, self.TWEETS_HASTHTAGS)
        pug(self.graph.tweet_retweeter.graph, self.TWEETS_RETWEETERS)
        pug(self.graph.tweet_link.graph, self.TWEETS_LINKS)
        pug(self.graph.tweet_mentioned.graph, self.TWEETS_MENTIONED_USERS)
        pug(self.graph.tweet_respondent.graph, self.TWEETS_RESPONDENTS)
        # uploadimage(self.USER_USER + '.gv.png'),
        results['graph'] = [uploadimage(self.USERS_FAVORITES + '.gv.png'),
                            uploadimage(self.QUERIES_TWEETS + '.gv.png'),
                            uploadimage(self.TWEETS_HASTHTAGS + '.gv.png'),
                            uploadimage(self.TWEETS_RETWEETERS + '.gv.png'),
                            uploadimage(self.TWEETS_LINKS + '.gv.png'),
                            uploadimage(self.TWEETS_MENTIONED_USERS + '.gv.png'),
                            uploadimage(self.TWEETS_RESPONDENTS + '.gv.png')]
        return results


twitter_wrapper = Wrapper(consumer_key, consumer_secret)


def search_for_tweets(fields):
    twitter_wrapper.search_tweets(int(fields.pop('count', 10)), fields)
    return twitter_wrapper.return_all_data()

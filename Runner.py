from termcolor import cprint

import pickle


from twitterApp.Twitter.Wrapper import Wrapper
import pandas as pd
import json
from twitterApp.Twitter.Plot import plot_unweighted_graph as plot


consumer_key='UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret='CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'
twitter=Wrapper(consumer_key,consumer_secret)


while True:
    fields={'q':input("q:"),'result_type':'popular','lang':'en'}
    tweets=twitter.search_tweets(20,fields)
    print(len(tweets))
    favs=twitter.get_user_favorites('1155475035123081217',10)
    print(len(favs))
    # reps=twitter.get_replies('georgegalloway','1295061069870829575',max_explored=1000)
    # print(len(reps))
    reters=twitter.get_retweeters('1295061069870829575',10)
    print(len(reters))
    plot(twitter.graph.tweet_hashtag.graph,'tweets_hashtags')

    pickle.dump(twitter, open("cocooooo.best","wb"))
    twitter = pickle.load(open("cocooooo.best","rb"))

   

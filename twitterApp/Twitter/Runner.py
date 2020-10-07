from termcolor import cprint

'''
TODO: Put static code here.
'''
from twitterApp.Twitter.Wrapper import Wrapper, search_for_tweets
import pandas as pd
import json
from twitterApp.Twitter.Plot import plot_unweighted_graph as plot


consumer_key='UFkzPnRg6teYYVpopicJlHu2L'
consumer_secret='CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P'
twitter=Wrapper(consumer_key,consumer_secret)
fields={'q':'trump biden','result_type':'recent','lang':'en'}


tweets=twitter.search_tweets(10,fields)
print(len(tweets))
print(json.dumps(twitter.return_all_data(),indent=3,default=str))


# favs=twitter.get_user_favorites('1155475035123081217',10)
# print(len(favs))
# # reps=twitter.get_replies('georgegalloway','1295061069870829575',max_explored=1000)
# # print(len(reps))
# reters=twitter.get_retweeters('1295061069870829575',10)
# print(len(reters))


# plot(twitter.graph.tweet_hashtag.graph, 'tweets_hashtags.svg')

#
i=0
while i>0:
    i+=1
    '''
    TODO: Put dynamic code here.
    '''
    cprint(f'IN [{i}]: ',color='blue',end='')
    stmnt = input()
    if stmnt == '/*-':
        break
    cprint(f'OUT [{i}]: ', 'yellow',end='')
    try:
        exec(stmnt)
        print()
    except Exception as err:
        cprint(err,color='red')

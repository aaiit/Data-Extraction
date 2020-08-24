import pickle as pk

from twitterApp.Twitter.DataStructures.Graphs.Unweighted_Bipartite_Graph import Unweighted_Bipartite_Graph
from twitterApp.Twitter.DataStructures.Graphs.Unweighted_Ordered_Graph import Unweighted_Ordered_Graph
from twitterApp.Twitter.DataStructures.Graphs.Weighted_Bipartite_Graph import Weighted_Bipartite_Graph


class GraphBase:
    FILE_NAME = 'TTT'

    def __init__(self):
        ########   LEVEL 0
        self.query_tweet = Unweighted_Bipartite_Graph()
        self.tweet_hashtag = Unweighted_Bipartite_Graph()
        self.tweet_mentioned = Unweighted_Bipartite_Graph()
        self.tweet_retweeter = Unweighted_Bipartite_Graph()
        self.tweet_link = Unweighted_Bipartite_Graph()
        self.user_favorite = Unweighted_Bipartite_Graph()
        self.user_user = Unweighted_Ordered_Graph()
        self.tweet_respondent = Weighted_Bipartite_Graph()

    def save_graph(self):
        pk.dump(self, open(self.FILE_NAME, 'wb'))

    def load_graph(self):
        self.__dict__ = pk.load(open(self.FILE_NAME, 'rb')).__dict__

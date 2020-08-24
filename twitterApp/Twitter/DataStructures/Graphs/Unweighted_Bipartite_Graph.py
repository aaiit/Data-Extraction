import json


class Unweighted_Bipartite_Graph:
    '''
    Level 0:
    Queries-Tweets,
     Tweets-Hashtags,
      Tweets-Retweet_Users,
       Tweets-Favorite_Users,
        Tweets-Mentioned_Users,
         Tweets-Links,

    Level 1:
    HashTags-Trends

    '''

    def __init__(self):
        # The graph is dict=>list
        self.graph = {}

    def add_node(self, node):
        if node not in self:
            self.graph[node] = set()

    def add_edge(self, start, end):
        if start in self:
            self.graph[start].add(end)
        else:
            raise AttributeError('start doesn\'t exist in the graph')

    def add_list_edges(self, start, end: list):
        self.add_node(start)
        for t in end:
            self.add_edge(start, t)

    def __str__(self):
        return json.dumps(self.graph, indent=3, default=str)

    def __contains__(self, node):
        return node in self.graph

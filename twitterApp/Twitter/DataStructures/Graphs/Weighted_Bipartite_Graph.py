import json


class Weighted_Bipartite_Graph:
    '''
    Level 0:
    Tweets-Reply_Users

    Level 1:
    Users-Places,
     Users-HashTags,
      Users-Trends,
       Query-CommonWords.

    '''

    def __init__(self):
        # The graph is dict=>dict=>weight
        self.graph = {}

    def add_node(self, node):
        if node not in self:
            self.graph[node] = {}

    def add_edge(self, start, end, weight):
        if start in self:
            self.graph[start][end] = weight
        else:
            raise AttributeError('start doesn\'t exist in the graph')

    def add_list_edges(self, start, end: list, weights: list):
        self.add_node(start)
        for t, weight in zip(end, weights):
            self.add_edge(start, t, weight)

    def __str__(self):
        return json.dumps(self.graph, indent=3, default=str)

    def __contains__(self, node):
        return node in self.graph

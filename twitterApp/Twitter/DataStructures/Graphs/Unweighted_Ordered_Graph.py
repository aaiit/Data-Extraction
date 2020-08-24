import json


class Unweighted_Ordered_Graph:
    '''
    Level 0:
    Users - Users(following)


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

    def __str__(self):
        return json.dumps(self.graph, indent=3, default=str)

    def __contains__(self, node):
        return node in self.graph

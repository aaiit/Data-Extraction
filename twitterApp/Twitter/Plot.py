import networkx as nx
import matplotlib.pyplot as plt

def plot_unweighted_graph(graph, filename):
    if not isinstance(graph, dict):
        return
    g = nx.Graph()
    for start in graph:
        g.add_node(start)
        for end in graph[start]:
            g.add_edge(start.lower(),end,color='r')
            g.add_node(end)
    plt.figure(1, figsize=(g.number_of_nodes()/2, g.number_of_nodes()/2))
    nx.draw_spring(g,with_labels=True,node_size=200,font_size=6,node_color='r')
    plt.savefig(filename,format='svg')
    plt.show()

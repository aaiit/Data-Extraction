

def plot_unweighted_graph(graph, filename):
    import networkx as nx
    import matplotlib.pyplot as plt

    if not isinstance(graph, dict):
        return
    g = nx.Graph()
    for start in graph:
        g.add_node(start)
        for end in graph[start]:
            g.add_edge(start.lower(),end)
            g.add_node(end)
    plt.figure(1, figsize=(g.number_of_nodes()/2+1, g.number_of_nodes()/2+1))
    nx.draw_spring(g,with_labels=True,node_size=500,font_size=2)
    plt.savefig(filename,format='svg')
    plt.show()

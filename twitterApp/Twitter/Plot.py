from graphviz import Digraph, Graph


def plot_unweighted_graph(graph, filename):
    if not isinstance(graph, dict):
        return
    g = Graph(format='png', filename=filename + '.png')
    for start in graph:
        g.attr('node', color='red', shape='rarrow')
        g.node(start, label=start)
        for end in graph[start]:
            g.attr('node', color='blue', shape='egg')
            g.node(end, label=end)
            g.edge(start, end, constraint='false')
    g.render(filename=filename + '.gv', view=True)

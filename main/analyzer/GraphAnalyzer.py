import networkx as nx


class GraphAnalyzer:
    def __init__(self, graphs):
        self.__graphs = graphs
        self.early_age_graph = self.__convert_multi_graph_to_graph(graphs['early_age'])
        self.middle_age_graph = self.__convert_multi_graph_to_graph(graphs['middle_age'])
        self.elder_age_graph = self.__convert_multi_graph_to_graph(graphs['elder_age'])

    def __convert_multi_graph_to_graph(self, multi_graph):
        graph = nx.Graph()
        for u, v, data in multi_graph.edges(data=True):
            w = data['weight'] if 'weight' in data else 1.0
            if graph.has_edge(u, v):
                graph[u][v]['weight'] += w
            else:
                graph.add_edge(u, v, weight=w)
        return graph

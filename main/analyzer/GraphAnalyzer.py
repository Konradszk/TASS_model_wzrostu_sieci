import networkx as nx


class GraphAnalyzer:
    def __init__(self, graphs):
        self.__graphs = graphs
        self.early_age_graph = nx.MultiGraph(graphs['early_age'])
        self.middle_age_graph = nx.MultiGraph(graphs['middle_age'])
        self.elder_age_graph = nx.MultiGraph(graphs['elder_age'])

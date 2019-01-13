import networkx as nx
import collections
import matplotlib.pyplot as plt


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

        print(nx.degree_assortativity_coefficient(graph))
        print(nx.transitivity(graph))
        #print(nx.clustering(graph))
		
        G = graph
        G.remove_nodes_from(list(nx.isolates(G)))
        pos = nx.layout.spring_layout(G)

        node_sizes = [3 + 10 * i for i in range(len(G))]
        M = G.number_of_edges()

        nodes = nx.draw_networkx_nodes(G, pos, node_size=20)
        edges = nx.draw_networkx_edges(G, pos,arrows=True, arrowstyle='->',
                               arrowsize=10, edge_color='black',
                               width=2)
        
        degree_sequence=sorted([d for n, d in G.degree()], reverse=True)
        degreeCount= collections.Counter(degree_sequence)
        deg, cnt = zip(*degreeCount.items())

        fig, ax = plt.subplots()
        plt.bar(deg, cnt, width=0.80, color='b')

        plt.title("Degree Histogram")
        plt.ylabel("Count")
        plt.xlabel("Degree")
        plt.show()
		
		
		
        return graph

		
		
        
        
        
        
		
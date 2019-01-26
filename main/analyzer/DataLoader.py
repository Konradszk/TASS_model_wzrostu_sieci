import sys
import networkx as nx


class DataLoader:
    def __init__(self, db):
        self.__db = db
        self.__collection_list = None
        self.__get_sorted_collections()
        self.article_data = {}
        self.get_data_from_db()
        self.graphs = {}

    def __get_sorted_collections(self):
        self.__collection_list = self.__db.list_collection_names()
        self.__collection_list.sort()

    def get_data_from_db(self):
        if len(self.__collection_list) < 3:
            print('WebScraping has not been finished. Too less data.')
            sys.exit()
        if len(self.article_data) == 0:
            self.article_data['early_age'] = self.__db[self.__collection_list[0]].find_one()
            self.article_data['middle_age'] = self.__db[self.__collection_list[1]].find_one()
            self.article_data['elder_age'] = self.__db[self.__collection_list[2]].find_one()
            self.__remove_id()
        return self.article_data

    def __remove_id(self):
        for date in self.article_data.keys():
            self.article_data[date].pop('_id')

    def get_graphs(self):
        if len(self.graphs) == 0:
            self.__create_graphs()
        return self.graphs

    def __create_graphs(self):
        for data in self.article_data.keys():
            self.__create_graph(name=data)

    def __create_graph(self, name):
        graph = nx.MultiGraph()
        for comment in self.article_data[name].keys():
            author = self.article_data[name][comment]['name']
            graph.add_node(author)
            for replay in self.article_data[name][comment]['replay']:
                graph.add_node(replay)
                graph.add_edge(author, replay, weight=1.0)
        self.graphs[name] = graph

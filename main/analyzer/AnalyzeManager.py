from main.analyzer.DataLoader import DataLoader
from main.analyzer.GraphAnalyzer import GraphAnalyzer


class AnalyzeManager:
    def __init__(self, db):
        self.__data_loader = DataLoader(db)
        self.__graph_analyzer = GraphAnalyzer(self.__data_loader.get_graphs())
        GraphAnalyzer.analyze(self.__graph_analyzer.early_age_graph)
        GraphAnalyzer.analyze(self.__graph_analyzer.middle_age_graph)
        GraphAnalyzer.analyze(self.__graph_analyzer.elder_age_graph)

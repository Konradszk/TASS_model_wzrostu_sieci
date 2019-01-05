class DataLoader:
    def __init__(self, db):
        self.__db = db

    def get_graphs(self):
        return None

    def get_data_from_db(self):
        print(self.__db.list_collection_names())

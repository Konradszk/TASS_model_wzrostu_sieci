import pymongo


class Driver:
    def __init__(self, url):
        self.__url = url
        self.__db_client = None
        self.db = None
        self.__connect()

    def __connect(self):
        self.__db_client = pymongo.MongoClient(self.__url)
        self.db = self.__db_client['TASS']
        if 'TASS' in self.__db_client.list_database_names():
            print('DB cConnection property has been initialized')

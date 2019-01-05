import pymongo


class Driver:
    def __init__(self, url, database_sufix):
        self.__url = url
        self.__db_client = None
        self.db = None
        self.__connect(database_sufix)

    def __connect(self, database_sufix):
        self.__db_client = pymongo.MongoClient(self.__url)
        db_name = 'TASS_' + database_sufix
        self.db = self.__db_client[db_name]
        if db_name in self.__db_client.list_database_names():
            print('DB cConnection property has been initialized')

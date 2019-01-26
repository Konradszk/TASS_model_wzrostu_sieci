import datetime


class DownloadSaver:
    def __init__(self, db):
        self.__db = db

    def save_data_comment(self, json_data):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        collection = self.__db[date]
        collection.insert_one(json_data)

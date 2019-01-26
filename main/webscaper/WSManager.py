from main.webscaper.CommentDownloader import CommentDownloader
from main.webscaper.DownloadSaver import DownloadSaver


class WSManager:
    def __init__(self, db, url):
        self.__ds = DownloadSaver(db)
        self.__cd = CommentDownloader(url)
        self.comment_json = self.__cd.get_comment_data()
        self.__ds.save_data_comment(self.comment_json)

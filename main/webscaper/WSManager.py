from main.webscaper.CommentDownloader import CommentDownloader
from main.webscaper.DownloadSaver import DownloadSaver


class WSManager:
    def __init__(self, db, url):
        self.__ds = DownloadSaver(db)
        self.__cd = CommentDownloader(url)

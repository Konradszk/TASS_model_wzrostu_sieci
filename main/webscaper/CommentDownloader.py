import requests


class CommentDownloader:
    def __init__(self, url):
        self.__url = url
        self.page = self.__get_page()

    def __get_page(self):
        file = requests.get(self.__url)
        if file.status_code != 200:
            print('Cannot get page: ', self.__url)
            return
        return file.content

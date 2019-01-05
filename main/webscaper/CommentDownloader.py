import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CommentDownloader:
    def __init__(self, url):
        self.__url = url
        self.page = self.__get_page()
        self.soup = None

    def __get_page(self):
        self.__prepare_web_page()
        return ''

    def __prepare_web_page(self):
        browser = webdriver.Chrome()
        browser.get(self.__url)
        browser.implicitly_wait(10)
        browser.find_element_by_class_name('rodo-popup-agree').click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'comments4-1'))
        )
        self.__expand_all_comment(browser)
        element = browser.find_element_by_class_name('forum__list')
        self.get_comments(element.get_attribute('innerHTML'))
        time.sleep(10)
        # dodać przewijanie stron
        browser.quit()

    def __expand_all_comment(self, browser):
        show_attr = browser.find_elements_by_class_name('forum__comment-replies-show')
        for attr in show_attr:
            attr.click()

    def get_comments(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        comment_div = self.soup.find_all(class_='forum__comment', recursive=False)
        comments = {}
        for comment in comment_div:
            data = {'name': comment.find(class_='forum__comment-author-name').text,
                    'date': comment.find(class_='forum__comment-author-date').text,
                    'voteup': comment.find(class_='forum__comment-action--voteup').text,
                    'votedown': comment.find(class_='forum__comment-action--votedown').text}
            comments[data['name']] = data

        json_comments = json.dumps(comments)
        print(json_comments)
        print(len(comment_div))
        # trzeba dodać mechanizm łapania zagnieżdzeń

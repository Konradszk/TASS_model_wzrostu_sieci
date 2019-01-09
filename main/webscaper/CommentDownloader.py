import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CommentDownloader:
    def __init__(self, url):
        self.__url = url
        self.comment_data = {}
        self.__soup = None

    def get_comment_data(self):
        browser = webdriver.Chrome()
        browser.get(self.__url)
        time.sleep(10)
        browser.implicitly_wait(40)
        browser.find_element_by_class_name('rodo-popup-agree').click()
        is_next_page = True
        while is_next_page:
            self.__prepare_web_page(browser)
            try:
                next_button = WebDriverWait(browser, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "forum__pagination-next--active"))
                )
                next_button.click()
                time.sleep(1)
            except TimeoutException:
                is_next_page = False
        browser.quit()
        return self.comment_data

    def __prepare_web_page(self, browser):
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'comments4-1'))
        )
        self.__expand_all_comment(browser)
        element = browser.find_elements_by_class_name('forum__list')
        self.__get_comments(element[-1].get_attribute('innerHTML'))

    def __expand_all_comment(self, browser):
        actions = ActionChains(browser)
        show_attr = browser.find_elements_by_class_name('forum__comment-replies-show')
        for attr in show_attr:
            actions.move_to_element(show_attr)
            try:
                attr.click()
            except WebDriverException:
                print('cannot expand')
            time.sleep(1)

    def __get_comments(self, html):
        self.__soup = BeautifulSoup(html, 'html.parser')
        comment_div = self.__soup.find_all(class_='forum__comment', recursive=False)
        comments = {}
        for comment in comment_div:
            data = {'name': comment.find(class_='forum__comment-author-name').text.replace('.', ''),
                    'replay': []
                    }
            replays = comment.find_all(class_='forum__comment', recursive=True)
            for replay in replays:
                replay_author = replay.find(class_='forum__comment-author-name').text.replace('.', '')
                data['replay'].append(replay_author)
            comments[data['name']] = data
        self.comment_data.update(comments)
        print(len(self.comment_data))

from main.db_driver.driver import Driver
from main.webscaper.WSManager import WSManager


def main(url):
    db_driver = Driver('mongodb://localhost:27017/')
    ws_manager = WSManager(db_driver, url)

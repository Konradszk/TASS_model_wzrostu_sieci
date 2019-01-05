from main.analyzer.AnalyzeManager import AnalyzeManager
from main.db_driver.driver import Driver
from main.webscaper.WSManager import WSManager


def main(url, database_sufix):
    db_driver = Driver('mongodb://localhost:27017/', database_sufix)
    WSManager(db_driver.db, url)
    AnalyzeManager(db_driver.db)

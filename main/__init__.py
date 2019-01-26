from main.analyzer.AnalyzeManager import AnalyzeManager
from main.db_driver.driver import Driver
from main.webscaper.WSManager import WSManager


def main(url, database_suffix, should_ws, should_analyze):
    db_driver = Driver('mongodb://localhost:27017/', database_suffix)
    if should_ws:
        WSManager(db_driver.db, url)
    if should_analyze:
        AnalyzeManager(db_driver.db)

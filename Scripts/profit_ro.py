import helpers
from datetime import date

def get_latest_news():
    source = helpers.get_source("https://www.profit.ro/toate")
    news = {}
    newsID = 1

    


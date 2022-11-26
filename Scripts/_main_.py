import news_retrieval_module as rm
import time
import requests
import helpers


def main():
    news_retrieval_module = rm.NewsRetrievalModule()
    pause_len = 300

    while True:

        news_retrieval_module.get_latest_news_ziarul_financiar()
        news_retrieval_module.get_latest_news_wall_street_ro()
        news_retrieval_module.get_latest_news_profit_ro()

        helpers.pause(pause_len)

if __name__ == "__main__":
    main()

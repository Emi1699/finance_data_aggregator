import retrieval_module as rm
import time
import requests
import helpers


def main():
    retrieval_module = rm.RetrievalModule()
    pause_len = 300

    while True:

        retrieval_module.get_latest_news_ziarul_financiar()
        retrieval_module.get_latest_news_wall_street_ro()
        retrieval_module.get_latest_news_profit_ro()

        helpers.pause(pause_len)

if __name__ == "__main__":
    main()


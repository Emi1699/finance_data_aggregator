import retrieval_module as rm
import time

def main():
    retrieval_module = rm.RetrievalModule()

    while True:

        retrieval_module.get_latest_news_ziarul_financiar()
        retrieval_module.get_latest_news_wall_street_ro()
        retrieval_module.get_latest_news_profit_ro()

        print("\n\nSLEEPING 5 MINUTES...\n\n")
        time.sleep(300)

if __name__ == "__main__":
    main()


import retrieval_module as rm
import time
from progress.bar import Bar

def main():
    retrieval_module = rm.RetrievalModule()

    while True:

        retrieval_module.get_latest_news_ziarul_financiar()
        retrieval_module.get_latest_news_wall_street_ro()
        retrieval_module.get_latest_news_profit_ro()

        print("\n\nSLEEPING 5 MINUTES...\n\n")
        bar = Bar('Processing', max=300)
        for i in range(300):
            time.sleep(1)
            bar.next()
        bar.finish()

if __name__ == "__main__":
    main()


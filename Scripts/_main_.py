import retrieval_module as rm
import time
from progress.bar import Bar

def main():
    retrieval_module = rm.RetrievalModule()
    pause = 300

    while True:

        retrieval_module.get_latest_news_ziarul_financiar()
        retrieval_module.get_latest_news_wall_street_ro()
        retrieval_module.get_latest_news_profit_ro()

        print()
        bar = Bar(f"SLEEPING FOR {pause} SECONDS ({pause/60} MINUTES)...", max=pause)
        for i in range(pause):
            time.sleep(1)
            bar.next()
        bar.finish()

if __name__ == "__main__":
    main()


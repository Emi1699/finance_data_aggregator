import retrieval_module as rm

def main():
    retrieval_module = rm.RetrievalModule()

    retrieval_module.get_latest_news_ziarul_financiar()
    retrieval_module.get_latest_news_wall_street_ro()
    retrieval_module.get_latest_news_profit_ro()

if __name__ == "__main__":
    main()


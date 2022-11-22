import helpers
import requests
import re
import file_system

def sort_news_by_tickers():
    with open(file_system.get_path_to_file("ziarul_financiar", __file__, "nbs"), 'r', encoding="utf-8") as file:
        for line in file:
            link_to_source = helpers.get_link_from_string(line)[0:-2]
            source_txt = requests.get(link_to_source).text # get page's content (including the text of the news)
            
            if tickers_in_news(["societatea energetica electrica", "electrica s.a.", "electrica sa"], source_txt):
                file_system.write_to_file("electrica", link_to_source, "nbt") # 'nbt' = 'news by ticker'
            if tickers_in_news(["fondul proprietatea"], source_txt):
                file_system.write_to_file("fondul_proprietatea", link_to_source, "nbt")
            if tickers_in_news(["omv", "petrom", "snp"], source_txt):
                file_system.write_to_file("omv_petrom", link_to_source, "nbt")
            if tickers_in_news(["transilvania", "tlv"], source_txt):
                file_system.write_to_file("transilvania", link_to_source, "nbt")

# match a single ticker with the text in the news
def ticker_in_news(ticker, news_text):
    return True if re.search(ticker, news_text, re.IGNORECASE) else False

# match a list of tickers with the text in the news
def tickers_in_news(tickers, news_text):
    for ticker in tickers:
        if ticker_in_news(ticker, news_text):
            return True
    
    return False

sort_news_by_tickers()

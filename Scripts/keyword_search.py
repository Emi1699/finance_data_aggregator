import helpers
import requests
import re


linkk = "https://www.zfcorporate.ro/retail-agrobusiness/mesajul-fermierilor-vrem-sa-investim-in-irigatii-bani-gasim-accesul-21331789"
source_txt = requests.get(helpers.get_link_from_string(linkk)).text

# helpers.write_to_file(source_txt, "rsp")
# startIndex = source_txt.index("text-content")

def search_tickers():
    with open(helpers.get_path_to_file("ziarul_financiar", __file__, "nbs"), 'r', encoding="utf-8") as file:
        for line in file:
            source_txt = requests.get(helpers.get_link_from_string(line)[0:-2]).text
            
            if tickers_in_news(["societatea energetica electrica", "electrica s.a.", "electrica sa"], source_txt):
                helpers.write_to_file("electrica", helpers.get_link_from_string(line)[0:-2], "nbt")
            if tickers_in_news(["fondul proprietatea"], source_txt):
                helpers.write_to_file("fondul_proprietatea", helpers.get_link_from_string(line)[0:-2], "nbt")
            if tickers_in_news(["omv", "petrom", "snp"], source_txt):
                helpers.write_to_file("omv_petrom", helpers.get_link_from_string(line)[0:-2], "nbt")
            if tickers_in_news(["transilvania", "tlv"], source_txt):
                helpers.write_to_file("transilvania", helpers.get_link_from_string(line)[0:-2], "nbt")

# match a single ticker with the text in the news
def ticker_in_news(ticker, news_text):
    return True if re.search(ticker, news_text, re.IGNORECASE) else False

# match a list of tickers with the text in the news
def tickers_in_news(tickers, news_text):
    for ticker in tickers:
        if ticker_in_news(ticker, news_text):
            return True
    
    return False

search_tickers()


# print(tickers_in_news(["country managEr", "Daniel buHai", "GeorGE Copos"], source_txt))

# search_tickers()

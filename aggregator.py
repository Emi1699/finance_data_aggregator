from bs4 import BeautifulSoup as bs
import requests
from datetime import date

def get_latest_news_ziarul_financiar():
    source = get_source("https://www.zf.ro/")
    news = {}
    newsID = 1

    latestNews_wrapper = source.select(".clear.latest-wrapper")

    for wrapper in latestNews_wrapper:
        for list_el in wrapper.find_all("li"):

            newsTime = str(date.today()) + " @ " + list_el.find("small").text
            newsLink = "https://www.zf.ro/" + list_el.find("a")['href']
            newsText = list_el.find("a").text

            if not news_already_read("news.txt", newsText):
                news[newsID] = (newsTime, newsText, newsLink)

            newsID += 1

    with open('news.txt', 'a', encoding='utf-8') as f:
        for article in news.values():
            f.write(str(article)+ "\n\n")

    f.close()

    print("SUCCESS! CHECK THE 'news.txt' FILE!")

def get_source(url):
    html = requests.get(url).content

    return bs(html, 'html5lib')

def print_utf8(s):
    print(s.encode("utf-8"))

def news_already_read(file_name, news):
    """ Check if any line in the file contains given string """
    with open(file_name, 'r', encoding='utf-8') as read_obj:
        for line in read_obj:
            if news in line:
                return True
    return False

get_latest_news_ziarul_financiar() #entry point
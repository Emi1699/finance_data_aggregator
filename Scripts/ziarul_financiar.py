from datetime import date
import helpers

def get_latest_news_ziarul_financiar():
    source = helpers.get_source("https://www.zf.ro/")
    news = {}
    newsID = 1

    latestNews_wrapper = source.select(".clear.latest-wrapper")

    for wrapper in latestNews_wrapper:
        for list_el in wrapper.find_all("li"):

            newsTime = str(date.today()) + " @ " + list_el.find("small").text
            newsLink = "https://www.zf.ro/" + list_el.find("a")['href']
            newsText = list_el.find("a").text

            if not helpers.news_already_read("./News/ziarul_financiar.txt", newsText):
                news[newsID] = (newsTime, newsText, newsLink)

            newsID += 1

    with open('./News/ziarul_financiar.txt', 'a', encoding='utf-8') as f:
        for article in news.values():
            f.write(str(article)+ "\n\n")

    f.close()

    helpers.add_news_to_excel(news)

    print("SUCCESS! CHECK THE 'ziarul_financiar.txt' FILE!")

get_latest_news_ziarul_financiar() #entry point
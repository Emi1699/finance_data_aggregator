import os
from datetime import date
import helpers
from news import News


def pause():
    programPause = input("\nPress the <ENTER> key to continue...\n")

def get_latest_news(sourceLink = "https://www.profit.ro/toate"):
    source = helpers.get_source(sourceLink)
    news = {}
    id = 1

    # find path to output file
    absolute_path = os.path.dirname(__file__)
    relative_path = "../News/profit_ro.txt"
    output_file = os.path.join(absolute_path, relative_path) 

    latestNews_wrapper = source.select("ul.articles")

    for wrapper in latestNews_wrapper:
        for list_el in wrapper.find_all("li"):
            if not list_el.has_attr("id"):

                newsDate = list_el.select("div.col-xs-12.col-sm-8.col-md-9")[0].select("div")[0].text
                newsText = list_el.select("div.col-xs-12.col-sm-8.col-md-9")[0].select("a")[0].text
                newsLink = "https://www.profit.ro" + list_el.select("div.col-xs-12.col-sm-8.col-md-9")[0].select("a")[0]['href']

                newsPiece = News(newsDate, newsText, newsLink, id)
                news[newsPiece.id] = (newsPiece.date, newsPiece.text, newsPiece.link)

                id += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        for article in news.values():
            f.write(str(article)+ "\n")
    f.close()

    # helpers.add_news_to_excel(news)

    print("SUCCESS! CHECK THE 'profit_ro.txt' FILE!")

    


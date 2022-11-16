from datetime import date
import helpers
import os
from news import News

def get_latest_news(sourceLink = "https://www.zf.ro/"):
    source = helpers.get_source(sourceLink)
    news = {}
    id = 1

    absolute_path = os.path.dirname(__file__)
    relative_path = f"../News/{__name__}.txt"
    output_file = os.path.join(absolute_path, relative_path) 

    latestNews_wrapper = source.select(".clear.latest-wrapper")

    for wrapper in latestNews_wrapper:
        for list_el in wrapper.find_all("li"):

            newsDate = str(date.today()) + " @ " + list_el.find("small").text
            newsLink = sourceLink+ list_el.find("a")['href']
            newsText = list_el.find("a").text

            newsPiece = News(newsDate, newsText, newsLink, id)
            news[newsPiece.id] = (newsPiece.date, newsPiece.text, newsPiece.link)

            id += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        for article in news.values():
            f.write(str(article)+ "\n")

    f.close()

    # helpers.add_news_to_excel(news)

    print(f"SUCCESS! CHECK THE '{__name__}.txt' FILE!")


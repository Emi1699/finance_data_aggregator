from datetime import date
import helpers
from news import News

def get_latest_news(sourceLink = "https://www.zf.ro/"):
    source = helpers.get_source(sourceLink)
    news = {}
    id = 1

    # get relative path to output file (determined by this file's name; output file is in the 'News' directory)
    output_file = helpers.get_path_to_output(__name__, __file__)

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

    print(f"SUCCESS! CHECK THE '{__name__}.txt' FILE!")


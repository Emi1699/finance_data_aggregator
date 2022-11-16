from datetime import date
import helpers
from news import News

def get_latest_news(sourceLink = "https://www.wall-street.ro/"):
    source = helpers.get_source(sourceLink)
    news = {}
    id = 1

    # get relative path to output file (determined by this file's name; output file is in the 'News' directory)
    output_file = helpers.get_path_to_output(__name__, __file__)

    latestNews_wrapper = source.select(".list-unstyled.clearfix.top")

    # print(len(latestNews_wrapper))

    for li_element in latestNews_wrapper[0].select("li>a"):

        newsLink = li_element['href']
        newsText = li_element.text[2:-1]

        # this time it is trickier to get the date; we have to access each article by itself and get the date from the articles page
        articleDateSource = helpers.get_source(newsLink).select("div.article-infos>span.data")[0]

        if len(articleDateSource.select("span")) > 0: # updated
            newsDate = articleDateSource.select("span")[0].text
        else:
            newsDate = articleDateSource.select("a")[0].text

        newsPiece = News(newsDate, newsText, newsLink, id)
        news[newsPiece.id] = (newsPiece.date, newsPiece.text, newsPiece.link)

        id += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        for article in news.values():
            f.write(str(article)+ "\n")

    f.close()

    # helpers.add_news_to_excel(news)

    print(f"SUCCESS! CHECK THE '{__name__}.txt' FILE!")
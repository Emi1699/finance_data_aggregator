from datetime import date
import helpers
from news import News

def get_latest_news(sourceLink = "https://www.wall-street.ro/ultima-ora/index.html"):
    print(f"\nRetrieving news from wall-street.ro ...")

    source = helpers.get_source(sourceLink)
    news = {}
    id = 1

    # get relative path to output file (determined by this file's name; output file is in the 'News' directory)
    output_file = helpers.get_path_to_output(__name__, __file__)

    for page in range(1, 4): #loop through the pages of news on the website

        if page > 1:
            source = helpers.get_source(f"https://www.wall-street.ro/articol/Ultima-Ora/pagina-{page}.html")

        latestNews_wrapper = source.select(".list-unstyled.clearfix.top")

        for li_element in latestNews_wrapper[0].select("li>a"):

            newsLink = li_element['href']
            newsText = li_element.text[2:-1]

            # this time it is trickier to get the date; we have to access each article by itself and get the date from the article's page
            articleDateSource = helpers.get_source(newsLink).select("div.article-infos>span.data")[0]

            if len(articleDateSource.select("span")) > 0: # updated
                newsDate = articleDateSource.select("span")[0].text
            else:
                newsDate = articleDateSource.select("a")[0].text

            newsPiece = News(newsDate, newsText, newsLink, id)

            if (newsPiece.date, newsPiece.text, newsPiece.link) not in news.values():
                news[newsPiece.id] = (newsPiece.date, newsPiece.text, newsPiece.link)
                id += 1
            else:
                continue

    with open(output_file, 'w', encoding='utf-8') as f:
        for article in news.values():
            f.write(str(article)+ "\n")

    f.close()

    print(f"SUCCESS! CHECK THE '{__name__}.txt' FILE!\n")
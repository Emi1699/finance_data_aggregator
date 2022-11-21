from datetime import date
import helpers
from news import News

class RetrievalModule():

    # get latest news from ziarul-financiar
    def get_latest_news_ziarul_financiar(self, sourceLink = "https://www.zf.ro/"):
        print(f"\n\nRetrieving news from ziarul-financiar.ro ...")

        source = helpers.get_source(sourceLink)
        news = {}
        id = 1

        latestNews_wrapper = source.select(".clear.latest-wrapper")

        for wrapper in latestNews_wrapper:
            for list_el in wrapper.find_all("li"):

                newsDate = str(date.today()) + " @ " + list_el.find("small").text
                newsLink = sourceLink+ list_el.find("a")['href']
                newsText = list_el.find("a").text

                newsPiece = News(newsDate, newsText, newsLink, id)
                news[newsPiece.id] = (newsPiece.date, newsPiece.text, newsPiece.link)

                id += 1

        helpers.write_news_to_file("ziarul_financiar", news)


    # get latest new from wall-street.ro
    def get_latest_news_wall_street_ro(self, sourceLink = "https://www.wall-street.ro/ultima-ora/index.html"):
        print(f"\n\nRetrieving news from wall-street.ro ...")

        source = helpers.get_source(sourceLink)
        news = {}
        id = 1

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
            news[newsPiece.id] = (newsPiece.date, newsPiece.text, newsPiece.link)

            id += 1

        helpers.write_news_to_file("wall_street", news)

    # get latest news from profit.ro
    def get_latest_news_profit_ro(self, sourceLink = "https://www.profit.ro/toate"):
        print(f"\n\nRetrieving news from profit.ro ...")

        news = {}
        id = 1

        for page in range(1, 3):

            if page == 1:
                source = helpers.get_source(sourceLink)
            else:
                source = helpers.get_source(f"{sourceLink}?p={page}")

            # get featured piece of news
            self.getFeatured(source, news, id)
            id += 1

            # get news from the list below
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

        helpers.write_news_to_file("profit_ro", news)

    def getFeatured(self, source, news, id):
        feat = source.select("div.col-xs-12.col-md-6 h2")[0]

        newsDate = source.select("div.col-xs-12.col-md-6 div")[0].text
        newsText = feat.select("a")[0].text
        newsLink = "https://www.profit.ro" + feat.select("a")[0]['href']

        newsPiece = News(newsDate, newsText, newsLink, id)
        news[newsPiece.id] = (newsPiece.date, newsPiece.text, newsPiece.link)
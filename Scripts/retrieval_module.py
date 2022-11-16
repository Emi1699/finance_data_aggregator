from datetime import date
import helpers
from news import News

class RetrievalModule():

    # get latest news from ziarul-financiar
    def get_latest_news_ziarul_financiar(self, sourceLink = "https://www.zf.ro/"):
        print(f"\nRetrieving news from ziarul-financiar.ro ...")

        source = helpers.get_source(sourceLink)
        news = {}
        id = 1

        # get relative path to output file (determined by this file's name; output file is in the 'News' directory)
        output_file = helpers.get_path_to_output("ziarul_financiar", __file__)

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

        print(f"SUCCESS! CHECK THE '{__name__}.txt' FILE!\n")

    # get latest new from wall-street.ro
    def get_latest_news_wall_street_ro(self, sourceLink = "https://www.wall-street.ro/ultima-ora/index.html"):
        print(f"\nRetrieving news from wall-street.ro ...")

        source = helpers.get_source(sourceLink)
        news = {}
        id = 1

        # get relative path to output file (determined by this file's name; output file is in the 'News' directory)
        output_file = helpers.get_path_to_output("wall_street", __file__)

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

    # get latest news from profit.ro
    def get_latest_news_profit_ro(self, sourceLink = "https://www.profit.ro/toate"):
        print(f"\nRetrieving news from profit.ro ...")

        news = {}
        id = 1

        # get relative path to output file (determined by this file's name; output file is in the 'News' directory)
        output_file = helpers.get_path_to_output("profit_ro", __file__)

        for page in range(1, 4):

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

        with open(output_file, 'w', encoding='utf-8') as f:
            for article in news.values():
                f.write(str(article)+ "\n")
        f.close()

        print(f"SUCCESS! CHECK THE '{__name__}.txt' FILE!\n")

    def getFeatured(self, source, news, id):
        feat = source.select("div.col-xs-12.col-md-6 h2")[0]

        newsDate = source.select("div.col-xs-12.col-md-6 div")[0].text
        newsText = feat.select("a")[0].text
        newsLink = "https://www.profit.ro" + feat.select("a")[0]['href']

        newsPiece = News(newsDate, newsText, newsLink, id)
        news[newsPiece.id] = (newsPiece.date, newsPiece.text, newsPiece.link)
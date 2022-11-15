import bs4
import requests
import json

# dictionar global
d = {
        "movie": [],
        "title": [],
        "content": [],
        "rating": [],
        "date": [],
        "user": [],
    }

# pentru fiecare film, formez linkul de review-uri si apelez functia care ia infos despre ele
def get_films():

    imdb_string = "https://www.imdb.com/chart/top/"
    html = requests.get(imdb_string).content
    soup = bs4.BeautifulSoup(html, "html.parser")

    lines = soup.select("tbody.lister-list tr")

    for line in lines:
        cells = [cell for cell in line.select("td")]
        link_reviews, title_movie = get_link_reviews(cells) ### aici apelez ex 1
        get_reviews_information(link_reviews, title_movie) ### aici apelez ex 2 & 3



######## EXERCITIUL 1 - formez linkul de review-uri pentru fiecare film
def get_link_reviews(cells):

    url_movie = cells[1].select_one("a")["href"]
    title_movie = cells[1].select_one("a").text
    link_reviews = f"https://www.imdb.com{url_movie}reviews"
    return link_reviews, title_movie



######## EXERCITIUL 2 & 3 - iau infos despre review-uri si le bag in dictionarul d
def get_reviews_information(link_reviews, title_movie):

    html = requests.get(link_reviews).content
    soup = bs4.BeautifulSoup(html, "html.parser")
    review_list = soup.select_one("div.lister-list")
    reviews = review_list.select("div.lister-item")

    for review in reviews:
        title = review.select_one("a").text.strip()
        user = review.select_one("span.display-name-link a").text
        date = review.select_one("span.review-date").text
        content = review.select_one("div.content div.text.show-more__control").text.strip()

        # am decis sa nu pun in lista de review-uri pe cele care nu au rating
        try:
            rating = review.select_one("span.rating-other-user-rating span").text
        except Exception:
            continue

        d["rating"].append(rating)
        d["movie"].append(title_movie)
        d["title"].append(title)
        d["content"].append(content)
        d["date"].append(date)
        d["user"].append(user)



###### EXERCITIUL 4 - transmit cate review-uri de la fiecare film vreau sa-mi incarce
# apasa pe Load More
def get_reviews_information_with_nr_reviews(id_movie, title_movie, nrReviews):

    link_reviews = f"https://www.imdb.com/title/{id_movie}/reviews"

    while nrReviews > 0:

        html = requests.get(link_reviews).content
        soup = bs4.BeautifulSoup(html, "html.parser")
        review_list = soup.select_one("div.lister-list")
        reviews = review_list.select("div.lister-item")

        while nrReviews < len(reviews):
            reviews.pop(-1)

        for review in reviews:

            title = review.select_one("a").text.strip()
            user = review.select_one("span.display-name-link a").text
            date = review.select_one("span.review-date").text
            content = review.select_one("div.content div.text.show-more__control").text

            try:
                rating = review.select_one("span.rating-other-user-rating span").text
            except Exception:
                continue

            d["rating"].append(rating)
            d["movie"].append(title_movie)
            d["title"].append(title)
            d["content"].append(content)
            d["date"].append(date)
            d["user"].append(user)

            nrReviews -= 1

        try:
            # iau html-ul cand apas pe Load More si formez un nou link
            dataKey = soup.select_one("div.load-more-data")["data-key"]
            link_reviews = f"https://www.imdb.com/title/{id_movie}/reviews/_ajax?paginationKey={dataKey}"
        except Exception:
            print("No more reviews to show")
            break



# Salvez dictionarul in json
# modific dictionarul pentru a afisa infos despre fiecare review, pe rand
def to_json(dictionar):

    json_list = []

    valueLength = len(list(dictionar.values())[0])

    for index in range(valueLength):
        exemplu = {
            "movie": "",
            "title": "",
            "content": "",
            "rating": "",
            "date": "",
            "user": ""
        }
        for key in list(dictionar.keys()):
            exemplu[key] = dictionar[key][index]

        json_list.append(exemplu)

    with open("reviews.json", "w") as f:
        json.dump(json_list, f, indent=4)




### Luam review-urile de la toate 250 de filme ( dureaza destul de mult sa ruleze)
# get_films()

### Luam primele X review-uri de la primul film
# get_reviews_information_with_nr_reviews("tt0111161", "The Shawshank Redemption", 35)
# to_json(d)
# review_dataset = pd.DataFrame(d)
# review_dataset.to_csv("reviews.csv", index=False)
# print(review_dataset.head())

### Luam review-urile de la primul film si le salvez in json
# get_reviews_information("https://www.imdb.com/title/tt0111161/reviews", "The Shawshank Redemption")
# to_json(d)
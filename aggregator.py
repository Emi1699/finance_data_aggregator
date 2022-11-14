from bs4 import BeautifulSoup as bs
import requests

keywords = ['BVB', 'SNP']    

def lovely_soup(url):
    r = requests.get(url)
    return bs(r.content, 'lxml')


articles = {} # dict that holds article titles and links to them
i = 1 # used to populate the above dict

website = 'https://www.zf.ro/companii/'
categories = ['']


for page in range(1, 6):
    if page == 1:
        pass
    else:
        website += "page/" + str(page)

    soup = lovely_soup(website)
    news = soup.findAll('div', {'class': 'flux news clear'})

    for title in news:
        clearDivs = title.findAll('div', {'class': 'clear'})

        for clDiv in clearDivs:
            h2Tags = clDiv.findAll('h2')

            for h2Tag in h2Tags:
                aTags = h2Tag.findAll('a', {'class': 'articleTitle h3'})

                for aTag in aTags:
                    articles[i] = (aTag['title'], "SURSA: https://www.zf.ro" + aTag['href'] + " ")
                    i += 1

with open('articles.txt', 'a', encoding='utf-8') as f:
    for article in articles.values():
        # if article not in articles.values():
        f.write(str(article)+ "\n\n")

f.close()
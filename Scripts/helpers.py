from datetime import datetime, timedelta
import time
from alive_progress import alive_bar
from bs4 import BeautifulSoup as bs
import requests
import re
# from progress.bar import Bar

def get_source(url):
    html = requests.get(url).content

    return bs(html, 'html5lib')

def print_utf8(s):
    print(s.encode("utf-8"))

# find 'https[...]' substring in a given string
def get_link_from_string(str):
    return re.search("(?P<url>https?://[^\s]+)", str).group("url")

# wait for len_pause seconds and display a loading bar
def pause(len_pause):
    print()
    with alive_bar(len_pause, title='Waiting...', length=50, bar="smooth") as bar:
        for _ in range(len_pause):
            time.sleep(1)
            bar()

def transform_date_to_ddmmyyyy(date_str):
    date = None

    if word_in_substr("astăzi", date_str):
        date = str(datetime.now().strftime('%d-%m-%Y')) + ' @ ' + date_str[8:]

    if word_in_substr("ieri", date_str):
        date = datetime.now() - timedelta(1)
        date = datetime.strftime(date, '%d-%m-%Y') + ' @ ' + date_str[6:]

    return date

def word_in_substr(word, sub_str):
    return True if re.search(word, sub_str, re.IGNORECASE) else False

# print(transform_date_to_ddmmyyyy('astă zi, 14:00'))


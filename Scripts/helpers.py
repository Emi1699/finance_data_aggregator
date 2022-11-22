import time
from alive_progress import alive_bar
from bs4 import BeautifulSoup as bs
import requests
from openpyxl.workbook import Workbook
import os
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

def pause(len_pause):
    print()
    with alive_bar(len_pause, title='Waiting...', length=50, bar="smooth") as bar:
        for _ in range(len_pause):
            time.sleep(1)
            bar()

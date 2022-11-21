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

def news_already_read(file_name, news):
    """ Check if any line in the file contains given string """
    with open(file_name, 'r', encoding='utf-8') as read_obj:
        for line in read_obj:
            if str(news) in line:
                return True
    return False

def add_news_to_excel(news):
    headers = ['Date', 'Text', 'Link']
    workbook_name = './News by Source/ziarul_financiar.xlsx'
    wb = Workbook()
    page = wb.active
    page.title = 'Ziarul Financiar Today'
    page.append(headers)

    for new in news.values():
        page.append(new)

    wb.save(filename = workbook_name)

def get_path_to_file(name, file):
    absolute_path = os.path.dirname(file)
    relative_path = f"../News by Source/{name}.txt"
    output_file = os.path.join(absolute_path, relative_path)

    return output_file

# append new pieces of news at the top of the file (so that the most recent news are at the top)
def write_news_to_file(name, news):
    # get relative path to output file (determined by this file's name; output file is in the 'News by Source' directory)
    output_file = get_path_to_file(name, __file__)
    saved = ""

    # check if file exists
    # if it does, read its content and saved it in a temporary variable
    if os.path.isfile(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
                saved = f.read()

    # overwrite the file with the new piece of news (essentially, putting it at the top)
    with open(output_file, 'w', encoding="utf-8") as f:
        for article in news.values():
            # if not news_already_read(output_file, article):
            if str(article) not in saved:
                f.write(str(article)+ "\n")

    # append the content that we temporarily saved earlier
    with open(output_file, 'a', encoding="utf-8") as f:
        f.write(saved)

    print(f"\t|\n\t|__SUCCESS! THE LATEST NEWS HAVE BEEN SAVED ON YOUR SYSTEM!")

    f.close()

def write_to_file(txt, fl):
    output_file = get_path_to_file(fl, __file__)

    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(txt)

    print(f"Content has been written to file.")

def get_link_from_string(str):
    return re.search("(?P<url>https?://[^\s]+)", str).group("url")

def pause(len_pause):
    print()
    with alive_bar(len_pause, title='Waiting...', length=50, bar="smooth") as bar:
        for _ in range(len_pause):
            time.sleep(1)
            bar()

    # print()
    # bar = Bar(f"SLEEPING FOR {len_pause} SECONDS ({len_pause/60} MINUTES)...", max=len_pause)
    # for i in range(len_pause):
    #     time.sleep(1)
    #     bar.next()
    # bar.finish()

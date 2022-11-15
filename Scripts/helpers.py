from bs4 import BeautifulSoup as bs
import requests
from openpyxl.workbook import Workbook

def get_source(url):
    html = requests.get(url).content

    return bs(html, 'html5lib')

def print_utf8(s):
    print(s.encode("utf-8"))

def news_already_read(file_name, news):
    """ Check if any line in the file contains given string """
    with open(file_name, 'r', encoding='utf-8') as read_obj:
        for line in read_obj:
            if news in line:
                return True
    return False

def add_news_to_excel(news):
    headers = ['Date', 'Text', 'Link']
    workbook_name = './News/ziarul_financiar.xlsx'
    wb = Workbook()
    page = wb.active
    page.title = 'Ziarul Financiar Today'
    page.append(headers)

    for new in news.values():
        page.append(new)

    wb.save(filename = workbook_name)
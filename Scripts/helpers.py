from bs4 import BeautifulSoup as bs
import requests
from openpyxl.workbook import Workbook
import os

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
    workbook_name = './News/ziarul_financiar.xlsx'
    wb = Workbook()
    page = wb.active
    page.title = 'Ziarul Financiar Today'
    page.append(headers)

    for new in news.values():
        page.append(new)

    wb.save(filename = workbook_name)

def get_path_to_output(name, file):
    absolute_path = os.path.dirname(file)
    relative_path = f"../News/{name}.txt"
    output_file = os.path.join(absolute_path, relative_path)

    return output_file

# append new pieces of news at the top of the file (so that the most recent news are at the top)
def write_news_to_file(name, news):
    # get relative path to output file (determined by this file's name; output file is in the 'News' directory)
    output_file = get_path_to_output(name, __file__)
    saved = ""

    print(output_file)
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

    print(f"SUCCESS! NEWS HAS BEEN WRITTEN TO FILE!")

    f.close()



# print(news_already_read(get_path_to_output("ziarul_financiar", __file__), ('2022-11-17 @ 13:04', 'Omniasig a încheiat primele nouă luni din 2022 cu subscrieri de 1,5 mld. lei, consemnând un avans de 35% faţă de aceeaşi perioadă a anului trecut. Subscrierile pe zona auto, RCA şi Casco, cumulat reprezintă circa 73% din total, respectiv 1,1 mld. lei', 'https://www.zf.ro//banci-si-asigurari/omniasig-incheiat-primele-luni-2022-subscrieri-1-5-mld-lei-21330197')
# ))
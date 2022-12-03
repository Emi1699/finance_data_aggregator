'''

This module holds all file related methods and operations (e.g. read, write, etc)

'''

import os
from openpyxl import Workbook

def line_already_in_file(file_name, ln):
    """ Check if any line in the file contains given string """
    with open(file_name, 'r', encoding='utf-8') as read_obj:
        for line in read_obj:
            if str(ln) in line:
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

# append new pieces of news at the top of the file (so that the most recent news are at the top)
def write_news_dict_to_file(name, news, dir_path):
    # get relative path to output file (determined by this file's name; output file is in the 'News by Source' directory)
    output_file = get_path_to_file(name, __file__, dir_path)
    saved = ""

    # check if file exists
    # if it does, read its content and saved it in a temporary variable
    if os.path.isfile(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
                saved = f.read()

    # overwrite the file with the new piece of news (essentially, putting it at the top)
    with open(output_file, 'w', encoding="utf-8") as f:
        for article in news.values():
            
            if str(article) not in saved:
                f.write(str(article)+ "\n")

    # append the content that we temporarily saved earlier
    with open(output_file, 'a', encoding="utf-8") as f:
        f.write(saved)

    print(f"\t|\n\t|__SUCCESS! THE LATEST NEWS HAVE BEEN SAVED ON YOUR SYSTEM!")

    f.close()

def get_path_to_file(name, file, dir_path):
    absolute_path = os.path.dirname(file)
    relative_path = dir_path.value + name
        
    output_file = os.path.join(absolute_path, relative_path)

    return output_file

# overwrite
def write_to_file(fl, txt, dir_path, finish_text = "Content has been written to file."):
    output_file = get_path_to_file(fl, __file__, dir_path)
    
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(txt + "\n")

    # print(f"{finish_text}")

# append if not already in file
def append_to_file(fl, txt, dir_path, finish_text = "Content has been written to file."):
    output_file = get_path_to_file(fl, __file__, dir_path)

    with open(output_file, 'a', encoding="utf-8") as f:
        if not line_already_in_file(output_file, txt):
            f.write(txt + "\n")

    # print(f"{finish_text}")

# exact same implementation as the one above; the reason I have it is because
# it makes the code more readable in the module where this is used
def write_ticker_to_file(fl, txt, dir_path, finish_text = "Content has been written to file."):
    output_file = get_path_to_file(fl, __file__, dir_path)

    with open(output_file, 'a', encoding="utf-8") as f:
        if not line_already_in_file(output_file, txt):
            f.write(txt + "\n")

    print(f"{finish_text}")

def clear_file(fl, dir_path):
    output_file = get_path_to_file(fl, __file__, dir_path)

    open(output_file, 'w').close()
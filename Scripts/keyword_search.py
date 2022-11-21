import helpers
import requests


linkk = "https://www.zfcorporate.ro/retail-agrobusiness/mesajul-fermierilor-vrem-sa-investim-in-irigatii-bani-gasim-accesul-21331789"
source_txt = requests.get(helpers.get_link_from_string(linkk)).text

helpers.write_to_file(source_txt, "rsp")
startIndex = source_txt.index("text-content")

print("se " in source_txt)


def search_tickers():
    with open(helpers.get_path_to_file("ziarul_financiar", __file__), 'r', encoding="utf-8") as file:
        for line in file:
            source_txt = requests.get(helpers.get_link_from_string(line)[0:-2]).text

            helpers.write_to_file(source_txt, "rsp")
            startIndex = source_txt.index("text-content")

            print(source_txt[startIndex:startIndex+1])

# search_tickers()

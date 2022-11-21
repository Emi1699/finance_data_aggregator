import helpers
import requests


source_txt = requests.get(helpers.get_link_from_string("https://www.zf.ro//eveniment/alzheimer-au-fost-descoperite-doua-bauturi-care-protejeaza-creierul-21339432")).text

helpers.write_to_file(source_txt, "rsp")
startIndex = source_txt.index("text-content")

print(source_txt[startIndex:startIndex+1])





def search_tickers():
    with open(helpers.get_path_to_file("ziarul_financiar", __file__), 'r', encoding="utf-8") as file:
        for line in file:
            print(f"\n\n{line}\n\n")
            source_txt = requests.get(helpers.get_link_from_string(line)[0:-2]).text

            helpers.write_to_file(source_txt, "rsp")
            startIndex = source_txt.index("text-content")

            print(source_txt[startIndex:startIndex+1])

search_tickers()

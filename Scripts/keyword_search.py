import helpers
import requests
import re
import file_system

running = True
testing = not running

def test():
    link_to_source = "https://www.wall-street.ro/articol/Economie/291740/iohannis-a-cerut-omv-sa-inceapa-cat-mai-rapid-exploatarea-in-perimetrul-neptun-deep-din-marea-neagra.html"
    source_txt = requests.get(link_to_source).text # get page's content (including the text of the news)
    source_txt = source_txt[0:(int)(-len(source_txt) * 0.358)] # ONLY SEARCH IN THE TOP 5% OF THE DOCUMENT

    print(len(source_txt))
    file_system.write_to_file("test", source_txt)
    print(ticker_in_news('omv', source_txt))

def sort_all_news_by_tickers():
    # sort_news_by_tickers_from("wall_street")
    # sort_news_by_tickers_from("profit_ro")
    sort_news_by_tickers_from("ziarul_financiar")

def sort_news_by_tickers_from(source):
    print(f"\nSorting news from {source} by ticker...\n")

    with open(file_system.get_path_to_file(source, __file__, "nbs"), 'r', encoding="utf-8") as file:
        link = 1
        for line in file:
            print(f"> searching link {link} ...")
            link_to_source = helpers.get_link_from_string(line)[0:-2]
            source_txt = requests.get(link_to_source).text # get page's content (including the text of the news)
            source_txt = source_txt[0:(int)(-len(source_txt) * 0.95)] # ONLY SEARCH IN THE TOP 5% OF THE DOCUMENT
            
            check_all_tickers(source_txt, link_to_source, f"> news written to file")

            link += 1
            
# match a single ticker with the text in the news
def ticker_in_news(ticker, news_text):
    return True if re.search(ticker, news_text, re.IGNORECASE) else False

# match a list of tickers with the text in the news
def tickers_in_news(tickers, news_text):
    for ticker in tickers:
        if ticker_in_news(ticker, news_text):
            return True

    return False

def check_all_tickers(source_txt, link_to_source, finish_message):
    if tickers_in_news(["societatea energetica electrica", "electrica s.a.", "electrica sa"], source_txt):
        file_system.write_to_file("EL_SOCIETATEA ENERGETICA ELECTRICA", link_to_source, finish_message)

    if tickers_in_news(["fondul proprietatea"], source_txt):
        file_system.write_to_file("FP_FONDUL PROPRIETATEA", link_to_source, finish_message)

    if tickers_in_news(["omv", "petrom ", "snp", " petrom"], source_txt):
        file_system.write_to_file("SNP_OMV PETROM", link_to_source, finish_message)

    if tickers_in_news(["banca transilvania", "tlv"], source_txt):
        file_system.write_to_file("TLV_BANCA TRANSILVANIA", link_to_source, finish_message)

    if tickers_in_news([" tts ", "transport trade services"], source_txt):
        file_system.write_to_file("TTS_TRANSPORT TRADE SERVICES", link_to_source, finish_message)

    if tickers_in_news([" tel ", "transelectrica"], source_txt):
        file_system.write_to_file("TEL_TRANSELECTRICA", link_to_source, finish_message)

    if tickers_in_news(["tgn", "transgaz"], source_txt):
        file_system.write_to_file("TGN_TRANSGAZ", link_to_source, finish_message)
    
    if tickers_in_news(["sng", "romgaz"], source_txt):
        file_system.write_to_file("SNG_ROMGAZ", link_to_source, finish_message)

    if tickers_in_news(["brd", "groupe societe generale"], source_txt):
        file_system.write_to_file("BRD_GROUPE SOCIETE GENERALE", link_to_source, finish_message)

    if tickers_in_news([" ever ", "evergent investments", "evergent"], source_txt):
        file_system.write_to_file("EVER_EVERGENT INVESTMENTS", link_to_source, finish_message)

    if tickers_in_news(["erste group bank", "erste group", "erste"], source_txt):
        file_system.write_to_file("EBS_ERSTE GROUP BANK AG", link_to_source, finish_message)

    if tickers_in_news(["purcari wineries", "purcari"], source_txt):
        file_system.write_to_file("WINE_PURCARI WINERIES PUBLIC COMPANY LIMITED", link_to_source, finish_message)

    if tickers_in_news(["medlife"], source_txt):
        file_system.write_to_file("M_MEDLIFE", link_to_source, finish_message)

    if tickers_in_news(["snn", "nuclearelectrica"], source_txt):
        file_system.write_to_file("SNN_NUCLEARELECTRICA", link_to_source, finish_message)

    if tickers_in_news(["sfg", "sphera franchise group"], source_txt):
        file_system.write_to_file("SFG_SPHERA FRANCHISE GROUP", link_to_source, finish_message)
    
    if tickers_in_news([" roce ", "romcarbon"], source_txt):
        file_system.write_to_file("ROCE_ROMCARBON", link_to_source, finish_message)

    if tickers_in_news(["aquila"], source_txt):
        file_system.write_to_file("AQ_AQUILA PART PROD", link_to_source, finish_message)

    if tickers_in_news(["trp", "teraplast"], source_txt):
        file_system.write_to_file("TRP_TERAPLAST", link_to_source, finish_message)

    if tickers_in_news(["conpet"], source_txt):
        file_system.write_to_file("COTE_CONPET", link_to_source, finish_message)

    if tickers_in_news([" transi ", "transilvania investments"], source_txt):
        file_system.write_to_file("TRANSI_TRANSILVANIA INVESTMENTS ALLIANCE", link_to_source, finish_message)

    if tickers_in_news(["smtl", "simtel"], source_txt):
        file_system.write_to_file("SMTL_SIMTEL TEAM", link_to_source, finish_message)

    if tickers_in_news(["nrf", "norofert"], source_txt):
        file_system.write_to_file("NRF_NOROFERT", link_to_source, finish_message)

    if tickers_in_news(["safe", "safetech"], source_txt):
        file_system.write_to_file("SAFE_SAFETECH INNOVATIONS", link_to_source, finish_message)

    if tickers_in_news(["arobs", "arobs transilvania"], source_txt):
        file_system.write_to_file("AROBS_AROBS TRANSILVANIA SOFTWARE", link_to_source, finish_message)

    if tickers_in_news(["milk", "agroserv"], source_txt):
        file_system.write_to_file("MILK_AGROSERV MARIUTA", link_to_source, finish_message)

if running:
    sort_all_news_by_tickers()

if testing:
    test()
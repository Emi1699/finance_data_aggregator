from companies import Company

def get_curl_params(company):
    cookies, headers, params, data = None, None, None, None

    if company == Company.SOCIETATEA_ENERGETICA_ELECTRICA:
        pass

    elif company == Company.FONDUL_PROPRIETATEA:
        pass

    elif company == Company.OMV_PETROM:
        cookies = {
            'cookiesession1': '678B2878UVWXYZABCDEFGIJKLMNOA93E',
            '_ga': 'GA1.2.1355707676.1668264785',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'r531010gcksuyk5l1zlmmucc',
            '_gid': 'GA1.2.1648857741.1669896986',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=SNP',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'cookiesession1=678B2878UVWXYZABCDEFGIJKLMNOA93E; _ga=GA1.2.1355707676.1668264785; BVBCulturePref=en-US; ASP.NET_SessionId=r531010gcksuyk5l1zlmmucc; _gid=GA1.2.1648857741.1669896986; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SNP',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$3e15e9b5-87d7-4a5a-be83-3c24a87642f9',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'lez1YVnx/mmqQDMjoRxkj9ZvFpsBSiKErpS8BVFFdOWIeQWndl8letfHKGTm3BSXpuwXet5wjLhdPHiEbPDjRItyi5lnPMGRB4UYP5rImClpuhmB4VuJi8I7JrgnWqHYComsqdXnFY2QgNFLoJWT69pSY6QvdHMuGYC4IYngJDjWEYZy4yD0Hrkq0mAKgh/vHJ//1dOiJcB2e6DGt7yfQeavNBMY4B50mXhnUecLmVUq6wssbD/l3ydsUFoT9vsTHBZYV1+lXCXEF0ovV7rK1A==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$3e15e9b5-87d7-4a5a-be83-3c24a87642f9': 'Trading',
        }

    elif company == Company.BANCA_TRANSILVANIA:
        pass

    elif company == Company.TRANSPORT_TRADE_SERVICES:
        pass

    elif company == Company.CNTEE_TRANSELECTRICA:
        pass

    elif company == Company.SNTGN_TRANSGAZ:
        pass

    elif company == Company.SNGN_ROMGAZ:
        pass

    elif company == Company.GROUP_SOCIETE_GENERALE:
        pass

    elif company == Company.EVERGENT_INVESTMENTS:
        pass

    elif company == Company.ERSTE_GROUP_BANK:
        pass

    elif company == Company.PURCARI_WINERIES:
        pass

    elif company == Company.MEDLIFE:
        pass

    elif company == Company.NUCLEARELECTRICA:
        pass

    elif company == Company.SPHERA_FRANCHISE_GROUP:
        pass

    elif company == Company.ROMCARBON:
        pass

    elif company == Company.AQUILA_PART_PROD:
        pass

    elif company == Company.TERAPLAST:
        pass

    elif company == Company.CONPET:
        pass

    elif company == Company.TRANSILVANIA_INVESTMENTS_ALLIANCE:
        pass

    elif company == Company.SIMTEL_TEAM:
        pass

    elif company == Company.NOROFERT:
        pass

    elif company == Company.SAFETECH_INNOVATIONS:
        pass

    elif company == Company.AROBS_TRANSILVANIA_SOFTWARE:
        pass

    elif company == Company.AGROSERV_MARIUTA:
        pass


    return [cookies, headers, params, data]
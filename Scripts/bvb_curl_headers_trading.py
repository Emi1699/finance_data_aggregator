from companies import Company

def get_curl_params(company):
    cookies, headers, params, data = None, None, None, None

    if company == Company.SOCIETATEA_ENERGETICA_ELECTRICA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=EL',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'EL',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$9f244a2d-d5f7-4eb4-a4fd-fdfe81b902ea',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'nbmXFd1GO2EPK580dcfQCynJOw+6HOKWMqRcnQrnJmbcTY2Fc2sV9t/TDBaHuYgh4pIW/RIAMx/RZ5/LMrBDSBMwD+/OwKOeDzrX6U0ZYdom+fpXwx1o0KdgegnGv9xTNjE3fTpS7N58LrLZ12ebpx0a1Dx/yGMqcLIRRs1f+yJoPPZ7++NrrISK36AWjJWqYVHkz7lhaTFtnddynGNYVCpFtfcxoYHIWuJAF7YzPilZJi9FyBLPYZtBsw8Fi1kjjUqq7OIQd12AfUYzhlGLvQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$9f244a2d-d5f7-4eb4-a4fd-fdfe81b902ea': 'Trading',
        }

    elif company == Company.FONDUL_PROPRIETATEA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=FP',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'FP',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$4f04522c-8e97-4574-8db6-5cbe92cf4d83',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'lMnNEjgDPJ8UlQaHQ4IiEnWXxh2P+5P7F0kJARzIFNrVgUkAlWFFwz9i7Rr0oX78RtejQUySFcmxJmL79gsR2gPvbx9uOq9vyJcTX75/ShV2WxhjM2rEbu5WwFeVtyqE4iLJHGH16hVuQFPnrcAragA8vzwG98CJD+R+0ayFXOACTiIFHpdrYP8janpdz4qlg8cpiK4d8JbMzqfxscSWwiciTy21wJ5n9tTCXc6IMnOql7jM1OG8xeojxLg6BdMkMvS3ANcMzow4nVGzxlKg2A==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$4f04522c-8e97-4574-8db6-5cbe92cf4d83': 'Trading',
        }

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
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=TLV',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TLV',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$f0a1a678-801f-4f17-baab-5217907c6f15',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'r2Umzk8AyiA9iCLn0dewP7rMokCWvFiDz5oOjiw38U1FYAnmF+VqbixgP4BqPPgDWQBENF78OByMUzBYch4Eume2rFYKYpeu0CDrzBuYW2O6HJ8i9+IRDYXDwSA5m9ig8GRbCLg3F7TBgGV9Ykct3rU/Q+OA1tC73WPC2eHJuOiE8P4rqAsDWNz7TmZ0r9Xc8YzMEPd4BSjyoZslhslgOam1cZQrsNIJldUaNyuXqFZisrY+DlIrQU6uX4oiQf/luBx5q69J4DneeWszZdwqbg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$f0a1a678-801f-4f17-baab-5217907c6f15': 'Trading',
        }

    elif company == Company.TRANSPORT_TRADE_SERVICES:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=TTS',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TTS',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$daf83193-f8c9-4ae1-8ffe-c3679b5d28ae',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'rmApjFAGW70bGZu+CGwr54RhoogAy/wU2zJXCp7eC73DsRrV9XVmSg6nmKVlwGqubO8h2Ac+p8vNTvBhJ4BPYZpd4Syrg+3RmKbWu5UnMPGfK6AvP6CQYfpbF+0fwcGfvyoWz+IyBsHoys8l7+FIOI+QPSSh9qE7sJmntakMTe5WjVSwLcpmIbP9WDOXKndo981J1ZN1w2vxmSDDfXV2uApNEvzKtYbDWaNcQ296r1PCxijUE7T2+cFwQX7fVjJRf1to2QJ0vAykzbyJBmob8w==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$daf83193-f8c9-4ae1-8ffe-c3679b5d28ae': 'Trading',
        }

    elif company == Company.CNTEE_TRANSELECTRICA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=TEL',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TEL',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$3a5bbd5c-2387-4c43-bbfb-d858ff099ab0',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '1sSkLO1MBbXPlKHSmQB+MpY0CSYiPpgbgrXu5RzFcfYWpUsboV/sJLHI6g3EG6AfAjEvW4BeusVp1q29R/QaMBq6YbafifW7MrushxKr0XgUyEPfbSk2wEd+P4CcygyRFj3xKX3Ebc0otCa24MZpnGdq/zpLMG7nZ0tBxx0CR6kboSvyvsfNxNNhAOKfAqNi+XtCbavgBzy0rR5+EctJyqIb7AJP9z0KGGF5m0PCkDAbqpSKrzHg/ABTF5kYa4+AUwPwSzaFTD8SZwvXqd4lDh/qB8Rxhq6jOqMBP5PrwYTNHEtLZgM9UTTp5ZPNgrBa+haM/X2+D1zcGTPkqvI0fgnudBYCnAR5B+Y1Fp3eaGNGe8WNln6wVCqJu5fu66p9AXRnrWYYQY2lzpNAP90a+sGHzSJxRy3uVLPkhKkBH29zA9h/DK7IkIte9eXN53IglSej13ZsMxeWOdq/9dEG/1uHzt08D16b1NrLCuLWFdLZ6CUEd2hLaceHh+WCWq/l6gAoB9JjV0Nh72Pb299F4zex7QhUsgECGHQHYDCWJHg+uLDvIc78XsgphZw4E9RokKZu0Eu9gqk4FTcFq2b47fIoP6NYuqRugQmFeUty8mxPfrsyPolYm/zyjkLN1gT43XClDL6gjG2GPhrJlMQVMkAcIacGXx2iCRGpw+gKx68QXrYF8bQ0vkQ3njmHQdYVGRn5fJf6oF9BMF6GkXDSVcNOupHoaPnxTGIrd5TMP/H7kfj0RkZNTUpCWg5EHYTWGFUdEGEIa0INOoBNfnpLCJ/q6lBPeTjndlv3MAR5MgwsI+Acjcpt0khNaUrS5rE3r6gSd5kkuD+YHaQgd1+fGFtYjKJhTag48pXzPuGxrjUT3ezmkALr30rAnD58zKrI7k9tKnhiGd7rWi3T6dOXljCPk5hFzgtePgkxFjmzsChG3MaJZ/gvF4WnaUHP8LUxZIuc0FQmf1UEP1xxz/TovzFZhxyoEdo7Xxdnplqt7/XE5vqxxagPIjMd8KvwDlW65lHVBneucRMPN2b2QMpllzVYDbhfajX7UoPgYImzygG9v1/SxWLDGQ9A1YwZ4zr7ZQIYCXNRwNLTxQcv9h7Wm6TraZRJnKaYHCH9BkAIJrM4I/k4qIO+uwAq9J54VcssSIkTCo41He+606mHZlABj8CxfsA0illCqlHJhBznajMyaqKB13SrdwYTMX3S3+mvU6YdvXQmd13OHrFeSfeDCJmN8ttnE7UJ0Kyh4SiG9LeIwa0ZQhILDRgv2kb2/XX45gTNyPfHIPL1DiKboOJDT8tGQ31JCVmOMmzQqqpAJDdL8mss8GKs3x3hIglladwQOLmDWCf3b67bdxrgxIDwhMhhWAhUDHmMyteE49FlkMqB6QTj7SJrKEbQDe3XnqmCD6zms8vZP12+xIRFm5a1KUTrkvjy6tagMtNvrdC3bfqYS8l+IlvwVkjsiifZqeoKkkQkKtL9RwJwwFfbiJS3b/BJ9CgzpiDQPGLRO660AFRCoXsKuZU4K1/P08eN1/9B+Qjlz1bD4Cvhnj9FeNjrEoWzd91PB7ARLt/sYPBGCIv++cO+9CoJPvZxFT6rBYRveL6C9GeCskhW0PKvSq64sYkffyd7q9aH6t2lqFxz16Cmb3AzZK3nBO4ikAwQ0VgkpizX9i2tqvaOlQWoSG2TXes3Rfz5MJPJRNLFxVKOIpO0aFlTdDWfGWYtC9atHAsRoupWd5dRxHrUXW0lFNvLaAfxM7Broyt2/FhnOlopxeKCVDkImW1QC3Vs/k1bos2mYmaOyPWCpfBMZI+wmOKuhilWpNnIfucp15nbZREf0AbM0g4S35K25Fr+Po4ftod9HBku988c4hkOFU1FzHiX5nq8zLzBHe2Q4v5al4NPRv4Jdx/u7KC97X2Wdb3RuZY+gFkU5aF/nQVmsWgWgGOsGrkOy/Qsw/jwUMvN+jKzrPDlsMYzjSFJEA0UeEyPZh6CC7xQNqF//FCzjpS+9QH5ahcbsBU+7pN7jB0bYkGQdA5RurQNED6A+Lah3oaxyXJQB5A9so86wtAQmloQPe9gE7cT9OgT1g4imvqxBGfgTcTZekKNlDtgsq84itbgz/X3BcI+/sSOV2HAKS5Dt/I5yMKdTiokc1fHJMmUJwBPGH8WZdwun/zWxL3X314erK84khqCF4cTaMHsRUkBDGSF6YpVbRVFc+xQO8BJnfPACfH5tEjiAAXJoOCz2HPYjuO63YP5WF37JQp4N4E15WE96pKKTLtmYuigzemDFlZhrP1bDZobnp5QcLbW9NMBZVsefPzJGeLOZzT13MYXe2NucVQ8zsJLvnwbyrDX2B5q1PMk+cB/LS6B9l4tsEExBpJ86fU4Q3GTXVXGerB1GfNotGyEwh4OtW1AieL7ikYxvuSnJ2IFPvqfCVlz6o24OvVhj6eNWModhBrQ+zmoF43JFH/V+OzOG6lzzF5OC2I8pSJGkDwrBHnsohBtHdR1+KrBurVcl2ho4aRhZuavjkjdK638V8Jm4iO4cHJ8iuc5t1ufqdI8iceoBTWtrnr6CoAheCW1O+YedKK6SJNPKUrxdh3dVsXoRzbGr5vzfl77gt47UShMZag+8MGfGoMCEvXLD2VCSLh7y5PHo8uCLoxMMd8/velwPS36Srn11CXRI2GFwGxBZ41rdDCacvMoTsO2NspGI/5T8znisVXs9/UjcwU80UE9XWU+rHQnBTxGzdqeJGhdqk0kUnRK0MHIjQ9e8GATUsKSsAVehPe48QR+GqGpyxhtluoBLqZ2cEtfOfHU1AudoQpKJmB7udMURQP9KSzF3PsnWsuBeCCTv88Tr/I0mSo/E8N8lvuBDtwtmDtJLboGMbnfGuOL0RC2qyikf/wXBnxqYEGwYRBcY/y7IyVGRTYRQsOwbMnV3XuoRfumRZ5pWqR9cL1Rt0q6Nz2xnoYWn3MBnVQqUaiKbgc0VRW/gW4+T4Y/9ZG2+hkNvveLb4rQc1QoCfP3mUU2PQGpa8lx6rrl9CMylAsCyqTuPpLvrlErHylSieOGFH73tcEBYn5ug0eDZd+2UqWe75STnxMSYyfSrMPEuL2zfyi8zRyslvg6ijM0/s/DuzI3GKU/SpWFFjcZjx3zWLbOPdARmAEq7lJzGHK/xu7icUClevfXFYpiv7VobdFS8JqTRVxeZ5WqsoTisNRuJ62JNEKwkZ7d/G2duuZnEfNBA8k0BfxDMDtlR8I9X5sgRRthlKn4/vQ8SPTrFESNX02yazoGOdPWDLWAle4SPNkJ/NiCIgBT7TaqWtPOV/sGOO7Knibd7o4Kms6nSx7nVt2wn5L7xREfrgCtPoY2m1i9gx+B0yEAuAVdqoTL3tqn2OW+fRf5CALPsdNsQ8HAfDrTmvriohPiDNM2IUcQVmkFkBIkwexj5PdbYV7uFE4RCSL1afViW+Bmpzt9XiqzAbqUr15bfomHgzzsYYdzRm8chN54uWULGbe7V3OPrQfliV52LpV34BsP0CpNr2YfWAUUuDkt1hxRYuR3VNG7+QMmkti4QP0LitcvFfJfURu2XwE5ohpA1xyBuH4wI1wMHUZzWkklZHQgihkQ6/MKBfZK/RZNkyroN0QZlM7RLuek38JHtxVK443QYUk+cHc3L8EbWp6Ab0HmVqGB3ED0fABpLaYZTr+PAw4ctwtXsqoDS81jV4L+mHctwlTDVkPJ9jGdr3TN13oJu4PA/BOsqZY55GAgc8MoS6BszBhbhift2A0Ots1856BdiOOz3ZzVhXhZViWH/hRnyjH9aW0dj5EEg5g4sCTv6Fhx2IHy+jHl2CK3yHTwWP9VpPE1Oco+0qU6p+8YES1ZlCvhZOsBcAjpoMWYGvzFC5klZJ2oAPZuskuRzgQbG8731Wky2fO/trJ/ra6ryWQnWg4VwgGgL62f0x6p8j83FXKLrFLbOUiAKtfOvRhnwe+QBbE6oP0u70QQoAmqExWuPhVeO4VdMimVOUDGUspgneaiQgWU16GSBVAyK3/UFRWIKvkaIUcsQkRfhLLmxRnGDlXhiIG9Nrn9S2SlFWBAZu6rU2ioGY+/3O8zuhh00dvc9zVsnnzafoDOPHWc5VucZE35VfEiVNwGl3hxstwukplvxyqiQiJRsrwervzdGU5XHuHQtladvh72tqv/rzSSpYp0zRSmu0I1zzV5sULVnFPjAedbJW/RtC4pDEWYydUh4AOTgs0sX/RqJ4XSBGegctEYESCnqpuKnIwFXb/foiKASF6ZjQIIltuB7DRzx3DiEplYrADO0tLuRkV00C/BneLxnT/F/C6D9n6eG2b3cXSs8AL9p4Z50UM0Ga0lwwzB2IK0+egwut/oFR+xyij7qIvq9ZLyOSx7kiUTdmjT0Z4c8MnBlb4hk5kVfh7MniiRfNv2Yy56NWKrkNf9XrGi8N93weDnpnEKhcVC7GsRhpaqnRJDTZwlzDbv17yMlDzRnvBQgtCId3qMkwWjK3zOP/CwyOSUMk84GWNQjQ4zmNp2m85bLpjrJVKwQF/kKhxhfL+oSIUmMj+3E4FlW+vDGSp0LhIAkvygXF1uT4HqjGNiMheqQP73rieBWky9nP0mTmPJ2eCj793ORFgNrK4E0kWg3RkEhvPCvcZwN2oMKDEClohimGxdy2BEN6QwYFCUmoHdxfYhZUk6xSeJy2mbfS+hGT3muFQawnqM9JMs23RwjemJ5zfu9xwtMuY4iMStwn5LqOvqaY4lirYCIZtyIfqU28h7mFJZkDsopFseH/GqMSCpzbbuTXQYKM4=',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'p+ItEu5IzF42lho0nyES/fxnsItzRYuDcwgk+yBZVBVl3Cqqv+SQgpNsCjN1gMiKqCnbRGeZebdZyzRw5gQvbn14zvts6GObuHewoDdVMGnxQeJenv+8ZMku1H58wLg8s1MO3cFzsTGEBJD9WnzUstqc9uzm93FuEof//1p45CJQWptfLCRPHzLiBxT6fBvfeaMXRuzoCLlAcwUWgB7CehkydtpQam0gIsO8JlWwjI0QzjNHbjKkavu3Mzmi3R6tipEd78JtZlht4XP53AoTXw==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$3a5bbd5c-2387-4c43-bbfb-d858ff099ab0': 'Trading',
        }

    elif company == Company.SNTGN_TRANSGAZ:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=TGN',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TGN',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$1f3fa9f1-b909-486b-b59c-f9eb21b45cc0',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': 'sWCZGQZZB2jybceJL4QhcmCCC1dj5vbejW6Bas4AanYrfOpA/aKmpWiZ0S5TdFtRnKBEg5lw6qhBfoNeXKyRFjUSo+MOA1ncYmojcF4/RmJLP73OZ1WPR264Yr9WVy0idvtiupoQnJLqh3yI/T3+gh6fcOgCl00HjPx0e/fQzQR1lgS2HQgJ6kfuBIewk0IVVjayR6sk8NG5X1omoAyurFdQIVlL1q4zKW0u2imi/mX1776oVYkGq9z3I1cAIN13H404cyBrb1FN6le92L/FhDi1AfTSprry23TCo4/e+4Z0EKSjXjvJbbElqAMbMaS/hZmRHK40LCzebtMJDwNpF/5rihQQhINMlt3HVX3jg3T2TAfDFe+IMBSKq1kcFEmiGvVeBeftnwV5kPNnkf44PhmWzW/IRm8MmBY9ONWPvMaGfE9SvaMYzwqqC1w4nCIwbngT0OfGzLVZzEYL3xs4eD1pfOyprjXjdtwJcTMuOlqHBGe4dIOyaGsEHs2uRSQHpo3NAGWIOY6rocVvjhARz+qreZMGoBCLAWfj8CuqTS24vQsmfImsQucQqzfnoJxYPi4fhrEzhdqTGqGFIU+GglUMhrcHJWg7KA6QzBIK/fOAG3WhdKaFEelRXF72gD0SuIyOpjrCFcDaiPz1Au3Dcko1SDrroHKLoqmWnC/juRvvooVJk+kMcDoJqTAugF32K4Kw+QUfZNRblLnIhOeekfd3o+d2Crit01zRI4RCxhrfFw4aC0vH2CTtq26XT9r7T92/ppcjKqgRWpOCVCxSxahPSf2bc4UgbYvQx7Jhu8vydxLzRH1FML4WewyvHt9whQuu2hmCkpYSqrMu0KuGVJI3KGL2ZyvHDdvudgPStWrBqZqX8IbsKKrQY5xwevWA+nkl08GJyrh3WGOzDMoPjaA7cwUQ9R70Bd7KRX7nHshxZCm9ZD5PrJKeHF3jBvN1yQjsYmKa3JKfpHBSR8nh2FT3yvpT+HiPKUxYUDDloM6POhkRZGlCBNNqNpe8YBsXzrFT9qSU8UzE9hFXADROSyjnVOHhI1aJj9vp3JdLEKkebDKt3dWiMaJVzCI1XC7gg6Um84VM0t8oiU/a0PVVgU2i7rn/1ovragRAQYvB/ukvBhpT438G6k1hpHJMJafIyY+xgMGGfwz8P4yZl4hUXpuXJjnm+GrRtFpFciIg7mR0M5SepRVjqaGaarghG8NfWOFYUybL38UcdiiniQ4I2gZmYO/57NBfOAt1UX9rM6ZR/CN/SyjDUwPR0YBznCdQ9RZSab7MqnqLg1wEBEIV+sLfUx+Bb7UNepXERdoUS9ZikFdPrdpwF1ATDYNfLNsbQf+GA/fT6bPLPmWGnnOyW7MqVQlaTbWRSP4vPWdrQI+5uw8K7Elaoo+TXPBFV4vHf2ToudD1IbU+vnVeJV4PjdR2UBUIfNhER94aw5zn7HVwODkTSXoAjcn//kiOXiEXHBRVnmTM2H8C5kTurNTGpadHdUMFYV81y3EbrYkX0ElUlFBa488Ba520xe0T9eJYlrw4/UipsWELtDv2ZwQ4jRHUbJzX8DjyVYox67/9otE/d6qiJWKy2w+mXSiHYyH3+mvTVSNkkypg8yhF2DM96CWRByPIMYc/0Pa53EQitIC+QSnupHwbfc0+EAN+uF+EmCbAka2uyOCl59fC4Vno4nDjAFuzi68HF4Yx0QKQRJYx9PYy17Doilk+XFQONTJZQSf+AotznoOXiTH1mt/0EhGhlKjGLpGIOAieicKKIIkpTLfZJayb/Npww1ge3m9nmZvJjT8PPNlTHR0jz0FrKpE24aqTVyF9RqeUgCsed0bNuFFQdp4UDynB6s8KsGCUrroC2kopCvtPIvjY3bXdPe7kxl6GszkUwvUFKnEFgfT5jt8N7ROP1xnwJaM//dotuA8pbS8VWZehmBuHRVZE39+7IPWs/KS6C7LeqkFDZXRz0ZohvbrrV0gT5hIhMEhMjF01c19WxFAXkyRy9ONszryzWdX11qlRlcmRM+HHWRAGhSlfjI4lL3wZe6Uo7u4S/Zo1+OG2h0Kx6YxFdRHOHPzdyhCI5N48xTYr/id/+f4tGnJ+kW6/NhDcNo72f6ylzpaNQAFuxMUBb/Y7+jLwfEnDHGVZEGmOLo1uPSvdH9vbporTiDe5u+mkhsCaXGXGewc2zFhAJMuK7QzMLkju5pRVzjy1WLf5gbcCWl+PliNyZ31cFpk0D4FsVpH8o25ueBhCaLq1b+CeZXi0JDdsl0ZSRCnR+ak0a+EPnlo/IvH6UkR9i2D9WA5J25B8IO4TwAAfeiBlNYeezSSIn1QKjtqnhsICpdS9XVB77ZFPabVyNXxuX1ehGI87jIp8ciAt6VaAuh/j0WTvd8USd11QeWuB18tMm7/qDTePODGaKnf0uIABoiIisK0u+TtRGRt5WFt4+ZY8kYX/vNVywD6KmA8mLOxPyKdGt/sCuxUMzPs7gEpoZd15kmmviDbdocMURwCl8RrW01D7pKdqDzZh1A9UX3w6Gr5s/drDf/tnlZqGmBTl38Ijps8FCoeUzUwGJJK/X+DKjk3cCJmCm4ast9u6lUbf6EE+1bLgW6gliaQzqWoFwPosF+9Io8yRwFhxBr4j+fK5/ASGGcAaBfA41RkSQJjcOusykBvbpvtoak9X+OlXmbXx5mtQApmVW05IC526+IPBMN7FyB7DuSG7JBzXTkgctoVkUzD2Qgnx99wt4hDO9tACH7MpiQSseLS/NZj53ofSf6dL9ZKLoxI87OTdoj2gly887///FuA4s1WAONcBXoPgmsGFgDri0ybv0UTsFdJOlgYBytCCB45n3gByxIoN/Ob9E9WyhcnTpEwNhGcZEIaCdcbipq5aIqyyGqCMRc1FmwW7vOw4mJZK3JO/56FgR5Q/ckgDsKwbLFCISwyYN56QEOShuPiunaBY9A7mz+XUy7VUb/Sp6pa7559m9GS4apeGfq+qpFydQvQ/jDGy3TGcCBo8w9dHUzz/sAgyOtGpZM7YFXyp4nfOz8mzT4WSDt1KGiPZJftGCOR+IjZFQAcigr7NykAMG9EwByc/4t94dia4ZAQ62JEvUIZPdGNQeYc9VGeavPyutwIvkbfza4v/k1bj6FFVCSjiBPwf94Otmh+8gJyR2h2TLvC34BadqcoT65+hrUVj45C2wtbh+VsEXqAbGFkmyQRxCgG8m19czW4eK8sSxD6CKMO98IUWrtf/BpzhK17TpxxRaIBU8ELMuUwuvKq75m0XjOFztB8FzQK82dV+wWNVYqIpVONlMkYL1QlT1VDXfPLexqGbiHvQs5Oq9Fm1VtaUbJT+rqu1VRkN3k5x6fzsPrDpML0YUaqIOarry8HcRuglHkx5Wc9B6UKke1XVzyZPo5VdmjP018L4s/f0EDMsC82386DeN/IcEtxr73PQW9CsNyoaQjqV9xcIZWlaEfPsISO1Sfl/JiH61o/Jm2RSs4CsCBzXDH8ZW+gbijMuEwYqsb1mUNYXMJwE6OFcvvwahfNQlltkNDf4oo+eXauF6Jfj8xljRoztEBAakpjsgOFvaSaAvUOwUJq0hVMBhPvs2kHNbzSZeoX88/pC4O0O2AobQn1A6fQzmQI90CI6PY0/vFjp6jyef63H08So1t/qo4QB0CKtCG62+C7IrjZbsWQ6ZKN8LDh0Mj9gwDUj/+EBLBck9vEbwjz/aDp4qHt5HYR1rLgWwxrYKsGN4oMpaqeFIb+bZc9Bc7zrv8xAOleWrv3SUz28TarSu8vWrD0JqPHVVJDWej+P4EqKPS6BI0hM/kGEr91NXA7R8CyNsaiE4pJvD9QO3qsMAwZpTAOzjQ/+LjW+wd8NrtUY/VQ8iFIc92gqgdhEzNceWNGyDfxqj80FfVQ/0jLIe3RAAXKApkHv5v9pp9n8HI9e+f0SOYM4DGDZ/KJzeu4GwFS8ZpQ4wHZ8QEZjY2QYE//IB66x7wX+R+wR8d7NQYlHhcNKcc6TJj4y1uB5toRif/rcZGOFkM24FuyOsU7pXG0ZzbydDGYuMtOfWqi60AKbDCPRxOoQ81MeBUf/XPuZ+qDe0a8bf5uMKAsmXln6fpy9UfuVL26OhDCB//qCxCBByrfLD07m4YjAYFmzwAyirYL8FqbAa90aeRiNZLdv4+cDUAvjWPl2S+w26fXB2heMES/AVaeKlv2QMoSkh+4AvD86dWSzNbcoDGMEQyOoly64wt3cs6c/06aIfarRjQiCWyknGoS6g8qzFtEp18vYZXhLc/8EENOkuyreZ2TQnnS0mnU7nY8PwM5rZqcIl18JNld9nau/nA3emHJpZY7EAnL6M/b/U1/fKmlR3schcqgA9LNHGQJeCQg3ppKWwwsktTwiC0aq/uxaqR1rE2X+GzYf7fsMelR+gLtKDGFJvDme+XqQSP8jKJkJkOgS6qvQSJ9DNhePivaQUIwJvyA7zQArES2iXLjVE6Lt7MgisPXTRlRhroNDwGxwE2DCQo2Uh7mfAIjnDF0qjM9HVQgOLgPBtqj1sPMK5ToWrCoHKVQZPu5MZ6Wwe0B6ESXGQN0l16ScwX6pllWky9mHrAjZVBCpbbC2QYcRHh2WOCUKfS7IpB/uJwTnIMQCil4WRn3dn9wBMj3zDk/T6sMwtpKKQO1xr1FjQJcrJxiF7ONC6IAYTRMoucexBnBKt+a4mVj7E+SsgLANVLL4yCV3XYAYPfAqJWucZANVQDCan/jPSzvDsbFHsD30CIBgyYPIrkH9ivr+KxYZ6awuS3sXFiJPPEuBI+I=',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': '5KRkMCBapXzx0cX5VW7fo/Ec1ycI0Au68zLPsZL3JOK85GG3gLcKNVgqS+ZEOa6itWjlAEtRvUPgqOb5MCT8i7VaAUbHzK6UDQoaC3XUCCIyyRxADAcjvz6bJH3abzbkhNVMzC/3f6TVTWplfYZ3/dWzeccm21CmiPZI4tO8fqQj4CfbxYLFNu1X7qTErUyVor9lF6vQCjg2bjKFVinhC1mRd/31VjzdkBhqUphRXB6P7PRgq3K0NGt684DR7HEOkg26FEp9V+R9o5U0LXKsUA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$1f3fa9f1-b909-486b-b59c-f9eb21b45cc0': 'Trading',
        }

    elif company == Company.SNGN_ROMGAZ:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=SNG',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SNG',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$986b82e3-37a5-4da2-aa60-71e589ad1a6f',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'pOtpmBQvpN4RzGAQ2KnltaqcRN8iQhO5Mkc+/OrarZVwPWfRFGCh04n5M65Wh4sfBLjq1Pvx/56JDhSMDUwjhGQiyLQBn/9/X0HuahiOlw9DfFMeKVg2PBC/Pc5/8IoYe4ZqXvIae2BrFpbTsqvHaou4QYqa1yNjGaB+CNsk/Y4CeQKIJwFqdb2jdp65a0LBy8Py5Bemom++NlpAsE1OW/5T+KgecVFF5SgU5mrg1ASfc7IA5jvl3sLGyY5CTr7+EdelCm45HkeZ/oRTnpLm4g==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$986b82e3-37a5-4da2-aa60-71e589ad1a6f': 'Trading',
        }

    elif company == Company.GROUP_SOCIETE_GENERALE:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=BRD',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'BRD',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$a220f018-04d1-41be-8cf6-cc92d78743d1',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'OFCZ7JWeKi2MtlFkxXX5eEehmm+pLHDw+6Uz05zPS08h27RpbHF6IQgX+Uhpl4dmP10r9eI/iUhj5C3RHstZ9zML8TumevwkEVDdO9nAquRkr7XeWc6A5G41dw+lKNLJ8NflszIAWeiPJvOAQdwbBWXMrUU9x6DhqZaUBp4NArC9GFdRzhZehNRyNEgNllsFTlNfHVr8TyHFER6dAbJYcHgLGmV7JixbKj+KY6OzpA/yVCQ6QX4UXEboRSwjIebC9RyEYegdfdOOByNokelfDg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$a220f018-04d1-41be-8cf6-cc92d78743d1': 'Trading',
        }

    elif company == Company.EVERGENT_INVESTMENTS:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=EVER',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'EVER',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$ad36e3f2-f9dd-42c6-8d2d-876c5f7e246b',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'MrZmrH88COUc0asYAi1Mk3c8mWWxm/s8t7wNjwYbY3UPeXHaJy8oksmTMWM4CoAmXajbIk6wnaGzXLOssqMHYLD4yALq5BHX4qTYHXzb3pHu5AdZ4zzE/H0NgFQgIcpwRb3qXoLyh8Bs2m8xTG2k7AEv/RhAZ1vd/gITbwoiF1TtIzjqj2rBrqAsIixDXYcXERo98Ybq84fnh83EIO+M62Nx1+sTkD4542RYiWGpWTrpyL7cIo9pMgHbjHZ4X3d0Rg+r7ZVr1mV9vb+/XB+LkA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$ad36e3f2-f9dd-42c6-8d2d-876c5f7e246b': 'Trading',
        }

    elif company == Company.ERSTE_GROUP_BANK:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=EBS',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'EBS',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$d96e1c69-c962-4f39-b44e-9b1ca125bad4',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'AettNgwiU+wAXZbM1rGpnuV+bigmVCFlcXYrDga2amhpSJavuSKc8yOq6LvIoBnDLd0BRApd2fZ0EGl3PpxJz5z/No/y9H/8YgJHDcXd/VU3qOLvVxKC/ZA2X1PQdi//xd+GLcbcKQ6Ss44l9izgRhmCcZzAQQ2SjYzelvKvQiVTzAt4pyfsi+n/R0lAoYnQlnSGgtoCs42ACKoa4Z4iZ0H2KXqnHveiwuPropVHaTVaTjPI9tdq+mitYgZBt6D/+XAAiNPYy4oHs6BLKgdS7A==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$d96e1c69-c962-4f39-b44e-9b1ca125bad4': 'Trading',
        }

    elif company == Company.PURCARI_WINERIES:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=WINE',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'WINE',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$3ccddf5d-847e-43c8-b92e-8fc901aa1152',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'tfYA1Wo0fvCQystHUI+0kS6lDfcKp72iSwYiokDXo96pcbiVHcOxizGtgrptp8FpyUe7EBTfe3NsKiQJmB3Rl4gcYdf5MZNMkR3wtUrZUZzEBHDHVXWjXXyorZNfE6SQk43L0qpRU+cd9QHI908YWNxHIDUp6qyqkRfQW1h314nm1ozdfwRaWVOHKBR1yvLh8iH9hXf2c/K22M70O5aAlHV4CQNsjHjJ0YYcWrJsBm8IB26ONCI//zFBro2CesEjGXwve4PkgPBD9hHt0QBgkQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$3ccddf5d-847e-43c8-b92e-8fc901aa1152': 'Trading',
        }

    elif company == Company.MEDLIFE:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=M',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'M',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$21184b43-ea08-4e42-b852-2735d6023f6d',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'unzQN6EPPJEShPieYXZ/5GaRqr4C6UIw8LqeSB01oxKn2yJd7+TqPNmgWR7gYTBl90woarlwbNJMSIBKGBYolAttEU5i8/I1gqcsz5DrmkYabJTMhMbnFmtNjjutVC0HlKLgGyAZ/qIfJq4lxi+gRtVY5Klonld56MBQVDs0TXXwDiRg+eLThdaZgCe9kkh6PuI+lBQ8tjjmQlzEdD8PhA9ydfluQXNhBzn6Jajz20c5UPL1ut1mi19UYLU7X2Rcj1nx+rX/i54S1/HNMr3rMQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$21184b43-ea08-4e42-b852-2735d6023f6d': 'Trading',
        }

    elif company == Company.NUCLEARELECTRICA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=SNN',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SNN',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$5eff1f9c-71ef-4333-9906-9891258d1c39',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': 'YjG5MIKjdMKEnLqwkQPSYjGLirySBM5p9hF0kXjo94bDryUJ7y8WSyEotuv6OgnIHxJ8J0RLxZR2sccLNDm0+Fp7qqf8lZ5pzXa7uD/MqKlz5YW1PhQosnWPyDcV2JWpMyjd+fX+3JyO2YJimynlts/bcltNejQqAh+DLTx7TItAWUVJZ8rG4/g3R8osx4+qyVWXKJEG5rN7rLU9ckdRtiNx6YF+AgminkNm438DleNdzgyNaadbuOy3SK1MI6NpWNSxLWlrmEmCAyp4AjId9g/9UIYCiiI/QbgVaRA5NHSfUeb+0Kw5rLZtwGmik0Ty3en0IYoK6sxFbCfwSxXCDxdUMQgAEK2485AZTia0xQGZJnZ4YAGUmVJUe6MQIluT9Ub6EMbuK2Da6Y9S6UIbIzdCav0rfjXBQDJxBhzuRzAXCxjtelKRae+2DIhsQQrszQ4hmecuFB6JcQmmqN2IGJu63czkb45D7yHrSLFuTTuErGjcUaEeD0J5pKJwvTZfZxkW8z7OvlV2UgW4Uom9jCYujkQWoNMKQTfgfq/LQRg6EByX0bQesCqiLSsyI0wE4BjM7PUElShGQWCGDlqZ7QvTloDaK0yAn24sFOv5VCYkEyBYdjyGsxbhGMKz6Dnx0ka8I8B/uouemK17x/7XDSX+OuC/N37i2GWdagbfEkwI/u6bZoqdWjcIRl6LaFGUMJHlidmSX8a4SGVou+MhVaEfD1NsrXDMDYreqyfqRxX1TqIeljxn3MFQsnuPuLvPzhAv1XZ2rLhyG5RlADnh4mEwBsNA7FY/3n3kBaXcQTFz20kmtJZ8/8a/OSXoZ9bbBhAFF4Qb6qL+mDEpwtGCzf4Xb4ecKnuu2lRzhNtElVDExJt9Cg6EaN4EISQpYg3mTNjRKcowhIcuaTZVz+7XWq/uaF5Bw3A56dSo/5XOzkU86E3AePgzLCC2yRHcbmkDqRht5C5PqMbIcrOvIfbgnUC1vIExBY5TuUR3zCiEZLfkQiJAUiooMbYrg1o16KTyluZvl7NE2MyVp6dUu+yqT2NxJvLOWxVzEwSjnbDkLyK9Vnwkiq9veW06phs9mVw5iJKk/l4udVZDa/Dl2b2S1+dTPJGOoByPWSit01uvmVWGxXsb28/8ZLlAYwzR+PkOV+dHPDsoCtkdUIN7H1qDLdLlxdlSdVm8zvfIG/0e9/X2siwzqKS4z2our22wL20Rd8Ut5X3Jwg4I7jif3Di9RU0s/LlMJCuG+c1Mbzfk8loVGi7hprGzx34npuHdAweTJtfM1J8jZbAsPYO2AZNRSIZdSZRctBF6UcBEXYgIBC+wymCDJKbAl+sTTx66f+W+W3aHva3pR3DhRU3XjHzfZ1VLmdHp2lopF+mC5GWhmHCdIUkzj9ogPJ0fPxVPlLxShAj4Qp8xP09kYo1cv1ltrKv74aKXJTQK1xuiyKkEIHEiA+Kc4beUP3A/X3CxyutyIWJbH+H9zHgrVZjI0rHU0Ll7CkdifwqFdKrooObhq4NItkK0yL4UekwEqpOFJBGJGEQlpa6FSmAjeXcccvQAi9HmHAwZ/W0/M1Tl5upfXFUIew/Jw/DF/Cc/xY1JQa7x/qZhlnSjZEDGjg1DVcLXr9NTzLeyDWpjDHoIFXn1GID7yrhgouSPV6FmeODrO6TvIIWwVQca9Z1P9HGryjsPgL+38k9AJhltvPPuFasPIFWSOYZ02xhFBvYF72lNNna9qU0uUOlS2RtkQvxm6hrQOQG4UoRKRzGHsXhCt1D08UXAvpRX6QrzxHCZCsJeBlErHC8UhlR+2Z5bguXL0IuJ7RNkX8JvX4jymmJftk5bu7qLXrkqAbBGaHUNghHVz7nAN51cbgFAESwDhAUWah9foys9nZYy7eHdgG87u6PH5FtfOnSlghTdXGIbLF2lIOIlb1V34S4pIjmR4p/OM2F0yZQ3ja9sghAUER+e5AGWc7Un/Zgk96J+c0ahNE7keiWvIc27tVn/cXa7ouqAURK2vsUO0B09eDsxBugqCdCp1yDR2Eh5B04xfAqAE/k7pIFAtPHtsmYPFvR7wnMpB2VU9MOLVAfbGgGDuzNokkArT46lNdR7XkP2Zvm1/ap9e/PxUMZyuvyN7c4QrjLWbQzktNMeidwX/RLq9E3VqxUcRBSym6/hR42lowQ2GUECx1bh8Q9nqW304oxd40Jyv0V5/V0gI16omIrtorAc0Og7voaiagspMqMuVUDeLaFuTRPN0iMab2UDl2XSHHn9zrXiW6EY/I4khkeBbxiiBowLKurvNkzH0MtT0UJQIyQAF03fJ/oG6tTTW0JiVTvn5AKgMOoAC/pdj2qp43xMaGPy0s0udKUwXWUA1hgiXC+YrgSXa+0/CSfW+agpt9ltTpR1Yz+gowcK3pmpToPCfPuYAlsVvAnOpsrwlr7X1JtYBj1Cd89awIca2EQGNCa2QZMilHCCxbeSx5eUW+72+8iqmjjBaI71SjmnTYr1dRcWd9kej/ZiMDvmcmAW8Mtdmr/ipaj+ylv0qXkIpJCN90GTIvjyPFcFqIfXSMTigLFdAbXVkwB+3S0c1KbSa8LhHWaxBMkB52wImrgXqoGvPHA3ErGuwEp1i1vIsbreshR0z4bfeL79mE3hdtph48mWf5fZ8q53zIy5J1gKZn9oTcF1wvlPiI8HOOxhADUxlLiFvZQHj3/p4Moi51nadFyfh113o6tT18Wv0F0WxQurFYBUJWwIRutPODIHsTfDqs+hqMNZzYqrTL0Jj1UBZLiPDDNN0Pz63NHs9rt28FWZxww0iBmxzz/jIrt9hylAVfF0sJHIf32xB4EZwuftoaubwhFp2h8cA5FBTHvXEOvJgrXz4ios6H+WX0QjDkBUQdEmICTk+c4se9E+35KAH1rXMMOp501NLZY8W3aeI0VHzTmSckX5xBuJKkxOOlX2OLvz2vAyjHdJPB7gRMT+xwYa0m09t/1fYZtpj1mxiQ++NBTbA6NqYE3Ng3TsLxwqIihMsRvwz+HiqBnWpBbCOVy11Ef0c4FKNHsA7vFCyseR0Ng+888eiAOjGQ+G/XSaxpmvuDRFbV7BE8U4qmReZ5WO/xjBjOncuheLnxLG7aGTiW6K8C71V+PBhvLjx3tau8LxdJhY146A2zBieRL+mBZ4wgSezkRAED2vBtpoeSHAYtrsdXgipFZV+dXoDRMcpwFZCtMs6Z+GjlveZ4qJIGmeZIy7wefW8NGSR3IUvMekL42hkHTY9yLamN0pHWiLDT/4bwxIU8Cg2S5gtEL1PLCNX4nOynMKgQyQPgoWDRUerBRUT3dkxqU27dy8fF/lPBGwk2c7H+2G5WVoIqrGC9xJ3Y5VVgoYzQ0WLuEUMfw44pgzdgG8ke1xE0BF0Gquk/W7Tm+f94vnI/XwRz/4HmtsAXGltwNlt7+lt4yJC95GnoikBlYjpK4xAMMJpMH4yYbTX3svGl/LxLuI8JNdeNY8eQxBRj3NW9t5Fy27lw57Ez6/yDxjCs311q3AQK/dxKVuTnfIvqoZiPIJo2GMDJVDlb6WIq52Q/rw+z8DQznD/6BbHlhj7caPUTxuqIpn4qi/SRY7Ht5WYyd0afc8fBj1QWnNRNnw1YWb4uuPasgXUVCk95N+2C6Bz3SR4PQy04o/TykZQiVFDIitHyiSD9hpgL10xkkU78sQapmlk+5ObUIhq67eCYuOjKhsMHvn5z6ngdv+QNjYmMXwEcO7Qvc5ALORLB8l8Kvb2SYUZsNEe15V/RDnbDMpxYH9im411kCg/reAaRQtKPAGyzzdzdnPw1RSyOKXjhqbPz9LltQKFOW4tNNyq+roui1Q+b3i/TpYfO+7zCf9W9usiFJHUeQ22+RSfjeuOW3H4CsMqOz3qV0/9lj1Fakv7VZjLaV8yKjRDRn1k5hozbw4eqBJxgKCqiaGmG1iTqW7UoOwcqrsSXw1QqkzfB42bOhPOYaHiHfIX56VL5jErY9Eu2ELDlp7T2+LhNDIOWgn7Cjjax7/b+E7E0ROZGe8b06tP7lTEbtqdvW5E/2T3K18e+xEgv1D0sueJ33nBfxyRqtQy5UVCk9wgJsVGQjMi4nGI417fAES7y5Z5RzPxbHSrMZP9t+wDu5dRPAOoyN1ZOXHaA8kt6ocbXmgH9hu+x80D2VBFXmz30QZsMF2veOTvRlip7uc1z7CCkTXqPnMLpzdiTR5Jqu4RMN2yPhdob5RwrOlfe6TF+KJP0obvh5pxlIy2U0vjaxXlCqnv7LvjauMePZ7A92ZizwmisDxwLSi9j6Pu69a405+XGos7gk8QQYpMgGK0YJUpaeSUwi22hE/BExSOWjjS+3Q1hzt7zlSz+2Xvmlva3ONddmGaPeVH9eMGniykgSwDSvVNRCiqtaYNOQeieuCZUGmeH5M37iQAkDLgKvOcKHstleZyXQOjKnhNITKl5rS+srWEonc+ByWQbcx87qJvSsNHlPL3wwGYFD5dm6SJf2thEn3xic93F24C4oCmIeUxvd8obS9CGkpb0KDAF5LabmHZYwYa5S60Mrckfduv3lBmp25TSq9LFy2fA5LAOOgoR8kGqv+V5hu/LVt/8TYhjzRGvBfGHbBi8WBTcTEc95peyIyOo79/zFZX4SkRmBX1MA7UV8nISrxSxuONI1ToTh5dqY+LEMnoME6z0R36Va1xm2jM78+gFy8dR3KRkW10vi68x1yeMIAd38fq5NnCGDex7kkLiExzgjlQsSyhc/oba/0j5MyYvtUXlrYQhk3L2UD+qSG+9a64BWmlcvtr17k1j4WwshbAwgO5qbcwIyceLVMYGwy+RE3JwAPeyvXZzNvQpLKNLvWn/79Hg8hNfpAa500OzAc/8KVoEBlvg6yPtb3lyK/y0bnKJ+cuF+YGSISP02WNTSkvEDhBIA2qAR2IHrbflxNTBA2S3tsHzg0/IXIbyLzS++AdI6yjB0tUg==',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'GdbMDVypwDnefZq47Gd3sesF60QXYFkAAAnLiGEoob4vWtkst2ccnczXTkyXnuCg+6htARnFDEpPKEoOgtv0qEWmlmKBPWU4i22T0cKmraFe1A6zhDo3ptDzfM9DCh9fe9VjMhvDPeAzdeRgEou2ABD6E6BtCOs81Kkuuv3I38a5uuOUsmtcEQMirz4SOaLTGuotKXJSbauJfWo5ECLpCQknLSAVyazKM3TrPrDWFXuqQLOAm5mLkiQJ6aIDp3kDqv8TAG+gqXVR5LT6RvPx6g==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$5eff1f9c-71ef-4333-9906-9891258d1c39': 'Trading',
        }

    elif company == Company.SPHERA_FRANCHISE_GROUP:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=SFG',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SFG',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$d51a4325-4d4f-4599-80d6-b231a17a6e3e',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'jXZJLMB1195fa9CDeRDFaqXmcmJKnlByr3pMwblT15+udbtbQsU1oaO1/t6OJyFqJZjCJbG9g/59rPiUtSP3K/jL/vxhriVp4QQFl9kD3MVWXTsj2822KeXUiB0VTArnSoVfT3Gg4uqCvJ1O2WL1IL5GMxAx2l+aXnLB2qZh3H5DTqNWa37CJ1dw7uK4/zEQHBnxCQxPCg7apNR3XmW0ae1Ouu1HC9Mkq9zQKcE8gGQFZ/9hUzI2MRqqHvq5GM68tms/9EPjroZlY4a1A5qLEg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$d51a4325-4d4f-4599-80d6-b231a17a6e3e': 'Trading',
        }

    elif company == Company.ROMCARBON:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=ROCE',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'ROCE',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$29e849f5-30c9-44aa-b943-148ea6cd00ff',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'QNgizbHR4b2TkFqK0r3K3VIQyBUXgP1mIf0PWCsJlQlPbqhradrnpbcS0LnTXNCtqnoouVC4QaBD8RgEiNHSg2pjUTk6hNR0aLvLh6riC1+CyJnGinHcrhAH56Gnf25fwoiQgaHw1QLlw3FotH/LqjpeCF8uQWV5xsEVXlWEZDb4M1OkdWt10duUfjTK2i7B76zf26HkQLidp6FwEooLA+wptw3EVMvUTvVOsqd+JILk2bz/uwcAxk/99EQcqgUi+URoOlUbVhbcRi5oLsGqrA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$29e849f5-30c9-44aa-b943-148ea6cd00ff': 'Trading',
        }

    elif company == Company.AQUILA_PART_PROD:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=AQ',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'AQ',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$3bd5e135-a3ee-4e9d-bcc5-dfc2a1afd581',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'gO+YCLyPXDzmGHZcwmvb0LPUqoCTEyQfi/p2Xj+/Hnp2v2dlhe94INUGQDVqC3BWGs616R1Ya1xoSWOqRc7lTpjH0P+Vys6mVfKumKQpZnY0/0pbsdydM6i543t3P7RHSqOD/Tn7rIz2JPhKQxCl3M3v8OHSRfo6ibfyUvR8C8Ji+jSu4S44Lk/A+jAN9AO5pm2JK0YMxpg6Av/ylaJSfBSSOIfbHpYkaiPiT85i4hnhiQZq29/vswtVnCdH6wd2nGUSVahv0mgTh3ZmB62Y6g==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$3bd5e135-a3ee-4e9d-bcc5-dfc2a1afd581': 'Trading',
        }

    elif company == Company.TERAPLAST:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=TRP',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TRP',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$8c87625a-53c0-4b88-9e8a-2bd4d74105c8',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': '3L6M29qTN8AgSnZxs0+mHz50eLnRtQfWLhLdiV3gfUwlR/ntR0XXSQO396Eob/e7e88XPXGKz8WXN9NvsZzJIgLWLEEOjWrkHX/H+NLDyl5mtpAGZtDueJb+ucBJ3mvoc0YDnBuCROZHGSYj4dokG6yi1zQH6T/il7Wch6/8cGQIBDUZtTSMNe1NysMgV+CORK7byjCrzC3Db9obs16Urny8oSNC0l04gToSA1vy5YaH3K1xE2I1+XnN6awEs7eltZjco0Ruh01Duvd9XUibtg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$8c87625a-53c0-4b88-9e8a-2bd4d74105c8': 'Trading',
        }

    elif company == Company.CONPET:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=COTE',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'COTE',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$b6f29d6a-2c9d-481c-be29-5a900fb3ccb9',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'MMIhsPQCd5BY3aE4kLkwpHmP0aUpBdKD/k0q+g0P6KI4JbVV4VWNP7+CjA8QXFiiEkLDSaTsz5iUT0agXvGopZKrFVTg5mL8LMXfLR5Plohl0N0mmiuv+ElWsYtc4lvGvHk/HvghAsO3Rqn1ZJReULQqqoB3g61kKBnaCwJ7nhHOrukLj6Ofb5qE3eFurWL3atjZNhoubqPlgrAT6+IfGQUeuGhGdZOt5N2F4htV9rmxrhQCbXqTAW++zM6/ScNXFKX7gw2RkYnZJqzpdPCwRw==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$b6f29d6a-2c9d-481c-be29-5a900fb3ccb9': 'Trading',
        }

    elif company == Company.TRANSILVANIA_INVESTMENTS_ALLIANCE:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=TRANSI',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TRANSI',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$52a7e4ce-7f69-45aa-a3c3-e418ac321010',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'F4n1VISIVwyvj9ENvnxKa97Pup6b3ehOOtOv4NvL7SfeIRjP7NtLWpjKyFUvdYziciFmF6Bs1Qfkr2iP2NOmFChe7YhR12htImoFFfJ30a3IWheoQKzd0jVBoa8UdvMcMMR7jg9EZyODobEz6TPYhWQi2oR+mCDePpfgo1lCVULapEhr47l4RPxoPuLMl/5C/LSAXMGuYP6e9Co8eIFc3T+v0h/gipf1pV4KqYzwo/R9zgWzeesPtNsIqgtEBmCvrD1D+VMHW5/FI5ICyyKlKg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$52a7e4ce-7f69-45aa-a3c3-e418ac321010': 'Trading',
        }

    elif company == Company.SIMTEL_TEAM:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=SMTL',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SMTL',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$5629151b-24a4-492e-98be-fbb4099d7e7e',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'VfAUKecH+zmj61ex0CdE1ehSB1N9CcBTmzIf+xXE3XslvLY2PeA+2395MPpM88TOtyYsc++D2yz8TPZyi7a22N6Bks3bf1Jg6lUv6vRhZDjpUiL/klUBqqSInqfa7lcgcxF5TCnDPqde0RxHVPfIpH0UQg73KQppx6clBSV0RcazhVhwiIRLVpZOrKOG5h2NjW1oJAG1R7VR8vkdKl48CHOkIjrWuCBaIm4pxn7deDbNtrJtpkY/B+RNuLjwFLOO4ncoVM/m7l7UUn+h1vJxCQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$5629151b-24a4-492e-98be-fbb4099d7e7e': 'Trading',
        }

    elif company == Company.NOROFERT:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=NRF',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'NRF',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$4f8e0a8b-82f7-4276-a043-5b8af1bb7341',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': '+HBBiX0jFkOK8nMCODPfb+8xDQvvaeJmlVr9E2FxKQZd0XgOcJvBNIRQggUlERxQJKyJWBt3Do7j7E0JVkhI5zbY9EWtuCkbE0KxhuQvms1dzO1T16GOHBAMYjfqkB4Pwsxft7gVUdfIHyL9IuorDGhgT+5+Rn9oE2HufAQP6w/RasULZhkMn6TqnIOfsEGaz8dGyMSNexR8fnQaVTWbAIXGet9ebTBjySz0NI9tktBO3rGqqA6vSf/pkWeM1IeUlFw53J43h28F5ufJSr6lZQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$4f8e0a8b-82f7-4276-a043-5b8af1bb7341': 'Trading',
        }

    elif company == Company.SAFETECH_INNOVATIONS:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=SAFE',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SAFE',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$e0a1f5c3-a9f0-489c-8146-0bb553b744ab',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'joHcKcudYrpOR77vhkBuVd2zwWd3zmWf1kQKxB4AUc8wvlYx4Qq7PlgR8CP/7QiMipaNkoAqV94Hacl0CcMAQXApgUw8LlwgozwkOkHdr2NmKecigF6dw78gt1OFAtXILeNMYqjip/NRJfZPL6qTToidkKWOXov17AHA2MHgYOHvk0z9iIKtXZEq3xtIRu0fLCi19gYMe8/H8PWXO1hcp838mq1q9kftx+hgPuf8F3WYvk+ZcH6Wu710Ab10ydTm2U2/ud3SuVTJS4XIN31M3A==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$e0a1f5c3-a9f0-489c-8146-0bb553b744ab': 'Trading',
        }

    elif company == Company.AROBS_TRANSILVANIA_SOFTWARE:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=AROBS',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'AROBS',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$1af50dde-24db-4748-a9a5-8531b9d1d237',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': '/+QwUZUrzht2uaUOh/rEpPfbig19wUxHBUncbwvQyUTV6XJnZMUecZZMmaOaqgeeQVKNe5Z8c7J51QkL2XD+D8c9RwMW2zIcWRJDvfo9aBR6z4DgU2WWXR9oMYtXXeALfSN0+zUGAf3/t3gWla8EqzOtnaecnqLNLiYnKBY+a0eEimRpKZ9aUjDGFKFuCCbzLkpCG4Mn/a5B0ortZT7YzYNfef2WJ3Th726zMP085gd40DjwzrfKRUGy5f0ffO6VcKgOb7f6byZERpHRPAbBeQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$1af50dde-24db-4748-a9a5-8531b9d1d237': 'Trading',
        }

    elif company == Company.AGROSERV_MARIUTA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'kp5wvwqljjlszeaq222s5a3y',
            '_gid': 'GA1.2.1132341662.1670226404',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-MicrosoftAjax': 'Delta=true',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Origin': 'https://www.bvb.ro',
            'Connection': 'keep-alive',
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=MILK',
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=kp5wvwqljjlszeaq222s5a3y; _gid=GA1.2.1132341662.1670226404; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'MILK',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$5e7b33a5-026d-4406-a165-0faa3a3bcb0b',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'L3RSknO0HnkkYlv3M3V8P5gW1l1MzJKFcJ71hfkwOf8gmxt9ylJL+qkxNanvhCuNh68FR1F0GZOzNp0SYwBq2GIdL7I6vUyO4UvOPorLwzDbbXySqY80NBSCxYkY4unqbvO4rCYE7FKkiafgJdm3MpQ1K53t8Q6i0daV4yDZviWkiIE8jQDFdUmMt76PY/Bo3lHZJQuDxM03iDZxmB3viZc8upa7/nEWYTS9FLV0UAG4RDE80IyhIH3Puul4VJq5eJt8JpnF6YekupcVWYWNCg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$5e7b33a5-026d-4406-a165-0faa3a3bcb0b': 'Trading',
        }


    return [cookies, headers, params, data]
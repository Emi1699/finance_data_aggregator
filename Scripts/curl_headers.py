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
                'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
                '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'EL',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$a64b0a0b-1c56-416b-af36-9d141d43090a',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'ZQpZDVYvCDZ/i8awupidWOlBSKD8B5jVVLzKXAEub2LofjP88jXno4ROqI5qge8vxnK0C6asiCi8epUvynsekleV4+xKr2n0pxqVupwwAe4Ncp3DWfEcLi/TqZBMxehhkptvQ+aVWLTqgIuFntEjD1i7FeI9OSLmL11XGgGElHn2iS+4sAsbHvfGP23quxz+w2Vf6cAQFNLIEGkbsqK0MnFgZFYBtf7zBSdkEhMi8aJ16HVND+FpwgsiBGsFXNdCLjdR+jgd+56Rwhunow8oBg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$a64b0a0b-1c56-416b-af36-9d141d43090a': 'Financials',
        }
    
    elif company == Company.FONDUL_PROPRIETATEA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'FP',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$246665d4-8ec4-4b38-a89b-6ca0fcb90c50',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'erVpFqhv8FnEZhqs4CBxSIXjO4zVRw8T17YT4nXChdj6VwT+MPBQ7YkC7q4dkryQpo4t6A+fpY4WsOf8tOd+AJsYfeHpKDigY5605vTSnrO2DkBvd0eKbwbburydV46giI1GCPN8fRxzBO52AT40+kyF7lhPn71asOWP2SRlvyZ0o6QBVYlPmk1WFAh2JqtPIZTYTaY7GisdcEwi9sxskEJQ1wvycf5tp+NR9Mb7KvNjgA5Ysb9bQ9DVvZhIFaXC4kqJaEDK9Vu2KeNWG9XODw==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$246665d4-8ec4-4b38-a89b-6ca0fcb90c50': 'Financials',
        }
        
    elif company == Company.OMV_PETROM:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=SNP',
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SNP',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$12585c5d-b4ff-4f32-a4c7-1be7bac15203',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'dqF2UL8L0i9bS5n79PIlIfS82Ut2/QBPl1FG7lxhAZNzn8zjMt2RVE4LgF8FucCPDJiVbCeVjHZ1134uTo2ppO0iIYpU6ZrnQ8qfUM/JMtip6uTuH3V9S40ngLOlQuaxoHFsDjFzhAi6XLGVdLHC8UTdBh7o18L50ra1HAsctWggjyz2ghA0aEAvhyhz8NxO3XSXGHxG+u8AlSnfdlqAZmBgQwZChKJJwZYAcf/LclDhnF6l+dDhcvxnd6/dlRjNy890m4VzMCryHt+ua+hXCg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$12585c5d-b4ff-4f32-a4c7-1be7bac15203': 'Financials',
        }

    elif company == Company.BANCA_TRANSILVANIA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TLV',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$034b7b07-1a19-44bb-9720-87a54c700893',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'gT28VWAw57xzd2VuhzT7T1VwVNHFVCsU6dMa75jzGCqgcRjxIiiMqqqEsGq9Qji9S/R8eMy0xtCULGLSjFK/dA0rFlbM1srru/DzcZavKm9BRo00p8jNzz2MMynz7wFddn8U/Pke2huOs+kaLz/xQWiUHV+BvfNpkXRl97Z6ZTpUyUlGYjLZkRM4gbDGLCXn81F+NU9qzahB2cAWCjrSjbRWdVtN8KNDmvaXIVHJbVPKV2tBlxYjgq3cy4/+oltht275QSyiUO/pO2ermxdJYQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$034b7b07-1a19-44bb-9720-87a54c700893': 'Financials',
        }

    elif company == Company.TRANSPORT_TRADE_SERVICES:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TTS',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$02fff358-1918-45f5-80e4-222a02e635a5',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'E06JZ+y1DIru9jUxi4lJix8gIHDOPmmDsa/syfezbnaFRS9q5pxvaajS+9kIRcZ2gvK/lUL8yDC2hwgc/93wVI0IPb2+++i+FwGaZVrsHZkvZzirsVqV8pOHkVuOoOkr5WLjNUWxNPAALS3sE9cFRYXuLvW5PX0RiSiUyhFQiT+udxRICl4OP4cEzMmlZJJHhXKpKMqABdtVb6sHbQJkO/H8qWpB/o166nssoKm2CzzO368QuHqyYs0Nr2zhf8KqpeRrcjkr4n8pm/8k4I5tIA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$02fff358-1918-45f5-80e4-222a02e635a5': 'Financials',
        }

    elif company == Company.CNTEE_TRANSELECTRICA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=TEL',
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TEL',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$bc1b7175-427e-4cb3-afd3-47784c166a54',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'Qt4SGmxXozJmy4im55upYeUYn+btQulQ1O7JFHq7/8NZ7JUIxnM1OUBkymYzG0fFmUps5ndxoeJ0vsmwNOw+lc2j5pi0k2ztS7g9P4PkQJXoLDdPpZwgzHHlrSlCiQMVDU5gqtWi6WvL3Qo3vbCB6NsFJrzeEq7p7yWycAF2AIFUKBy837Kg4JCQN9a0Ios/Xc5ZDNB7vacsu+Q5y4GbLHmeRO8hJPH9C3VB4cfXWxiqBZ6tu/2j11ZC+yAsGabC5IjF9zcfqt7dnVD1cQjRlA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$bc1b7175-427e-4cb3-afd3-47784c166a54': 'Financials',
        }

    elif company == Company.SNTGN_TRANSGAZ:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TGN',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$e66d5338-f10b-499b-9a9e-02ab29ccddec',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'grlKQ75lPib6dSpVBKU3uuzlgCUn/7n+N5hW2EIVe3hXC1iBXm1MuZq+OCsDKYNwqcaDnKjGXscU9usZEs1mlbSFQH376ZzFQX2wKUgBjxIKXLr5kyTQLCbNpeV8cNe4fldUN+DV9WuMa1g2ZncMIsXxydOqkA0pMP6oWb5mFdu23QiD+KmXHgJQM9JVVbgTT6iOkjMIPwRgQqjZ0CS4324TnvCi9tc3uQgs4DCMnoh5W7CGGlL1YEfEDKwyfJ10LaFo1SU9AEKrEhlLNKssdg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$e66d5338-f10b-499b-9a9e-02ab29ccddec': 'Financials',
        }

    elif company == Company.SNGN_ROMGAZ:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SNG',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$2d0c2fbc-16ad-46dc-9675-fe4236cc0f33',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'rxMQ6Evv2jxFsSXJuJOwHNESGumE6wHXQXKQyHr6ODkiCex+LbYoNkSb4CJiTTrHSNWDpl4qr7Din6ouMC22TtZSCKNI2k3xn1ZH4U2WxN0NAzng+K4DguxV91W0X5PtB1JlDd0XnCNgvDnsl9k8FNmCa53ZXlfht+pnuUOeCunQW0kEXyU5qF4B+AoRtUipR0HrehMY/yzP2Ig3i6ieM/MZ6iK8VB8nJ1cvYARgGwPjlAhGbOQ+XOZtE6pzgM5uj4JPo+e8DSg2N3cl1BDRjA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$2d0c2fbc-16ad-46dc-9675-fe4236cc0f33': 'Financials',
        }

    elif company == Company.GROUP_SOCIETE_GENERALE:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'BRD',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$e17b5e67-bbf4-4a83-b405-5c423cfd5236',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': 'e+SWSshXkqNxC6g7gCKWtXIoVeUfeZzcxOE4zQbaP0ptOFaORV6iWcxGteAWgOaOHCFydZVtye2DFaHoWwt+d8aJ1/fY5iL5lQbjL4+4tBZ/g2JmggGq6dij6k8pHz4tjqlZIHSUgXHFu92VagU6RoJRwQOSdaSG1X5IHNFerxCWUmxIhv2Ba5ZIQZ1dNruX0+s5mWs61/maeL1Ec0n81AXqsLb4E+5GzKfZs506Fc1ALvdfpjnGZdqEsMI98xs77PSS2eCUviRwSViwVN4BKPgNa5ddli3io0wMlHzyEZw4DZxafCW577zcrqWdXSmOVhZMaJlH9kifYBbllxiUIsRpr71hK8FoNe/PQKUjVKU35vxg0/yfNdpLa0TH08R+SYsfq/91t+sEzXjh/w+OBLtMTk14BHhPGN9S+AiH0xFAfR6iqbGkKPCJtyvWUKT5mRnMbZhut6o5jqDmFKClokFv2foc/FS8+DgyvVG8Ttq6oyTEnv45J5ONJqc+Yzu4kwuiPDJAyprC7rRV3rvjNXGW5Y4ghtGXvr1JJ+e+Q/PO0FMqLHdmwgjtjvkyNXhiFqC2XEa6CeOG0ayPAuvf7nqbNTCxm0sQCtFxy9HrGCRR3LeqYOpuUcUsq29ox6PO1wXvKJa19Y3oGGJCpmU/7e9VlAmUskxiPUErubX9tD2blUtLP/gJRHCb/iA9wIuI0FT5H0BVPYBNXMPf11guPHW5B6Lpu8uocMsuDZpLMxYH+5dMoT7/6M9rV6M9aSZKJCGyjnW1MMiJSZQnQUshqQDRehpMYWAN4hOrUNPTHIrPfCqrc6J6njWQlfqSA2Wo3uHPEe55Vyu8wkJIGb4UU4j2Sl+R5au/NboDASaHZjRSmpnxHZ0bUlu9Zb0XjOBppYvmDqNgy9uxKENxkiSg3Apb4rXdjDpKmSxslbgwGE+yeNUPlIEmUQUC7oXOrSYbBCd0TmSHiC5D5PcvAngx/hf2cxkLfs1nj1QjaxtvD3lmMcRp3fCFlwKMtJx9gjTyq5GbhNuNhtSgqC426oyr2jr9Ecnz/8gcclDOxCZAN/NcXHxsTQKcxEIyPHt83h91VQTH3khSjyXMrbaw4HdiCjICKMdbJT5k0yNESKog3YptENs4fGPg4BwfTyTDLFjDMCLi5sMhQp2MzD9fjxfhhpUslkxv6YKMidEJp3MIzegfRrH2lgFMzTx1VCtDqk6eJbn5GlZZqLtdNDOrDQ0pFLR5bUtVnbDx3j7tFerYpB99odqr/jbKo+GD5YS5EjVEU7Q4xunfe5Q7eTkEJBN9fYchJIn4WNi11WSSJ6q8OInjuuotjX6C3XE3l3OfZ0StY6eRFQbdU6ThwjIEUNsJe/Js3YkSGMe0/erHGX/XSy8bBDKqUfslwexBTnsQclfNveceC6ejmfYTqJJhjK4boY3DvYfrjPSuy8+DPJJpMPdRYv713pX1aL5YTo3qu7834Cje2NNOprXBGe4YqgSEmS27Wd8RqO1/0JeS4b9n5++GJ89QdA3T2R67hwfSv+U4q7UggsJ6AghIfDi6wABNbKBsccy8qiy3Mkfgz0qmiOCMhat4U2f9gzUjccrccoYhkPgTJO3DdPhA4csQ4Hvdr+dwEoZIF+fq4dBnJA3GpBugSrOAdnxoxgwg068TsZsleyxS3XYWdKk46oSwaGIAcwHgVsOhgdJPUuXICNVvbGDf7TYmUT7oXb1WFIsEO8lJ2THDKKCnIh0OoD5RBr6OE0XE/vipvfMvxsvvFF477uuIHukw+WmTuK+tbxuh/Y+M6S6dHkHgkwW4OMMVYpipKMKjoIXBu7BH9gKMj4cCr50dSUpM4bmHT1x9CHNw+zJn78hnvOjWYBTP1ZHpdwtxJxEZvmnVrPRgmLrqV4zGqRMn8h92HPmi1a6dzTNJQ1M00G1GlHicpJn0T7dNVJB4scAOev8oIHChQY60nnQ6tF0RVjjWfdTK03NFJRMSZoLCjUXxA+zjC5epxHJAvHeIcxbUdJ8Mk3lIvUfp+h0IkvPHkC6WbO0MyvkqyTEn2/0chXf9rXSzMADrWMUIbcb3owCTPWLp72e3jVO4vkLiTHd3B+xRp/WTddJKFxB7FEBhbanfw8VIIbLM+4Ae22cNYT75w0SErq7WEkl+7A0Wq3LBoZ28TavyyH5jnazl128jFRoVoKGj6Q09kpW1K2af7n9VTsiH3/7cNgbRS8u2pxRXQgg5ycZmDxTyAWmqszXIqpWtkoWMpZh083mVoMdP1XL6O4TF8mj5OlknBllDTg6KLMSPPm0Y+Oi0hPgFaIm0cunnxlo6490dxP5w+M7iMgWlZBJNGYbfmEvjnMXTZrEdeln6OuIY37WgOnRYS24Z72VAOp48v/hfgXB1prJNRxMHFOrCTxUOg6NFy9XasbrqvCPKY0R8xuY/U9MbwkRZ1BkGJebhrxGMXXPvIwV+wC9fpDBFHkJUdpon6okb9KIiBKzocBoYOBiWCxBwDMik6pNfnqxyifNWGvMjAxxrA7vWqor+Q2s/mqE+U6ALpPlgLJSt0j1fVA1yGRQJFhNW8nIqFc/a6XgyiWk1E39FFswlrxWIJVWwsT0QTi1gYA8nTesM0/Hst/EjD3H7XuLmD+4mqdJbXLbdWSZaoAR0VBewUGrEmGXk6CBs3qp1PBtsFQqkLfC7hDREpXZ+GxbYZzV4/fWiPFa/QGRw/jPyPmDTQPaTHy9t/04x2Gnsp8jxF/nW9+W1jCdHF/2TiZEHxdEYBDCcDCrIeOtX2CK7YZrYSRW68Cbk5SUeJsqHEbuwuhVzq4ue91TA5qbB3gIEdtYoQXSmoLiNLKoT5mPu+/4y0eYrugP+Lg4aSl/VHDgzrJVm8+tLABxaaipqR9AhGjwYrtL+pkd/onSvCVEk1lfVNc+9fwiaRoGsadhYR04GCxzI53fOOLMFkpoX3iXJllF0z9g4EaNsMpw7/mf/N7kgR1ijvDI22z5NXvCVnCt2UMLPiHuZWNEI/Uv2EErP8qgXEptNhUvnk1u2VYeu7ySjmaHRY8RrVjaWKly/1NToayu7w25e2JqISd2A6VuXWPTCBIUrdcGrfOZH51T5lDXXXv9jAnOZYdfbgHSezrrRTwB6ruAX9yPYLXPj4NhLGMPg2ZCRZfwpYk4dj5OC3NijxiwAqCSKql8ftsqYkiudfEt0EEEHOi4FMwM+pAaklj6M9orhfQ9PO85KKdLSpjoezFWWMf1eGMParWyApUDgwAtXp5JoqdFZys+kKASxSW0/6o3jzsPlIlOm1sd+KuRqakiQFvOJ/ZytOWDJZZeBKZ/QXDINP6TNdCKnNfGoM/FOheW1f6gyLJVF8Yov/GBZmNOrESVTeKXCom+6sEEJmUTFuo34OLOs4DGGYQlEJJo87OFaXMMKALHs4xmwAoXVQvZ3qW6TddgtJrXm1uKmA4AgGcrl4kefXeacc+9kAACVYtNcR1yOI643oel4phsudkiFflwMaT5RgunkM3WxIJ3fN694Pemfz4/iPSdVejbYrGsCl73DEyfhtozbZ7z0xAkbl5DFDY8UK1h76QAiGO8Y1tB9PLN+GpmzS2iDUYchPyuLYlE5dfrSBj3Ae0tJtBvBM9y7D+IMGiyBUJNccwIcfcR+rvny2VuX6cdTbik+zSLP1u8TYpXmcMLQHu9YhDVS1ODfMGRYoJh9qjc8mB+8094uGj8epPPeVxLNjX7ExueJZqpzjtwF+4zkHXEr6pFquxNVwTLUdHy4KqQzHFlmflKz/21auuRqwdE1Dqc3HNXjb+nIFGP/kmPrOWjhXqb8PfTrPy0eGol+onp3nRyyMmfXdJGVMMKTiNqgtdntLep8ZGj3yssD7aN53d/VXbfc2/iug1bQk+8rV9zx0E6r4Qyu5snwSFCD1ARLdc/W2xkTVTLGJjmNiJeZv2kdO846inRIpiCPP4DkwXpiw5coOkDZCgcqh6AG4y2/xUm/DoTQtdXFhxmsDiEm5FCs1AUsBAb6ce5XkzYf/GxYoFXybLMn1IHfvVeVxoI+AEjkGMdt74ZscwtdVlhBQzWunER2aKbxezfHb2BKkChUazMuZpwD+Cj7CiHUAXYdnUXi8ksJ7nl/XR6LNew0wYviNgzkZ+zPdO1HxS3CJ6UJNMZ7k9Csgslo6tQx0FsSZIdu35xZjZqO1lfUx269EwCMpuLrgC41WPpecg16Xir0KK9Y0fwe7D2MO07Kn9/lGFjDTTnpmR4MpCxDbmPJefdMvJjJ8dZlXqQ1O1pSKKoYNhpctJq9NiLZEHTCr+q/ta403hvnuvxvdqRs8WbeQ1YUdbR2sLPkCnniiEmo+2rptbmvv+uEuOB2NxAVfEd1hBSXBx8hqz9iIPDiZIF+GI52as1dF6ZY0fGyM+Yp3v8ijyP3OVz9M7EwI5Ha80FOWwT9aNHGuRwnVdKdbY3UkFWKKixGBxwRLwex+Y03FQz0WnEM4HZfLs7sGB00GVPwlj6uD9gOS+faKpinDOQuc3WSc2kmIzZ7JFNM5PdaOi6LM6fZJcUstvbGql+IYqsO/vnpI4TVJTTVQ9lzuh50ujZ1HW6Jv6ICXBjMmwm9PPAELz2lkxYW90O+S2lHCkg2e9IpLnULAdbE5v5RL6d1Gsdnl2EuFn+Y4oW0eNOYlJ76QQGt0mvhkupqJaEmGagp+4vsLuk1z9Qlk2lD4p8JZEDDq64BdCAIl50rQG20Rw0IgwFFT/Nxa1adYKM+nPYCTB6MIsD4JwoYTrn59Ea0cQ==',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'WaEMBpS9v0J0TBjfSsOFSDZOIZeVBWrOmDKyH28SrNwp1xzfCQ/7fUfaqem8ZaR7yelUhIt1hnfWjrq/pYoQ+EN1u3CcARIBihe99jJHGLY7XtRQ4mTa2DJEO+gu93t9xFDczQn0V9XIKo9i8QgDCT+NLzWxoDaUo/ujZt7LQLx6Xlabq733cnu1KCdiz9klJCh49D/wsrnQuvwL0RjGQKCOb0s8zPQ9i0qKJ0Z77qhkJOyZpobdxa5WgMl6XXcTNA5Qms0PSKET7Pqcn+7oyw==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$e17b5e67-bbf4-4a83-b405-5c423cfd5236': 'Financials',
        }

    elif company == Company.EVERGENT_INVESTMENTS:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'EVER',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$5cb480dd-05c9-4038-9f11-e34bf4bf2fdd',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'niowbwXpDelw17kMKJTWv8uoHfENb4UTgLAF0+Xi5nfY8nGDKgR+b+PNvBC9FTAQDGCkj/xo+keDK8zhltZ10MpXmk3O9kFgUzhuIXhChCJYKFuNU9IWPRudaxNlQswfxCAjWQK0TPQITPkuZT+PDa3EC4/ouBGT+sfNiYrxgP3bGAt8H/LyV2H2+rzDzAqc8jde53V5fZiuOxN/fJO6qMu4Uz6PWmlxit77fn30Q6kF53007+nZuBOf1CuuWXQztAGrVl7cBqUsdRJcaBPuEQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$5cb480dd-05c9-4038-9f11-e34bf4bf2fdd': 'Financials',
        }

    elif company == Company.ERSTE_GROUP_BANK:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'EBS',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$bb35dd1c-7aeb-40a7-8046-0189068e093c',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': 'GHtsAKORr9+Dz1kz999d8jjSeyKn/hkIx2O0FjyN7SGeyRE6oSV9OLSkJVCrP1kBDJU+Ur9RttUwjDrfScHwSJWN0eWlTZ6RfJUu5LC6mWr7ViY5ZzkbvbKTWca2FUW+Dm1IQljKwVfZM2x+7TWcQWJwLo9tEoTrwDmAWGgNQynTpwQFYrXqd3tEggyq5kxTgaNVJXR+Mtn+qCjw9hlDFOg8+mISNUQsT216Y6y6q9CkBcMvk5xLPVvvBAEa8OIgDlqJE9JDRtE6ok9b+iYcqXkwpjjy9weuvGk0x3+XYLMmdWSn7t9eJKEM1Jn/OrKwHDY54Jwdp5GWbXBtbAQd/Al4Z1OvkK/zlW1jnZoJ+VAvU7iBeS3LAQBLQ1mzXyAiMZxSOGZdBnPmrQGj9eXUTlChf/D9ViE990YXP0TrBfiMyTyKpceto+UHXkle43hvjKA88lv/aidaUaOZT0+qCshuGspPwv9wLIaqTzyIk9i+mTYPKE6KNQ/jDns/t1FFwss+CmVS/OrSdNOdtwqQDrEgUB0T9kv8TPYh9PyM2pWs9ZZL20gtzM+NoyvrOaqxOc6QLzfbC8ZHjnBotkAR/bgssWkIEf8ImWv6nnsODoa9tgp/+/vHtHnVMOw59CvIOJRAPRrj67i8CxmcZRFi9tdJ71NDC8q5Hzr/oe9yKeT561Ruv/FowxFdKXMwQqDPWT1bCZXSMF6OIe3FYjDk8o6yHhx70WwxsrnGRrbNOXnsepqzpp5gMRSlrsCbUFym82LHPjA//SKbu0/z6hwn9Fw4zZbAl08eZfX5a7VYPUOmow0pXCZFXBHHdTxIEIs68dkjcIfOnEnsmeAOOdvG5zXhwqIQwCQN969ZTLNmIXwWJP/EKUPKaL2R+RsfWfIlxiohpWMUn2RIZhVpsxtcoMd0GzW641S1ZM2THboqfz7mY2STGSA9Omn99Ea5Ol/354/kazza+cSOND35S1Dy69c4pPHxbMUMbbg8xR5H4WyFF0ZJQKW7lxkEXtwDetm4ZXbjDPFWVwwzDhJg99JjaiLt4SUqiZ8pVFcTPKoQF/voz8tLqdws8iV6y9iFbBQDSwwWDbDVDSjv3F+8ttzsvzQYRFzzPNOQJ5DV6c/iNIge3alXapYGMUKZcNlG1pyCN3GCJ25LwGe1N6d6yrb/wwQW+J1leWEIuqdkqu8n8sbCBEhr9ugh78qUOmiumG65lqK5lIRogJoOmrY9YW3W8TUeKooc+O4yE6b2Ns9kwrfDid9cHeQR19w5G/wiV2Di3atJ3WCbIk07Gp58t0HG/4n9FU5PJeF9ThWG5H1LvSKDU8/APPjcmkSOIEKpZ8JpH0jY2ZsId2UYn1sarliNLDA6tz7ECb1VTnB5uqLneKUp5BoskLJXxk5KXMq5oWnxkFDx68yhr1ilMDBN1gB7PrGlBpwC/ij+1sD7vuXfcaYheCSuBjW+TLcOlyZekG1iuUMfpz2VC6clIdObDZUTct/OHOCtttfjtFhM3r7H0KBdzhO6FZXc86glW6Pmg8Wqsdv2rxzGU3cRx889NHLc/gAL+ZUFoYu77NuSu7Z4hNHFd4UpaezV0fXcL7oZNzs9/Yhd7WfmhafBuRIXx7lqnUc2GUt/47M+xGzhJb49Kd2OzgTiGSE78AvxNcUhXa/B9gJOdZ885pc1plrS2aT6F1xvQe1SbtRNv3go7nkQK6ngnWDenb3c4mcigEX4x0yx8TfZKgi8H2SrHBbzR+FwPl1WiwK5W/joo3l3u9kBcSGidNpSlXAmSeq5BTTsNaZB+D6C3n6sxY1m6Qkp05I5GKZ/H1WfEJfpoYBQKdnE3h0tkuUYrezkLtveffQHebwNa4opVJd0d7S7xhGoE6BDQL8Ka/ruYRurFpgb9iYVT25bDiq359ZYSz2Sh69Fq4qIxoHwF0mIWtgHbfLBhwD5ylJhc37Ew4YqT6OiNTfdPXEmqKbjONXysmLoc65Hx2Yo1Jqch7ioHwRKfyC8/BZyU7dTv71NGy6xmxOHm1xMtjm7Qvoc4SwKWqoUPRsbmLz85wnnNuXZw1d8WGkNcTRaG3WX/vYK68g5YRayNtP8C3+9rDUtuJ1N9gRXdW2L5QLNpBPDwbmEShCl9ZkO0KebgMfIPADXqqURYlFpdploJDZaMK0+aPZYk94Llry3M3XJD6ewrKsxHkbAUNYiqk6np53Dlosaauxj2Zb2Ns+8CA+pW2Ng6P8jqhKSfZRPitwZ22CaG4AK1V1vO2vn+VvIy1fn+KXaxFi/BUbudrkNVZnegHGWJSPnAEaeo9gOI52Wxz6hsUpDOb/ylyg3vw7ISzlUwIIv8B9DH6liLLtqxqXlPXKuJYqgeoY5sa7aUfGk9UFINhTPZ729s/KSi95htONy9ECIdwaIy5ieg2bcmquXhjNzy4g98iDasaAuEHmIWaSEZvD0Ys90L1g9vw39aQsKqfcvu0w6yOpgDAeEj9OUIDTbJtq2acBthXNr/wzHQhBydgEIwIleyUxr5F8VH1WbTEfc6+zjfstDeOokI+M3c3PENLcbwwu2FcNFb+u4vmEEOIWtRPpwlHEriCH6/R/y2lIaT1/H7Gt6O/ZSWJ6Cw9EJjYPwt7LEMCbvvqsbvxO6sbm+1/HrBgIe5rbXih3oGjROC3N+AU6MhEc2ELET/I4bf+aNC/Dol6Zz9XYELHeEIlx2h5VoKw/OCgMEtjrT66f89WRJXMlRjuNLSZMjZOJH9B5ec8dxZ6YvWHsN6kyNTwrZ5KlE07+4DgouDSexXng8pZTKJtG0D8V2sG+nW2liQUuFiznc36/ufjpcC8KjJOLE0ohSSZJ2uq2U/xxImlhY46Sk7+4LWChUaJS0VJRlISL3fPUfjNn7Z8OcLSOKrLgCoFTnbus/C7w1DNzV3vb7WFFJQC0L7DnqL6KPI9RTQ5z8x3Xc2bEkE4N/+RfptZrM8/fW+7VIYjcbmSoiTJNkyQkfi/bonnWE9plnuzLQZKcULS2VMR1tMYWTfqtPQnMDqZjCluT8gi1MT47QppXXpNuWbT/4M+Ptp1Ru5uE0PZSb6qeSdfGTwBJjQSg5YSgo90ILGF0X4PqDrXwFhfJ5g9ga5933nz4ftVp9O0ezhoKM1qjxD6sM08rCNetHy88lO9adgrae2H8YagEOLHQgcOWA9JijnXYl15zyAuqFseQYiFU2u+S7uhn5LqTrCYAAPtqGM6BzcF54MzSq4QaHv2m8PxGwVm1+BSBps5b5daBKd2XtTvmx2PN0bH9PCdf86pEWanCJLB0/CtRf0pqaPxucQMFxdCWyi7zRpv3AGNot8OyL/sE+Jc64CvVL01+ORoUrbXFfzvohXD2jptTsYYSKAFwz4xcEWTaKPTcshwbdtn0JoKRQueSHlnxktrp2WPvSxCsfPuDR1Hnxz0OuIxNGVEUmNRSiPGOtVZ5LSGkNRct3nanwJfIo+NAcaK69Y0zdugTdOn7UH7HtmDSNRnJS5mpgd469B2TgWmFKWNdCa2D4ye2k8L/wQ/9rRM9b0v2kwK7yguordvu6fvML7gUxnyNxLPqqCwVtICgCTAidJXaYjjsAsdU5Wa4HO7dJp55rYpvhOMOYC7Pi3jBmiJIBCQsWtlB6nXp+WzIgU4iGH4TeXoJ+JcQrw6KOs39bU14uisxlzxGcpHNC+lcWjAU9SAO4kfEIWUZyoqgqbOELlQId0CoRfN/O+zflZtIMCQoDbeozEM3oIl87Q+4bH0XKcyzQyoCLRqpq97X1pPfa+Vr9AsYv5UXWkUNlj3rdyA7qao7JlIQA7fKy+7Au90iLrQfu4e5Qb4q+laG4kju58TER3YfZMKFcWhgAc6cnHWmY9jQU3toVWp8/z07rv24hvQKDNLceQ7h8+TW9QL32cwZXsnvbBGMkjOE4QakoDTjNO67Bb1nlIyz9CHNuznI0TW68HURcRfX2pdPFcvgYxWlM/552qz5NepCyJjalV7YhFeVhjJIdu1IKr7NhO54sR9R61m3kiLhUOrRYT3J1U+vFChtjE2QmwxyIdlSA3gN2a5bu/s7tih6USqv2E/jS++6zdvfHEmvoF1Mko32D1YTUhY4nZJtAU8M9hCaM37hSo/VBxtrDAlpapQ33BMTAIo2B0AC5pztCai7x7Jq1BLvFLtWJEXgUMT7ZZcqVEURusayVQKWNoF4QQRGKebHFntKJSvB+FtHm4JTIqa9K6nFFhEactp832uLgSc8BpSofkV5fMyuIwpW9HpixzHoXP0euKA8EgDycN2Y4rFlPhLNF3U0gVuKNgQLmsr8OfGI4cm+XRb5kq7c0JNQSzv87WNWe/f5M0hwdEigE8jSYzdu1P1pcwJB0taznsdfApgxrESI3NA/fsPtlPMwZD5rCGGmJXZx2qKzsaoTOX5kgEwBlcGPU/IF2GG8l1Ean9C45YS607r2b42IBvoFBVposkOfqQzyDFvj6SYx1hnGVBN4lEtCEw7ofJnqiP8gFFpWM1fau77SIptnB/0BNADenegbDzKCpfmYybaxvjIe9EYnxcpoYIRldm3mfMTvwnmdJ1QrBDst95hCiE71Yvj3oAHOgJD9+Re86UlB8+riFSOhCQ10KTOu1',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': '0dyv4Er8tg758tgtebxmM/+37Z3mWA+KkOsxyOOiipaIrFea+q+JnW4zsiAZHPTXx8IQJaqplU6liMR9KvbMpzwsWqPvEkwCeLP2BccZWU47ljZCxmhdJ/Q0UY6AW0XMgoOTQrl76lfsCple+PARpWO+e2ogB8uhA1K4uLCTM4ya1fOqc9ZwAHM3CfTnWSsu3ayEzx2BblSmlfxugDu9dGYovhu+rNwB6oCnx16DYPfsanBhYmee81ZW+u5PXgNIXrZPs/Rkpuug8Z3Oevw6HA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$bb35dd1c-7aeb-40a7-8046-0189068e093c': 'Financials',
        }

    elif company == Company.PURCARI_WINERIES:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'WINE',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$e39d15cc-9e2b-4a13-a587-12387b2ca698',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'vksFnDSLwq92B2r8j1BJb6rXgKdcpfAc9NFSQTF8ZPUulJIHjRx98pWfy6oQtXrmwP0WDWM66DykLXFf1mwFXiOdoczhiJlr5rGe6gQZcgwXlY1zRM5YaS9hligFqhWA/fOD8WkoWdYeO0YJEza8NQAJwhbg5SU3SzO8at2hZ06ZTtmfltFHI6TZcyO8synI4qqGbKXBncDktfsbyGK+YskYEO68E1tgbGqlwnJ12vZbH7D758dtd47+aV/iiYRt29GkYiIrjCAi9PsuD8ohSA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$e39d15cc-9e2b-4a13-a587-12387b2ca698': 'Financials',
        }

    elif company == Company.MEDLIFE:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'M',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$7c962212-d5fe-489f-bff8-b358c38fc31b',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'ORXs375Pv7LCzeVT3aKlM0ytUZ6lmaE83KJ5zT6ls8GiwEV132R58Ngs/hLJdb37gfNscSicfdeWNPuSLEIBGwZVwNAlirxF12aEsNJ++nhQRmzI3+UvfbHnZIxACd//aqW/bTIgb/Mi99IabkDwj1EuphxbLWLRV+ET29wKHbBBq4e4RWGokXseiASfZjse9jiJpPIEbaHjbLdWR/W01QHfSZW8JTQ1LHr1jYBKUm7qetuYMsWLdOMXtfGW3XywAb2Irn8ekAQXcL90mkcE/g==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$7c962212-d5fe-489f-bff8-b358c38fc31b': 'Financials',
        }

    elif company == Company.NUCLEARELECTRICA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SNN',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$12f37a74-574d-4f60-a58a-b1f6fa7f23c9',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': '3qL8thR1PA6PzA/mAW4dXC3y7D+RH/qZm2fAQLDCTQz4DVuMUsFeGDHXakHAjxhrYWjAGHN7GfcVeWzWCHVtLvYD6+GWB4a0Y01pE4AxKTres69lgXMvPZEjESI2dbV3khP2ZFLae3bcaR4Qb2wLUWmy9X3aU0ucBc/YRmsZ6Y+JtzhnrMVuY5neRq47o5RS+nP+Lo5SCDH4/2xn5PN0nvcwrilGBP+OkaHhAPdXCvYUnUcCjPJNFsMOPrmQRltlzgVucrqETavsXlj6RoJpdw==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$12f37a74-574d-4f60-a58a-b1f6fa7f23c9': 'Financials',
        }

    elif company == Company.SPHERA_FRANCHISE_GROUP:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SFG',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$aa1735a4-f82e-4496-8d98-40e3a64dd6a0',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'kWzQvxJYZXZVFro1BoGStqT1K7uDLp+yS3ZzwCzFHrOz7rfFupw7ob7oQ6ZNRzk71Tkha+HFgmXw4I98pbwDFAHipDf4B3LIpTtJdJWRBNL6rtnyWnRePcxpvmvSqzBX/sSmdqGiVQwSdnHzZ/arctBcoH7bcZKQtI5tN/xwvFJD0simeNrhBNocif5FJGsGlr9tnuq05L4WIHgXnbN96O8ZaSuwjUYWVAsz84GkX+HEtpeoeASA/N+tR1bffRo7EFBaafOsJsWTY36DeXAc+g==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$aa1735a4-f82e-4496-8d98-40e3a64dd6a0': 'Financials',
        }

    elif company == Company.ROMCARBON:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'ROCE',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$80f4d8e4-a226-41bf-a816-1f83a8c4c8bd',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'zLJWmVcTRz4i/BLku9Dj4PyDrwFggGzV0yx7DzaHFbcRI26nFZqHZT31BYhe1fOZxY9c+4PmCt/6EB5fP8/h1+16466Z1c3CkNGhmOs+tTo1aLfanhIE+d9wiKiAL9mHPFRJlHgF2RRpKOkpRHKNNLRM5hsAz42DAFkCoQpQvsbUgEj3nCaBGKoaM8dJt5Cd6UiLHIVtokpUqRmy/+gMAEMa83beJHNBXYJTonpzG4Pf7gIXFVGFahmiSZGfky5xa3KF+9JdqoOnMn9MYQegLg==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$80f4d8e4-a226-41bf-a816-1f83a8c4c8bd': 'Financials',
        }

    elif company == Company.AQUILA_PART_PROD:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'AQ',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$c3ba9327-9140-4c1b-9654-b1f88330dd75',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'MXc2T7AunIRGKOuuULmByaL00hcKT6LvuZKRJvdugEEqG/39pGJU8m0ufHfCz8J6Mz+QHD5mHUL6h+G7OtO1OtnvTsuwYpIFOdcUZMdvzsDR/C611NwLWGawsrBd/eulD4lpYhK2xNihJj7Y2kovfXu1j2r8O3UCyutVTJdKN0sPgXseYEC18ehAYpO6/RqeWELHVRXLbtUmvqLk7tQNsNTuVMBSb1+rL7+Q/yGEpi+PlTaNBVBXxvcl0NBDRixwkRc6kfoaUVUofDYRStcb8A==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$c3ba9327-9140-4c1b-9654-b1f88330dd75': 'Financials',
        }

    elif company == Company.TERAPLAST:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TRP',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$d00330a1-9d22-4c26-a22e-6850a1aaf387',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'ixHHULjHdiNRFEiO+pcZ8WgioDTyeUbSaKcwCLO6s74+3HGceYaXR/fZTnqUov35scsDtlMEC1VD2Qi6yY2D3GN0G8+pzJC1rRkuQ8TJtf82BXi5+MBY8feHIew2GxfiUfjGDRGjwWvdPhO66aFdmZIGhvXgFGKqdYHI2Z/C0GxXHLU/vqkdv1hit5HxALCyrgWIQiw0VjAfuf1pEz/0LrktUpzGrdgkvz7iHCsgIq6TjGE128AvGck3vrJKlrndk0AVDa/p8WBtLVubz8sa7A==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$d00330a1-9d22-4c26-a22e-6850a1aaf387': 'Financials',
        }

    elif company == Company.CONPET:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'COTE',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$19b6a169-6df4-422c-9a03-56b76d422a90',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'esSeoPu0WMLUEXwO1w89sW8txWzVaalClNwz1IvVrz7gEQDo7v0HNdAJtTJclknJMtIOKkUbKtJ+MHsJcTdUACAbxE3j6r5JJ7yJ+5JcHJQS9LqEvq5Lf656IE0ScD0BuObrPrEmN02daPrxAQVAXUMzUg2u+kr9JvASImMT3DRcwaDwsnV1kZoS3iZhHJP6Q1UCJB/uvgRGrrElxJI7Y76GOPhucX7z7RzN90xw8tbb8ouMPo4mJX85wnyh7ruCE0gtwKmdX6MTbxA8tjjykQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$19b6a169-6df4-422c-9a03-56b76d422a90': 'Financials',
        }

    elif company == Company.TRANSILVANIA_INVESTMENTS_ALLIANCE:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'TRANSI',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$2d5f5eca-c949-49b5-ba45-793673f4c8f2',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'UZ7upIOc4xTiH9mDHRpIKkEJogkulSpoEoKQf9nWxFTZGCz2Jt6ROiNnQ89Oe3bq51dyVlQxklbB7kLr44Wq7oPbd0h9ShC+1ml+Xvk0W5BuikcPeovWkB4GAv9YQ24jeqKrLo+kbdjvqwrNX1zIRmfVPilg6ahovqr1eTGexlqQkISUfA3k4zKrBjVoXZtHa0W+eQ+d2d/Bn4Abt8mCJyKw43SBguDxkiyoUUu5w19YVS/7CVBuxeM5MXQLQf9lcKTSD/Cldk/l8jubK2tq0Q==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$2d5f5eca-c949-49b5-ba45-793673f4c8f2': 'Financials',
        }

    elif company == Company.SIMTEL_TEAM:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SMTL',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$a9f41cb4-313f-48e2-a6c5-0ab960ba9a34',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': '1DcwUyGPlXucc0TefMupTSDDPvnh2YElsoxhX4R9iFnquDkU/zWtlizy8kfXUCya/6HULYWLGcsDxTT03kqa0GyJelo0xx9HOHQ7/z16vuSkTOGUZSMdWDE1F8MIq+qwFsJPfobbbi3CjOqeAC9iRxnEu+FaOR/ZrR2MuWqT/NtgVvck22+qT1heEdpkcdf0FXJXsnmuDoeB9FDYd5y4X0IHpJMw0Tj62CIi6a0L3P6hAmWwIBjpIDuQkCm77G29ogls4P5VtntbkTPgZKnpeA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$a9f41cb4-313f-48e2-a6c5-0ab960ba9a34': 'Financials',
        }

    elif company == Company.NOROFERT:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'NRF',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$567c8404-fbdf-49c6-ab32-a1b186b4ec4e',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'GDGqusgDBeeODCqB15dzneeJnOudkPPIfkMq1oAK9fsuADWg6u3nynnPM3G5P4KKasez/XIaTsIne9oLrjtW0vXBicaYrP7K8MVrud7RQUHo6Bk4QSnDvk+jHLGF1c7r5BH2Hq6n+6x4gX7PuGVEUDr0eLuhmuNA8qJai3Sp/zC3hEu7AE/og8ZnGFmRa87o4azOmH4GK1E5sFV4TtPwgDlhFr2hUFXTj6oGLxlUtgc6oPNpcR+KHKESoQpjpfGrAj7fdghap7e1yf9nDdyEuQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$567c8404-fbdf-49c6-ab32-a1b186b4ec4e': 'Financials',
        }

    elif company == Company.SAFETECH_INNOVATIONS:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SAFE',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$bd95dfbd-5760-4688-bd95-458d87b7038c',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'cjl0K0vwWvh+nyB8ou7XZjlq7rSkP6xNs7iHEJy1hQhu03MTDh7G3l3BwLJ3r8cRjndLlF/sv5lpac8Rs9aRQTajhYsijMcxV7zF3BRnqoAmr2EnYF3/ESsxmi55JG7UPT0DK/tf4bAiTtccHjitPLEa9af2A/jh3JZ5Vm6ErS3Fxl9iwv9hG3az4C1RplgsmTEeJ7BTTl87Yno2prswwODlGq3hoMTZNku0fgdQX/0NjmhdbR6bOu29W5sUyo5WBL7HB6gQHU5fV57mK+My7w==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$bd95dfbd-5760-4688-bd95-458d87b7038c': 'Financials',
        }

    elif company == Company.AROBS_TRANSILVANIA_SOFTWARE:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'AROBS',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$22e90763-9fab-4299-ab4c-8801e9865f18',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'vP1Hv1aCkLxby9U5wMmviRCkip+ULYmvQe+jCZNkYwiPBDgcKUg6rK2EYiEp3oda0N9mFfO1eKwlPO1X95zJSOTZdHR165w9VPyrMrLhFfdg6KaV3JYLBXWy2seHqTTefbM9jf5eoLFHBH4+wZjLRxo4CchGXk51olvmF2qFYfpqaHueyIQI+BRFs5+7SUEr6pz0rbGgQcvT4p61nj79sqOOLbFDVJy1nujxVezdg43ETB/QShVzkCWzs7clM2tFnavhCanjEoY1/kQFBqvkJQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$22e90763-9fab-4299-ab4c-8801e9865f18': 'Financials',
        }

    elif company == Company.AGROSERV_MARIUTA:
        cookies = {
            '.ASPXANONYMOUS': 'DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2',
            'cookiesession1': '678B28781234ABCEFGHIJKLMNOPQA711',
            '_ga': 'GA1.2.1302759501.1665387244',
            'cookiebar': 'CookieAllowed',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': 'eqybdcxabu2p3jtp51ttdapf',
            '_gid': 'GA1.2.788802474.1669630649',
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
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=DUFIeE-aKUZW2e69gluAcwquiED3dG7A4l0oUTW4B8xmU-1GUqJAwdPLEal8KsxJ_xejJkeYy8xKbeB5r9b8GWG92EGdOzDteimnSENGtUQrsqQmv4uArCf421b3C7Nhy_J2Rx61xFETmnwx5gzKgg2; cookiesession1=678B28781234ABCEFGHIJKLMNOPQA711; _ga=GA1.2.1302759501.1665387244; cookiebar=CookieAllowed; BVBCulturePref=en-US; ASP.NET_SessionId=eqybdcxabu2p3jtp51ttdapf; _gid=GA1.2.788802474.1669630649; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'MILK',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$7378baf6-0641-471f-a71d-68859becb1fd',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'VEZ817v9ufpwQEFbfVw0+/1gdvaWJThJCDtBtJFtMUQR6Y+66cwW290GB1BJcttG89GPesxvsWftFH97b1KGwdXhAMi52X+kSEv7vKm9foh6RjSG9Q02SABKeevnvaaIYcvegXo3/RTW+BcUGyUVNK2rtaMqmQMcjI01lPVbQwmWvK6Nc6Z2HY2NFzW0nh0yhlkV7/DStB23rGA8HQKLkSkOUxJ6SEB0A0f9ZpJZAvWYEIzADbtkel8Bb0tvwF8DqvPEmFZG/xGkE6+liVSqRA==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$7378baf6-0641-471f-a71d-68859becb1fd': 'Financials',
        }


    return [cookies, headers, params, data]
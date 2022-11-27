from bs4 import BeautifulSoup
import requests
import file_system

class BvbRetrievalModule:
    
    def get_financials_data(self, company):
        financials_data = None
        financials = {}

        cookies = {
            'cookiesession1': '678B2878UVWXYZABCDEFGIJKLMNOA93E',
            '_ga': 'GA1.2.1355707676.1668264785',
            'BVBCulturePref': 'en-US',
            'ASP.NET_SessionId': '',
            '_gid': 'GA1.2.184486518.1669474268',
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
            # 'Cookie': 'cookiesession1=678B2878UVWXYZABCDEFGIJKLMNOA93E; _ga=GA1.2.1355707676.1668264785; BVBCulturePref=en-US; ASP.NET_SessionId=; _gid=GA1.2.184486518.1669474268; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            's': 'SNP',
        }

        data = {
            'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$1fd0ac19-eab2-4bd8-9189-e8e0f6f7d6fb',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': 'WwuIEGQtt8AmvGd7Tb7Ueh6B3hezBUY2JLaAI0pHsHC84lGIwXT7ndMbnpr/hC1zHKPTQCnwufmlUI7jGPHeUfKYzGUSM0LSxq0tOl2eg+raQ04j3j63G+WQ/7tBlEKHj3bWaf9BUsTIZeU7fe9V7VT0u1QIZKP3jqobqRhWw6JJ9QVNdDTTNWMQcCSATPcFJoE93s+ApmAzgwccmhPwTWzf5zqHM3+BADdPg87Gxbp+3Feix4k74OpgwYhyOJCjsmCN3MixgHumUQQZmjnswMsIXXiscO51ExGmTqQobCh74RJkez3XiN2jdYp/fya+X6lhUcSGjoTuARBdxVYpOIOef1nLSv4t9RwRwqJACNlBXzqmHEPe7kNYOMoSSjCmLaQGjGxPD2a+oQmg8BOT4AJ+H+CxZ8A2odoXWYOpzENyXcnKaU6dZkF/YVsuqM97Pg2okeU6ROYcS3ldSbAlbmXm71d+Gb3RQ57rOhxUr+PYdu4HbYkjGbiccyTYKCoc/9JbtKuRk+yVFqrGjAQB2SkvijNoYcxl48ht6pvWhiCHOl3F8Ch2A7pvn14phGx6zg85tOprkdMRxfag+ZFEC+dStAAHlcCEzhwAVJL4KZ9RcVwCYiSXGCzfkvazn6Rp/Hu4Jx0JbN9kgkWHdEt2eS1Kgr0u+iKQMs/UK4DiscRelY5Z+zaAOQIvyLz4zQjl1EWcaux25V3VXZUxjf+owsWSs/5BQByhzotJk0L+OZ0OAds6XZHYge08UrGV8VPlvn7NUUwjadYCRRW7/e36Fii2X7yjzFEA8mLH06CZqfdTeZYRXx9SNqMgzPinG0QQrManfIkx1z1KodQsDVthuqxSIUi06XSHfB+7gftJTJ3UMkdcDxDPTv/NGhg9MoNl1wG6kSija3NhJp0XnvGE0o5nyuwMvh2S9Qn0qyXPNvp45XzmsufD09otu2pXzuF+1ZJPh8Rz1P41nv7DdQjWYN16doyWaL5qe710DmafQYW4q7KKvAoLtBjxMShMuMPjNuLYOV823AEmGj/h7YsC7a1gYIBJhlZqg8VXdz0HCJoLP7IsuMGKaV1QxYscl6bAIi3Db7FVpOVWBghQK/GFzEHL26UeWg8WESimM+zrVou1h2hpPILFNHg1+/gZ65ghf3EggWfYbB1SctPZYVWj8qRMb24ZhVDeGGfdAtonRWTbylrp5N0/anX9pKppso5Cr68n8Frn8YS7fSGCexiwsQmVM9VztDdyD8xGbQGs+tB9YYYfqFdcOlIDqnlPL29UKlvdVH0IVyhkBHrKjtu8pxeJ/4ffCv4dp0VjIBoFLL5Qv8lpX4A1ICZsqH/TeeKfgjCWrp4fWNWw9JpNd+i6XJ+G1Rfs6A0U9MeocPRHKQqtimskweT4b/ahe0ycE7GHiEdEY/PFGO/id2GVlJVoOjhZ7Mzwpl1bgi4gAP1WnkcHViHtEoHTJOw86ILSjVfHM9N17Brnx24Cyttgdxd2uxpIERdllOL9wjSoSTe+ZqLjfsG7uWNnExjwnTohgIBbDhJwGnPxDx8gbg5WkFwfz1SN4RBc7/AAyqH8fdaQ3mZVNwN51g8IqyUnCBCLWi/Cr3EtfjleFEFCurxNpIHkDeN28KWPd59F46ZVdZCWx6V5lSt9ac+41+h5ZPEIC8rF/t0hRKU1Jq/TatCc06nK/NzIZ6/O8P9+0N6/bN6WrCpvPWmXrHPFkuMjK5wlGgEyORUOd0i0WLpCWLbwhkjSfgp8Kn0Idk+fJpIzVUfipAnB+XebXOrzVinbKyHxITFosEtD7snP6sWcpSojTs50r4qgcBE8hN7ZiEieHzm0GcK7yWA9QnjZ0sF2Dao9yu3oJlTEoaQH+h4cD1ofZy9sYswXH7HApZGD+YDXlIGSwMsiHExvV3KxOKK5O8T+h9qbSZSqoL0cNfpAS/VG0sLGiCDR+CdtD8t7tNJF0jLKEdBqcTppIKzVktQV/OKnJcKdJMg12Fyo+0bIcXd13+4BmEww6Nbz322D1pu9pT+oLncEPp5psIvmP7n8CBaNOdOk8xBD3S4OzAN2F07+DoMflqJJMJt4iltS2DnIikvPILzADNL5CLWqMV0nBwYfP8DbnQF2e7oTui/fkhJiyb6zoAuP6IOvgdvGrcbuONt+sdjr2FByD9TxrSs+uMiOeiTBdOkFSNp8r2MrEvSbJ64E7Miu9NhPimmTdgoq+6imW8JkxmVexpCzB9B6JOtcr3H3AJxjzAyq+7AekAho3T2GjTjLBJKnr2thXOhVKk2qBRVPkvbhHdhnSgHEN5vjs520gS6RtlKfQHdmJnhufmShvpJ5SfJVLGgB819svecWqLedWsoszB73he7zcof4UUbiqSSmzRMZOAN1qVhJkC4SHQV1Zt/hpW92zxmqXxIK8nytb9SOYntT8uL2Cvbx1qS0wAC2ietE9AQ8kLWn2nyPE3lIS+SDHMCKlqLs977GC5wS4N9/UTKObgDaBDprGfhfmr1ryvjJHe3+4oeh+VpfVygHkVZ7saKWkXDxtizl7vfCA6rfMTZpP11sUtppFpjXHUpKx3MtTAoHCXO9Bf8R6fX9Hu7cr3cqA42FcuLUkSbjnejQGYWAfAA8xB9RV24v1SnUYLCQF6IwgIYxUOgdzpWRwgyDSndm5y/t6QqPzD7r87qaOiwbrgHbCi2Xwox+HDJlE67k0xFOrMqs2RbZ6gINNC5eG9V/z/3POhddjEqwbiW9R6OcSdACE6tKACyoyT7dzGEJSRf4qdR+RZtRoDiolvgfpzs8wCXcQrWyKURgAEspX6EkXiRF8rwHPCitRvs0EJDXEanEgWV/r8c8Vbo/AijFE6dk4DSJwm/mN6eL9d652+snQBNlpzZJYkGvDWvYe0N8EHez2+awrLnNedwBZoZWMgrjH5bNVAJ1iO0ZPkteoYpw8wDDYippwaZ60DPfn+BqFlXLb2E55pfoW4eooWwqZ16K2ExPtLL7VrPoBmZcgHNq/x+LM5M/n9d/G/1QwZ+l5mYBBJwsKZlpePi8xwXr/p5GjPdkosCFd+ywncNKgs8if8lc5bQCjNlFF28ndrwPvijdj0gPVVKuMtCAZxERbPlPcPGz3TjwTixD2sqm0DR4wGQHT8yBYZgYOzSWEE8O3FXaQzdpv4zHlWAtEmVgaQWv2gTVFNsOfAmnTVzZLrT1+IVCEz1ZM3ivjgzEH5fqCJRNtRI/bUzagr7XMKYSvxrwu7adZfVZPxIuRO6Lv+Fxy0anpYFc7bmH81mv+5XMki3dkB9Z4eBOlsGKjr1kUO0bnE1e3NsKuMiUQTXlb92IIgR5eeS7nzWFmEVnk441TE52qPgL8ZpTUydxwxIwfBj74QzoDKLcryOe6BJgJm/jWMKAOZSDXeu/ABM1wI1LTjEYEtnq780Wgr+8rwNRC7VU1+xYObkHVVTqMaeZku03i5U3nAGJ22H5XcdLo3DIOW3fYaagrftKEqJuAOSuAGzxFcN11JNSGEPQSJc+lGsDHgqU6mh/+aY1px2kmThQglq9i8IO9KVdTcbnzrmi79vPQN8YNrV69JyfQzvRpFftPQZcrj6IHKj649OmUXiHeKyqMYTsvXf2WbGVUOffFIvf2t3aXlcj91Qx3oKwN2rQOOge2Cbnh2lgOyTrHmXyJmgHdXqZ2S42HLXi1cMdR+1kqQOB4/1Mjm7X4j4/yXVEzrQzHBnZ3B7p5w0rP6neZm9Npy0ALl25j9eeZ4016ZHt/J6y3P6xd4RIVpN5qTObRxOizbDeEip8tyRvNeQJED0Ig2O7FFRCNUaU9e9Vm/Mdj1Wye1hHmOT6Odcw9qI/4qX55HrOfIPcTa9fxX3hB/rvXjXq2DoMMnb5ScULIZXZOkebSl8w7BRBBdc5FAJwNXOc68oaMq6sCZ40unATeyhTw0FsIfBzwg7QuJeOEhcSyU8X5TdLK2235pmKDbQ2KSleaiR6EmZGOF3qatkDEWN3kxGz0+xVGGyRZ6RG0Wc3Hu4GIRi9gCHVAIm7j4O3vCB9JY4nZGE4c6MJvwNN6SKXn3+kM3ndN6Pro6kMo7P8Pr7BajkHhpa0xyXP73ttcXtMgNe93JCrvl2Hk8cZLPyxIKUNSuxyjc46swTrXRP5hw22pTtDrTp/VwbdU532Fw6pXxZorlkmnaSY1QhGDzQFCwaxqqux+6KYH+9Gncqwm+c+E+JpGB4DBzLUpVUQWMljb+GboGCp3NT/3k7bRLLdHGLGsNqlU/tJWej09fWpSgniEuSIYXB0+lUmIfOw+6eAxVEjhKYCgZ0VYJIBx47tPezH3vWQRVyt+eyz18UyRQq+NoRXRSUVPtR34Z4p/BeqHc2FLQUvPVkO7WzJIXaOPvvgInab/2Rq+gMUJh1WUAjp9rJsGBJ0bK3iRFIewv+3hIBOe5gXMSaVZNMEqDCBhAgbxgUKDX8BUyyKzqrQoQgjnXgQkd8JfPLNKdWkGNwz7sbl/d9lZxo17QUvcTZfjaceK1VpQg3fkkJKB2rXwhlLdYaAlTRNYbNLBQvztV+IKKqff0rcn5uBZ8eUq7T8a7Hf8YAnnRsxA5LjJIFWDYG6rkC2bo6pefHPq0NSrzfdwMxhJDQ1e2/jMcnlkUTkLqcHV+08SHfQl+OGc92rDPB67n4K4DP5gENjdjFCdOWdj9HYobXXOSpLaBZz5ZrHykqgZRGMw/6kOOuKnFUV1qLBEaW2B1oU2vGj+Nh+53qk5PB1XQZT4z0r5q0vaBa+FphHA1P0G1OxWjYLr601U5m+jLVXC652gKc2bju4Zzwcx6+URw1U/OF1zBh68pIQUTX9APAZd09eyfXdL+vifzg/KASCAmz3u1e9AWvjhCpAIznb12nXNyHlcL0aMyq5etZd/BzPGEdXBt/WT8eYYKUmu6lfR75OPLvm7bx9KGhVOwUGh//95RhgBZ+ciL4tPIuMPCnFIaFnMwr09H92b9pMgOOgRnRLuk2Qui2C1MN6GyV9ylY2QOkr+B085HzeDr/g3/Kjs7dim0Je+CKJcY9+j08GPBla4DeD/6doMmqrVsiCulTLn8GXEvFEOiO3tEULslkQyUEuaaFejSaHAHtxZRoXBxOpn6csKUvsnnZ2JRRqMmchcy5PtM28wFVsPe3r3GOqQZxZp6zkR0g9BrLRV32QKshi6aZ2PbHUSlDYbBqM30borVQZGbLwocgtvv9iEiH0WQeLlW8eZrJy4hlS0rjlMIbjWCIq9CP1mtGW32OQd0JkZl/yMBzf1pvT+7M2wb1Ec4J5+e1GlSlINZ7rUjMijW+dq5LmGZXy8GJ309qzrjiRbYA8mkVsZqDule5ffVH7nYvuIWsW0ah4YpwHZp2jGEdeYdanTr7lOI0IvZXPzZSos+jPop4VrdaTPvpgmjMgcrVY0qSWpHlhNbyr+/uW9lpdDiF/7YcmdnDItVqR694/SQ22nhEaHgAQ12wjWawmAYsQuiH1C0pfyRq6eYHW+JwC454Jwtz+9bNpHfFpryWSAnP9KArYKIqCesEQVM2WAWkX6/nrhxIzgZbU9TMotkFenbGHkHlFlbULFAPNLGXLa7pZGtZxfZmF+dwtikeKkh0+zfHivDhwDrXJAQocLVlf0bl5mkYyyE1eZrMgGuXbq4g9Xif5ROdU1axbfkU+7xkkFBm0axrB0az7fDG/brZ1k0I6gyT+4gLM2e3PljSgeuKzCAkgsgk5U3rOGzrWYR9aWIrnLO3JmpmUSMqQ3EU4lfiFA+ipG/2lX9v1JW4BIcKtSLBWRbOdX1ZFkC54bujFx8C0hwCYe1CcVTp9egE2Gl991mxlYTSsoKOE+xM+0hApDMER9BAk3rxPJ6gVqg==',
            '__VIEWSTATEGENERATOR': 'A396FC17',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': 'fof5C0ddN5nCe6EKHtDd80D7soQrHScg22Y4DZUYIFDJ+ob/3MB1K2A03rvGy1ukfbolRNAJgRbbhyXJU5SzkceW1GPWRcpdR6AmTryMSIFN+29cyuIUV5LUzjUrvvEZZxHR1O7A/hAf22XdcQWGtvcXZtXNxBbXXKcUccxBKD1Rekc2JoFkHK+eHuulUGSvrNfpdJYudtJSFymPOtIS4JU43xzaCgGGn+FktB7jU63ztL+Z+6huaK7lSKWHp2WhkOcjdDwTsuZy2JjlQgz2qQ==',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
            'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
            '__ASYNCPOST': 'true',
            'ctl00$body$IFTC$1fd0ac19-eab2-4bd8-9189-e8e0f6f7d6fb': 'Financials',
        }

        response = requests.post('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx', params=params, cookies=cookies, headers=headers, data=data)
        file_system.write_to_file("financials.html", response.text, "test")

        with open(file_system.get_path_to_file("financials.html", __file__, "test")) as financials_file:
            financials_data = BeautifulSoup(financials_file, 'html.parser')

        table_data = financials_data.select("table.table.table-hover.dataTable.no-footer.generic-table.compact.w100 tbody tr td")
        i = 0

        while i < len(table_data):
            data_row = ""

            # transform data to 'str' type
            table_data[i] = table_data[i].text
            table_data[i + 1] = table_data[i + 1].text
            table_data[i + 2] = table_data[i + 2].text
            table_data[i + 3] = table_data[i + 3].text

            # populate table with 'None' for rows with no values
            if len(table_data[i + 1]) == 1: table_data[i + 1] = "None"
            if len(table_data[i + 2]) == 1: table_data[i + 2] = "None"
            if len(table_data[i + 3]) == 1: table_data[i + 3] = "None"
            
            # format data in file to look readable
            right_padding = 65 - len(table_data[i])
            data_row = "{:>0} {:>{right_padding}} {:>30} {:>30}".format(table_data[i], table_data[i + 1], table_data[i + 2], table_data[i + 3], right_padding = right_padding)

            file_system.append_to_file("output.txt", data_row, "test")

            i += 4
        
        # print(financials_data)

bvb = BvbRetrievalModule()
bvb.get_financials_data("OMV")


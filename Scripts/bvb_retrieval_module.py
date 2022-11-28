from bs4 import BeautifulSoup
import requests
import file_system
from companies import Company

class BvbRetrievalModule:
    
    def get_financials_data_of_company(self, company):
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







        
        self.process_financials_data(company, cookies, headers, params, data)
    
    def process_financials_data(self, company, cookies, headers, params, data):
        print(f"> processing financial data from {company.name} ...")
        financials_data = None

        response = requests.post('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx', params=params, cookies=cookies, headers=headers, data=data)
        file_system.write_to_file("financials_temp.html", response.text, "financials_temp")

        with open(file_system.get_path_to_file("financials_temp.html", __file__, "financials_temp")) as financials_file:
            financials_data = BeautifulSoup(financials_file, 'html.parser')

        # contains the table with information about 
        table_data = financials_data.select("table.table.table-hover.dataTable.no-footer.generic-table.compact.w100 tbody tr td")

        # transform elements in table to strings
        for k in range(0, len(table_data)):
            table_data[k] = table_data[k].text
            
        # find length of the longest element in table (will be used for formatting the output file)
        formatting_longest = len(max(table_data, key = len)) + 25

        i = 0 # used to iterate over the values in the table
        
       # loop through each row of the table and write content to fil
        while i < len(table_data):
            data_row = "" # will contain each row in the output file

            # populate table with 'None' for rows with no values
            if len(table_data[i + 1]) == 1: table_data[i + 1] = "None"
            if len(table_data[i + 2]) == 1: table_data[i + 2] = "None"
            if len(table_data[i + 3]) == 1: table_data[i + 3] = "None"
            
            # format data in file to look readable
            right_padding = formatting_longest - len(table_data[i])
            data_row = "{:>0} {:>{right_padding}} {:>30} {:>30}".format(table_data[i], table_data[i + 1], table_data[i + 2], table_data[i + 3], right_padding = right_padding)

            # append to file (only if not already in file)
            file_system.append_to_file(company.value[0] + "_" + company.name, data_row, "financials")

            # each row in the file contains information about a specific financial indicator and its value for the last 3 years
            # thus, for every iteration through this while loop, we bundle information 4 rows at the time
            i += 4

        print(f"\t|\n\t|__SUCCESS!")

bvb = BvbRetrievalModule()
bvb.get_financials_data_of_company(Company.SOCIETATEA_ENERGETICA_ELECTRICA)
bvb.get_financials_data_of_company(Company.FONDUL_PROPRIETATEA)


from bs4 import BeautifulSoup
import requests
import file_system
from dir_path import DirPath as dir_path
from companies import Company
import bvb_curl_headers_financials
import bvb_curl_headers_trading
import helpers
import re

class BVBRetrievalModule:

    class Financials:

        def get_financials_for_all_companies(self, readable = False):
            for company in Company:
                self.get_financials_data_of_company(company, readable)

        # get 'financials' data for one single company
        def get_financials_data_of_company(self, company, readable = False):
            curl_params = bvb_curl_headers_financials.get_curl_params(company)
            self.process_financials_data(company, *curl_params, readable)
        
        # process 'financials' data (clean and write to file) for one single company, using the params passed as arguments
        def process_financials_data(self, company, cookies, headers, params, data, readable):
            print(f"> processing financial data from {company.name} ...")

            # initialize some variables that will be used in the method below
            output_file = helpers.createCompanyFile(company)
            dirpath = dir_path.BVB_FINANCIALS

            # clear file before writing to it
            file_system.clear_file(output_file, dirpath)

            financials_data = None # this variable will hold the response from calling the API (i.e. the table with the desired values)

            response = requests.post('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx', params=params, cookies=cookies, headers=headers, data=data)
            file_system.write_to_file("_financials_temp.html", response.text, dirpath)

            with open(file_system.get_path_to_file("_financials_temp.html", __file__, dirpath)) as financials_file:
                financials_data = BeautifulSoup(financials_file, 'html.parser')

            # contains the table with information about 
            table_data = financials_data.select("table.table.table-hover.dataTable.no-footer.generic-table.compact.w100 tbody tr td")

            # transform elements in table to strings
            for k in range(0, len(table_data)):
                table_data[k] = table_data[k].text

            # get last years for which data is available
            years = []
            yearsSection = financials_data.select("table#gvRapFinAnuale > thead > tr > th.text-right")
            for year in yearsSection:
                years.append(year.text)

            # check for how many years back there is data available
            years_back = len(yearsSection)

            # find length of the longest element in table (will be used for formatting the output file)
            if len(table_data) > 0: # table not empty (i.e. data exists)
                formatting_longest = len(max(table_data, key = len)) + 25

                # padding for first line ( name of the columns )
                right_padding = formatting_longest - len("Indicator")
                
                if readable:
                    # write the first row in the file (the name of the columns)
                    if years_back == 3:
                        data_row = "{:>0} {:>{right_padding}} {:>30} {:>30}".format("Indicator", years[0], years[1], years[2] + "\n", right_padding = right_padding)
                    elif years_back == 2:
                        data_row = "{:>0} {:>{right_padding}} {:>30}".format("Indicator",  years[0], years[1] + "\n", right_padding = right_padding)
                    elif years_back == 1:
                        data_row = "{:>0} {:>{right_padding}}".format("Indicator", years[0] + "\n", right_padding = right_padding)
                else:
                    if years_back == 3:
                        data_row = f"Indicator,{years[0]},{years[1]},{years[2]}"
                    elif years_back == 2:
                        data_row = f"Indicator,{years[0]},{years[1]}"
                    elif years_back == 1:
                        data_row = f"Indicator,{years[0]}"

                file_system.append_to_file(output_file, data_row, dirpath, True) # write first row to file (the name of the columns below)

            if len(table_data) > 0: # for some comapanies, there is no data
                i = 0 # used to iterate over the values in the table
                
                # loop through each row of the table and write content to fil
                while i < len(table_data):
                    data_row = "" # will contain each row in the output file

                    # populate table with 'NaN' for rows with no values
                    if len(table_data[i + 1]) == 1: table_data[i + 1] = "NaN"

                    if years_back > 1:
                        if len(table_data[i + 2]) == 1: table_data[i + 2] = "NaN"

                    if years_back > 2:
                        if len(table_data[i + 3]) == 1: table_data[i + 3] = "NaN"
                    
                    # format data in file to look readable
                    right_padding = formatting_longest - len(table_data[i])

                    if readable: # format data in file so that it looks readable to humans ...
                        if years_back == 3:
                            data_row = "{:>0} {:>{right_padding}} {:>30} {:>30}".format(table_data[i], table_data[i + 1], table_data[i + 2], table_data[i + 3], right_padding = right_padding)
                        elif years_back == 2:
                            data_row = "{:>0} {:>{right_padding}} {:>30}".format(table_data[i], table_data[i + 1], table_data[i + 2], right_padding = right_padding)
                        elif years_back == 1:
                            data_row = "{:>0} {:>{right_padding}}".format(table_data[i], table_data[i + 1], right_padding = right_padding)
                    else: # ... or not
                        # convert strings to floats and ints
                        if years_back >= 1:
                            if table_data[i + 1] != "NaN":
                                table_data[i + 1] = float(table_data[i + 1].replace(',', ''))

                                # if the digits on decimal places are 0, transform the number back to an int
                                if int(table_data[i+1]) == table_data[i+1]:
                                    table_data[i+1] = int(table_data[i+1])

                            data_row = f"{table_data[i]},{table_data[i + 1]}"

                        if years_back >= 2:
                            if table_data[i + 2] != "NaN":
                                table_data[i + 2] = float(table_data[i + 2].replace(',', ''))

                                # if the digits on decimal places are 0, transform the number back to an int
                                if int(table_data[i+2]) == table_data[i+2]:
                                    table_data[i+2] = int(table_data[i+2])

                            data_row = f"{table_data[i]},{table_data[i + 1]},{table_data[i + 2]}"

                        if years_back >= 3:
                            if table_data[i + 3] != "NaN":
                                table_data[i + 3] = float(table_data[i + 3].replace(',', ''))

                                # if the digits on decimal places are 0, transform the number back to an int
                                if int(table_data[i+3]) == table_data[i+3]:
                                    table_data[i+3] = int(table_data[i+3])

                            data_row = f"{table_data[i]},{table_data[i + 1]},{table_data[i + 2]},{table_data[i + 3]}"

                    # append to file (only if not already in file)
                    file_system.append_to_file(output_file, data_row, dirpath)

                    # each row in the file contains information about a specific financial indicator and its value for the last <years_back> years
                    # thus, for every iteration through this while loop, we bundle information (<years_back> + 1) rows at the time
                    i += (years_back + 1)

                print(f"\t|\n\t|__SUCCESS!\n")
            else:
                file_system.append_to_file(output_file, "!!! NO DATA FOUND !!!", dirpath)
                print(f"\t|\n\t|__ NO DATA FOR THIS COMPANY! MOVING ON ...\n")

    class Trading():

        class Performance():

            def get_trading_performance_for_all_companies(self, readable = False):
                for company in Company:
                    self.get_trading_performace_data_of_company(company, readable)
            
            def get_trading_performace_data_of_company(self, company, readable = False):
                curl_params = bvb_curl_headers_trading.get_curl_params(company)
                self.process_trading_performance_data(company, *curl_params, readable)

            def process_trading_performance_data(self, company, cookies, headers, params, data, readable):
                print(f"> processing trading performance data from {company.name} ...")

                # initialize variables that will be used later in the method
                output_file = helpers.createCompanyFile(company)
                dirpath = dir_path.BVB_TRADING_PERFORMANCE

                # clear file before writing to it
                file_system.clear_file(output_file, dirpath)

                trading_performance_data = None # this variable will hold the response from calling the API (i.e. the table with the desired values)

                # retrievr website source and write it to a temporary file
                response = requests.post('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx', params=params, cookies=cookies, headers=headers, data=data)
                file_system.write_to_file("_trading_performance_temp.html", response.text, dirpath)

                with open(file_system.get_path_to_file("_trading_performance_temp.html", __file__, dirpath)) as financials_file:
                    trading_performance_data = BeautifulSoup(financials_file, 'html.parser')
                
                table_column_names = trading_performance_data.select("table#gvPerfT th.text-right") # column names
                table_data = trading_performance_data.select("table#gvPerfT tbody td") # table data 

                # transform elements in table to strings
                for k in range(0, len(table_data)):
                    table_data[k] = table_data[k].text

                # transform column names to string
                for k in range(0, len(table_column_names)):
                    table_column_names[k] = table_column_names[k].text

                formatting_longest = 33 # used to format the data in the output file (if the readable argument is set to true)

                if len(table_data) > 0: # for some comapanies, there is no data
                    i = 0 # used to iterate over the values in the table
                    
                    # loop through each row of the table and write content to fil
                    while i < len(table_data):
                        data_row = "" # will contain each row in the output file

                        right_padding = formatting_longest - len(table_data[i])
                        
                        # format data in file so that it looks readable to humans ...
                        if readable:
                            data_row = "{:>1} {:>{right_padding}} {:>30} {:>30} {:>30}".format(table_data[i], table_data[i + 1], table_data[i + 2], table_data[i + 3], table_data[i + 4], right_padding = right_padding)
                        else:  # ... or not
                            # convert strings to floats and ints
                            table_data[i + 2] = float(table_data[i + 2].replace(',', ''))
                            table_data[i + 3] = float(table_data[i + 3].replace(',', ''))
                            table_data[i + 4] = float(table_data[i + 4].replace(',', ''))

                            # if the digits on decimal places are 0, transform the number back to an int
                            if int(table_data[i+2]) == table_data[i+2]:
                                table_data[i+2] = int(table_data[i+2])

                            if int(table_data[i+3]) == table_data[i+3]:
                                table_data[i+3] = int(table_data[i+3])

                            if int(table_data[i+4]) == table_data[i+4]:
                                table_data[i+4] = int(table_data[i+4])


                            data_row = f"{table_data[i]},{table_data[i + 1]},{table_data[i + 2]},{table_data[i + 3]},{table_data[i + 4]}"

                        # append to file (only if not already in file)
                        file_system.append_to_file(output_file, data_row, dir_path.BVB_TRADING_PERFORMANCE, True)

                        # each row in the file contains information about a specific time frame and its values
                        # thus, for every iteration through this while loop, we bundle information 5 columns at the time
                        i += 5

                    print(f"\t|\n\t|__SUCCESS!\n")
                else:
                    file_system.append_to_file(output_file, "!!! NO DATA FOUND !!!", dir_path.BVB_TRADING_PERFORMANCE)
                    print(f"\t|\n\t|__ NO DATA FOR THIS COMPANY! MOVING ON ...\n")
        
        class History():
            def get_trading_history_for_all_companies(self, readable = False):
                for company in Company:
                    self.get_trading_history_data_of_company(company, readable)
            
            def get_trading_history_data_of_company(self, company, readable = False):
                curl_params = bvb_curl_headers_trading.get_curl_params(company)
                self.process_trading_history_data(company, *curl_params, readable)

            def process_trading_history_data(self, company, cookies, headers, params, data, readable):
                print(f"> processing financial data from {company.name} ...")

                #initialize variable that will be used later in the method
                output_file = "_trading_history_temp.html"
                dirpath = dir_path.BVB_TRADING_HISTORY

                # clear file before writing to it
                file_system.clear_file(output_file, dirpath)

                trading_history_data = None # this variable will hold the response from calling the API (i.e. the table with the desired values)

                response = requests.post('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx', params=params, cookies=cookies, headers=headers, data=data)
                file_system.write_to_file("_trading_history_temp.html", response.text, dirpath)

                with open(file_system.get_path_to_file("_trading_history_temp.html", __file__, dirpath)) as financials_file:
                    trading_history_data = BeautifulSoup(financials_file, 'html.parser')

    class Overview():
        def get_overview_of_company(self, company, readable = False):
            print(f"> getting overview of {company}")

            # initialize variables that will be used throughout the method
            output_file = helpers.createCompanyFile(company) # create the name of the output file
            data_row = None # this will be appended to the output file, line by line
            dirpath = dir_path.BVB_OVERVIEW_PRICES
            formatting_longest = 40 # used for formatting in case we want to view the data in a more beautiful way (rather than viewing it in CSV format)
            company_source = "https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=" + str(company.value)
            i = 0 # used to loop through values in the table

            # clear output file before writing to it (this is because we are using the append method to write new data and we don't want to append updated data over old data)
            file_system.clear_file(output_file, dirpath)

            # get table from source page
            overview_table = helpers.get_source(company_source).select("table#ctl00_body_ctl02_PricesControl_dvCPrices tr td")

            # transform data in table to strings and remove empty strings (which are the empty rows that separate data on the website)
            overview_table = [x.text.strip() for x in overview_table if x.text.strip()]

            # append first line of the file (i.e. the name of the columns)
            if readable:
                right_padding = formatting_longest - len("Name")
                data_row = "{:>0} {:>{right_padding}}".format("Name", "Value", right_padding = right_padding)

                file_system.append_to_file(output_file, data_row, dirpath, True)
                file_system.append_to_file(output_file, "", dirpath, True)
            else:
                data_row = "Name,Value"
                file_system.append_to_file(output_file, data_row, dirpath, True)

            # iterate over the table and append its values into the output file
            while i < len(overview_table):
                if readable:
                    right_padding = formatting_longest - len(overview_table[i])
                    data_row = "{:>0} {:>{right_padding}}".format(overview_table[i], overview_table[i + 1], right_padding = right_padding )
                else:
                    data_row = f"{overview_table[i]},{overview_table[i + 1]}"

                file_system.append_to_file(output_file, data_row, dirpath, True)

                # we bundle information 2 elements at a time: name of price indicator and its value
                i += 2

            
bvb_trading_performance = BVBRetrievalModule().Trading().Performance()
bvb_financials = BVBRetrievalModule().Financials()
bvb_trading_history = BVBRetrievalModule().Trading().History()
bvb_overview = BVBRetrievalModule().Overview()

# get trading perfomance data for all comanies
# bvb_trading_performance.get_trading_performance_for_all_companies(readable=False)

# get financials data for all companies
# bvb_financials.get_financials_for_all_companies(readable=False)


# bvb_trading_history.get_trading_history_data_of_company(Company.OMV_PETROM)


bvb_overview.get_overview_of_company(Company.OMV_PETROM, readable=False)


from bs4 import BeautifulSoup
import requests
import file_system
from dir_path import DirPath as dir_path
from companies import Company
import bvb_curl_headers_financials
import bvb_curl_headers_trading
import helpers

class BVBRetrievalModule:

    class Financials:

        def get_financials_for_all_companies(self):
            for company in Company:
                self.get_financials_data_of_company(company)

        # get 'financials' data for one single company
        def get_financials_data_of_company(self, company):
            curl_params = bvb_curl_headers_financials.get_curl_params(company)
            self.process_financials_data(company, *curl_params)
        
        # process 'financials' data (clean and write to file) for one single company, using the params passed as arguments
        def process_financials_data(self, company, cookies, headers, params, data):
            print(f"> processing financial data from {company.name} ...")

            # clear file before writing to it
            file_system.clear_file(company.value[0] + "_" + company.name, dir_path.BVB_FINANCIALS)

            financials_data = None # this variable will hold the response from calling the API (i.e. the table with the desired values)

            response = requests.post('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx', params=params, cookies=cookies, headers=headers, data=data)
            file_system.write_to_file("_financials_temp.html", response.text, "financials_temp")

            with open(file_system.get_path_to_file("_financials_temp.html", __file__, dir_path.BVB_FINANCIALS)) as financials_file:
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

                # write the first row in the file (the name of the columns)
                if years_back == 3:
                    data_row = "{:>0} {:>{right_padding}} {:>30} {:>30}".format("Indicator", years[0], years[1], years[2] + "\n", right_padding = right_padding)
                elif years_back == 2:
                    data_row = "{:>0} {:>{right_padding}} {:>30}".format("Indicator",  years[0], years[1] + "\n", right_padding = right_padding)
                elif years_back == 1:
                    data_row = "{:>0} {:>{right_padding}}".format("Indicator", years[0] + "\n", right_padding = right_padding)

                file_system.append_to_file(company.value[0] + "_" + company.name, data_row, dir_path.BVB_FINANCIALS) # write first row to file (the name of the columns below)

            if len(table_data) > 0: # for some comapanies, there is no data
                i = 0 # used to iterate over the values in the table
                
                # loop through each row of the table and write content to fil
                while i < len(table_data):
                    data_row = "" # will contain each row in the output file

                    # populate table with 'None' for rows with no values
                    if len(table_data[i + 1]) == 1: table_data[i + 1] = "None"

                    if years_back > 1:
                        if len(table_data[i + 2]) == 1: table_data[i + 2] = "None"

                    if years_back > 2:
                        if len(table_data[i + 3]) == 1: table_data[i + 3] = "None"
                    
                    # format data in file to look readable
                    right_padding = formatting_longest - len(table_data[i])

                    if years_back == 3:
                        data_row = "{:>0} {:>{right_padding}} {:>30} {:>30}".format(table_data[i], table_data[i + 1], table_data[i + 2], table_data[i + 3], right_padding = right_padding)
                    elif years_back == 2:
                        data_row = "{:>0} {:>{right_padding}} {:>30}".format(table_data[i], table_data[i + 1], table_data[i + 2], right_padding = right_padding)
                    elif years_back == 1:
                        data_row = "{:>0} {:>{right_padding}}".format(table_data[i], table_data[i + 1], right_padding = right_padding)

                    # append to file (only if not already in file)
                    file_system.append_to_file(company.value[0] + "_" + company.name, data_row, dir_path.BVB_FINANCIALS)

                    # each row in the file contains information about a specific financial indicator and its value for the last <years_back> years
                    # thus, for every iteration through this while loop, we bundle information (<years_back> + 1) rows at the time
                    i += (years_back + 1)

                print(f"\t|\n\t|__SUCCESS!\n")
            else:
                file_system.append_to_file(company.value[0] + "_" + company.name, "!!! NO DATA FOUND !!!", dir_path.BVB_FINANCIALS)
                print(f"\t|\n\t|__ NO DATA FOR THIS COMPANY! MOVING ON ...\n")

    class Trading():

        class Performance():
            
            def get_trading_performace_data(self, company, readable = False):
                curl_params = bvb_curl_headers_trading.get_curl_params(company)
                self.process_trading_performance_data(company, *curl_params, readable)

            def process_trading_performance_data(self, company, cookies, headers, params, data, readable):
                print(f"> processing financial data from {company.name} ...")

                # clear file before writing to it
                file_system.clear_file(company.value[0] + "_" + company.name, dir_path.BVB_TRADING_PERFORMANCE)

                financials_data = None # this variable will hold the response from calling the API (i.e. the table with the desired values)

                # retrievr website source and write it to a temporary file
                response = requests.post('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx', params=params, cookies=cookies, headers=headers, data=data)
                file_system.write_to_file("_trading_performance_temp.html", response.text, dir_path.BVB_TRADING_PERFORMANCE)

                with open(file_system.get_path_to_file("_trading_performance_temp.html", __file__, dir_path.BVB_TRADING_PERFORMANCE)) as financials_file:
                    financials_data = BeautifulSoup(financials_file, 'html.parser')
                
                table_column_names = financials_data.select("table#gvPerfT th.text-right") # column names
                table_data = financials_data.select("table#gvPerfT tbody td") # table data 

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
                        else: # ... or not

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
                        file_system.append_to_file(company.value[0] + "_" + company.name, data_row, dir_path.BVB_TRADING_PERFORMANCE)

                        # each row in the file contains information about a specific time frame and its values
                        # thus, for every iteration through this while loop, we bundle information 5 columns at the time
                        i += 5

                    print(f"\t|\n\t|__SUCCESS!\n")
                else:
                    file_system.append_to_file(company.value[0] + "_" + company.name, "!!! NO DATA FOUND !!!", dir_path.BVB_TRADING_PERFORMANCE)
                    print(f"\t|\n\t|__ NO DATA FOR THIS COMPANY! MOVING ON ...\n")
        
        class History():
            pass


bvb_trading_performance = BVBRetrievalModule().Trading().Performance()
bvb_trading_performance.get_trading_performace_data(Company.OMV_PETROM, readable=False)


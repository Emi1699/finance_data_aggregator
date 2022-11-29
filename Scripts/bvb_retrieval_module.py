from bs4 import BeautifulSoup
import requests
import file_system
from companies import Company
import curl_headers

class BvbRetrievalModule:
    
    def get_financials_data_of_company(self, company):
        self.process_financials_data(company, *curl_headers.get_curl_params(company))
    
    def process_financials_data(self, company, cookies, headers, params, data):
        # clear file before writing to it
        file_system.clear_file(company.value[0] + "_" + company.name, "financials")

        print(f"> processing financial data from {company.name} ...")
        financials_data = None

        response = requests.post('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx', params=params, cookies=cookies, headers=headers, data=data)
        file_system.write_to_file("_financials_temp.html", response.text, "financials_temp")

        with open(file_system.get_path_to_file("_financials_temp.html", __file__, "financials_temp")) as financials_file:
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

            file_system.append_to_file(company.value[0] + "_" + company.name, data_row, "financials")
            # file_system.append_to_file(company.value[0] + "_" + company.name, "\n", "financials")

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
                file_system.append_to_file(company.value[0] + "_" + company.name, data_row, "financials")

                # each row in the file contains information about a specific financial indicator and its value for the last <years_back> years
                # thus, for every iteration through this while loop, we bundle information (<years_back> + 1) rows at the time
                i += (years_back + 1)

            print(f"\t|\n\t|__SUCCESS!\n")
        else:
            file_system.append_to_file(company.value[0] + "_" + company.name, "!!! NO DATA FOUND !!!", "financials")
            print(f"\t|\n\t|__ NO DATA FOR THIS COMPANY! MOVING ON ...\n")

bvb = BvbRetrievalModule()
# bvb.get_financials_data_of_company(Company.OMV_PETROM)

for company in Company:
    bvb.get_financials_data_of_company(company)
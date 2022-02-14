import openpyxl
import functools
import os
from os import path as relative_path
import datetime
import logging
import bisect

logging.basicConfig(filename="mini_project\logs.log", filemode='w',level = logging.DEBUG, format = '%(asctime)s:[%(levelname)-8s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def verify_file_name(path, extension):
    flag = True
    if relative_path.isfile(path) == False:
        logging.error("Provided path {0} is not a file program ended".format(path))
        flag = False
    if extension != ".xlsx":
        logging.critical("File type {0} is not supported".format(extension))
        flag = False
    if relative_path.exists(path) == False or flag == False:
        logging.critical("File {0} not found program ended".format(path))
    else:
        logging.info("File {0} successfully found".format(path))
        return flag
    return flag        


def parse_file_name(file):
    replacements = ('_')
    file = functools.reduce(lambda s, sep: s.replace(sep, ' '), replacements, file)
    return file.split()
    

def get_month_year(parsed):#list of strings as input
    month_year = [None,None]
    for text in parsed:
        if text.isnumeric():
            month_year[1] = int(text) # gets year
            logging.info("Found year from file name {0}".format(month_year[1]))
            if type(month_year[0]) == int:
                return month_year[0], month_year[1] #can return because year is given after month in the formating described
        try:
            month = datetime.datetime.strptime(text, "%B").month
            month_year[0] = month
            logging.info("Found month from file name '{0}' converting to month number {1} for later use".format(text, month_year[0]))

        except:
            logging.warning("Still searching for year and month from file name")

    logging.critical("could not find month and year program ended")
    quit()


#function does a smart scan
def get_month_year_cell_positions(sheet_obj, file_month, file_year):
    matching_datetime_cells = list()#list of cell coordionates that met description
    logging.debug("Starting search for all locations of rows with information about report on month {0} and year {1}".format(file_month, file_year))
    for row in sheet_obj:
        for column in row:
            if type(column.value) == datetime.datetime:
                if column.value.month == file_month and column.value.year == file_year:#gets the exact datetime here
                    cell_coordinates = (column.row, column.column)
                    logging.info("Found cell with approriate dating at cell_coordinates {0} with value {1}".format(cell_coordinates, column.value))
                    matching_datetime_cells.append(cell_coordinates)
    amt_of_matches = len(matching_datetime_cells)
    if amt_of_matches == 0:
         logging.critical("Could not find any suitable dates")
         quit()
    logging.info("Found {0} cells with approriate dating".format(amt_of_matches))
    return matching_datetime_cells


def get_row_information(sheet_obj, row, column):#assumes datetime can be in any column bu the months data is towards is right as specified 
    row_length = len(sheet_obj[row])
    row_info = list()
    seen_datetime = False # used so if two month cells are in same row so their values are seperated
    for x in range(0, row_length - column + 1):
        cell_value = sheet_obj.cell(row, column + x).value
        cell_column_name = sheet_obj.cell(1, column + x).value#can use 1 since the column name with be on top
        if type(cell_value) == datetime.datetime:
            if seen_datetime == False:
                #logging.info("Starting to display data for day of {0}".format(cell_value))
                row_info.append([cell_value, cell_column_name])
                seen_datetime = True
            else:
                return
        elif(cell_value == None or cell_column_name == None) == False:
            if type(cell_value) != float:
                #logging.info("{0} : {1} : row = {2} : column = {3}".format(cell_column_name, cell_value, row, column + x))
                row_info.append([cell_value, cell_column_name])

            else:
                #logging.info("{0} : {1}%  : row = {2} : column = {3}".format(cell_column_name, cell_value * 100, row, column + x))
                row_info.append([cell_value * 100, cell_column_name])
    return row_info


def print_row_in_priority_order(row):
    displaypriority = {
    "Calls Offered" : 0,
    "Abandon after 30s" : 1,
    "FCR" : 2,
    "DSAT" : 3,
    "CSAT" : 4
    }
    #logging.info(row[0][0].month)#display timestamp being worked on
    #logging.info(row[0][0].strftime("Values being displayed for %B"))
    logging.info(row[0][0].strftime("Values being displayed for %d - %m - %Y"))
    row.remove(row[0])

    sorted(row, key=lambda x: displaypriority[x[1].strip()], reverse=False)#sort information based on a dictionary lookup key and  example given
    for cell in row:
        cell[1] = cell[1].strip() #sanitize display for output
        if type(cell[0]) == float:
            logging.info("{} : {}%".format(cell[1], cell[0])) #for display percetages
        else:
            logging.info("{} : {}".format(cell[1], cell[0])) #for non percentages
    

logging.debug("Start of program mini_project")
path = "C:\\Users\\mskwa_000\\Downloads\\problem_statement_cloud_foundations\\expedia_report_monthly_january_2018.xlsx" #from another directory
#path = "C:\\Users\\mskwa_000\\Downloads\\problem_statement_cloud_foundations\\expedia_report_monthly_march_2018.xlsx" #from another directory
#path = "C:\\Users\\mskwa_000\\Documents\\expedia_report_test_file_monthly_january_2018.xlsx" #from another directory
#path = "mini_project\expedia_report_monthly_march_2018.xlsx"#make so program accepts only excel file #from same directory
#path = "mini_project\expedia_report_monthly_january_2018.xlsx" #from same directory
#path = "mini_project\expedia_report_test_file_monthly_january_2018.xlsx" #from same directory

logging.debug("Check to see if file path exists")

#important to do add for is_proper_path (basically the ifs and else into a function)
file_name, extension = os.path.splitext(path)

if verify_file_name(path, extension) == False:
    logging.critical("file name {0} could not be verify program ended".format(path))
    quit()
else:
    logging.info("file name {0} could be verified program continuing".format(path))

logging.debug("Starting to parse file name {0}".format(path))
parse = parse_file_name(file_name)
logging.info("Successfuly parsed file_name {0} and is of supported type {1}".format(path, extension))

logging.debug("Starting search for month and year from parse of file name {0}".format(path))
file_name_month, file_name_year = get_month_year(parse)
logging.info("Completed search for month and year from file name {0} : file_name_month = {1}, file_name_year = {2}".format(path, file_name_month, file_name_year))

logging.debug("Starting to load excel worksheet")
wb_obj = openpyxl.load_workbook(path, read_only=True)
sheet_obj= wb_obj.active
logging.info("Successfully loaded excel worksheet")

cell_positions = get_month_year_cell_positions(sheet_obj, file_name_month, file_name_year)#return list of (row,column)
rows_info = list()
for match in cell_positions:# to be able to handle all instances that can fit the described time frame
    rows_info.append(get_row_information(sheet_obj, match[0], match[1]))


for row in rows_info:
    print_row_in_priority_order(row)

logging.info("programing successfuly finished execution")

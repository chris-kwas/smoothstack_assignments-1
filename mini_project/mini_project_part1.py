from distutils.log import error
from operator import contains
from posixpath import split
from openpyxl import Workbook
import openpyxl
import functools
import os
import datetime
from datetime import date


def parse_file_name(file):
    #things to do for error checking
    #make sure file is right type
    #make sure file is right name
    replacements = ('_', '.')
    file = functools.reduce(lambda s, sep: s.replace(sep, ' '), replacements, file)# study this line more for latter
    return file.split()
    

def get_month_year(parsed):#list of strings as input
    month_year = [None,None]
    for text in parsed:
        if text.isnumeric():
            month_year[1] = int(text) # gets year
            if type(month_year[0]) == int:
                return month_year[0], month_year[1] #can return because year is given after month in the formating described
        try:
            month = datetime.datetime.strptime(text, "%B").month
            month_year[0] = month
        except:
            #print(text, "not a month")
            pass
    error("could not find month and year program terminated")
    quit()


def get_month_year_cell_positions(sheet_obj,file_month, file_year):
    matching_datetime_cells = list()
    for row in sheet_obj.rows:
        cell = row[0].value
        if type(cell) == datetime.datetime:
            if cell.month == file_month and cell.year == file_year:
                print(cell.month,cell.year, "got the cell row = {0} and the column {1}".format(row[0].row, row[0].column))
                cell_coordinates = (row[0].row, row[0].column)
                matching_datetime_cells.append(cell_coordinates)
    if len(matching_datetime_cells) == 0:
         error("Could not find")
         quit()
    return matching_datetime_cells


def get_row_information(sheet_obj, row, column):
    print("The day of {0}".format(sheet_obj[str(row)][column - 1].value))
    for x in range(1, len(sheet_obj[str(row)])):
        colummn_title = sheet_obj[1][x].value
        column_value = sheet_obj[str(row)][x].value
        if colummn_title != None and column_value != None:
            print("{0} value = {1}".format(colummn_title,column_value))#can use 1 since tod column name with be on top

#--------------------------------------------------------------------------
#IMPORTANT ASK ABOUT NEEDING TO LOOK AT THE OTHER WORK SHEETS IN THE PROJECT -- first sheet only
#IMPORTANT ASK ABOUT if the month and be in any row or guarnteed to be the first one #information about the month is GUARANTEED to be towards the right of the month cell 
                                                                                      # but month cell not guarnteed to be first column need to do a smart search
#--------------------------------------------------------------------------
#needs to be able to show all instance that could apply not just one
#log message ex picked up file and processed file
if __name__ == '__main__':#get rid of this line latter
    path = "mini_project\expedia_report_monthly_march_2018.xlsx"#make so program accepts only excel file
    file_name, extension = os.path.splitext(path)
    parse = parse_file_name(file_name)
    print(parse)
    file_name_month, file_name_year = get_month_year(parse)
    print("file_name_month = {}, file_name_year = {}".format(file_name_month, file_name_year))

    wb_obj = openpyxl.load_workbook(path, read_only=True)
    sheet_obj= wb_obj.active
    cell_positions = get_month_year_cell_positions(sheet_obj, file_name_month, file_name_year)#return list of (row,column)
    print(cell_positions)
    
    for match in cell_positions:# so am able to handle all instances that can fit the described time frame
        get_row_information(sheet_obj, match[0], match[1])



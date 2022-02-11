from operator import contains
from posixpath import split
import openpyxl
#import dataclasses
import functools
import os

def parse_file_name(file):
    #things to do for error checking
    #make sure file is right type
    #make sure file is right name

    # months_shorthand = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
    #       'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}
    replacements = ('_', '.')
    file = functools.reduce(lambda s, sep: s.replace(sep, ' '), replacements, file)# study this line more for latter
    return file.split()
    

def get_month_year(parsed):
    months = {'january' : 'Jan', 'february':'Feb', 'march' : 'Mar', 'april' :  'Apr', 'may' :  'May', 'june' : 'Jun', 'july' : 'Jul',
        'august' : 'Aug', 'september' :  'Sep', 'october' : 'Oct', 'november' :  'Nov', 'december' : 'Dec'}
    month_year = [None,None]
    for text in parsed:
        if contains(months,text):
            month_year[0] = months[text]
        if text.isnumeric():
            month_year[1] = text[-2] + text[-1]#get last to digits
    return (month_year[0],month_year[1])

if __name__ == '__main__':#get rid of this line latter
    path = "mini_project\expedia_report_monthly_january_2018.com"
    file_name, extension = os.path.splitext(path)
    parse = parse_file_name(file_name)
    result = get_month_year(parse)
    print(result,extension)

# wb_obj = openpyxl.load_workbook(path)
# sheet_obj = wb_obj.active
# cell_obj = sheet_obj.cell(row = 9, column = 1)#remember excel starts counting at base 1
# print(cell_obj.value)




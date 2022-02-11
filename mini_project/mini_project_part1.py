from operator import contains
from posixpath import split
import openpyxl
#import dataclasses
import functools

def parse_file_name(file):
    #things to do for error checking
    #make sure file is right type
    #make sure file is right name

    months = {'january' : 'Jan', 'february':'Feb', 'march' : 'Mar', 'april' :  'Apr', 'may' :  'May', 'june' : 'Jun', 'july' : 'Jul',
          'august' : 'Aug', 'september' :  'Sep', 'october' : 'Oct', 'november' :  'Nov', 'december' : 'Dec'}
    months_shorthand = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}
    replacements = ('_', '.')
    file = functools.reduce(lambda s, sep: s.replace(sep, ' '), replacements, file)# study this line more for latter
    words = file.split()
    month_year = [None,None]
    for word in words:
        if contains(months,word):
            print(months[word])
            month_year[0] = months[word]
        if word.isnumeric():
            month_year[1] = word[-2] + word[-1]#get last to digits
            print(word)
    return month_year


if __name__ == '__main__':#get rid of this line latter
    path = "mini_project\expedia_report_monthly_january_2018.xlsx"

    print(parse_file_name(path))

# wb_obj = openpyxl.load_workbook(path)
# sheet_obj = wb_obj.active
# cell_obj = sheet_obj.cell(row = 9, column = 1)#remember excel starts counting at base 1
# print(cell_obj.value)




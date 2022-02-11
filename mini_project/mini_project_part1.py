import openpyxl

wb = openpyxl.load_workbook("expedia_report_monthly_january_2018.xlsx")
ws = wb.active
for row in ws.iter_rows(values_only=True):
    print(row)
#print("C:\Users\mskwa_000\AppData\Local\Temp\Temp1_problem_statement_cloud_foundations.zip\expedia_report_monthly_january_2018.xlsx")
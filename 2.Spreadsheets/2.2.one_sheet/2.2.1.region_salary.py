import xlrd, statistics as st
import wget

# url = ' https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
# wget.download(url)

wb = xlrd.open_workbook('salaries.xlsx')
sheet = wb.sheet_by_index(0)

for row in sheet.get_rows():
    print(row)

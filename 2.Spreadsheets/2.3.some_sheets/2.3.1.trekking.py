import xlrd, statistics as st
import wget

# url = ' https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
# wget.download(url)

wb = xlrd.open_workbook('trekking1.xlsx')
sheet = wb.sheet_by_index(0)
names_calories = [(sheet.cell(i, 0).value, sheet.cell(i, 1).value) for i in range(1, sheet.nrows)]
names_calories.sort(key=lambda x: (-x[1], x[0]))
list(map(lambda x: print(x[0]), names_calories))

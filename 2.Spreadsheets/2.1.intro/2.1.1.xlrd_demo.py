import xlrd
import wget

# url = 'https://stepik.org/media/attachments/lesson/245266/tab.xlsx'
# wget.download(url)

wb = xlrd.open_workbook('tab.xls')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
nmin = sh.row_values(6)[2]
for rownum in range(7, 27):
    temp = sh.row_values(rownum)
    nmin = min(nmin, temp[2])
print(nmin)
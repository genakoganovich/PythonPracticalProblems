import xlrd, math

wb = xlrd.open_workbook('trekking2.xlsx')
url = 'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx'


def download_file():
    import wget
    wget.download(url)


def replace(row):
    return list(map(lambda x: 0 if x == '' else x, row))


def get_table(sheet):
    return {sheet.cell_value(i, 0): replace(sheet.row_values(i, 1))
            for i in range(1, sheet.nrows)}


def get_layout(sheet):
    return [sheet.row_values(i) for i in range(1, sheet.nrows)]


def get_result(table, layout):
    cal = p = f = c = 0
    for item in layout:
        cal += table[item[0]][0] * item[1] / 100
        p += table[item[0]][1] * item[1] / 100
        f += table[item[0]][2] * item[1] / 100
        c += table[item[0]][3] * item[1] / 100

    return list(map(lambda x: str(math.floor(x)), [cal, p, f, c]))


print(' '.join(get_result(get_table(wb.sheet_by_index(0)), get_layout(wb.sheet_by_index(1)))))

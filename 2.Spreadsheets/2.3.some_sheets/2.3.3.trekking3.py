import xlrd, math

wb = xlrd.open_workbook('trekking3.xlsx')
url = 'https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx'


def download_file():
    import wget
    wget.download(url)


def replace(row):
    return list(map(lambda x: 0 if x == '' else x, row))


def get_table(sheet):
    return {sheet.cell_value(i, 0): replace(sheet.row_values(i, 1))
            for i in range(1, sheet.nrows)}


def get_layout_days(sheet):
    layout = {}
    for i in range(1, sheet.nrows):
        layout.setdefault(sheet.cell_value(i, 0), []).append(sheet.row_values(i, 1))
    return layout


def get_result(table, layout):
    cal = p = f = c = 0
    for item in layout:
        cal += table[item[0]][0] * item[1] / 100
        p += table[item[0]][1] * item[1] / 100
        f += table[item[0]][2] * item[1] / 100
        c += table[item[0]][3] * item[1] / 100

    return list(map(lambda x: str(math.floor(x)), [cal, p, f, c]))


def run(table, layout_days):
    for layout in layout_days.values():
        print(' '.join(get_result(table, layout)))


run(get_table(wb.sheet_by_index(0)), get_layout_days(wb.sheet_by_index(1)))

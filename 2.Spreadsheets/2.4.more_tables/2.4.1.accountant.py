import xlrd, math
from os import listdir
from os.path import isfile, join


# wb = xlrd.open_workbook('trekking3.xlsx')

def create_file_list(dir_path):
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f))]


def download_file():
    import wget
    path = 'https://stepik.org/media/attachments/lesson/245299/'
    file_name = 'rogaikopyta.zip'
    url = f'{path}{file_name}'
    wget.download(url)
    import zipfile
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall('.')


def get_payroll(dir_path, data_row, name_col, pay_col):
    payroll = list()
    for file_name in create_file_list(dir_path):
        wb = xlrd.open_workbook(join(dir_path, file_name))
        sheet = wb.sheet_by_index(0)
        payroll.append([sheet.cell_value(data_row, name_col), str(int(sheet.cell_value(data_row, pay_col)))])
    return payroll


def run(dir_path):
    result = get_payroll(dir_path, 1, 1, 3)
    result.sort(key=lambda x: x[0])
    result = list(map(lambda x: ' '.join(x), result))

    with open('payroll.txt', 'w', encoding='utf-8') as f_out:
        f_out.writelines('\n'.join(result))


run('input')

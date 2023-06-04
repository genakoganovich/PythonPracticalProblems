import xlrd, statistics as st
import wget

# url = ' https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
# wget.download(url)

wb = xlrd.open_workbook('salaries.xlsx')
sheet = wb.sheet_by_index(0)


def get_max_median_salary_city():
    data_rows = [sheet.row_values(i, 1) for i in range(1, sheet.nrows)]
    medians = list(map(lambda x: st.median(x), data_rows))
    max_median_index = medians.index(max(medians)) + 1
    return sheet.cell(max_median_index, 0).value


def get_prof_max_mean_salary():
    data_cols = [sheet.col_values(i, 1) for i in range(1, sheet.ncols)]
    means = list(map(lambda x: st.mean(x), data_cols))
    max_mean_index = means.index(max(means)) + 1
    return sheet.cell(0, max_mean_index).value


print(get_max_median_salary_city(), get_prof_max_mean_salary())

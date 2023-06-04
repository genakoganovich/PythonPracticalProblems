from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


def test():
    with open("5.html") as fp:
        soup = BeautifulSoup(fp, 'html5lib')

    print(sum(map(lambda td: int(str(td.string).strip()), soup.find_all('td'))))


def run():
    resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html')  # скачиваем файл
    html = resp.read().decode('utf8')  # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser')  # делаем суп
    print(sum(map(lambda td: int(str(td.string).strip()), soup.find_all('td'))))


run()

from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
print('Python' if str(html).count('Python') > str(html).count('C++') else 'C++')

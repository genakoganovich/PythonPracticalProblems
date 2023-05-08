from urllib.request import urlopen
import re

html = str(urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8'))

words = [str(w).replace('<code>', '').replace('</code>', '') for w in re.findall('<code>(.*?)</code>', html)]
words_dict = {w: words.count(w) for w in words}
max_length = max(list(words_dict.values()))
longest_words = [w for w in words_dict.keys() if words_dict[w] == max_length]
longest_words.sort()
print(' '.join(longest_words))

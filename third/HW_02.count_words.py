"""В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don
 t, it s, didn t итд (после того, как убрали знак
 препинания апостроф) считать двумя словами.
Цифры за слова не считаем.


Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке."""
import re
from collections import Counter
from operator import itemgetter
# text = ' lost Hello world. ball ball ball Hollo Hollo Hollo Hello Python. Hello again.Hello world. Hello Python. Hello again.Hello world. Hello Python. Hello again.Hello world. Hello Python. Hello again.'
text = "Python 3.9 is the latest version of Python. It's awesome!"
text = text.replace('It\'s ', 'It s ')
text = text.lower()

text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r"\d+", "", text, flags=re.UNICODE)
text = text.split()
text = sorted(text)
text = reversed(text)
word_counts = Counter(text)

most_words = word_counts.most_common(10)

print(most_words)



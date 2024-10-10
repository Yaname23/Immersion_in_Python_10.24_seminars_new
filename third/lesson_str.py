print('-------------работа со строками-----------')
print('-------------замена символов с replace -----------')
text = 'Hello, world!'
print(text[6])
print(text[3:7])

new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')
print('-------------другие методы-----------')
print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))# ответ -1 говорит о том, что такой буквы в строке нет
#разворот
print(text[::-1])
print('-------------форматирование строк-----------')
name = 'Alex'
age = 12
text_2 = 'Меня зовут %s и мне %d лет' % (name, age)
print(text_2)
print('-------------')
text_3 = 'Меня зовут {} и мне {} лет' . format(name, age)
print(text_3)
print('-------------')
text_4 = f'Меня зовут {name} и мне {age} лет'
print(text_4)
print('-------------')
pi = 3.1415
print(f'Число ПИ с точностью 2 знака: {pi:.2f}')
print('-------------')
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')
print('-------------')
num = 2 *pi * data[1]
print(f'{num = :_}')
print('-------------строковые методы-----------')
print('-------split------')
link = 'https://translate.yandex.ru/'
urls = link.split('/')
print(urls)
print('-------------')
a, b, c = input('введите три числа через пробел: ').split()
print(c, b, a)
print('-------------')
a, b, c, *_ = input('введите не менее трёх чисел через пробел: ').split()
print(b, c, a)

print('-------join------')
data = ['https:', '', 'translate.yandex.ru', '']
url = '/'.join(data)
print(url)
print('-------ещё методы------')
text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print('-------------')
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5 ))



print('-------------работа со  словарями, dict-----------')
print('------------------------')
a = { 'one': 42, 'two': 3.14, 'ten': 'Hello world'}
b = dict( one=42, two=3.14, ten='Hello world')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world')])
print(a, b, c, sep='\n')
print(a==b==c)
print('-------добавление ключа------')

my_dict ={ 'one': 1, 'two': 2, 'three': 3, 'four': 4}
x = 10
my_dict['ten'] = x
print(my_dict)
print('-------доступ к значению словаря------')
TEN = 'ten'
print(my_dict['two'])
print(my_dict[TEN])
# print(my_dict[1]) будет ошибка
print('-------доступ к значению словаря  через метод get------')

print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))

print('-------методы------')
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam = }\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs = }\t{my_dict=}')
print('-------------')
my_dict1 ={ 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict1.keys())

for key in my_dict1.keys():
    print(key)
print('-------------')
print(my_dict1.values())

for value in my_dict1.values():
    print(value)
print('-------------')
print(my_dict1.items())

for tuple_data in my_dict1.items():
    print(tuple_data)
    print(f'{tuple_data[0] = } value before 100 - {100 - tuple_data[1]}')
print('-------способ получше------')
for key, value in my_dict1.items():
    print(f'{key = } value before 100 - {100 - value}')

print('-------удаление последнего ключ-значения из словаря------')
spamm = my_dict1.popitem()
print(f'{spamm = }\t{my_dict1 = }')
egggs = my_dict1.popitem()
print(f'{egggs = }\t{my_dict1 = }')
print('-------------')
sp = my_dict1.pop('two')
print(f'{sp = }\t{my_dict1 = }')
# err = my_dict_1.pop('six')
# err = my_dict_1.pop
print('------обновление словаря-------')
my_dict1 ={ 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict1.update(dict(six=6))
print(my_dict1)
my_dict1.update(dict([('five', 5), ('two', 42)]))
print(my_dict1)
my_dict1 ={ 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict =my_dict1 | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)
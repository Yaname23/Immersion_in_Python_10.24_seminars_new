print('-------------работа с множествами, set-----------')
my_set = { 1, 2, 3, 4, 2, 5, 6, 7}
print(my_set)
my_f_set = frozenset(( 1, 2, 3, 4, 2, 5, 6, 7))
print(my_f_set)
#not_set = { 1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} будет ошибка типа
print('----------методы--------------')
my_set = { 3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)
# my_set.add(9, 10) будет ошибка типа
my_set.add((9, 10))
print(my_set)
print('----------remove--------------')
my_set = { 3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set)
#my_set.remove(10)-KeyError: 10
print('------------discard------------')
my_set = { 3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set)
my_set.discard(10)
print(my_set)
print('-----------intersection-------------')
my_set = { 3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection((other_set))
print(f'{my_set = }\n{other_set = }\n{new_set = }')
print('------------------------')
my_set = { 3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set
print(f'{my_set = }\n{other_set = }\n{new_set = }')
print('-----------union-------------')
my_set = { 3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.union(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
print('------------------------')
new_set2 = my_set | other_set
print(f'{my_set = }\n{other_set = }\n{new_set2 = }')
print('----------difference--------------')
my_set = { 3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
print('------------------------')
new_set2 = my_set - other_set
print(f'{my_set = }\n{other_set = }\n{new_set2 = }')
print('------------------------')
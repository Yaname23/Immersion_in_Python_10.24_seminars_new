"""Задание №7

✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях."""

user_input = input("ВВедите что-нибудь: ")
my_dict = {}

for item in user_input:
    my_dict[item] = my_dict.get(item, 0) + 1
print(my_dict)
print('___вариант 2_ с set_')
for item in set(user_input):
    # print(set(user_input))
    my_dict[item] = user_input.count(item)
print(my_dict)
print('__вариант 3___')
for item in user_input:

    my_dict[item] = user_input.count(item)
print(my_dict)
"""Задание №1
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""
def func():
    while True:
        try:
            num = input("Введите число: ")
            num = float(num)
            return int(num) if int(num) == num  else num
        except ValueError as e:
            print('Ты ввёл не число')

if __name__ == '__main__':
    print(func())
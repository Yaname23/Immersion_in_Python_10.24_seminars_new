# Пользватель вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# 1. целое положительное число
# 2. вещественное положительное и отрицательное число
# 3, строку в нижнем регистре, если в сроке есть хотя бы одна
# заглавная буква
# 4, в строку в нижнем регистре в остльных случаях

НЕ РАБОТАЕТ!ДОДЕЛАТЬ!

data = input("введите что-нибудь: ")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(data))
for i in data:
    if i in numbers:
        data = int(data)

if type(data) == int:
    print(float(data), float(data * -1))
elif type(data) == float:
    print(int(data))
else:
    print(data.lower())
print(type(data))
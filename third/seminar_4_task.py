'''создайте вручную список с повторяющимися элементами, удалите
из него все элементы, которые встречаются дважды, если встречются
нечетное колиечство раз-элемент остаётся в списке'''
import  random
print('-------- Задача 4---------')
number = [ 2, 4, 6, 2, 2, 4, 4, 4, 4, 8, 10, 9, 9, 12, 14, 16, 18]
for item in number:
    if number.count(item) >= 2:
        number.remove(item)
        number.remove(item)
print(number)
print('-------- вариант 2--------')
number = [ 2, 4, 6, 2, 2, 4, 4, 4, 4, 8, 10, 9, 9, 12, 14, 16, 18]
random.shuffle(number)
for item in number:
    if (count := number.count(item)) >= 2:
        for _ in range(count//2):
            number.remove(item)
            number.remove(item)
print(number)
print('-------- вариант 3--------')
lst = [ 2, 4, 6, 2, 2, 4, 4, 4, 4, 8, 10, 9, 9, 12, 14, 16, 18]
# lst = [1,2,3,1,2,3]
i = 0
while i < len(lst):
    item = lst[i]
    if lst.count(item)>=2:
        lst.remove(item)
        lst.remove(item)
    else :
        i += 1
print(lst)
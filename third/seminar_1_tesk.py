#Вручную создайте список с целыми числами, которые повторяются. Получите новый список
#который сожержит уникальные (без постора) элиемнты исходного списка
import random

num = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6]
new_number = []
for i in num:
    if i not in new_number:
        new_number.append(i)
print(new_number)
# подготовьте 2 решения, короткое и длинное, которое не использует другие коллекции
#помимо списков
print('-------------')
print(nums := [random.randint(0, 10) for _ in range(15)])
print(list(set(nums)))
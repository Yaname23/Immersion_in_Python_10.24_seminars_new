#работа со списками
list_1 = list()
list_2 = list((3.14, True, "Hello world!"))
list_3 = []
list_4 = [3.14, True, "Hello world!"]
print(list_1)
print(list_2)
print(list_3)
print(list_4)
print('_______пример 2______________')

my_list = [2, 4, 6, 8, 10, 12]
print(my_list[0])
# print(my_list[6])
print(my_list[-1])
# print(my_list[-10])
print('_______пример 3______________')

a = 42
b = 'hello world'
c = [1, 3, 5, 7]
my_list1 = [None]
my_list1.append(a)
print(my_list1)
my_list1.append(b)
print(my_list1)
my_list1.append(c)
print(my_list1)

my_list1.append(my_list1)# так делать нельзя
print(my_list1)
print('_______пример 4______________')
d = 42
e = 'hello world'
f = [1, 3, 5, 7]
my_list2= [None]
my_list2.extend(e)
print(my_list2)
my_list2.extend(f)
print(my_list2)
my_list2.extend(my_list2)
print(my_list2)
print('_______пример 5______________')

spam = my_list.pop()
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
# err = my_list.pop(10)
print('_______пример 6______________')

my_list4 = [2, 4, 2, 6, 2, 8, 10, 2, 12]
spamm = my_list4.count(2)
print(spamm)
eggss = my_list4.count(3)
print(eggss)
print('_______пример 7_________index_____')
ind = my_list4.index(4)
print(ind)
# ind2 = my_list4.index(4, ind + 1, 90)
# print(ind2)
# err = my_list4.index(3)
print('_______пример 8_____________')

mil_list = [2, 4, 6, 8, 10, 12]
mil_list.insert(2, 555)
print(mil_list)
mil_list.insert( -2, 13)
print(mil_list)
mil_list.insert(42, 73)
print(mil_list)
print('_______пример 9______________')
m_list = [2, 4, 6, 8, 10, 12]
m_list.remove(6)
print(m_list)
# m_list.remove(3)
# print(m_list)
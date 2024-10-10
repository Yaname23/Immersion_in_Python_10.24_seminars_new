print('----------сортировка с функцией sorted------------')
my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
print('----------reverse с функцией sorted------------')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')
print('----------сортировка со списочным методом sort------------')
my_list1 = [4, 8, 2, 9, 1, 7, 2]
my_list1.sort()
print(my_list1)
my_list1.sort(reverse=True)
print(my_list1)
print('----------разворот неупорядоченного списка с reversed------------')
my_list2 = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list2)
print(type(res), res)

rev_list2 = list(reversed(my_list2))
print(my_list2)
print(rev_list2)

for item in reversed(my_list2):
    print(item)

print('----------разворот с методом reverse------------')
m_list = [4, 8, 2, 9, 1, 7, 2]
m_list.reverse()
print(m_list)
print('-----')
m_list = [4, 8, 2, 9, 1, 7, 2]
new_list = m_list[:: -1] #делает разворот
print(m_list, new_list, sep='\n')

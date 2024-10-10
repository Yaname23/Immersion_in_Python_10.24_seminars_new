import copy

print('--------создание копий________')
print('--------срезы_______')
a_list = [ 2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(a_list[2:7:2])
print(a_list[:7:2])
print(a_list[2::2])
print(a_list[2:7:])
print(a_list[8:3:-1])
print(a_list[3::])
print(a_list[:7:])
print('--------копирование_______')
new_list = a_list
print(a_list, new_list, sep='\n')
a_list[2] = 555
print(a_list, new_list, sep='\n')
print('--------ещё копирование_______')
b_list = [ 2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list_b = b_list.copy()
print(b_list, new_list_b, sep='\n')
b_list[2] = 555
print(b_list, new_list_b, sep='\n')
print('--------копирование c matrix_______')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m =matrix.copy()
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
print('--------копирование c matrix-вариант 2_______')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
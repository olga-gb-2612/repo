# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

from random import randint
C = []
for element in input(f'Введите через пробел размер двух массивов: ').split():
     C.append(int(element))
print(C)
N = []
for i in range(C[0]):
     N.append(randint(1,20))
print(N)
M = []
for i in range(C[1]):
     M.append(randint(1,20))
print(M)
#i = set(N).intersection(set(M))
print(sorted(set(N).intersection(set(M))))
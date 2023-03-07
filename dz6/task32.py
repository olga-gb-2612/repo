# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
N = int(input("введите размер массива: "))
x = []
for i in range(N):
     x.append(randint(-20,20))
print(x)
diap = []
for element in input(f'Введите через пробел границы диапазона: ').split():
     diap.append(int(element))
new=[]
for i in range(N):
    if x[i]>=diap[0] and x[i]<=diap[1]:
            new.append(i)
print(new)

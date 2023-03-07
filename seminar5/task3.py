# Замена макс числа на минимальные

from random import randint

def change_list(lst):
    max_val = max(lst)
    for i in range(len(lst)):
        if lst[i] == max_val:
            lst[i] = 1
    return lst

n = int(input('Введите длину списка: '))
marks = [randint(1, 5) for i in range(n)]
print('Исходный список:', marks)
marks = change_list(marks)
print('Измененный список:', marks)
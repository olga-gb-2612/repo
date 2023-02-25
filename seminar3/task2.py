# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

#from random import randint
# list_1 = [randint(1, 10) for i in range(1, 11)]   #ЧЕРЕЗ СРЕЗЫ  
# print(list_1)
# k = int(input('Введите k: '))
# print(list_1[-k:len(list_1)] + list_1[:-k])

lst = [1, 2, 3, 4, 5]
k = 3
for i in range(k):
    lst.insert(0, lst.pop(-1))
print(lst)



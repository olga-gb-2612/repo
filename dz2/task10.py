# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint
n = int(input('Введите кол-во монет: '))
count=0
list = []
for i in range(n):
    list.append(randint(0,1))
   
    if list[i]>0:
        count=count+1
print(list)
if count < n/2:
    print(count)
else:
    print(n-count)     


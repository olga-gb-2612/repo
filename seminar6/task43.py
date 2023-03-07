import random as rd
r = int(input('Введите количество элементов массива: '))
lst_rnd = [rd.randint(0,10) for i in range(r)]

ecsept_index = []
count = 0

print(lst_rnd)

for i in range(r - 1):
    for j in range(i + 1, r):
        if lst_rnd[i] == lst_rnd[j] and j not in ecsept_index and i not in ecsept_index:
            count += 1
            ecsept_index.append(i)
            ecsept_index.append(j)
            print(f'{lst_rnd[i]}(индекс {i}), {lst_rnd[j]}(индекс {j})')
print(f'Всего пар : {count}')
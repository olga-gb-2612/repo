# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

i = int(input("введите трехзначное число: "))
while(i<100 or i>999):
    i = int(input("введите трехзначное число: "))
res = 0
while(i>0):
    res +=i%10
    i=i//10
print(res)

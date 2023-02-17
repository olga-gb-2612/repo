# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

i = int(input("Введите номер билета: "))
i1 = i//100000
i2 = i//10000 - i1*10
i3 = i//1000 - (i1*100+i2*10)
i4 = i//100 - (i1*1000+i2*100+i3*10)
i5 = i//10 - (i1*10000+i2*1000+i3*100+i4*10)
i6 = i%10
if (i1+i2+i3)==(i4+i5+i6):
    print("yes")
else:
    print("no")
    

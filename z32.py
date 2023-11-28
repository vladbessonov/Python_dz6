# Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
n= int(input('Введите размер массива N= '))
min=int(input('Введите минимальный диапазон значений в массиве MIN= '))
max=int(input('Введите максимальный диапазон значений в массиве MAX= '))

arr1=[random.randint(-10,10) for i in range(n)]
print(arr1)
rezalt_i=[]

for i in range(len(arr1)):                           
    if arr1[i] > min and arr1[i] < max:
        rezalt_i.append(i)
            
print(rezalt_i)











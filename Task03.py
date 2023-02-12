# Задача:
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

n = int(input('Ввведите количество элементов списка: '))

list = []
for i in range(n):
    list.append(random.randint(0, 10))
print(list)

list1 = []
[list1.append(i) for i in list if i not in list1]
print(list1)
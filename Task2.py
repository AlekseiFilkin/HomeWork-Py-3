'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

import random
n = int(input('Введите длину массива N: '))
index = 0
list = []
for i in range(1,n+1):
    i = random.randint(1,n)
    list.append(i)
print(list)
x = int(input('Введите число X: ' ))
min = abs(x - list[0])
for j in range(1, n):
    count = abs(x - list[j])
    if count < min:
        min = count
        index = j
print(f'Число {list[index]} наиболее близкий элемент к числу {x}')
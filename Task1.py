'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''
import random

n = int(input("Введите количество элементов: "))
new_list = []
for i in range(1, n+1):
    i = random.randint(1,n)
    new_list.append(i)
print(new_list)
x = int(input("Введите число которое необходимо найти: "))
i = 0
for index in range(len(new_list)):
    if new_list[index] == x:
        i += 1
print(f'Число {x} встретилось {i} раз')
# -*- encoding: utf-8 -*-

# 2. Во втором массиве сохранить индексы четных элементов
# первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями
# 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random

size = 10
first = [random.randint(0, 99) for _ in range(size)]
# first = [8, 3, 15, 6, 4, 2]
second = []
for i in range(len(first)):
    if first[i] % 2 == 0:
        second.append(i)
print(second)

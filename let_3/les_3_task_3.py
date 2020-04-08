# -*- encoding: utf-8 -*-

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


size = 10
# first = [random.randint(0, 99) for _ in range(size)]
first = [8, 3, 15, 6, 4, 2]
second = []
max = 0
min = 0
for i in range(len(first)):

    if first[max] < first[i]:
        max = i
    else:
        min = i

first[min], first[max] = first[max], first[min]
print(first)

# -*- encoding: utf-8 -*-

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import sys

# Вариант a.
def f_a(size):
    # size = 10
    list_x = [random.randint(0, 99) for _ in range(size)]
    print(sys.getsizeof(list_x))
    # list_x = [8, 3, 15, 6, 4, 2]
    max = 0
    min = 0
    print(sys.getsizeof(max), sys.getsizeof(min))
    for i in range(len(list_x)):
        print(sys.getsizeof(i))
        if list_x[max] < list_x[i]:
            max = i
        else:
            min = i

    list_x[min], list_x[max] = list_x[max], list_x[min]
    print(sys.getsizeof(list_x))
    return list_x

# Cуммарная память 192+24+24+28 = 268


# Вариант b.
def f_b(size):
    # size = 10
    list_x = [random.randint(0, 99) for _ in range(size)]
    print(sys.getsizeof(list_x))
    # list_x = [8, 3, 15, 6, 4, 2]
    list_x_c = list_x[:]
    print(sys.getsizeof(list_x_c))
    for j in range(len(list_x_c) - 1):
        for i in range(len(list_x_c) - j):
            if i == 0:
                continue
            if list_x_c[i] < list_x_c[i - 1]:
                list_x_c[i], list_x_c[i - 1] = list_x_c[i - 1], list_x_c[i]

    min = list_x_c[0]
    max = list_x_c[-1]
    print(sys.getsizeof(min))
    print(sys.getsizeof(max))

    list_x[list_x.index(min)], list_x[list_x.index(max)] = list_x[list_x.index(max)], list_x[list_x.index(min)]
    return list_x

# Cуммарная память 192+144+28+28+28+28 = 268


# Вариант c.
def f_c(size):
    # size = 10
    list_x = [random.randint(0, 99) for _ in range(size)]
    print(sys.getsizeof(list_x))
    # list_x = [8, 3, 15, 6, 4, 2]
    max = 0
    min = 0
    print(sys.getsizeof(max))
    print(sys.getsizeof(min))
    for i in range(len(list_x)):

        if list_x[max] < list_x[i]:
            max = i

    for i in range(len(list_x)):

        if list_x[max] > list_x[i]:
            min = i

    list_x[min], list_x[max] = list_x[max], list_x[min]
    return list_x

# Cуммарная память 192+28+28+28 = 276




f_c(10)

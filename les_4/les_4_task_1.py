# -*- encoding: utf-8 -*-

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
# f_a(100)
# 1000 loops, best of 3: 117 usec per loop

# f_a(1000)
# 1000 loops, best of 3: 1.15 msec per loop

# f_a(10000)
#10 loops, best of 3: 12.6 msec per loop



# f_b(100)
# 1000 loops, best of 3: 842 usec per loop

# f_b(1000)
# 1000 loops, best of 3: 78.1 msec per loop

# f_b(10000)
#10 loops, best of 3: 8.25 sec per loop


# f_c(100)
# 1000 loops, best of 3: 120 usec per loop

# f_c(1000)
# 1000 loops, best of 3: 1.13 msec per loop

# f_c(10000)
#10 loops, best of 3: 12.7 msec per loop



# Вариант a.
def f_a(size):
    # size = 10
    list_x = [random.randint(0, 99) for _ in range(size)]
    # list_x = [8, 3, 15, 6, 4, 2]
    max = 0
    min = 0
    for i in range(len(list_x)):

        if list_x[max] < list_x[i]:
            max = i
        else:
            min = i

    list_x[min], list_x[max] = list_x[max], list_x[min]
    return list_x


# Вариант b.
def f_b(size):
    # size = 10
    list_x = [random.randint(0, 99) for _ in range(size)]
    # list_x = [8, 3, 15, 6, 4, 2]
    list_x_c = list_x[:]
    for j in range(len(list_x_c) - 1):
        for i in range(len(list_x_c) - j):
            if i == 0:
                continue
            if list_x_c[i] < list_x_c[i - 1]:
                list_x_c[i], list_x_c[i - 1] = list_x_c[i - 1], list_x_c[i]

    min = list_x_c[0]
    max = list_x_c[-1]
    list_x[list_x.index(min)], list_x[list_x.index(max)] = list_x[list_x.index(max)], list_x[list_x.index(min)]
    return list_x

# Вариант c.
def f_c(size):
    # size = 10
    list_x = [random.randint(0, 99) for _ in range(size)]
    # list_x = [8, 3, 15, 6, 4, 2]
    max = 0
    min = 0
    for i in range(len(list_x)):

        if list_x[max] < list_x[i]:
            max = i

    for i in range(len(list_x)):

        if list_x[max] > list_x[i]:
            min = i

    list_x[min], list_x[max] = list_x[max], list_x[min]
    return list_x

# import cProfile
# cProfile.run('f_c(10000000)')

# import timeit
# print(timeit.timeit("x = 2 + 2"))
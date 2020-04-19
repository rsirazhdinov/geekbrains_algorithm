# -*- encoding: utf-8 -*-

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50). Выведите на
# экран исходный и отсортированный массивы.


import random

SIZE = 3
# a = [random.randint(0, 49) for _ in range(SIZE)]
a = [7, 6, 49, 5, 2]
print(a)


def sort_slice(array):
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    middle = len(array) // 2

    left = sort_slice(array[0: middle])
    right = sort_slice(array[middle:])

    result = []

    l = left.pop(0)
    r = right.pop(0)

    while l is not None or r is not None:

        if l is None:
            result.append(r)
            if len(right) > 0:
                r = right.pop(0)
            else:
                r = None
        elif r is None:
            result.append(l)
            if len(left) > 0:
                l = left.pop(0)
            else:
                l = None
        elif r < l:
            result.append(r)
            if len(right) > 0:
                r = right.pop(0)
            else:
                r = None
        else:
            result.append(l)
            if len(left) > 0:
                l = left.pop(0)
            else:
                l = None

    return result

print(sort_slice(a))

# -*- encoding: utf-8 -*-

# 3. Массив размером 2m + 1, где m — натуральное число, заполнен
# случайным образом. Найдите в массиве медиану. Медианой называется
# элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который
# не рассматривался на уроках (сортировка слиянием также недопустима).


import random

m = 10
size = 2 * m + 1
# a = [random.randint(0, 49) for _ in range(size)]
a = [7, 6, 49, 5, 2, 10, 11, 12, 13]
print(a)


def mediana(array):
    result_index = 0
    higher = 0
    lower = 0

    for i in range(1, len(array)):
        if array[i] > array[result_index]:
            higher += 1
        elif array[i] < array[result_index]:
            lower += 1
    print('higher={}'.format(higher))
    print('lower={}'.format(lower))
    if higher == lower:
        return higher
    step = abs(int((higher - lower) / 2))
    print(step)
    order_stak = []
    order_stak.append(array[result_index])

    result = array[result_index]
    for i in range(step):
        current = None
        for el in array:
            if higher > lower:
                if result < el:
                    if current is None:
                        current = el
                    elif el < current:
                        current = el
            else:
                if result > el:
                    if current is None:
                        current = el
                    elif el > current:
                        current = el

        result = current
        return result

    # print(higher)
    # print(lower)


m = mediana(a)
print('mediana = {}'.format(m))

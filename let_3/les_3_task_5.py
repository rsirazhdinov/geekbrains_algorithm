# -*- encoding: utf-8 -*-

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


size = 10
# first = [random.randint(0, 99) for _ in range(size)]
first = [8, 3, -4, -15, 6,  2, -2, 3, 3]
result_index = None
for i, item in enumerate(first):
    if item < 0:
        if result_index is None:
            result_index = i
        if first[result_index] < item:
            result_index = i

print(result_index, first[result_index])
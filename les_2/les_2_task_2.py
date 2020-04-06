# -*- encoding: utf-8 -*-

# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).

x = input('Введите число: ')
count_event = 0
count_odd = 0
i = 0
for i in range(len(x)):
    if int(x[i]) % 2 == 0:
        count_event += 1
    else:
        count_odd += 1
print('Четных цифр {}, нечетных {}'.format(count_event, count_odd))
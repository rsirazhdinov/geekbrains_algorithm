# -*- encoding: utf-8 -*-

# 4. Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите число: '))
a = 1
s = 0

for i in range(n):
    s += a
    a = a / 2

print('Сумма n первых членов последовательности: {}'.format(s))

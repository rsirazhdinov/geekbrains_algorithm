# -*- encoding: utf-8 -*-

from collections import namedtuple, OrderedDict, deque
import itertools

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем
# счисления, задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант
# не подходит. Поэтому использование встроенных функций для перевода из одной системы счисления
# в другую в данной задаче под запретом.


a = deque(input('Введите чило a: '))
b = deque(input('Введите число b: '))
a.reverse()
b.reverse()

hex_to_int = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

int_to_hex = {v: k for k, v in hex_to_int.items()}

# Summa
summa = deque()
k = deque([0], maxlen=1)
for i in itertools.zip_longest(a, b, fillvalue=0):
    try:
        x = int(i[0])
    except ValueError:
        x = hex_to_int[i[0]]

    try:
        y = int(i[1])
    except ValueError:
        y = hex_to_int[i[1]]

    z = x + y + k[0]
    z_i = z % 16

    if z_i > 9:
        z_d = int_to_hex[z_i]
    else:
        z_d = str(z_i)
    print(z_d)

    summa.appendleft(z_d)
    k.append(z // 16)
# print(a,b)

print(summa)

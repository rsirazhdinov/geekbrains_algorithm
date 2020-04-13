# -*- encoding: utf-8 -*-
#
# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple, OrderedDict

N_company = int(input('Введите количество предприятий: '))
enterprise = namedtuple('enterprise', 'name profit')
enterprises = []
summa = 0
for i in range(N_company):
    t = []
    name = input('Введите название {} предприятия: '.format(i + 1))
    t.append(name)
    profit = int(input('Введите прибыль {} предприятия: '.format(i + 1)))
    summa += profit
    t.append(profit)
    company = enterprise._make(t)
    enterprises.append(company)

if N_company > 0:
    average_profit = summa / N_company
else:
    average_profit = 0

higher = []
lower = []
for elem in enterprises:
    if elem.profit >= average_profit:
        higher.append(elem)
    else:
        lower.append(elem)

print('Средняя прибыль предприятий за год: {} млн руб'.format(average_profit))
print('Предприятий, у которых прибыль выше среднего:')

for elem in higher:
    print(elem.name)

print('Предприятий, у которых прибыль ниже среднего:')

for elem in lower:
    print(elem.name)

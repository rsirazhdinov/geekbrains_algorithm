# -*- encoding: utf-8 -*-

# 1. В диапазоне натуральных чисел от
# 2 до 99 определить, сколько из них кратны каждому из чисел в
# диапазоне от 2 до 9. Примечание: 8 разных ответов..

result = {i: 0 for i in range(2, 10)}
for i in range(2, 100):
    for k in result.keys():
        if i % k == 0:
            result[k] += 1
print(result)
#

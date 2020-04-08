# -*- encoding: utf-8 -*-

# 4. Определить, какое число в массиве встречается чаще всего.


size = 10
# first = [random.randint(0, 99) for _ in range(size)]
first = [8, 3, 15, 6, 4, 2, 2, 3, 3]
print(first)
frequency = {}.fromkeys(first, 0)
max_freq = 0
max_elem = first[0]
for item in first:

    frequency[item] += 1
    if max_freq < frequency[item]:
        max_freq = frequency[item]
        max_elem = item
print(max_freq)
print(max_elem)

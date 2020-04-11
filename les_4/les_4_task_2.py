# -*- encoding: utf-8 -*-


#a Решето Эратосфена
def f_a(n):
    arat_list = [i for i in range(n)]
    arat_list[1] = 0

    for i in range(2, n):
        if arat_list[i] != 0:
            j = i * 2
            while j < n:
                arat_list[j] = 0
                j += i
    result_list = [e for e in arat_list if e != 0]
    for e in arat_list:
        if e != 0:
            result_list.append(e)
    return result_list


# b Классический способ
def f_b(n):
    result = []
    for i in range(2, n, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in result:
            if j * j - 1 > i:
                result.append(i)
                break
            if (i % j == 0):
                break
        else:
            result.append(i)
    return result

import cProfile
cProfile.run('f_b(1000000)')



# Оценка алгоритмов
# a: python3 -m timeit -n 10 -s "import les_4_task_5" "les_4_task_5.f_a(1000000)"
# a: 10 loops, best of 3: 441 msec per loop

#         78504 function calls in 0.490 seconds
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.008    0.008    0.490    0.490 <string>:1(<module>)
   #      1    0.027    0.027    0.027    0.027 les_4_task_5.py:18(<listcomp>)
   #      1    0.396    0.396    0.482    0.482 les_4_task_5.py:6(f_a)
   #      1    0.054    0.054    0.054    0.054 les_4_task_5.py:7(<listcomp>)
   #      1    0.000    0.000    0.490    0.490 {built-in method builtins.exec}
   #  78498    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#
# b:python3 -m timeit -n 10 -s "import les_4_task_5" "les_4_task_5.f_b(1000000)"
# b: 10 loops, best of 3: 98 msec per loop

# 5 function calls in 0.112 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.112    0.112 <string>:1(<module>)
#         1    0.112    0.112    0.112    0.112 les_4_task_5.py:26(f_b)
#         1    0.000    0.000    0.112    0.112 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



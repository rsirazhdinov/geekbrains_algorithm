# -*- encoding: utf-8 -*-
from collections import deque

N = 4
deq = deque()
deq.append(0)
is_visited = [False for _ in range(N)]
is_visited[0] = True

list_edge = set()

while len(deq) > 0:
    current = deq.pop()
    for i in range(N):
        if current != i:
            list_edge.add(tuple({current, i}))
        if current != i and not is_visited[i]:
            is_visited[i] = True
            deq.appendleft(i)



print('{} человек совершили {} рукопожатий'.format(N, len(list_edge)))
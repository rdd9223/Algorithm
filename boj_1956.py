# 운동

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

V, E = map(int, input().split())
paths = [list(map(int, input().split())) for _ in range(E)]
cycle = [-1]
graph = defaultdict(list)
for path in paths:
    start, end, value = path
    graph[start].append([end, value])


def dfs(s, discovered=[]):
    print(discovered)
    discovered.append(s)
    for e, v in graph[s]:
        if not e in discovered:
            discovered = dfs(e, discovered)
    return discovered


for i in range(V):
    a = dfs(i + 1)
    print(i, a)

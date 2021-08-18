# 운동

import sys
from collections import defaultdict, deque

input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
table = [[INF for _ in range(V)] for _ in range(V)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    table[start - 1][end - 1] = cost

result = INF

for i in range(V):
    for j in range(V):
        '''
        원래 플로이드 워셜 알고리즘이면 있어야 하는 코드
        하지만 사이클을 만들어야하기 때문에 생략
        '''
        # if i == j:
        #     table[i][j] = 0
        for k in range(V):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])
    result = min(result, table[i][i])

if result == INF:
    print(-1)
else:
    print(result)

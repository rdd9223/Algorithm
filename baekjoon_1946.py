# 신입 사원
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    ranks = []
    n = int(input())

    for _ in range(n):
        ranks.append(list(map(int, input().split())))
    ranks = sorted(ranks, key=lambda x: x[0])
    count = 1
    min = ranks[0][1]

    for j in range(1, n):
        if ranks[j][1] < min:
            min = ranks[j][1]
            count += 1

    print(count)

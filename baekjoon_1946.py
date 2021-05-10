# 신입 사원
import sys

input = sys.stdin.readline

t = int(input())
ranks = []
passRanks = []

for i in range(t):
    ranks.append([])
    passRanks.append([])
    n = int(input())

    for _ in range(n):
        ranks[i].append(list(map(int, input().split())))
    ranks[i] = sorted(ranks[i], key=lambda x: x[0])

for i in range(t):
    for j in range(len(ranks[i])):
        if j == 0:
            passRanks[i].append(ranks[i][j])
            continue

        elif ranks[i][j][1] < min(list(map(lambda x: x[1], passRanks[i]))):
            passRanks[i].append(ranks[i][j])
            continue

    print(len(passRanks[i]))

# 2293 동전1

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coinList = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k)]

for i in coinList:
    for j in range(k):
        if j + 1 == i:
            dp[j] += 1
        elif j + 1 > i:
            dp[j] += dp[j-i]

print(dp[-1])

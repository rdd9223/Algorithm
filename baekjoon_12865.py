# 평범한 배낭

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
itemArr = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    itemArr.append([W, V])

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j < itemArr[i][0]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1]
                           [j - itemArr[i][0]] + itemArr[i][1])

print(dp[N][K])

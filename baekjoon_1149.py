# RGB거리

import sys

input = sys.stdin.readline

N = int(input())
itemList = [[0, 0, 0]]
for _ in range(N):
    R, G, B = map(int, input().split())
    itemList.append([R, G, B])

for i in range(1, N + 1):
    itemList[i][0] = itemList[i][0] + min(itemList[i-1][1], itemList[i-1][2])
    itemList[i][1] = itemList[i][1] + min(itemList[i-1][0], itemList[i-1][2])
    itemList[i][2] = itemList[i][2] + min(itemList[i-1][0], itemList[i-1][1])

print(min(itemList[N][0], itemList[N][1], itemList[N][2]))

# 주사위 쌓기
import sys

input = sys.stdin.readline

size = int(input())
diceList = []
maximumAmount = 0
pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

for i in range(size):
    line = list(map(int, input().split()))
    diceList.append(line)

for i in range(6):
    result = []
    tmp = [1, 2, 3, 4, 5, 6]
    tmp.remove(diceList[0][i])
    pairNum = diceList[0][pair[i]]
    tmp.remove(pairNum)
    result.append(max(tmp))
    for j in range(1, size):
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.remove(pairNum)
        pairNum = diceList[j][pair[diceList[j].index(pairNum)]]
        tmp.remove(pairNum)
        result.append(max(tmp))
    result = sum(result)
    if maximumAmount < result:
        maximumAmount = result

print(maximumAmount)

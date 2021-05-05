# 주사위 쌓기
import sys

input = sys.stdin.readline

size = int(input())
diceList = []
maximumAmount = 0

for i in range(size):
    line = list(map(int, input().split()))
    diceList.append(line)


def putDice(bottom, s=0, floorIdx=0):
    if floorIdx == size:
        global maximumAmount
        if maximumAmount < s:
            maximumAmount = s
        return
    else:
        idx = diceList[floorIdx].index(bottom)
        floor = diceList[floorIdx]
        if idx == 0 or idx == 5:
            s += max(floor[1], floor[2], floor[3], floor[4])
            floorIdx += 1
            putDice(floor[5 if idx == 0 else 0], s, floorIdx)
            return
        elif idx == 1 or idx == 3:
            s += max(floor[0], floor[2], floor[5], floor[4])
            floorIdx += 1
            putDice(floor[3 if idx == 1 else 1], s, floorIdx)
            return
        elif idx == 2 or idx == 4:
            s += max(floor[0], floor[1], floor[3], floor[5])
            floorIdx += 1
            putDice(floor[4 if idx == 2 else 2], s, floorIdx)
            return


for i in diceList[0]:
    putDice(i)

print(maximumAmount)

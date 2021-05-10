# 거스름돈
import sys

input = sys.stdin.readline

pay = int(input())
change = 1000 - pay
amount = 0

while change:
    if change - 500 >= 0:
        amount += 1
        change -= 500
        continue
    elif change - 100 >= 0:
        amount += 1
        change -= 100
        continue
    elif change - 50 >= 0:
        amount += 1
        change -= 50
        continue
    elif change - 10 >= 0:
        amount += 1
        change -= 10
        continue
    elif change - 5 >= 0:
        amount += 1
        change -= 5
        continue
    elif change - 1 >= 0:
        amount += 1
        change -= 1
        continue

print(amount)

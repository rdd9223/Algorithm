import sys
import itertools

input = sys.stdin.readline

count = 0
size, amount = map(int, input().split())
numList = list(map(int, input().split()))

for i in range(1, size+1):
    combinations = list(itertools.combinations(numList, i))
    for elem in combinations:
        if sum(elem) == amount:
            count += 1

print(count)

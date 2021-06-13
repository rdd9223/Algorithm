# 포도주 시식
import sys

input = sys.stdin.readline

n = int(input())
wine = [0] + list(int(input()) for _ in range(n))
mem = [0]

for i in range(1, n + 1):
    if i < 3:
        mem.append(wine[i] + mem[i-1])
    else:
        maxCase1 = mem[i - 1]
        maxCase2 = wine[i] + mem[i - 2]
        maxCase3 = wine[i] + wine[i - 1] + mem[i - 3]

        mem.append(max(maxCase1, maxCase2, maxCase3))

print(mem[n])

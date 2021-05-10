# 동전 0
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = []
count = 0
for _ in range(n):
    a.append(int(input()))

a = sorted(a, reverse=True)

for coin in a:
    count += k // coin
    k %= coin

print(count)

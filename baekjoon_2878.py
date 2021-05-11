# 캔디캔디
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
friends = []

for _ in range(n):
    friends.append(int(input()))

friends.sort()
difference = sum(friends) - m
amount = 0

for i in range(n):
    tmp = min(friends[i], difference // (n - i))
    amount += tmp ** 2
    difference -= tmp

print(amount % 2**64)

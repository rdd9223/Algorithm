# 캔디캔디
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
friends = []

for _ in range(n):
    friends.append(int(input()))

difference = sum(friends) - m
amount = 0

for i in range(n):
    amount += (difference // (n - i)) ** 2
    difference -= difference // (n - i)

print(amount)

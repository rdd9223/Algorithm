# 캔디캔디
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
friends = []

for _ in range(n):
    friends.append(int(input()))

for _ in range(m):
    if max(friends) == 0:
        continue
    friends[friends.index(max(friends))] -= 1

print(sum(map(lambda x: x**2, friends)))

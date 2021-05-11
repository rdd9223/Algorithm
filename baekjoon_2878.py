# 캔디캔디
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
friends = []

for _ in range(n):
    friends.append(int(input()))

difference = sum(friends) - m
amount = 0

for i in range(n, 0, -1):
    if i == 1:
        amount += difference ** 2
        break

    amount += (difference % i) ** 2
    difference -= difference % i

print(amount % 2**64)

# 5개 4명

# case 1
# 1 2 3 4
# 0 0 2 3
# 1 4 1 1 = 7

# case 2
# 1 2 3 4
# 0 0 1 4
# 1 4 4 0 = 9

# case 3
#

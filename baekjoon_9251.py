# Longest Common Subsequence
import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()

fLen = len(first)
sLen = len(second)

table = [[0] * (sLen + 1) for _ in range(fLen + 1)]

for i in range(fLen + 1):
    for j in range(sLen + 1):
        if i == 0 or j == 0:
            table[i][j] = 0

        elif first[i - 1] == second[j - 1]:
            table[i][j] = table[i-1][j] + 1

        else:
            table[i][j] = max(table[i - 1][j], table[i][j-1])
print(table[fLen][sLen])

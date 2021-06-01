# Longest Common Subsequence
import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()

fLen = len(first)
sLen = len(second)

table = [[0] * (sLen + 1) for _ in range(fLen + 1)]

for i in range(1, fLen + 1):
    for j in range(1, sLen + 1):
        if first[i - 1] == second[j - 1]:
            table[i][j] = table[i-1][j-1] + 1

        else:
            table[i][j] = max(table[i - 1][j], table[i][j-1])
print(table[fLen][sLen])

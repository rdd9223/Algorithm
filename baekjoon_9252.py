import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()

fLen = len(first)
sLen = len(second)

memory = [[0] * (fLen + 1) for _ in range(sLen + 1)]

for i in range(sLen + 1):
    for j in range(fLen + 1):
        if i == 0 or j == 0:
            continue
        elif first[j - 1] == second[i - 1]:
            memory[i][j] = memory[i-1][j-1] + 1
        else:
            memory[i][j] = max(memory[i - 1][j], memory[i][j - 1])

print(memory[sLen][fLen])

if memory[sLen][fLen] != 0:
    startPoint = fLen + 1
    lcs = []
    for i in reversed(range(sLen + 1)):
        for j in reversed(range(startPoint)):
            if j == 0:
                break
            if memory[i][j - 1] != memory[i][j] and memory[i-1][j] != memory[i][j]:
                startPoint = j
                lcs.append(first[j - 1])
                break
    reverseLcs = "".join(lcs[::-1])
    print(reverseLcs)

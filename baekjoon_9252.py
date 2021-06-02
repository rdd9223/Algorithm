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

lcs = []
print(memory[sLen][fLen])

while fLen > 0 and sLen > 0:
    if memory[sLen][fLen - 1] == memory[sLen][fLen]:
        fLen -= 1
    elif memory[sLen - 1][fLen] == memory[sLen][fLen]:
        sLen -= 1
    else:
        lcs.append(first[fLen-1])
        fLen -= 1
        sLen -= 1
if lcs:
    reverseLcs = "".join(lcs[::-1])
    print(reverseLcs)

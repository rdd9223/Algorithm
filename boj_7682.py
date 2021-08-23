# 틱택토

import sys

input = sys.stdin.readline

result = []

while True:
    line = input().strip()

    if line == "end":
        break

    xCount = line.count('X')
    oCount = line.count('O')
    dotCount = line.count('.')

    if xCount == 5 and oCount == 4 and dotCount == 0:
        if line[0] == line[1] and line[1] == line[2] and line[0] == 'O':
            result.append('invalid')
            continue
        if line[0] == line[3] and line[3] == line[6] and line[0] == 'O':
            result.append('invalid')
            continue
        if line[0] == line[4] and line[4] == line[8] and line[0] == 'O':
            result.append('invalid')
            continue
        if line[1] == line[4] and line[4] == line[7] and line[1] == 'O':
            result.append('invalid')
            continue
        if line[2] == line[4] and line[4] == line[6] and line[2] == 'O':
            result.append('invalid')
            continue
        if line[2] == line[5] and line[5] == line[8] and line[2] == 'O':
            result.append('invalid')
            continue
        if line[3] == line[4] and line[4] == line[5] and line[3] == 'O':
            result.append('invalid')
            continue
        if line[6] == line[7] and line[7] == line[8] and line[6] == 'O':
            result.append('invalid')
            continue
        result.append('valid')
        continue

    if line[0] == line[1] and line[1] == line[2]:
        if line[0] == 'O' and xCount == oCount:
            result.append('valid')
            continue
        elif line[0] == 'X' and xCount == oCount + 1:
            result.append('valid')
            continue
    if line[0] == line[3] and line[3] == line[6]:
        if line[0] == 'O' and xCount == oCount:
            result.append('valid')
            continue
        elif line[0] == 'X' and xCount == oCount + 1:
            result.append('valid')
            continue
    if line[0] == line[4] and line[4] == line[8]:
        if line[0] == 'O' and xCount == oCount:
            result.append('valid')
            continue
        elif line[0] == 'X' and xCount == oCount + 1:
            result.append('valid')
            continue
    if line[1] == line[4] and line[4] == line[7]:
        if line[1] == 'O' and xCount == oCount:
            result.append('valid')
            continue
        elif line[1] == 'X' and xCount == oCount + 1:
            result.append('valid')
            continue
    if line[2] == line[4] and line[4] == line[6]:
        if line[2] == 'O' and xCount == oCount:
            result.append('valid')
            continue
        elif line[2] == 'X' and xCount == oCount + 1:
            result.append('valid')
            continue
    if line[2] == line[5] and line[5] == line[8]:
        if line[2] == 'O' and xCount == oCount:
            result.append('valid')
            continue
        elif line[2] == 'X' and xCount == oCount + 1:
            result.append('valid')
            continue
    if line[3] == line[4] and line[4] == line[5]:
        if line[3] == 'O' and xCount == oCount:
            result.append('valid')
            continue
        elif line[3] == 'X' and xCount == oCount + 1:
            result.append('valid')
            continue
    if line[6] == line[7] and line[7] == line[8]:
        if line[6] == 'O' and xCount == oCount:
            result.append('valid')
            continue
        elif line[6] == 'X' and xCount == oCount + 1:
            result.append('valid')
            continue
    result.append('invalid')

for txt in result:
    print(txt)

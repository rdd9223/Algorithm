import sys

input = sys.stdin.readline

size = int(input())

userList = []

for i in range(size):
    a = input().split()
    userList.append([int(a[0]), int(a[1])])

for i in range(size):
    count = 1
    for j in range(size):
        if userList[i] is userList[j]:
            continue
        elif userList[i][0] < userList[j][0] and userList[i][1] < userList[j][1]:
            count += 1
    if i == size-1:
        print(count, end="")
    else:
        print(count, end=" ")

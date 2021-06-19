# 나무 자르기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
maxHeight = max(trees)
flag = (start + end) // 2

while True:
    height = maxHeight - flag
    length = sum(
        list(map(lambda x: 0 if x <= height else (x - height), trees)))

    if flag == start:
        maxHeight -= (end if M > length else start)
        break

    if M <= length:
        end = flag
    else:
        start = flag
    flag = (start + end) // 2

print(maxHeight)

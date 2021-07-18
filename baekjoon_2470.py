# 두 용액
import sys

input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))

solutions.sort()
minimum = solutions[0] + solutions[N - 1]
answerLeft = 0
answerRight = N - 1
left = 0
right = N - 1

while left < right:
    tmp = solutions[left] + solutions[right]

    if abs(tmp) < abs(minimum):
        minimum = tmp
        answerLeft = left
        answerRight = right

    if tmp == 0:
        minimum = 0
        answerLeft = left
        answerRight = right
        break
    elif tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1

print(solutions[answerLeft], solutions[answerRight])

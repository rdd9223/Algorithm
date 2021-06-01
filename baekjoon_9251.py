# Longest Common Subsequence
import sys

sys.setrecursionlimit(10**6)
memory = []
input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()


def lcs(x, y):
    # x와 y를 이미 계산했는지 메모리를 뒤져서 검사함. 있으면 함수 종료
    if [x, y] in memory or [y, x] in memory or len(x) == 0 or len(y) == 0:
        return 0

    # x와 y의 마지막 알파벳이 같다면 둘다 하나씩 깎고 length를 1 증가시키고 lcs돌림, memory에 저장
    if x[-1] == y[-1]:
        memory.append([x, y])

        return 1 + lcs(x[: -1], y[: -1])

    # x와 y의 마지막 알파벳이 같지 않다면 왼쪽, 오른쪽을 각각 하나씩 깎고 lcs를 돌림, memory에 저장
    else:
        memory.append([x, y])

        return max(lcs(x[: -1], y), lcs(x, y[: -1]))


print(lcs(first, second))

import sys

input = sys.stdin.readline


def fn(param):
    count = 1
    prev = 0
    for i in range(1, N):
        if houses[i] - houses[prev] >= param:
            count += 1
            prev = i
    return count >= C


def search():
    low = 1
    high = houses[N - 1]  # 왜 풀이에서 이 경우에 + 1을 해주는지 모르겠음
    while low + 1 < high:
        mid = (low + high) // 2
        if fn(mid):
            low = mid
        else:
            high = mid
    return low


N, C = list(map(int, input().split()))
houses = [int(input()) for _ in range(N)]

houses.sort()
print(search())

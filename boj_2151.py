import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

field = [input().strip() for _ in range(n)]
visited = [[float('inf')] * n for _ in range(n)]

# 방향 (동남서북)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 입구, 출구
S = []

for i in range(n):
    for j in range(n):
        if field[i][j] == "#":
            S.append((i, j))


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                if field[nx][ny] == '*':
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                # if field[nx][ny] == '!':
                #     break
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx += dx[i]
                ny += dy[i]


(sx, sy), (ex, ey) = S

bfs(sx, sy)

print(visited[ex][ey] - 1)

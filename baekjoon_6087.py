'''
    7 . . . . . . .
    6 . . . . . . C
    5 . . . . . . *
    4 * * * * * . *
    3 . . . . * . .
    2 . . . . * . .
    1 . C . . * . .
    0 . . . . . . .
      0 1 2 3 4 5 6
'''

import sys
from collections import deque

input = sys.stdin.readline

w, h = map(int, input().split())
field = []

for _ in range(h):
    field.append(input().strip())

# 동남서북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited = [[float('inf')] * w for _ in range(h)]
C = []
for i in range(h):
    for j in range(w):
        if field[i][j] == "C":
            C.append((i, j))


def bfs(field, x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            while True:
                if not(0 <= newX < h and 0 <= newY < w):
                    break
                if field[newX][newY] == '*':
                    break
                if visited[newX][newY] < visited[x][y] + 1:
                    break
                queue.append((newX, newY))
                visited[newX][newY] = visited[x][y] + 1
                newX = newX + dx[i]
                newY = newY + dy[i]


bfs(field, C[0][0], C[0][1])

print(visited[C[1][0]][C[1][1]] - 1)

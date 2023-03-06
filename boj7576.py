import sys
from collections import deque
input = sys.stdin.readline

queue = deque([])

w, h = map(int, input().split())
matrix = []
for _ in range(h):
    matrix.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for i in range(h):
    for j in range(w):
        if matrix[i][j] == 1:
            queue.append([i, j])

while queue:
    y, x = queue[0][0], queue[0][1]
    queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and matrix[ny][nx] == 0:
            matrix[ny][nx] = matrix[y][x] + 1
            queue.append([ny, nx])

days = 0
for i in range(h):
    for j in range(w):
        if matrix[i][j] == 0:
            print(-1)
            exit()
    days = max(days, max(matrix[i]))

print(days - 1)
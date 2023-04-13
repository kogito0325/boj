import sys
from collections import deque
input = sys.stdin.readline

queue = deque([])

w, h, d = map(int, input().split())
matrix = []
for di in range(d):
    temp_matrix = []
    for __ in range(h):
        temp_matrix.append(list(map(int, input().split())))
    matrix.append(temp_matrix)

dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(d):
    for j in range(h):
        for k in range(w):
            if matrix[i][j][k] == 1:
                queue.append([i, j, k])

while queue:
    z, y, x = queue[0][0], queue[0][1], queue[0][2]
    queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < w and 0 <= ny < h and 0 <= nz < d and matrix[nz][ny][nx] == 0:
            matrix[nz][ny][nx] = matrix[z][y][x] + 1
            queue.append([nz, ny, nx])

days = 0
for i in range(d):
    for j in range(h):
        for k in range(w):
            if matrix[i][j][k] == 0:
                print(-1)
                exit()
        days = max(days, max(matrix[i][j]))

print(days - 1)
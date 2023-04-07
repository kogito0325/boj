from collections import deque

h, w = map(int, input().split())
maze = [0] * h
visit = [[False] * w for _ in range(h)]

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

for i in range(h):
    maze[i] = input()

queue = deque([(0, 0, 1)])

while queue:
    y, x, cnt = queue.popleft()
    if visit[y][x]:
        continue
    visit[y][x] = True
    if (y, x) == (h-1, w-1):
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w and int(maze[ny][nx]):
            queue.append((ny, nx, cnt+1))

print(cnt)

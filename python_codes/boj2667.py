from collections import deque

n = int(input())

matrix = [0] * n

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    matrix[i] = list(map(int, ' '.join(input()).split()))

cnts = []
while True:
    found = False
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                found = True
                break
        if found:
            break
    if not found:
        break
    cnt = 0
    queue = deque([(i, j)])
    visit = [[False] * n for _ in range(n)]
    while queue:
        y, x = queue.popleft()
        if visit[y][x]:
            continue
        visit[y][x] = True
        matrix[y][x] = 0
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < n and matrix[ny][nx]:
                queue.append((ny, nx))
    cnts.append(cnt)
        
print(len(cnts))
cnts.sort()
print(*cnts, sep='\n')
import sys
from collections import deque

input = sys.stdin.readline

n, r = map(int, input().split())

matrix = [[0] * n for _ in range(n)]
nlist = [i for i in range(n)]
cnt = 0

for _ in range(r):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    matrix[a][b] = 1
    matrix[b][a] = 1
    if a in nlist:
        nlist.remove(a)
    if b in nlist:
        nlist.remove(b)

while True:
    queue = deque([])
    for i in range(n):
        found = False
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                matrix[j][i] = 0
                found = True
                queue.append(i)
                queue.append(j)
                break
        if found:
            break
    if not found:
        break
    while queue:
        y = queue.popleft()
        for i in range(n):
            if matrix[y][i] == 1:
                queue.append(i)
                matrix[y][i] = 0
                matrix[i][y] = 0
    cnt += 1

print(cnt + len(nlist))
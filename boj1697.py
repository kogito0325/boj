from collections import deque

a, b = map(int, input().split())

MAX = 10 ** 5
visit = [False] * (MAX + 1)
queue = deque([(a, 0)])
cnt = 0
while not visit[b]:
    n, cnt = queue.popleft()
    if visit[n]:
        continue
    visit[n] = True
    if 0 <= n-1 <= MAX:
        queue.append((n-1, cnt+1))
    if 0 <= n+1 <= MAX:
        queue.append((n+1, cnt+1))
    if 0 <= n*2 <= MAX:
        queue.append((n*2, cnt+1))
print(cnt)
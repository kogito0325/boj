from collections import deque

ma, mb, mc = map(int ,input().split())
queue = deque([(0, 0, mc)])
visit = [[[False] * (mc+1) for _ in range(mb+1)] for __ in range(ma+1)]
empty = []
while queue:
    a, b, c = queue.popleft()
    if visit[a][b][c]:
        continue
    visit[a][b][c] = True
    if not a and c not in empty:
        empty.append(c)

    queue.append((max(0, a + b - mb), min(mb, a + b), c))
    queue.append((max(0, a + c - mc), b, min(mc, a + c)))

    queue.append((min(ma, a + b), max(0, a + b - ma), c))
    queue.append((a, max(0, b + c - mc), min(mc, b + c)))

    queue.append((min(ma, a + c), b, max(0, a + c - ma)))
    queue.append((a, min(mb, b + c), max(0, b + c - mb)))
print(*sorted(empty))

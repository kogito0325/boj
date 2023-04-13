import sys
import heapq
input = sys.stdin.readline

n = int(input())
nlist = []
for _ in range(n):
    ans = int(input())
    if not ans:
        if not nlist:
            print(0)
            continue
        print(heapq.heappop(nlist))
        continue
    heapq.heappush(nlist, ans)
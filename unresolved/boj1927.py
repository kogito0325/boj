import sys
input = sys.stdin.readline

n = int(input())
nlist = []
for _ in range(n):
    ans = int(input())
    if not ans:
        if not nlist:
            print(0)
            continue
        nlist.sort(reverse=True)
        print(nlist.pop())
        continue
    nlist.append(ans)
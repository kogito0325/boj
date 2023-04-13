import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nlist = list(map(int, input().split()))

prt_list = [0]
whole = 0

for k in nlist:
    prt_list.append(whole + k)
    whole += k

for _ in range(m):
    a, b = map(int, input().split())
    print(prt_list[b] - prt_list[a - 1])
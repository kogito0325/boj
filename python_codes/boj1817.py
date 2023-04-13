n, lim = map(int, input().split())
if not n:
    print(n)
    exit()
nlist = list((map(int, reversed(input().split()))))
cnt = 1
load = 0
while nlist:
    b = nlist.pop(0)
    if load + b <= lim:
        load += b
    else:
        cnt += 1
        load = b
print(cnt)
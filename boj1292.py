nlist = []
for i in range(1, 1001):
    nlist += [i] * i

a, b = map(int, input().split())
print(sum(nlist[a-1: b]))
input()
nlist = list(sorted(map(int, input().split())))
print(nlist[0] * nlist[-1] if len(nlist) > 1 else nlist[0] ** 2)
from copy import deepcopy

input()
nlist = map(int, input().split())
nlist2 = deepcopy(nlist)
dic = {n: i for i, n in enumerate(sorted(set(nlist)))}

for x in nlist2:
    print(dic[x], end=' ')
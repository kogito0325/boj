n, m = map(int, input().split())

nlist = list()
for i in range(n):
    nlist.append([0 for j in range(m)])

for l in range(2):
    for i in range(n):
        for j, k in enumerate(map(int, input().split())):
            nlist[i][j] += k

for i in nlist:
    for j in i:
        print(j, end=' ')
    print()

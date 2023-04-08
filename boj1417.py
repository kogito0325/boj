n = int(input())
nlist = [0] * n
for i in range(n):
    nlist[i] = int(input())

cnt = 0
while True:
    mn = max(nlist)
    if nlist[0] == mn and nlist.count(mn) == 1:
        break
    for i in range(1, n):
        if nlist[i] == mn:
            nlist[i] -= 1
            nlist[0] += 1
            cnt += 1
            mn = max(nlist)
            if nlist[0] == mn and nlist.count(mn) == 1:
                break

print(cnt)

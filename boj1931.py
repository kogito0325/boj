n = int(input())
nlist = [0] * n
for i in range(n):
    nlist[i] = tuple(map(int, input().split()))
nlist.sort()
result = []
i1 = 0
i2 = 1
# print(*nlist, sep='\n')
while i1 < n and i2 < n:
    a1, a2 = nlist[i1]
    b1, b2 = nlist[i2]
    if a2 <= b1:
        result.append((a1, a2))
        i1 = i2
        i2 += 1
        continue
    if b1 <= a2:
        if b2 <= a2:
            i1 = i2
            i2 += 1
            continue
        if a2 <= b2:
            i2 += 1
            continue

print(len(result) + 1)
# print(result)
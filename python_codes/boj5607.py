a, b = 0, 0

for _ in range(int(input())):
    anum, bnum = map(int, input().split())
    if anum > bnum:
        a += anum + bnum
    elif anum < bnum:
        b+= anum + bnum
    else:
        a += anum
        b += bnum

print(a, b)

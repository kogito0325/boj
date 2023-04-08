from math import sqrt

a, b = map(int, input().split())
up = 0

for n in range(a, b+1):
    prm = 0
    while True:
        isprm = True
        for i in range(2, round(sqrt(n))+1):
            if not n % i:
                prm += 1
                isprm = False
                n //= i
                break
        if isprm:
            prm += 1
            break
    isprm = True
    if prm == 1:
        continue
    if prm <= 3:
        up += 1
        continue
    for i in range(2, round(sqrt(prm))+1):
        if not prm % i:
            isprm = False
            break
    if isprm:
        up += 1
print(up)

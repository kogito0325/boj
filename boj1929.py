import math

n, m = map(int, input().split())
plist = []

for i in range(n, m+1):
    if i == 1:
        continue
    elif i == 2:
        plist.append(i)
    else:
        is_prime = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            plist.append(i)

print(*plist, sep='\n')

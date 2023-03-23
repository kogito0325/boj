nlist = [i for i in range(1, 10001)]

for i in range(1, 10001):
    num = i + sum(map(int, str(i)))
    if num in nlist:
        nlist.remove(num)

print(*nlist, sep='\n')
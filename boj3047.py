nlist = list(map(int, input().split()))
nlist.sort()
a = nlist[0]
b = nlist[1]
c = nlist[2]

for i in input():
    if i == 'A':
        print(a, end=' ')
    elif i == 'B':
        print(b, end=' ')
    else:
        print(c, end=' ')
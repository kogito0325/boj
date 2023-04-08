nlist = [0] + [1] * 90

n = int(input())
for i in range(2, n+1):
    nlist[i] = nlist[i-1] + nlist[i-2]

print(nlist[n])
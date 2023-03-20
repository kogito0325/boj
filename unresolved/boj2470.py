n = int(input())
nlist = list(map(int, input().split()))
solution = 2000000000
a, b = 0, 0
for i in range(n-1):
    for j in range(i+1, n):
        temp = abs(nlist[i] + nlist[j])
        if temp <= solution:
            if not temp:
                print(min(nlist[i], nlist[j]), max(nlist[i], nlist[j]))
                exit()
            solution = temp
            a, b = nlist[i], nlist[j]
print(min(a, b), max(a, b))
print(solution)
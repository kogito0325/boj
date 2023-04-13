n = int(input())
for i in range(n):
    print(' '*i+'*'*((n-i-1)*2+1))
n=n-1
for i in range(n):
    print(' '*(n-i-1)+'*'*((i+1)*2+1))
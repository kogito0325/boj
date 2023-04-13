import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nset = set()
for _ in range(n):
    nset.add(input().rstrip())
mset = set()
for _ in range(m):
    mset.add(input().rstrip())

fset = list(sorted(nset.intersection(mset)))
print(len(fset), *fset, sep='\n')

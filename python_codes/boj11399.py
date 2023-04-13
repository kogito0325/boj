n = int(input())
nlist = list(sorted(map(int, input().split())))
whole = 0
for i in range(n + 1):
    whole += sum(nlist[:i])

print(whole)
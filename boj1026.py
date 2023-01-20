loop_range = int(input())

alist = sorted(map(int, input().split()))
blist = list(reversed(sorted(map(int, input().split()))))

whole = 0

for i in range(loop_range):
    whole += alist[i] * blist[i]

print(whole)
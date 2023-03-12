target = int(input())
nlist = []
default = 100

if (n:=int(input())) > 0:
    nlist = list(map(int, input().split()))

cnt = 0
min_d = abs(target - 100)

for _ in range(min_d):
    upfound = False
    downfound = False
    up = target + cnt
    down = max(0, target - cnt)
    
    for n in nlist:
        n = str(n)
        if n in str(up):
            upfound = True
        if n in str(down):
            downfound = True
    if upfound and downfound:
        cnt += 1
        continue
    if not upfound and downfound:
        print(min(min_d, cnt + len(str(up))))
        exit()
    if not downfound and upfound:
        print(min(min_d, cnt + len(str(down))))
        exit()
    print(min(min_d, cnt + len(str(up)), cnt + len(str(down))))
    exit()

print(min_d)
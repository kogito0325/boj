nlist = list(map(int, input().split()))
m = min(nlist)
while True:
    m += 1
    cnt = 0
    for n in nlist:
        if not m % n:
            cnt += 1
        if cnt >= 3:
            print(m)
            exit()
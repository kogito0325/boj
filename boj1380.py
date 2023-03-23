cnt = 0
while n:=int(input()):
    cnt += 1
    nlist = [0] * n
    blist = [False] * n
    for i in range(n):
        nlist[i] = input()
    for _ in range(n * 2 - 1):
        i = int(input().split()[0])-1
        blist[i] = not blist[i]
    
    for i in range(n):
        if blist[i]:
            print(cnt, nlist[i])
            break
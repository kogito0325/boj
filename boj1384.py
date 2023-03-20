cnt = 0
while n:=int(input()):
    cnt += 1
    exist = False
    names = []
    messages = []
    for _ in range(n):
        s = input().split()
        names.append(s[0])
        messages.append(s[1:])
    print('Group', str(cnt))
    for i in range(n):
        for j in range(n-1):
            if messages[i][j] == 'N':
                nasty = i-j-1 if i-j-1 >= 0 else i-j-1+n
                print(names[nasty] + ' was nasty about ' + names[i])
                exist = True
    if not exist:
        print('Nobody was nasty')
    print()


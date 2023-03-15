for _ in range(int(input())):
    s = input()
    for i in range(1, 101):
        if len(s) == (i**2):
            break
    for j in range(i-1, -1, -1):
        for k in range(0, len(s), i):
            print(s[j+k], end='')
    print()
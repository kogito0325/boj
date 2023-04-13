oc = '-\(@?>&%'
while (string := input()) != '#':
    num = 0
    for i, c in enumerate(reversed(string)):
        if c not in oc:
            num -= 8 ** i
        else:
            num += 8 ** i * oc.index(c)
    print(num)

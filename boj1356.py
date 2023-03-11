s = input()
for i in range(1, len(s)):
    a, b = s[:i], s[i:]
    print(a, b)
    sum1, sum2 = 1, 1
    for n in a:
        sum1 *= int(n)
    for n in b:
        sum2 *= int(n)
    if sum1 == sum2:
        print('YES')
        exit()
print('NO')

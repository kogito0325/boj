cnt = 0
a, b = map(int, input().split())

while a != b:
    cnt += 1
    if a + 1 == b:
        a += 1
    elif a - 1 == b:
        a -= 1
    elif a * 2 == b:
        a *= 2
    elif a * 2 < b:
        if abs(b - (a+1) * 2) > abs(b - (a * 2 + 1)):
            a = a * 2 + 1
        else:
            a = (a + 1) * 2
        cnt += 1
    else:
        
        a -= 1

print(cnt)
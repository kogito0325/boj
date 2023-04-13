cnt = 0
for i in range(1, n:=int(input()) + 1):
    if i < 100:
        cnt += 1
    elif i < 1000:
        a, b, c = map(int, str(i))
        if a - b == b - c:
            cnt += 1

print(cnt)
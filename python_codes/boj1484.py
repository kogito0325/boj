n = int(input())
now = 1
prev = 1
ans = []

while True:
    dis = now**2 - prev**2
    if abs(now - prev) <= 1 and dis >n:
        break
    if dis == n:
        ans.append(now)
        now += 1
    elif dis > n:
        prev += 1
    elif dis < n:
        now += 1

if not ans:
    print(-1)
else:
    print(*ans, sep='\n')
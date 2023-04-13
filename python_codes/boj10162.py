time = int(input())

if time % 10:
    print(-1)
else:
    print(time // 300, end=' ')
    time -= 300 * (time // 300)
    print(time // 60, end=' ')
    time -= 60 * (time // 60)
    print(time // 10)
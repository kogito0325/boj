ball = 1
for _ in range(int(input())):
    fir, sec = map(int, input().split())
    ball = fir if ball == sec else sec if ball == fir else ball
print(ball)
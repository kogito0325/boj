fir, sec = map(int, input().split())
standard = fir * sec

people = map(int, input().split())
for p in people:
    print(p - standard, end=' ')
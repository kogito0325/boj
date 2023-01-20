a, b = map(int, input().split())
x = (a + b) / 2
y = a - x
x = int(x)
y = int(y)
if x + y == a and x >= 0 and y >= 0:
    print(max(x, y), min(x, y))
else:
    print(-1)
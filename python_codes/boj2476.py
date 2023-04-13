best = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        best = max(best, 10000 + a * 1000)
    elif a in [b, c]:
        best = max(best, 1000 + a * 100)
    elif b == c:
        best = max(best, 1000 + b * 100)
    else:
        best = max(best, max(a, b, c) * 100)

print(best)

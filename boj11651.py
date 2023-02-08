import sys

points = []
for _ in range(int(input())):
    points.append(list(map(int, sys.stdin.readline().split())))

points.sort(key=lambda x:x[0])
points.sort(key=lambda x:x[1])
for p in points:
    print(*p)
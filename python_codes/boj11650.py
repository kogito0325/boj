num_range = int(input())
points = list((0, 0) for _ in range(num_range))

for i in range(num_range):
    points[i] = tuple(map(int, input().split()))

points.sort()

for p in points:
    print(*p)

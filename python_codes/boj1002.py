import math

for _ in range(int(input())):
    x1, y1, dist1, x2, y2, dist2 = map(int, input().split())
    dist = math.dist((x1, y1), (x2, y2))
    if (x1, y1, dist1) == (x2, y2, dist2):
        print(-1)
    elif dist > dist1 + dist2:
        print(0)
    elif dist == dist1 + dist2:
        print(1)
    else:
        if abs(dist2 - dist1) == dist:
            print(1)
        elif abs(dist2 - dist1) > dist:
            print(0)
        else:
            print(2)

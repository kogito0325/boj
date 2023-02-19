import sys
input = sys.stdin.readline

w, h = map(int, input().split())
box = []
for i in range(h):
    box.append(list(map(int, input().split())))

days = 0
while True:
    raw_exist = False
    changed = False
    for y in box:
        if 0 in y:
            raw_exist = True
            break
    if not raw_exist:
        break
    for y in range(h):
        for x in range(w):
            if box[y][x] == 1:
                if 0 <= y - 1 < h and box[y - 1][x] == 0:
                    box[y - 1][x] = 2
                    changed = True
                if 0 <= y + 1 < h and box[y + 1][x] == 0:
                    box[y + 1][x] = 2
                    changed = True
                if 0 <= x - 1 < w and box[y][x - 1] == 0:
                    box[y][x - 1] = 2
                    changed = True
                if 0 <= x + 1 < w and box[y][x + 1] == 0:
                    box[y][x + 1] = 2
                    changed = True
    if not changed:
        print(-1)
        quit()
    days += 1
    for y in range(h):
        for x in range(w):
            if box[y][x] == 2: box[y][x] = 1

print(days)
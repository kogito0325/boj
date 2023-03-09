n = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for _ in range(n):
    searched = []
    w, h, k = map(int, input().split())
    matrix = []
    for _ in range(h):
        matrix.append([0] * w)
    points = [0] * k

    for i in range(k):
        points[i] = list(map(int, input().split()))
        points[i][0], points[i][1] = points[i][1], points[i][0]
        matrix[points[i][0]][points[i][1]] = 1
    
    cnt = 0
    
    while points:
        x, y = points[0]
        to_search = list((y, x))
        while to_search:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < w and 0 <= ny < h and matrix[ny][nx] == 1:
                    if (ny, nx) not in searched:
                        to_search.append((ny, nx))
                        searched.append((ny, nx))
            matrix[y][x] = 0
            for p in range(len(points)):
                if points[p] == (y, x):
                    points.pop(p)
        cnt += 1

    print(cnt)
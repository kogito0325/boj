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
        y, x = points[0]
        if not matrix[y][x]:
            points.pop(0)
            continue
        cnt += 1
        to_search = [[y, x]]
        matrix[y][x] = 0
        while to_search:
            y, x = to_search.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < w and 0 <= ny < h and matrix[ny][nx] == 1:
                    to_search.append([ny, nx])
                    matrix[ny][nx] = 0

    print(cnt)
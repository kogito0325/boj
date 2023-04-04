h, w = map(int, input().split())

matrix = [0] * h
res = [0] * h

for i in range(h):
    matrix[i] = list(' '.join(input()).split())
for i in range(h):
    res[i] = list(' '.join(input()).split())

cnt = 0

for y in range(h-2):
    for x in range(w-2):
        if matrix[y][x] != res[y][x]:
            cnt += 1
            for i in range(3):
                for j in range(3):
                    matrix[i+y][j+x] = '1' if matrix[i+y][j+x] == '0' else '0'

for i in range(h):
    for j in range(w):
        if matrix[i][j] != res[i][j]:
            print(-1)
            exit()
print(cnt)
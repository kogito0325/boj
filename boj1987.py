h, w = map(int, input().split())
matrix = [0] * h
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
check = [0] * 26

for i in range(h):
    matrix[i] = input()

high = 0
def tracking(y, x, matrix:list, check:list, temphigh):
    global high
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not (0 <= ny < h and 0 <= nx < w):
            continue
        cn = ord(matrix[ny][nx]) - ord('A')
        if not check[cn]:
            temp = check
            temp[cn] = 1
            tracking(ny, nx, matrix, temp, temphigh+1)
            temp[cn] = 0
    high = max(high, temphigh)
check[ord(matrix[0][0])-ord('A')] = 1
tracking(0, 0, matrix, check, 1)
print(high)
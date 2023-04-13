def tetro(num, y, x, mat:list):
    result = 0
    try:
        if not num:
            result = sum(mat[y][x:x+4])
    except IndexError:
        pass

    try:
        if num == 1:
            result = mat[y][x] + mat[y+1][x] + mat[y+2][x] + mat[y+3][x]
    except IndexError:
        pass

    try:
        if num == 2:
            result = mat[y][x] + mat[y+1][x] + mat[y][x+1] + mat[y+1][x+1]
    except IndexError:
        pass

    try:
        if num == 3:
            result = mat[y][x] + mat[y+1][x] + mat[y+2][x] + mat[y+2][x+1]
    except IndexError:
        pass

    try:
        if num == 4:
            result = mat[y][x+1] + mat[y+1][x+1] + mat[y+2][x+1] + mat[y+2][x]
    except IndexError:
        pass

    try:
        if num == 5:
            result = mat[y][x] + mat[y][x+1] + mat[y+1][x] + mat[y+2][x]
    except IndexError:
        pass

    try:
        if num == 6:
            result = mat[y][x] + mat[y][x+1] + mat[y+1][x+1] + mat[y+2][x+1]
    except IndexError:
        pass

    try:
        if num == 7:
            result = mat[y][x] + mat[y+1][x] + mat[y+1][x+1] + mat[y+2][x+1]
    except IndexError:
        pass

    try:
        if num == 8:
            result = mat[y][x+1] + mat[y+1][x] + mat[y+1][x+1] + mat[y+2][x]
    except IndexError:
        pass

    try:
        if num == 9:
            result = mat[y][x+1] + mat[y][x+2] + mat[y+1][x] + mat[y+1][x+1]
    except IndexError:
        pass

    try:
        if num == 10:
            result = mat[y][x] + mat[y][x+1] + mat[y+1][x+1] + mat[y+1][x+2]
    except IndexError:
        pass

    try:
        if num == 11:
            result = mat[y][x] + mat[y][x+1] + mat[y][x+2] + mat[y+1][x+1]
    except IndexError:
        pass

    try:
        if num == 12:
            result = mat[y][x+1] + mat[y+1][x] + mat[y+1][x+1] + mat[y+1][x+2]
    except IndexError:
        pass

    try:
        if num == 13:
            result = mat[y][x+1] + mat[y+1][x] + mat[y+1][x+1] + mat[y+2][x+1]
    except IndexError:
        pass

    try:
        if num == 14:
            result = mat[y][x] + mat[y+1][x] + mat[y+1][x+1] + mat[y+2][x]
    except IndexError:
        pass

    try:
        if num == 15:
            result = mat[y][x+2] + mat[y+1][x] + mat[y+1][x+1] + mat[y+1][x+2]
    except IndexError:
        pass

    try:
        if num == 16:
            result = mat[y][x] + mat[y+1][x] + mat[y+1][x+1] + mat[y+1][x+2]
    except IndexError:
        pass

    try:
        if num == 17:
            result = mat[y][x] + mat[y][x+1] + mat[y][x+2] + mat[y+1][x+2]
    except IndexError:
        pass

    try:
        if num == 18:
            result = mat[y][x] + mat[y][x+1] + mat[y][x+2] + mat[y+1][x]
    except IndexError:
        pass

    return result

h, w = map(int, input().split())
matrix = [[0] for _ in range(h)]
for i in range(h):
    matrix[i] = list(map(int, input().split()))

res = 0
for y in range(h):
    for x in range(w):
        for i in range(19):
            res = max(res, tetro(i, y, x, matrix))
print(res)
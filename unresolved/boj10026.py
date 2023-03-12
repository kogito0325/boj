n = int(input())
matrix = [0] * n

target = n * n
whole = 0

for i in range(n):
    matrix[i] = input()

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

while True:
    for i in range(n):
        found = False
        for j in range(n):
            if matrix[i][j] != 'M':
                x = j
                y = i
                found = True
                break
        if found:
            break
    for d in range(4):
        pass
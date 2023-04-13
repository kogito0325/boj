n = int(input())
matrix = [[0]*n for _ in range(n)]
for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

query = [0]
searched = []

while query:
    i = query.pop(0)
    for x in range(n):
        if matrix[i][x] == 1 and x not in searched:
            query.append(x)
            searched.append(x)

print(len(searched) - 1)
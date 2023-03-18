n = int(input())
matrix = [[0] * 9 for _ in range(5)]
for i in range(n):
    for j, k in enumerate(map(int, input().split())):
        matrix[j][k-1] += 1

print(*matrix, sep='\n')

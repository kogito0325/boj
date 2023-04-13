sets = list(map(int, input().split()))
rights = [1, 1, 2, 2, 2, 8]
for i, n in enumerate(sets):
    print(rights[i] - n, end=' ')

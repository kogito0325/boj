datas = [(1, 0), (0, 1)]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(datas), n + 1):
        datas.append((datas[i-2][0] + datas[i-1][0], datas[i-2][1] + datas[i-1][1]))
    print(*datas[n])

n , m = map(int, input().split())
row = []
cnt = 0
for _ in range(n):
    if 'X' not in (s:=input()):
        cnt += 1
        continue
    for i, c in enumerate(s):
        if c == 'X':
            row.append(i)

print(max(m - len(set(row)), cnt))

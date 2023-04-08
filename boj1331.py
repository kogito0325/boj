visit = [[False] * 6 for _ in range(6)]
alp = 'ABCDEF'
oa, ob = -1, -1
valid = True
sa, sb = 0, 0
for _ in range(36):
    s = input()
    a, b = alp.index(s[0]), int(s[1])-1
    if visit[a][b]:
        valid = False
    visit[a][b] = True
    if oa + ob == -2:
        sa, sb = oa, ob = a, b
        continue
    if (abs(a - oa), abs(b - ob)) in ((1, 2), (2, 1)):
        oa, ob = a, b
        continue
    valid = False

if valid and (abs(a - sa), abs(b - sb)) in ((1, 2), (2, 1)):
    print('Valid')
else:
    print('Invalid')
nlist = []
rejects = 0
input()

for sit in map(int, input().split()):
    if sit in nlist:
        rejects += 1
    else:
        nlist.append(sit)

print(rejects)

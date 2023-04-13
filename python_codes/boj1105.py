a, b = map(int, input().split())
min8 = 0
if len(str(a)) - len(str(b)):
    print(min8)
    exit()
for i in range(len(str(a))):
    if str(a)[i] == str(b)[i]:
        if str(a)[i] == '8':
            min8 += 1
        continue
    break

print(min8)

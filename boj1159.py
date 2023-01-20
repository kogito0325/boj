members = {}

for _ in range(int(input())):
    member = input()
    if member[0] not in members:
        members[member[0]] = 1
    else:
        members[member[0]] += 1

fir = ''
for k in members:
    if members[k] >= 5:
        fir += k

if fir == '':
    print('PREDAJA')
else:
    print(*sorted(fir), sep='')
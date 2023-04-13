whole = 0
nlist = list()

for _ in range(int(input())):
    answer = input()
    if answer == '0':
        nlist.pop(-1)
    else:
        nlist.append(answer)

for c in nlist:
    whole += int(c)

print(whole)

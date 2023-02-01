members = list()
for i in range(int(input())):
    num, name = input().split()
    num = int(num)
    members.append((num, name, i))

for m in sorted(members, key=lambda x:x[0]):
    print(m[0], m[1])
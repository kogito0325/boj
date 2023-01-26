whole = 0
for i in range(4):
    whole += int(input())
print(whole // 60, whole % 60, sep='\n')
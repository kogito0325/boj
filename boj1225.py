whole = 0
n, m = input().split()
for i in n:
    for j in m:
        whole += int(i) * int(j)

print(whole)
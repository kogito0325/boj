num = 0
for i in list(map(int, input().split())):
    num += i**2

print(num % 10)

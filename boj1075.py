n = int(input()[0:-2] + '00')
f = int(input())

for _ in range(0, f + 1):
    if n % f == 0:
        print(str(n)[-2:])
        break
    n += 1
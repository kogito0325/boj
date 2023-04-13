input()
primes = 0

for n in map(int, input().split()):
    if n == 1:
        continue
    elif n in [2, 3]:
        primes += 1
    else:
        flag = False
        for i in range(2, n):
            if n % i == 0:
                flag = True
                break
        if not flag:
            primes += 1

print(primes)

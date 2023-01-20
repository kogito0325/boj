n, r = map(int, input().split())

son = 1
mom1, mom2 = 1, 1
for i in range(1, n + 1):
    son *= i

for i in range(1, r + 1):
    mom1 *= i

for i in range(1, n - r + 1):
    mom2 *= i

print(int(son / (mom1 * mom2)))
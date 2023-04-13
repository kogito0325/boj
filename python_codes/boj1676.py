whole = 1
n = int(input())
if n == 0:
    print(0)
else:
    for i in range(1, n + 1):
        whole *= i
    for i, c in enumerate(str(whole)[::-1]):
        if c != '0':
            print(i)
            break
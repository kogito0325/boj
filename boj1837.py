m, n = map(int, input().split())

found = False

for i in range(2, n):
    if m % i == 0:
        print('BAD', i)
        found = True
        break
    
if not found:
    print('GOOD')
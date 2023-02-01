people, step = map(int, input().split())
step -= 1
target = 0
table = list(i for i in range(people))
print('<', end='')
while True:
    target = (target + step) % len(table)
    print(table.pop(target) + 1, end='')
    if not len(table):
        break
    print(', ', end='')
print('>')
    
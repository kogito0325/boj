num = int(input())

for i in range(num):
    print(' ' * (num - i - 1), end='')
    for j in range(i + 1):
        print('* ', end='')
    print()
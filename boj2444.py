num = int(input())
[print(' ' * (num - i) + '*' * (i * 2 - 1)) for i in range(1, num + 1)]
[print(' ' * i + '*' * ((num - i) * 2 - 1)) for i in range(1, num)]
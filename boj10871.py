length, num = input().split()

numbers = map(int, input().split())
for i in numbers:
    if i < int(num):
        print(i, end=' ')
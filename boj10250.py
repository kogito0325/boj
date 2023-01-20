for i in range(int(input())):
    height, width, number = map(int, input().split())
    number -= 1
    print(f'{number % height + 1}{number // height + 1 :02}')
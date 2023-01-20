while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    

    abcs = list((a, b, c))
    biggest = max(abcs)
    abcs.remove(biggest)
    if biggest ** 2 == abcs[0] ** 2 + abcs[1] ** 2:
        print('right')
    else:
        print('wrong')

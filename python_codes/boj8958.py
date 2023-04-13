for i in range(int(input())):
    score = 0
    for answer in input().split('X'):
        for point in range(len(answer)):
            score += point + 1
    print(score)

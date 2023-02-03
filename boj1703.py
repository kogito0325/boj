while (answer:=list(map(int, input().split())))[0]:
    offset = 0
    result = 1
    for i in range(answer[0]):
        result = result * answer[1 + offset] - answer[2 + offset]
        offset += 2
    print(result)

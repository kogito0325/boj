for _ in range(int(input())):
    mul, word = input().split()
    result = ''
    for c in word:
        result += c * int(mul)
    print(result)

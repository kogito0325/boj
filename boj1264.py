while (answer := input()) != '#':
    count = 0
    for c in answer.upper():
        if c in "AEIOU":
            count += 1
    print(count)
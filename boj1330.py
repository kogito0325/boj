numbers = input().split()

a = int(numbers[0])
b = int(numbers[1])

print('<' if a < b else '>' if a > b else '==')

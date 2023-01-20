num1 , num2 = input().split()

num1 = ''.join(reversed(num1))
num2 = ''.join(reversed(num2))

print(max(int(num1), int(num2)))

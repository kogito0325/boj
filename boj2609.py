num1, num2 = map(int, input().split())
num3 = num1 * num2

if num1 < num2:
    num1, num2 = num2, num1

if not num1 % num2:
    remainder = num2
else:
    while True:
        remainder = num1 % num2
        if not num2 % remainder:
            break
        else:
            num1 = num2
            num2 = remainder

print(remainder)
print(num3 // remainder)

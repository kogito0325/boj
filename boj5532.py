days = int(input())
math = int(input())
korean = int(input())
sorvable_math = int(input())
sorvable_korean = int(input())

if math % sorvable_math:
    math = math // sorvable_math + 1
else:
    math = math // sorvable_math

if korean % sorvable_korean:
    korean = korean // sorvable_korean + 1
else:
    korean = korean // sorvable_korean

print(days - max(korean, math))
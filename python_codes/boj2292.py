'''
1 = 1
2 ~ 7 = 2
8 ~ 19 = 3
20 ~ 37 = 4
38 ~ 61 = 5
62 ~ 91 = 6
'''

num = int(input())
rooms = 1
repeat = 0

while True:
    repeat += 1
    if num > rooms:
        rooms += repeat * 6
    else:
        break

print(repeat)

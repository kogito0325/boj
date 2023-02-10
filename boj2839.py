sugar = int(input())
fives = 0
threes = 0

fives = sugar // 5
sugar -= fives * 5

threes = sugar // 3
sugar -= threes * 3

while sugar and fives >= 0:
    fives -= 1
    if fives == -1:
        print(fives)
        exit()
    else:
        sugar += 5
        threes += sugar // 3
        sugar %= 3

whole = fives + threes
print(whole)
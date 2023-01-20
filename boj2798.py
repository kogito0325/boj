count, black_jack = map(int, input().split())

numbers = sorted(list(map(int, input().split())))
biggest = 0

for i in numbers:
    for j in numbers[1:]:
        for k in numbers[2:]:
            if biggest < i + j + k <= black_jack and i != j and i != k and j != k:
                biggest = i + j + k

print(biggest)

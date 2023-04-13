tiles = [input() for i in range(8)]

count_f = 0
raw = 1

for fs in tiles:
    index = 0
    if not raw % 2:
        index += 1

    for f in fs:
        index += 1
        if index % 2 and f == 'F':
            count_f += 1

    raw += 1

print(count_f)

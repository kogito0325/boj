height, width, blocks = map(int, input().split())
length = height * width
ground = []
for h in range(height):
    for i in map(int, input().split()): ground.append(i)

cases = []
for n in range(0, max(ground) + 1):
    temp_block = blocks
    time = 0
    for i in ground:
        reminder = i - n
        if reminder > 0:
            time += 2 * reminder
        elif reminder < 0:
            time += abs(reminder)
        temp_block += reminder
    if temp_block < 0:
        break
    cases.append((time, n))

temp_list = []
for x in cases:
    temp_list.append(x[0])

min_time = min(temp_list)
max_height = 0
for x in cases:
    if x[0] == min_time and x[1] > max_height:
        max_height = x[1]

print(min_time, max_height)
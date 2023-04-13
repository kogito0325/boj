people, goal, step = map(int, input().split())
table = [0 for _ in range(people)]
now = 0
while True:
    table[now] += 1
    if table[now] >= goal:
        break
    if not table[now] % 2:
        now -= step
        if now < 0:
            now += people
    elif table[now] % 2:
        now += step
        if now >= people:
            now -= people

print(sum(table) - 1)
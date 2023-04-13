n, m = map(int, input().split())
bot_y, bot_x, direction = map(int, input().split())

room_to_clear = [list(map(int, input().split())) for _ in range(n)]

cleared = 0

while True:
    if room_to_clear[bot_y][bot_x] == 0:
        room_to_clear[bot_y][bot_x] = 2
        cleared += 1

    go_able = False
    for _ in range(4):
        x_offset = 0
        y_offset = 0

        direction -= 1
        if direction < 0:
            direction = 3

        if direction == 0:
            y_offset -= 1
        elif direction == 1:
            x_offset += 1
        elif direction == 2:
            y_offset += 1
        elif direction == 3:
            x_offset -= 1

        target = room_to_clear[bot_y + y_offset][bot_x + x_offset]
        if target== 1:
            continue
        elif target == 0:
            go_able = True
            bot_x += x_offset
            bot_y += y_offset
            break

    if not go_able:
        if direction == 0:
            bot_y += 1
        elif direction == 1:
            bot_x -= 1
        elif direction == 2:
            bot_y -= 1
        elif direction == 3:
            bot_x += 1

        if room_to_clear[bot_y][bot_x] == 1:
            break

print(cleared)

height, width, blocks = map(int, input().split())
ground = [[0 for i in range(width)] for j in range(height)]
for h in range(height):
    ground[h][0:width] = map(int, input().split())

print(ground)
